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

def regions_as_select(regions):
    s = '<select id="select-regions" class="form-control">'
    s = s + f'<option value="">Choose region</option>'
    for region in regions:
        s =  s + f'<option value="{region.id}">'+region.name+'</option>'
    s = s + '</select>'
    return s

def countries_as_select(countries):
    s = '<select id="select-countries" class="form-control">'
    s = s + f'<option value="">Choose country</option>'
    for country in countries:
        s =  s + f'<option value="{country.id}">'+country.name+'</option>'
    s = s + '</select>'
    return s