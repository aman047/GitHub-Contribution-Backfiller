
## 📘 `GitHub Contribution Backfiller`  
> _Automated Backdated Commits with Python & Git_  
A personal experiment in scripting GitHub contributions to simulate learning progress and explore Git internals.

---

### 🛠️ Project Overview

This project demonstrates how to programmatically generate and backdate Git commits using Python. The goal was to build a contribution timeline that reflects structured learning across different topics — using a mix of realistic file types and folders.

Rather than manually committing, I wrote a script to automate:
- File creation (code, notes, models, etc.)
- Git add/commit with **custom timestamps**
- Randomized commit patterns to resemble real work
- Contribution simulation across multiple years (2022–2025)

---

### 🚀 Features

✅ **Backdated Commits**  
Simulates commits with specific past dates using `--date` and `--author` in Git.

✅ **Randomized Patterns**  
Commits 3–4 times per week with different times and filenames to avoid obvious patterns.

✅ **Multi-File Support**  
Works with various extensions: `.py`, `.md`, `.ipynb`, `.html`, `.css`, `.h5`, `.json`, `.txt`, etc.

✅ **Structured Directory Layout**  
Organizes commits across folders like `Python/`, `ML/`, `Web-Dev/`, `Data/`, etc.

✅ **Batch Push**  
Pushes all commits at once for efficient syncing.

---

### 🧠 What I Learned

- Deep dive into **Git internals** and commit manipulation
- Handling **author identity** and GitHub email verification
- Automating workflows with **Python subprocess** and Git CLI
- Ethics and perception around GitHub contributions
- File system handling and randomized scripting

---

### 📂 Sample Output Structure
```
learning-notes/
├── Python/
│   └── log_20230104.py
├── Web-Dev/
│   └── log_20230215.html
├── Data/
│   └── log_20230312.csv
├── README.md
```

---

### 🧩 How It Works

```bash
python backdate_commits_2025.py
```

The script:
1. Chooses a random day in each week (3–4 days/week)
2. Creates a file with a random type and message
3. Backdates the commit
4. Repeats for a date range (e.g., Jan–Mar 2025)

---

### ⚠️ Ethical Note

This project was built for **learning purposes**. While it demonstrates how GitHub tracks contributions, it's not meant to deceive. Always be transparent when showcasing projects like this.

---

### ✨ Inspired Use Cases
- Simulating educational progress
- Testing contribution heatmaps
- Teaching Git basics in a visual way
- Generating mock Git activity for tutorials/demos

---

### 📌 Author

**Aman Jain**  
🟢 GitHub: [@aman047](https://github.com/aman047)  
📧 Email: amanjain0411@gmail.com

---

Let me know if you want a version tailored to your `learning-notes` repo specifically — I can plug in the actual folder names too. Want that?
