from typing import NamedTuple, List

from ldap3 import Server, Connection, MOCK_SYNC
from ldap3.core.exceptions import LDAPException


class LdapAttributes(NamedTuple):
    """place holder for ldap attributes.
    if more attributes are needed, add them here.
    must be identical to the LDAP names."""

    givenName: str
    sortableSurname: str
    cn: List[str]  # this comes as a list, don't ask why.
    employeeNumber: str
    emplId: str
    mail: str
    uid: str
    accountStatus: str


class LDAPNoUsernameError(Exception):
    def __init__(self, *args, anr=None, **kwargs):
        self.anr = anr
        super().__init__(args, kwargs)

    def __str__(self):
        return f"User {self.anr} does not have an ID. Did you close VPN?"


class LDAPUserNotActive(Exception):
    """
    Raise when employee or student is added who is disabled.
    """

    def __init__(self, attr: LdapAttributes):
        self.attr = attr
        self.message = (
            f"{self.attr.employeeNumber}-{self.attr.emplId}-{self.attr.cn} is disabled"
        )

    def __str__(self):
        return self.message


class LDAPNumberNotFoundError(Exception):
    def __init__(self, type: str, number: str):
        """
        type
        :param type: student or employee
        :param number: student number or employee number
        """
        self.type = type
        self.number = number
        s = "ANR" if type == "Employee" else "Student number"
        self.message = f"{type} {s} {number} not found!"

    def __str__(self):
        return self.message


class LDAPError(Exception):
    pass


def search_ldap(attribute: str, value: str) -> LdapAttributes:  # noqa: C901
    """Searches the Tilburg University LDAP server for the given username and returns
    a tuple of first name, last name, full name, ANR, emplId and email address.
    Permission has been granted by TiU's legal department for
    retrieving this data. Raises LDAPError on any kind of error."""
    LDAP_MOCK = None

    baseDN = "o=Universiteit van Tilburg,c=NL"
    searchFilter = "(" + attribute + "={})".format(value)

    response = None
    try:
        server = Server("ldaps.uvt.nl", use_ssl=True)
        if LDAP_MOCK is None:
            conn = Connection(server, auto_bind=True)
        else:
            conn = Connection(server, client_strategy=MOCK_SYNC)
            try:
                conn.strategy.entries_from_json(LDAP_MOCK)
                conn.bind()  # no automatic bind for a mock ldap server connection
            except FileNotFoundError as E:
                logger.error(f"file {LDAP_MOCK} not found or {E}")
        conn.search(baseDN, searchFilter, attributes=LdapAttributes._fields)
        response = conn.response[0]["attributes"]  # ignore all other stuff
        for key in response:
            if type(response[key]) == list and len(response[key]) > 0:
                response[key] = response[key][0]
        attributes = LdapAttributes(**response)
        if not attributes.uid:
            raise LDAPNoUsernameError
        if attributes.accountStatus == "Disabled":
            raise LDAPUserNotActive(attributes)
        return attributes
    except LDAPException as E:
        raise LDAPError(f"Cannot connect due to {E}")
    # No username returned is assumed to be an error, coz we need it!
    except LDAPNoUsernameError as E:
        raise LDAPError(f"Cannot connect due to {E}")
    except IndexError:
        t = "Student" if attribute == "emplId" else "Employee"
        ex = LDAPNumberNotFoundError(type=t, number=value)
        raise ex
    except LDAPUserNotActive:
        raise
    except (Exception) as E:
        raise LDAPError(f"Error in LDAP query, {response}")


def search_anr_in_ldap(anr):
    return search_ldap("employeeNumber", anr)


def search_student_number_in_ldap(student_number):
    return search_ldap("emplId", student_number)


def search_username_in_ldap(username):
    return search_ldap("uid", username)
