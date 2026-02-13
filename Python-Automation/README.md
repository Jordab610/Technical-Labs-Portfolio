# Technical Portfolio: Hybrid Systems Admin & SRE Mindset

This repository is a live documentation of my professional development, bridging the gap between System Administration and Site Reliability Engineering. My goal is to apply software engineering principles to improve infrastructure reliability, scalability, and efficiency.

## 🎯 Development Goals
* **Automate for Reliability:** Utilizing Python to automate repetitive manual tasks, reducing human error.
* **Resilient Tooling:** Implementing SRE-level standards (try/except blocks, input normalization) to build robust, crash-proof tools.
* **Data-Driven Operations:** Parsing system logs and inventory data to generate actionable incident reports.

## 📈 Technical Evolution (Project Logs)

### Phase 1: Foundational Logic & Data Persistence
*Focus: Mapping infrastructure data and interacting with the file system for automated analysis.*

* **System Log Parser (`log_parser.py`)** - *Feb 12, 2026*
    * Implemented **File I/O** to scan external `server_logs.txt`.
    * Built a **Resilient Data Pipeline** using `try/except` to catch `FileNotFoundError` and ensure graceful failure.
    * Uses dictionary aggregation to provide a summary report of system errors.
* **SRE-Mindset Asset Finder (`sre_asset_finder.py`)** - *Feb 9, 2026*
    * Designed for resilient asset lookups; uses `try/except` for error handling and `.strip().lower()` for input normalization.
* **Advanced Health Check (`master_check.py`)** - *Feb 6, 2026*
    * Simulates a network scan by mapping inventory to status dictionaries with $O(1)$ efficiency.

## 🛠️ Tech Stack & Skills
* **Languages:** Python (File I/O, Exception Handling, Data Structures)
* **Infrastructure:** Systems Administration (Linux/Windows), Log Analysis, Troubleshooting.
* **Version Control:** Git / GitHub.

---
*Professional Log maintained by a Technical Support professional at Astreya (Google Support).*