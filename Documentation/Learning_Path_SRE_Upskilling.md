# Learning Path: From IT Support to SRE

> **Purpose:** This document is my personal roadmap and commitment to upskilling. I use it to stay intentional about *how* I learn—not just what I build—so I can improve AI-produced code, test for reliability, and grow my infrastructure skills. Recruiters: this shows I'm actively building habits that reduce downtime and improve user support.

---

## 1. Why This Matters (The "Why" Behind the Plan)

**SRE** stands for **Site Reliability Engineering**. In practice, it means:

- **Reliability:** Systems stay up; users don’t hit unexpected downtime.
- **Observability:** When something breaks, we can see *what* and *why* quickly.
- **Reducing toil:** Automating repetitive work so we focus on improvements, not firefighting.

To get there, I need to:

1. **Understand code, not just run it** — So I can fix and improve what AI (or anyone) produces.
2. **Test before “shipping”** — So changes don’t cause outages.
3. **Build infrastructure skills** — Servers, networks, and automation are the foundation.

This learning path is how I’m building those habits in my portfolio projects.

---

## 2. Improving Code (Including AI-Generated Code)

AI can write a script quickly, but *I* am responsible for whether it’s correct, safe, and maintainable. Here’s how I approach it.

### 2.1 Read Line-by-Line and Summarize

**What:** After getting code (from AI or elsewhere), I read every line and write a one-line summary of what it does.

**Why:** If I can’t explain it, I don’t truly understand it. Understanding is the first step to improving and debugging.

**Example (from a script):**
- `chmod +x *.sh` → “Makes all `.sh` files in this directory executable so the shell can run them.”
- `if command -v gh &> /dev/null` → “Checks if the `gh` command exists by sending its output to ‘nowhere’ so we don’t clutter the screen.”

### 2.2 Ask “What Could Go Wrong?”

**What:** For each script or change, I list at least 2–3 failure cases.

**Why:** Users hit edge cases (wrong folder, missing file, no permissions). Thinking about failure *before* deployment prevents downtime.

**Examples:**
- Script assumes it’s run from a specific directory → **Improvement:** Use absolute paths or check current directory.
- Script doesn’t check if a file exists before reading → **Improvement:** Add an `if [ -f "file" ]` (or Python equivalent) and exit with a clear error.

### 2.3 Make One Improvement Yourself

**What:** For every AI-generated (or copied) script, I change or add at least one thing on my own (e.g., better error message, a safety check, a comment).

**Why:** Small, deliberate edits build confidence and ensure I’m not just “accepting” code blindly. It also shows in my portfolio that I can extend and harden code.

---

## 3. Testing So Users Don’t Deal With Downtime

Testing doesn’t have to mean a full test suite from day one. It means **checking behavior before it affects users**.

### 3.1 “Happy Path” Test

**What:** Run the script with the *expected* inputs and environment (e.g., correct folder, file present).

**Why:** Confirms the script does what I think it does in the normal case. If it fails here, it would definitely fail for users.

### 3.2 “Sad Path” Test (Break It on Purpose)

**What:** Run the script in a “wrong” scenario: wrong directory, missing file, no permissions, empty input.

**Why:** Ensures the script fails *safely* (clear error, no data loss) instead of crashing in a confusing way. This is how we avoid surprises in production.

### 3.3 Document What You Tested

**What:** In each project’s README or Project_Template, I write a short “Verification & Testing” section: what I ran, what I broke on purpose, and what “success” looked like.

**Why:** Recruiters and future-me can see that I take reliability seriously. It also forces me to think through scenarios before I say “done.”

---

## 4. Infrastructure Skills (What I’m Building Toward)

SRE sits at the intersection of **software** and **infrastructure**. I’m growing both.

### 4.1 Concepts I’m Learning (With “What” and “Why”)

| Concept | What it is (simple) | Why it matters for SRE |
|--------|----------------------|-------------------------|
| **IP & subnets** | How machines get addresses and how networks are split (e.g., 192.168.1.0/24) | So I can design and troubleshoot networks and firewall rules. |
| **DNS** | System that turns names (e.g., `web-01`) into IP addresses | Most outages and slowness tie back to DNS or naming. |
| **Logs** | Files or streams where apps and OS write what they did and what went wrong | First place we look when something breaks (observability). |
| **Process management** | How the OS runs and restarts services (systemd, cron, etc.) | So services come back after a reboot or crash (reliability). |
| **Containers (e.g., Docker)** | Lightweight, consistent “boxes” to run an app and its dependencies | Foundation for modern deployments and consistency across dev/prod. |

### 4.2 How I’m Practicing

- **Linux-Administration:** Scripts that check system health, clean logs, and set up environments (directly tied to observability and toil reduction).
- **Networking-Windows:** Domain Controller and identity labs (understanding how enterprise networks and auth work).
- **Python-Automation:** Scripts that could talk to APIs, parse logs, or drive health checks (foundation for automation and tooling).

Every project in this repo is chosen to stretch one of these areas and is documented with the [Project Template](./Project_Template.md).

---

## 5. How This Shows Up in My Portfolio

- **Project write-ups** use the template with **Challenges & Troubleshooting** and **Verification & Testing** so it’s clear I test and reflect.
- **Code** includes comments or README sections that explain *why* a choice was made, not just *what* the code does.
- **This document** shows that I have a structured approach to learning and to validating code before it affects users.

I update this path as I add new skills and projects. Last focus: *improving and testing AI-generated code*, *documenting what I learned*, and *practicing infrastructure in labs*.
