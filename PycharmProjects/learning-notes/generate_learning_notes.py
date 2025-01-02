import os
import subprocess
import random
from datetime import datetime, timedelta

# === Config ===
start_date = datetime(2023, 1, 1)
end_date = datetime(2023, 7, 31)
author_name = "Aman Jain"
author_email = "amanjain0411@gmail.com"
commit_msg = "Learning progress"
file_extensions = ['.py', '.md', '.html', '.css', '.json', '.txt', '.h5']

# === Generator ===
current_date = start_date

while current_date <= end_date:
    # Randomly choose whether to commit on this day (~50% chance)
    if random.random() < 0.5:
        num_commits_today = random.randint(1, 2)  # 1-2 commits per day

        for _ in range(num_commits_today):
            ext = random.choice(file_extensions)
            filename = f"note_{current_date.strftime('%Y%m%d')}_{random.randint(100,999)}{ext}"

            # Create dummy content
            with open(filename, "w") as f:
                f.write(f"Commit on {current_date.strftime('%Y-%m-%d')} at {datetime.now().time()}")

            commit_time = current_date + timedelta(
                hours=random.randint(9, 20),
                minutes=random.randint(0, 59)
            )
            commit_date_str = commit_time.strftime("%Y-%m-%dT%H:%M:%S")

            # Git add and commit
            subprocess.run(["git", "add", filename])
            subprocess.run([
                "git", "commit",
                f"--date={commit_date_str}",
                f"--author={author_name} <{author_email}>",
                "-m", f"{commit_msg} on {commit_time.strftime('%Y-%m-%d %H:%M')}"
            ])

    # Move to next day
    current_date += timedelta(days=1)

# Final push
subprocess.run(["git", "push", "origin", "main"])
