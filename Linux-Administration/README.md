# Live Portfolio: Engineering High-Reliability Systems
This repository is a transparent record of my professional evolution. I am currently applying **SRE (Site Reliability Engineering) Standards** to System Administration tasks.

## 🎯 The SRE Standard
- **Toil Reduction:** Automating repetitive setup and maintenance tasks.
- **Observability:** Building tools that provide visibility into system health.
- **Operational Excellence:** Maintaining production-grade documentation.

## 🛠️ Active Projects

### 🏗️ Automated Environment Setup (`install.sh`)
* **Purpose:** A "Bootstrap" script that prepares the local environment for execution.
* **Features:** - Batch-updates permissions (`chmod +x`) for all project scripts.
  - Performs dependency checks (e.g., verifying GitHub CLI installation).

### 🖥️ Proactive Health Monitoring (`check_system.sh`)
* **SRE Application:** Monitoring **Saturation**. Identifies when disk or memory limits reach critical thresholds.
* **Skillset:** Log-parsing with `grep` and resource auditing.

### 🧹 Maintenance Automation (`cleanup_logs.sh`)
* **SRE Application:** Managing **Technical Debt**. Ensures system performance by removing stale data.
* **Skillset:** Time-based file manipulation and audit logging.

## 🚀 Getting Started (SRE Deployment)
To deploy this toolkit on a new macOS/Linux workstation:

1. **Clone the Repo:**
   ```bash
   gh repo clone Jordab610/Linux-System-Automation
   cd Linux-System-Automation
