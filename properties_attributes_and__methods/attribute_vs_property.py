"""
     Attributes are good for holding a value.

     Properties are good if value access or
         assignment should be restricted.
"""
import re
EMAIL_FORMAT = re.compile("[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+")


def is_email(email: str) -> bool:
    return re.match(EMAIL_FORMAT, email) is not None


class User:
    def __init__(self, username):
        # Username is attribute as any
        #   username is good
        self.username = username

        # Email is property as it has to be
        #  restricted to xxx@yyy.zzz syntax
        self._email = None

    # using property decorator
    # as a getter function
    @property
    def email(self):
        return self._email

    # a setter function
    @email.setter
    def email(self, new_email):
        if not is_email(new_email):
            raise ValueError("'{}' is in wrong email format".format(new_email))

        self._email = new_email


WRONG_EMAIL = "abc"
GOOD_EMAIL = "mark@gmail.com"

mark = User("mark")

mark.email = GOOD_EMAIL

print(mark.email)

mark.email = WRONG_EMAIL
