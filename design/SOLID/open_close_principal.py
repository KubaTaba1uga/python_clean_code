"""
        When designing a class, its logic should be encapsulated in a way
                which allow for extensions but don't require modifications.

        Adding new feature shouldn't require logic modification, if it does
                propably a class should be redesigned. Logic extending,  
                shouldn't change its orginal implementation. 
"""

# Let's design a part of system to identify events

EVENT_DATA = {"before": {"session": 0}, "after": {"session": 1}}


# Bad design
#  Adding new event require logic modification
#       by adding next elif statement
class Event:
    def __init__(self, raw_data):
        self._raw_data = raw_data


class UnknownEvent(Event):
    """Event which cannot be identified from its data"""


class LoginEvent(Event):
    """Event which represent user login"""


class LogoutEvent(Event):
    """Event which represent user logout"""


class SystemMonitor:
    """Identify events that occured in the system"""

    def __init__(self, event_data):
        self.event_data = event_data

    def identify_event(self):
        if (
            self.event_data["before"]["session"] == 0
            and self.event_data["after"]["session"] == 1
        ):
            return LoginEvent(self.event_data)

        elif (
            self.event_data["before"]["session"] == 1
            and self.event_data["after"]["session"] == 0
        ):
            return LogoutEvent(self.event_data)

        else:
            return UnknownEvent


# Good design
# Adding new event require class creation
#       which inherit from event and has implemented
#       meet_condition method
class Event:
    def __init__(self, raw_data):
        self._raw_data = raw_data

    def meet_condition(self) -> bool:
        return False


class UnknownEvent(Event):
    """Event which cannot be identified from its data"""


class LoginEvent(Event):
    """Event which represent user login"""

    def meet_condition(self):
        if (
            self._raw_data["before"]["session"] == 0
            and self._raw_data["after"]["session"] == 1
        ):
            return True
        else:
            return False


class LogoutEvent(Event):
    """Event which represent user logout"""

    def meet_condition(self):
        if (
            self._raw_data["before"]["session"] == 1
            and self._raw_data["after"]["session"] == 0
        ):
            return True
        else:
            return False


class SystemMonitor:
    def __init__(self, event_data):
        self.event_data = event_data

    def identify_event(self):
        """Identify events that occured in the system"""
        for event in Event.__subclasses__():

            event = event(self.event_data)

            if event.meet_condition():
                return event

        return UnknownEvent
