from django.conf import settings
from django.db import connections, DatabaseError


def get_default_db(database_alias ='default'):
    """return database settings"""
    return settings.DATABASES[database_alias]


def get_default_vendor(database_alias ='default'):
    """return database vendor of the requested connection
    a DatabaseError exception can be raised"""
    # Check database connection
    connections[database_alias].ensure_connection()
    return connections[database_alias].vendor
