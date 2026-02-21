#!/bin/bash

echo "Auto-heal triggered at $(date)" >> /tmp/autoheal.log
ansible-playbook /root/self-healing-infrastructure-devops/ansible/restart_node_exporter.yml >> /tmp/autoheal.log 2>&1

#!/bin/bash

chmod +x scripts/autoheal.sh
