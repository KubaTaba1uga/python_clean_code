# Lets imagine travelling app, which
#       need to track all previous journeys
#       of user, car and more


class Traveller:
    def __init__(self, name, current_target):
        self.name = name
        self._current_target = current_target
        self.previous_targets = []

    @property
    def current_target(self):
        return self._current_target

    @current_target.setter
    def current_target(self, target):
        self.previous_targets.append(self._current_target)
        self._current_target = target


class Transport:
    def __init__(self, name, current_target):
        self.name = name
        self._current_target = current_target
        self.previous_targets = []

    @property
    def current_target(self):
        return self._current_target

    @current_target.setter
    def current_target(self, target):
        self.previous_targets.append(self._current_target)
        self._current_target = target


# In previous solution is a DRY violation
#       which could be avoided using descriptors.


class TrackTargetsHistoryDescriptor:
    def __init__(self, target_history_name="previous_targets"):
        self.target_history_name = target_history_name

    def __set_name__(self, instance, _name):
        self._name = _name

    def __get__(self, instance, instance_class=None):
        return instance.__dict__[self._name]

    def __set__(self, instance, value):
        self._add_target_to_history(instance)
        instance.__dict__[self._name] = value

    def _set_default(self, instance):
        if not instance.__dict__.get(self.target_history_name):
            instance.__dict__[self.target_history_name] = []

    def _add_target_to_history(self, instance):
        self._set_default(instance)
        target = instance.__dict__.get(self._name)
        if target is not None:
            getattr(instance, self.target_history_name).append(target)


class BetterTraveler:
    current_target = TrackTargetsHistoryDescriptor("previous_targets")

    def __init__(self, name, current_target):
        self.name = name
        self.current_target = current_target


class BetterTransport:
    current_destination = TrackTargetsHistoryDescriptor("destinations_history")

    def __init__(self, name, current_target):
        self.name = name
        self.current_destination = current_target


traveller_example = {"name": "Jessica", "current_target": "Barcelona"}

transport_example = {"name": "VW Transporter 12", "current_target": "London"}
