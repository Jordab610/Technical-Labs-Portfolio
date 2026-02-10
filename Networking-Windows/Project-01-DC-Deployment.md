# Lab 01: Windows Server 2022 Installation & Base Configuration

## 1. Executive Summary
**Objective:** Deploy a foundational Windows Server 2022 instance to serve as the Primary Domain Controller (DC) for a hybrid lab environment.
**Tech Stack:** Windows Server 2022 Datacenter, Oracle VM VirtualBox 7.
**Key Skills:** Virtualization management, Resource Provisioning, Enterprise Naming Conventions.

---

## 2. Architecture & Design
**Hardware Provisioning (Host: 32GB RAM):**
* **vCPU:** 2 Cores
* **RAM:** 8192 MB (8GB)
* **Storage:** 60GB Dynamically Allocated VDI
* **Network Mode:** NAT (Initial phase for updates)

**Network Logic:**
* **Hostname:** `SVR-DC01`
* **IP Address:** `10.0.0.10` (Static)
* **Gateway:** `10.0.0.1`
* **DNS:** `127.0.0.1` (Self-referencing for AD DS)

---

## 3. Implementation Steps
1. **VM Creation:** Configured VirtualBox container with optimized specs for 32GB host.
2. **ISO Boot:** Attached Windows Server 2022 ISO and bypassed Unattended Installation to ensure manual control over OS version.
3. **OS Selection:** Selected **Windows Server 2022 Datacenter (Desktop Experience)**.
4. **Initial Setup:** Renamed Server and setup network logic.
![Initial Server Setup Proof](Initial-Setup.png)
---

## 4. Design Decisions (The "Senior Tech" Perspective)
* **Why 8GB RAM?** Given the 32GB host capacity, 8GB was allocated to ensure the GUI and future Active Directory services remain highly responsive during heavy lab testing.
* **Why Static IP?** Core infrastructure must have a fixed address to prevent DNS resolution failures and authentication outages for client machines.