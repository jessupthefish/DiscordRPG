import sys
from database_handler import RPGDatabase

db = RPGDatabase()


# Helper functions
def str_to_class(classname):
    return getattr(sys.modules[__name__], classname)
