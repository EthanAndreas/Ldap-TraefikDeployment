#!/bin/bash

echo "\033[34mGenerate ldif file\033[0m"
/bin/python3 scripts/ldif.py

echo "\033[34mStart ansible\033[0m"
ansible-playbook -i ansible/inventory.yaml ansible/playbook_tpl.yaml