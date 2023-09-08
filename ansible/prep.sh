#!/bin/bash

# Update the server
sudo apt update && sudo apt upgrade -y

# Install Ansible
sudo apt install ansible -y

# Run the Ansible playbook
# ansible-playbook playbook.yml