import os
import random
import subprocess
from datetime import datetime, timedelta

# Topics and folders
topics = {
    "python": ["lambda_functions", "file_handling", "list_comprehension"],
    "machine-learning": ["regression_vs_classification", "model_evaluation", "overfitting_underfitting"],
    "data-science": ["data_cleaning", "eda", "feature_engineering"],
    "sql": ["joins_cheatsheet", "window_functions", "groupby_having"],
    "powerbi": ["creating_dashboards", "measures_vs_columns"],
    "cloud": ["aws_ec2_s3", "gcp_bigquery", "cloud_intro"]
}

# Repo path
repo_path = os.getcwd()

# Date range
start_date = datetime(2025, 1, 1)
end_date = datetime(2025, 3, 11)

# Create folders
for folder in topics:
    folder_path = os.path.join(repo_path, folder)
    os.makedirs(folder_path, exist_ok=True)

# Generate commits
current_date = start_date
while current_date <= end_date:
    if random.random() < 0.65:  # 65% chance to commit on a day
        commit_count = random.randint(1, 3)
        for _ in range(commit_count):
            topic_folder = random.choice(list(topics.keys()))
            file_topic = random.choice(topics[topic_folder])
            file_path = os.path.join(repo_path, topic_folder, f"{file_topic}.md")

            with open(file_path, "a") as f:
                f.write(f"# {file_topic.replace('_', ' ').title()}\n")
                f.write(f"Learned about {file_topic.replace('_', ' ')} on {current_date.strftime('%d %b %Y')}.\n\n")

            # Format date for Git
            date_str = current_date.strftime("%Y-%m-%dT%H:%M:%S")
            env = os.environ.copy()
            env["GIT_AUTHOR_DATE"] = date_str
            env["GIT_COMMITTER_DATE"] = date_str

            subprocess.run(["git", "add", "."], cwd=repo_path)
            subprocess.run(["git", "commit", "-m", f"Added notes on {file_topic.replace('_', ' ')}"], cwd=repo_path, env=env)
    current_date += timedelta(days=1)

print("✅ Backdated commits created!")
print("🚀 Now run: git push origin main")
