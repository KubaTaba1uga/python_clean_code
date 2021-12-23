"""
        Single Responsibility Principle (SRP),
                stands that each class should have only
                one responsibility. Following the rule, class
                should do only one thing and be specially
                designed for the job requirements. (UNIX philosophy)

        If class has to be updated upon, changes in different
                parts of domain problem, it should be decoupled into
                more classes. 

        The smaller the class is, the better. Class should be 
                designed in a way, which require useage most 
                of attributes and propertties by methods all the time.
                If some attribute or method is used from time to time,
                maybe it should be separeted into another class.
"""


# Bad design
class SystemMonitor:
    # SystemMonitor class is responsible for three tasks,
    #   each of them should be independent from the others.
    #   Changing load_actiovity method shouldn't require
    #   changes in the other methods. Howerver grouping
    #   them into one will lead to that situation at some point.
    def load_activities(self):
        """Get the events from the source"""

    def identify_events(self):
        """Parse the source data into events (domain objects)"""

    def stream_events(self):
        """Send events to an external agent"""


# Good design
class ActivitiesLoader:
    def load_activities(self):
        """Get the events from the source"""


class EventsParser:
    """Create events objects, based on raw data"""

    def identify_events(self, activities_data):
        """Parse raw data, into domain objects
        which corresponds to events type"""


class EventsStreamer:
    def stream_events(self, events_objects):
        """Send events to external agent"""


class SystemMonitor:
    activity_loader = ActivitiesLoader
    events_parser = EventsParser
    events_streamer = EventsStreamer

    def run(self):
        """Organize sending parsed events to an external agent"""
