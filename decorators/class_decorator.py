"""
        Decorator changes class behaviours without changing
                its implementation.

        It's specially useful for extending preconditions.

        ALWAYS USE @functools.wraps IN WRAPPED FUNCTION!!!
                It keep docstrings and name of function.
"""
from datetime import datetime


# Lets imagine Monitoring System which
#       require extension for third party
#       data target. This data target shouldn't
#       be able to read specific data, for
#       example: passwords.

EVENT_DATA = {
    "username": "chwial",
    "password": "chwial123#$%",
    "ip": "199.132.0.222",
    "timestamp": datetime.now(),
}

# Bad design
# Adding another serializer require creating
#       new class for each event.
class LogInBadSerializer:
    def __init__(self, event):
        self.event = event

    def serialize(self):
        return {
            "username": self.event.username,
            "password": "****************",
            "ip": self.event.ip,
            "timestamp": self.event.timestamp.strftime("%Y-%m-%d %H: %M"),
        }


class LogInBadEvent:
    SERIALIZER = LogInBadSerializer

    def __init__(self, username, password, ip, timestamp):
        self.username = username
        self.password = password
        self.ip = ip
        self.timestamp = timestamp

    def serialize(self):
        return self.SERIALIZER(self).serialize()


# Good design
# Adding new serializer require creating
#       function to format data, and pass it to
#       Serialization object.
# EventSerializer


def hide_field(field) -> str:
    return "****************"


def show_orginal(field):
    return field


def format_time(timestamp: datetime) -> str:
    return timestamp.strftime("%Y-%m-%d %H: %M")


class EventSerializer:
    def __init__(self, serialization_fields: dict):
        """Fields with assigned formatters.

        : transformations : dict {"username": show_orginal}
        """
        self.serialization_fields = serialization_fields

    def serialize(self, event):
        """Format fields, with assigned formatters"""
        serialized_event = {}

        for field, formatter in self.serialization_fields.items():
            serialized_event[field] = formatter(getattr(event, field))

        return serialized_event


# Creating class decorator
class Serialization:
    def __init__(self, **serialization_fields):
        # Create EventSerializer object with all
        #       arguments passed to __init__
        self.serializer = EventSerializer(serialization_fields)

    def __call__(self, event_class):
        # Create function which will serialize
        #       event data and assign it to event
        #       instance
        def serialize_method(event_instance):
            return self.serializer.serialize(event_instance)

        event_class.serialize = serialize_method
        return event_class


@Serialization(
    username=show_orginal, password=hide_field, ip=show_orginal, timestamp=format_time
)
class LogInEvent:
    def __init__(self, username, password, ip, timestamp):
        self.username = username
        self.password = password
        self.ip = ip
        self.timestamp = timestamp


event = LogInEvent(**EVENT_DATA)
serialized_event = event.serialize()
