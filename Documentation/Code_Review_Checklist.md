# Code Review Checklist (Including AI-Generated Code)

Use this checklist **before** you consider any script or change "done"—especially when the first draft came from AI. The goal is to *understand* and *harden* the code so users don’t hit downtime or confusing errors.

---

## 1. Understanding

- [ ] I read every line and can explain what each block does in one sentence.
- [ ] I know what **inputs** the script expects (files, paths, env vars, arguments).
- [ ] I know what **output** or **side effects** it has (prints, files created, services restarted).

**Why:** If you can’t explain it, you can’t safely change it or debug it when it fails.

---

## 2. Failure Modes (“What Could Go Wrong?”)

- [ ] I listed at least 2–3 ways this could fail (wrong directory, missing file, no permissions, bad input).
- [ ] For each failure, the script either **handles it** (clear error message, exit code) or I **documented** that it’s assumed (e.g., “Must be run from project root”).

**Why:** Users and production hit edge cases. Thinking about them in advance prevents surprises and downtime.

---

## 3. Safety & Clarity

- [ ] Destructive actions (delete, overwrite, restart) are clear in the code or README.
- [ ] Error messages are **actionable** (e.g., “File X not found; create it or run from directory Y”).
- [ ] I added or improved at least **one** thing myself (comment, check, or error message).

**Why:** Safe, clear behavior builds trust and makes support faster when something does go wrong.

---

## 4. Fit for the Portfolio

- [ ] README or project doc states **purpose** and **how to run** the script.
- [ ] Any non-obvious choice has a short **“why”** in a comment or in the doc.

**Why:** Recruiters and future-you benefit from clear intent and reasoning.

---

*Keep this checklist next to you when reviewing AI output or your own code. Checking every box doesn’t take long and becomes habit over time.*
