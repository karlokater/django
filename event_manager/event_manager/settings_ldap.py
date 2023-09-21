import ldap
from django_auth_ldap.config import (
    LDAPSearch,
    LDAPGroupQuery,
    GroupOfNamesType,
    PosixGroupType,
)

AUTH_LDAP_SERVER_URI = "ldap://192.168.178.40"
AUTH_LDAP_BIND_DN = "cn=admin,dc=example,dc=com"
AUTH_LDAP_BIND_PASSWORD = "password123"
AUTH_LDAP_USER_SEARCH = LDAPSearch(
    "dc=example,dc=com", ldap.SCOPE_SUBTREE, "(uid=%(user)s)"
)
AUTH_LDAP_GROUP_SEARCH = LDAPSearch(
    "dc=example,dc=com", ldap.SCOPE_SUBTREE, "(objectClass=top)"
)
AUTH_LDAP_GROUP_TYPE = PosixGroupType(name_attr="cn")

# wenn eingeloggt, werden alle ldap groups und user unter
# gruppe angelegt.
AUTH_LDAP_MIRROR_GROUPS = True

# Populate the Django user from the LDAP directory.
AUTH_LDAP_REQUIRE_GROUP = "cn=enabled+gidNumber=501,ou=groups,dc=example,dc=com"

# um User zu blockieren, kann man sie der DENY Gruppe zurordnen
AUTH_LDAP_DENY_GROUP = "cn=disabled+gidNumber=504,ou=groups,dc=example,dc=com"

AUTH_LDAP_USER_ATTR_MAP = {
    "first_name": "givenName",
    "last_name": "sn",
    "email": "mail",
    "username": "uid",
    "password": "userPassword",
}
AUTH_LDAP_PROFILE_ATTR_MAP = {"home_directory": "homeDirectory"}
AUTH_LDAP_USER_FLAGS_BY_GROUP = {
    "is_active": "cn=active+gidNumber=500,ou=groups,dc=example,dc=com",
    "is_staff": "cn=staff+gidNumber=502,ou=groups,dc=example,dc=com",
    "is_superuser": "cn=superuser+gidNumber=504,ou=groups,dc=example,dc=com",
    #    "is_active": "cn=active+gidNumber=500,ou=groups,dc=example,dc=com",
    #    "is_staff": "cn=staff+gidNumber=503,ou=groups,dc=example,dc=com",
    #    "is_superuser": "cn=superuser+gidNumber=502,ou=groups,dc=example,dc=com"
}

AUTH_LDAP_ALWAYS_UPDATE_USER = True
AUTH_LDAP_FIND_GROUP_PERMS = True
AUTH_LDAP_CACHE_TIMEOUT = 3600

AUTH_LDAP_FIND_GROUP_PERMS = True


# Keep ModelBackend around for per-user permissions and maybe a local
# superuser.
AUTHENTICATION_BACKENDS = (
    "django_auth_ldap.backend.LDAPBackend",   # LDAP Zugriff
    "django.contrib.auth.backends.ModelBackend",  # Standard
    # 'ldaptest.backend_ldap.CustomLDAPBackend',
)
