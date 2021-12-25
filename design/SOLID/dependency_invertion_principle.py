"""
        Dependency Invertion Principle (DIP)  stands that, software
                 components should be protected from things that are
                 fragile, volatile or out of control. Code should not require
                 modification in case of fragile parts changes, it should
                 require adding extensions only. It is done by creating
                 API that stands between volatile part and the app.
"""


from open_close_principal import Event


# Bad design
# Adding another data target to whom
#       events would be sent to, require
#       changes in EventStreamer class
class Syslog:
    @classmethod
    def send_data(event: Event):
        ...


class EventStreamer:
    def stream(self, data_target: Syslog):
        """Stream data to data target"""


# Good design
# Adding another data target require
#       new class which will inherit
#       from DataTargetClient and has
#       implemented send_data method.
#       It is up to data target to implement
#       the interface correctly.
# DataTargetClient is specifying API
#       which stands between data targets
#       and its client class.
class DataTargetClient:
    def __instancecheck__(cls, instance):
        # Every subclass of abstract class is recognized
        #   as its instance
        return cls.__subclasscheck__(type(instance))

    def __subclasscheck__(cls, subclass):
        # Every class that has implemented send_data
        #       method is recognized as DataTargetClient subclass
        return hasattr(subclass, "send_data") and callable(subclass.send_data)

    @classmethod
    def send_data(event: Event):
        ...


class Syslog(DataTargetClient):
    @classmethod
    def send_data(event: Event):
        ...


class EventStreamer:
    def stream(self, data_target: DataTargetClient):
        ...
