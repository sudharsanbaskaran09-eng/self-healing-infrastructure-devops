## Project: Self-Healing Infrastructure using Prometheus, Alertmanager & Ansible

This project demonstrates a production-style self-healing infrastructure that automatically detects service failures and performs recovery actions without manual intervention. It follows real-world Site Reliability Engineering (SRE) practices by combining monitoring, alerting, and automated remediation.

The system continuously monitors services using Prometheus. When a failure is detected, an alert is triggered and routed through Alertmanager, which then invokes an automated recovery workflow using Ansible to restore the failed service.

---

## Problem Statement
In real-world production environments, service downtime can lead to business impact and revenue loss. Manual monitoring and recovery increase Mean Time to Recovery (MTTR) and are error-prone.

This project addresses that problem by implementing an automated, self-healing mechanism that detects failures early and restores services automatically.

---

## Solution Overview
The solution implements an end-to-end self-healing workflow:
- Continuous monitoring of services
- Automated alerting on failure detection
- Event-driven remediation using Ansible
- Automatic service recovery without human intervention

---

## Architecture
Service (NGINX / Node Exporter)
|
v
Prometheus (Monitoring & Alert Rules)
|
v
Alertmanager (Alert Routing)
|
v
Webhook Listener
|
v
Ansible Playbook (Auto-Healing)
|
v
Service Restart & Recovery

---

## Key Features
- Real-time monitoring using Prometheus
- Alert-based failure detection
- Alert routing with Alertmanager
- Automated remediation using Ansible
- Docker-based service orchestration
- Zero manual intervention during recovery
- Production-style incident lifecycle simulation

---

## Technology Stack
- Prometheus – Metrics collection and alerting
- Alertmanager – Alert routing and handling
- Ansible – Automated remediation
- Docker & Docker Compose – Service orchestration
- Python – Webhook listener
- Linux (WSL Ubuntu) – Execution environment

---

## How It Works
1. Prometheus continuously monitors services
2. A service failure is detected (e.g., node_exporter stopped)
3. Prometheus fires an alert based on alert rules
4. Alertmanager receives and routes the alert
5. Alertmanager triggers a webhook
6. The webhook executes an Ansible playbook
7. Ansible restarts the failed service
8. Prometheus detects recovery and resolves the alert

---

## Failure Simulation
- Service is intentionally stopped to simulate a real incident
- Alert transitions from Inactive → Firing
- Automated recovery is triggered
- Service is restored automatically
- Alert transitions from Firing → Inactive

This validates the complete self-healing workflow.

---

## Key Learnings
- Designing production-style monitoring systems
- Writing meaningful alert rules
- Understanding alert routing and escalation
- Automating recovery workflows using Ansible
- Debugging real-world DevOps and SRE issues
- Building reliable and resilient infrastructure

---

## Real-World Relevance
This project reflects how modern DevOps and SRE teams:
- Reduce MTTR
- Automate incident response
- Build resilient systems
- Eliminate repetitive manual recovery tasks

