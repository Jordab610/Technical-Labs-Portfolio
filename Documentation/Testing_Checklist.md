# Testing Checklist (Before You “Ship”)

Use this **before** you mark a script or change as ready for others (or for your portfolio). The goal is to catch problems *before* users see downtime or confusing failures.

---

## 1. Happy Path (Normal Use)

- [ ] I ran the script in the **intended** environment (correct directory, required files present, expected permissions).
- [ ] The result matched what I expected (output, files created, or state changed as described).
- [ ] I noted the **success criteria** (e.g., “Script prints OK for all 4 servers” or “Log file is created under `/var/log/...`”).

**Why:** If it doesn’t work in the normal case, it will definitely fail for users. Documenting success criteria helps you and others verify later.

---

## 2. Sad Path (Break It on Purpose)

- [ ] I ran the script from the **wrong directory** (if it assumes a path). Result: clear error, no silent wrong behavior.
- [ ] I removed or renamed a **required file** (if any). Result: script reports the problem instead of crashing oddly.
- [ ] I tested with **missing permissions** if the script needs to read/write/execute something. Result: failure is obvious and safe.

**Why:** Production and real users hit these cases. Failing in a predictable, safe way is better than corrupting data or leaving the system in a bad state.

---

## 3. Documentation

- [ ] I added a short **“Verification & Testing”** (or similar) section in the project README or write-up.
- [ ] I wrote **what I ran** (commands or steps) and **what “success” looked like** (output or state).
- [ ] If I found a bug while testing, I fixed it or documented it as a known limitation.

**Why:** Recruiters see that you test deliberately. Future-you can re-run the same checks after changes. It also reinforces the habit of “define success before you’re done.”

---

*Run through this for every script or automation you add to the portfolio. It gets faster with practice and directly supports reliability and user support.*
