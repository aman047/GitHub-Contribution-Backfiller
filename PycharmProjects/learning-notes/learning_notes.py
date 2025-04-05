import os
import random
import subprocess
from datetime import datetime, timedelta

# Configuration
start_date = datetime(2023, 1, 1)
end_date = datetime(2023, 12, 31)
author_name = "Aman Jain"
author_email = "amanjain0411@gmail.com"
commit_msg_base = "Learning progress"

# File types to simulate realistic learning
file_types = [
    ".py", ".ipynb", ".md", ".html", ".css", ".sql", ".h5", ".csv", ".json", ".txt"
]

# Simulated directories in the learning-notes repo
directories = [
    "Python", "Machine-Learning", "Deep-Learning", "Web-Dev", "SQL", "Notes", "Data"
]

# Set working directory to the repo (adjust if needed)
repo_dir = os.path.abspath("learning-notes")
os.makedirs(repo_dir, exist_ok=True)
os.chdir(repo_dir)

current_date = start_date
committed_dates = []

while current_date <= end_date:
    if random.random() < 0.75:  # ~75% chance to commit on a given day
        # Random file path and content
        dir_choice = random.choice(directories)
        ext_choice = random.choice(file_types)
        filename = f"{dir_choice}/log_{current_date.strftime('%j')}{ext_choice}"
        os.makedirs(os.path.dirname(filename), exist_ok=True)

        with open(filename, "w", encoding="utf-8") as f:
            f.write(f"Simulated work on {current_date.strftime('%Y-%m-%d')}")

        # Random time
        hour = random.randint(9, 22)
        minute = random.randint(0, 59)
        second = random.randint(0, 59)
        date_str = current_date.replace(hour=hour, minute=minute, second=second).isoformat()

        # Git add and commit
        subprocess.run(["git", "add", filename])
        subprocess.run([
            "git", "commit",
            f"--date={date_str}",
            f"--author={author_name} <{author_email}>",
            "-m", f"{commit_msg_base} on {current_date.strftime('%Y-%m-%d')}"
        ])
        committed_dates.append(current_date.strftime('%Y-%m-%d'))

    # Increment by 1 to 3 days
    current_date += timedelta(days=random.randint(1, 3))

# Final push
subprocess.run(["git", "push", "origin", "main"])

committed_dates[:10]  # Return first few commit dates for verification
