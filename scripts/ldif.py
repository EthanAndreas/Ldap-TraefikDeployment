import csv
import os
import base64
import hashlib


def generate_group_ldif(user_info, gid):
    ldif = f"""
dn: cn={user_info['Login']},ou=Group,dc=ansible,dc=fr
objectClass: posixGroup
objectClass: top
cn: {user_info['Login']}
gidNumber: {gid}
"""
    return ldif


def generate_ssha_password(password):
    salt = os.urandom(4)
    salted_password = password.encode() + salt
    sha1_hash = hashlib.sha1(salted_password).digest()
    ssha_password = base64.b64encode(sha1_hash + salt).decode()
    return f"{{SSHA}}{ssha_password}"


def generate_user_ldif(user_info, uid, gid):
    dn = f"uid={uid},ou=People,dc=ansible,dc=fr"

    ldif = f"""
dn: {dn}
objectClass: top
objectClass: inetOrgPerson
objectClass: person
objectClass: organizationalPerson
objectClass: posixAccount
objectClass: shadowAccount
cn: {user_info['Firstname']} {user_info['Name']} 
sn: {user_info['Name']}
uid: {uid} 
givenName: {user_info['Firstname']}
userPassword: {generate_ssha_password(user_info['Password'])}
loginShell: /bin/bash
gidNumber: {gid}
uidNumber: {uid}
homeDirectory: /home/{uid}
"""
    return ldif


Group_ldif = """
dn: ou=Group,dc=ansible,dc=fr
objectClass: organizationalUnit
ou: Group
"""

People_ldif = """
dn: ou=People,dc=ansible,dc=fr
objectClass: organizationalUnit
ou: People
"""

i = 1000
with open("ansible/roles/openldap/templates/file.ldif.j2", "w") as file_ldif:
    file_ldif.write(Group_ldif)
    file_ldif.write(People_ldif)

    with open("assets/usr.csv", newline="") as csvfile:
        reader = csv.DictReader(csvfile, delimiter=";")
        for row in reader:
            user_ldif = generate_user_ldif(row, i, i)
            file_ldif.write(user_ldif)
            user_group_ldif = generate_group_ldif(row, i)
            file_ldif.write(user_group_ldif)
            i += 1
