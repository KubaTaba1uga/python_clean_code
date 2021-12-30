"""
        Inheritance should be used only to specialize object
            within domain that it was designed it mind.

        Mixing implementation logic with buissness logic
            is one of bad inheritance example.
"""

# Imagine a system for inssurance company
#    where policy has to be applied to specified
#    customer.
# Let's use dictionary to make that available.
from collections import UserDict
from datetime import date

POLICY_DATA = {"0": {"fee": 1000.0, "expiration_date": date(2022, 1, 1)}}
NEW_POLICY_DATA = {"fee": 1100.0, "expiration_date": date(2023, 1, 1)}


# Bad inheritance
class InsurancePolicy(UserDict):
    # UserDict gives extra behaviours
    #   beyond required ones which are
    #   not necesserly needed and could
    #   lead to misinterprentations about
    #   API usage
    def change_in_policy(self, customer_id, **policy_data):
        self[customer_id].update(**policy_data)


new_policy = InsurancePolicy(POLICY_DATA)
print("Policy before change", new_policy["0"])

new_policy.change_in_policy("0", fee=1100.0)
print("   Policy after change", new_policy["0"])

print("All policy behaviours", dir(new_policy), end="\n\n")


# Good composition
class InsurancePolicy:
    # Object has only needed behaviours
    # Dictionary bahaviours are decoupled
    #    from object itself.
    def __init__(self, policy_data):
        self._policy_data = policy_data

    def change_in_policy(self, customer_id, **policy_data):
        self._policy_data[customer_id].update(**policy_data)

    def __getitem__(self, customer_id):
        return self._policy_data[customer_id]

    def __len__(self):
        return len(self._policy_data)


new_policy = InsurancePolicy(POLICY_DATA)
print("Policy before change", new_policy["0"])

new_policy.change_in_policy("0", fee=1100.0)
print("   Policy after change", new_policy["0"])

print("All policy behaviours", dir(new_policy))
