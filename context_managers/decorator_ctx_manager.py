"""
    Using context manager as decorator has one main flaw:
          Object can not be passed
          between __enter__, code and __exit__

    Also with key word cannot be used
"""
from contextlib import ContextDecorator

# Let's imagine a offline database backup job
#  backup can be performed only if db
#  is switched off, after backup
#  it has to be switched on indepndly
#  upon backup fail/success


def stop_database():
    print("Stopping database")


def start_databse():
    print("Starting database")


class DatabaseManager(ContextDecorator):
    def __enter__(self):
        stop_database()

    def __exit__(self, exc_type, exc_value, exc_tryceback):
        start_databse()


@DatabaseManager()
def backup_database_offline():
    print("Backuping database")


backup_database_offline()
