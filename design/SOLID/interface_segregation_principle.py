"""
        An interface is represented by the set of methods and
                object exposes. Interface separetes the definition
                of the exposed behaviour from its implementation.

        In Python interfaces are implicitly defined by a class
                according to its methods. It is possible because
                Python follow duck typing principle:

                        If it walks like a duck, quack like a duck or
                                it says it is a duck. Then it must be a duck.

        Interface Segregation Principle stands, that the interface
                should be as small as it is possible. However there is
                limitation which should be concerned when following
                this principle:

                        Abstraction which require strict implementation
                                cannot be disassembled into smaller classes.

        In Python ISP is complied, by creating abstract base classes
                (ABS).
"""


# Bad design
# Every class that subclass EventParser
#       would have non required methods
#       Example:
#               JsonEventParser would have
#                       from_xml
#               XmlEventParser would have
#                       from_json
class EventParser:
    @classmethod
    def from_xml(event_data):
        ...

    @classmethod
    def from_json(event_data):
        ...


# Good design
# Implementation of parse method
#       is dependent only on subclass
#       specification.
class EventParser:
    def __instancecheck__(cls, instance):
        # Every subclass of abstract class is recognized
        #   as its instance
        return cls.__subclasscheck__(type(instance))

    def __subclasscheck__(cls, subclass):
        # Every class that has implemented parse_data
        #       method is recognized as EventParser subclass
        return hasattr(subclass, "parse_data") and callable(subclass.parse_data)

    @classmethod
    def parse_data(event_data):
        """Create event object from formatted data in appropriate standard"""
        ...


class JsonEventParser(EventParser):
    @classmethod
    def parse_data(event_data):
        """Create Event object from json formatted data"""
        ...


class XmlEventParser(EventParser):
    @classmethod
    def parse_data(event_data):
        """Create Event object from xml formatted data"""
        ...
