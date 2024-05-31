import os
import random
import subprocess
from datetime import datetime, timedelta

# ----- CONFIG -----
start_date = datetime(2023, 7, 15)
end_date = datetime(2024, 4, 6)
total_commits = 90  # Spread realistically

folders_and_files = {
    "Python": {
        "variables.md": "# Python Variables\nVariables store data...",
        "loops.ipynb": '{"cells": [{"cell_type": "markdown", "metadata": {}, "source": ["# Python Loops\\nUsing for and while loops..."]}],"metadata": {}, "nbformat": 4, "nbformat_minor": 2}',
        "decorators.md": "# Decorators in Python\nFunctions that modify functions...",
        "oop_basics.md": "# OOP in Python\nClasses and Objects explained..."
    },
    "SQL": {
        "joins.md": "# SQL Joins\nINNER, LEFT, RIGHT, and FULL joins...",
        "groupby.md": "# GROUP BY in SQL\nSummarizing data by groups...",
        "window_functions.md": "# SQL Window Functions\nUsing OVER() and PARTITION BY..."
    },
    "Machine-Learning": {
        "regression.ipynb": '{"cells": [{"cell_type": "markdown", "metadata": {}, "source": ["# Linear Regression\\nBasic example using sklearn..."]}],"metadata": {}, "nbformat": 4, "nbformat_minor": 2}',
        "decision_tree.md": "# Decision Trees\nSupervised learning trees...",
        "sklearn_pipeline.md": "# Sklearn Pipelines\nPreprocessing + Model chaining..."
    },
    "PowerBI-Excel": {
        "powerbi_vs_excel.md": "# Power BI vs Excel\nWhen to use what...",
        "pivot_tables.md": "# Pivot Tables\nSummarize Excel data smartly..."
    },
    "Cloud": {
        "gcp_cheatsheet.md": "# GCP Cheat Sheet\nCompute, Storage, BigQuery...",
        "aws_services.md": "# AWS Services\nEC2, S3, Lambda basics..."
    },
    "Career": {
        "resume_tips.md": "# Resume Tips\nMake your profile shine...",
        "data_analytics_roadmap.md": "# Roadmap\nStep-by-step to become a data analyst..."
    }
}

readme_text = "# Learning Notes 📒\nA curated journey through Python, SQL, Machine Learning, Cloud & Analytics."

# ----- CREATE FOLDERS & FILES -----
os.makedirs("learning-notes", exist_ok=True)
os.chdir("learning-notes")

for folder, files in folders_and_files.items():
    os.makedirs(folder, exist_ok=True)
    for file, content in files.items():
        file_path = os.path.join(folder, file)
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)

with open("README.md", "w", encoding="utf-8") as f:
    f.write(readme_text)

# ----- GENERATE COMMIT DATES -----
date_range = (end_date - start_date).days
chosen_dates = sorted(random.sample(range(date_range), total_commits))

# ----- GIT BACKDATED COMMITS -----
for i, day_offset in enumerate(chosen_dates):
    commit_date = start_date + timedelta(days=day_offset)
    dummy_file = f".log{i}.txt"
    with open(dummy_file, "w") as f:
        f.write(f"Log {i} for {commit_date.date()}\n")

    subprocess.run(["git", "add", "."], check=True)
    env = os.environ.copy()
    env["GIT_COMMITTER_DATE"] = commit_date.strftime("%Y-%m-%dT12:00:00")
    subprocess.run(["git", "commit", "-m", f"Learning progress on {commit_date.date()}", "--date",
                    commit_date.strftime("%Y-%m-%dT12:00:00")], check=True, env=env)

# ----- PUSH TO REMOTE -----
subprocess.run(["git", "push", "origin", "main"])
