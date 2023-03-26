#!/usr/bin/python3
"""
domain users faker for ansible

ansible-playbook playbook.yml \
-e '$(python3 fakergen.py | jq -c -r '.')'
"""

import random
import sys

from faker import Faker
from unidecode import unidecode
import json

if len(sys.argv) > 1:
    USERS_MAX = int(sys.argv[1])
else:
    USERS_MAX = 100

users_model = [
  {'locale': 'fr_FR', 'proportion': 40},
  {'locale': 'nl_BE', 'proportion': 40},
  {'locale': 'it_IT', 'proportion': 5},
  {'locale': 'es_ES', 'proportion': 5},
  {'locale': 'de_DE', 'proportion': 5},
  {'locale': 'en_GB', 'proportion': 5},
]

groups = [
  {'name': 'Direction', 'proportion': 25},
  {'name': 'Accounting', 'proportion': 10},
  {'name': 'Business', 'proportion': 15},
  {'name': 'Marketing', 'proportion': 10},
  {'name': 'Sales', 'proportion': 10},
  {'name': 'Production', 'proportion': 20},
  {'name': 'IT', 'proportion': 25},
  {'name': 'Facilities', 'proportion': 10},
  {'name': 'R & D', 'proportion': 25},
]

groups_proportion = []
groups_name = []

for group_params in groups:
    group_name = group_params['name']
    group_proportion = group_params['proportion']
    groups_name.append(group_name)
    groups_proportion.append(group_proportion)


def password_generator(firstname, surname):
    """
    Password Generator
    """
    return ''.join([str(x).upper()
                    for x in random.choices(list(firstname), k=1)]
                   + [str(x) for x in random.choices(list(range(0, 9)),
                      k=4)]
                   + random.choices(['%', '!', '#'])
                   + [str(x).lower()
                      for x in random.choices(list(surname), k=1)])


domain_users = []

for definition in users_model:
    fake = Faker(definition['locale'])
    USERS_NUMBER = int(USERS_MAX * definition['proportion'] / 100)
    for _ in range(USERS_NUMBER):
        firstname = unidecode(fake.first_name())
        surname = unidecode(fake.last_name())
        group = random.choices(groups_name, weights=(groups_proportion))
        domain_users.append({'firstname': firstname,
                             'surname': surname,
                             'groups': group,
                             'password': password_generator(firstname,
                                                            surname)})

print(json.dumps({'domain_users': domain_users}))
