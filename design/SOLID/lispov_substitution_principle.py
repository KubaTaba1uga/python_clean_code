"""
        Lispov's substitution principle (LSP) stands that, for any
                class, a class client should be able to use any of client's
                subtypes, without noticing a difference (app won't stop
                running).

        A class should define clear and concise interface.
                As long  subtypes respect the interface, the program
                will remain correct.

        Some LSP withdrawals, could be recognize by MyPy and  pyLint.
                MyPy output example:
                        lispov_substitution_principle.py:22:
                         error: Argument 1 of "meet_condition" is incompatible with supertype "Event";
                         supertype defines the argument type as "Dict[str, dict]"
  
                pyLint output example:
                        lispov_substitution_principle.py:37:4:
                        W0221: Number of parameters was 2 in 'Event.meet_condition' 
                        and is now 3 in overridden 'BadLogOutEvent.meet_condition' method (arguments-differ)

        However more subtle LSP withdrawals could be spotted
                only by a code review. 
"""


class Event:
    def meet_condition(self, event_data: dict[str, dict]) -> bool:
        ...


# Bad design
class BadLoginEvent(Event):
    # DbC is violated by changing inputs datatypes
    def meet_condition(self, event_data: list) -> bool:
        ...


# Good design
class GoodLoginEvent(Event):
    def meet_condition(self, event_data: dict[str, dict]) -> bool:
        ...


# Bad design
class BadLogOutEvent(Event):
    # DbC is violated by adding argument which is not in parent class
    def meet_condition(self, event_data: dict[str, dict], override: bool) -> bool:
        if override:
            ...
        ...
