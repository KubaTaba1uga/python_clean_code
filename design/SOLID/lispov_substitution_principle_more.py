"""
        More subtle LSP violations, could be spotted
                only by code review. To help recognizaing
                such situations two LSP rules has been
                established:

                        1. Subclass cannot make stricter
                                preconditions than parent class

                        2. Subclass cannot make weaker
                                postconditions than parent class
"""


class Event:
    def __init__(self, raw_data: dict[str, dict]):
        self._raw_data = raw_data

    def meet_condition(self) -> bool:
        return False


class UnknownEvent(Event):
    """Event which cannot be identified from its data"""

    # Bad design
    def meet_condition(self) -> bool or type(None):
        # Returning object which could be interpreted
        #   in other way than assumed in parent class is
        #   violation of 2. rule
        return None

    # Good design
    def meet_condition(self) -> bool:
        return False


# Bad design
class LoginEvent(Event):
    """Event which represent user login"""

    def meet_condition(self):
        # Demanding input data which contain
        #       "session" key is violation of 1. rule
        #       as preconditions are stricter now
        return (
            self._raw_data["before"]["session"] == 0
            and self._raw_data["after"]["session"] == 1
        )


# Good design
class LogoutEvent(Event):
    """Event which represent user logout"""

    def meet_condition(self):
        # Input data doesn't require "session"
        #       key anymore, so preconditions
        #       aren't stricter. Preconditions are
        #       the same as in parent class
        return (
            self._raw_data["before"].get("session") == 1
            and self._raw_data["after"].get("session") == 0
        )


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
