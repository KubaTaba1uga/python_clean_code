from datetime import datetime
from abc import ABC, abstractmethod

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


def hide_field(field) -> str:
    return "****************"


def show_orginal(field):
    return field


def format_time(timestamp: datetime) -> str:
    return timestamp.strftime("%Y-%m-%d %H: %M")


class FormatDataDescriptor:
    SERIALIZATION_PREFIX = "fmt_"

    def __init__(self, fmt_function, fmt_field_prefix=SERIALIZATION_PREFIX):
        """Format field, with passed formatting function"""
        self.fmt = fmt_function
        self.fmt_field_prefix = fmt_field_prefix

    def __set_name__(self, instance_class, name):
        self._name = name
        self.fmt_field_name = self.fmt_field_prefix + name

    def __set__(self, instance, value):
        (
            instance.__dict__[self._name],
            instance.__dict__[self.fmt_field_name],
        ) = value, self.fmt(value)

    def __get__(self, instance, instance_class=None):
        try:
            return instance.__dict__[self._name]
        except KeyError:
            raise AttributeError(f"{instance} hasn't attribute {self._name}")


class Serialization(ABC):
    @abstractmethod
    def serialize(self) -> dict:
        """Return instance attributes formatted versions in place of orginals"""
        return dict()


class LogInEvent(Serialization):
    SERIALIZATION_PREFIX = "formatted_"
    username = FormatDataDescriptor(show_orginal, SERIALIZATION_PREFIX)
    password = FormatDataDescriptor(hide_field, SERIALIZATION_PREFIX)
    ip = FormatDataDescriptor(show_orginal, SERIALIZATION_PREFIX)
    timestamp = FormatDataDescriptor(format_time, SERIALIZATION_PREFIX)

    def __init__(self, username, password, ip, timestamp):
        self.username = username
        self.password = password
        self.ip = ip
        self.timestamp = timestamp

    def serialize(self) -> dict:
        return {
            "username": getattr(self, self.SERIALIZATION_PREFIX + "username"),
            "password": getattr(self, self.SERIALIZATION_PREFIX + "password"),
            "ip": getattr(self, self.SERIALIZATION_PREFIX + "ip"),
            "timestamp": getattr(self, self.SERIALIZATION_PREFIX + "timestamp"),
        }
