import os
import json
import subprocess
from datetime import datetime, timedelta

base_dir = "learning-notes"

notebooks = {
    "Python/loops.ipynb": {
        "cells": [
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": ["# Python Loops\nUnderstanding `for` and `while` loops."]
            },
            {
                "cell_type": "code",
                "execution_count": None,
                "metadata": {},
                "outputs": [],
                "source": ["for i in range(5):\n    print(i)"]
            }
        ],
        "metadata": {},
        "nbformat": 4,
        "nbformat_minor": 2
    },
    "Machine-Learning/regression.ipynb": {
        "cells": [
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": ["# Linear Regression\nUsing scikit-learn to build a basic regression model."]
            },
            {
                "cell_type": "code",
                "execution_count": None,
                "metadata": {},
                "outputs": [],
                "source": [
                    "from sklearn.linear_model import LinearRegression\n",
                    "from sklearn.model_selection import train_test_split\n",
                    "from sklearn.datasets import make_regression\n\n",
                    "X, y = make_regression(n_samples=100, n_features=1, noise=0.1)\n",
                    "X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)\n",
                    "model = LinearRegression()\n",
                    "model.fit(X_train, y_train)\n",
                    "print(model.score(X_test, y_test))"
                ]
            }
        ],
        "metadata": {},
        "nbformat": 4,
        "nbformat_minor": 2
    }
}

# Git Config
author_name = "Aman Jain"
author_email = "amanjain0411@gmail.com"

# Set the 2023 range
start_date = datetime(2023, 1, 1)
end_date = datetime(2023, 12, 31)
current_date = start_date

while current_date <= end_date:
    # Add date-based folder name for realism
    folder_suffix = current_date.strftime("%Y-%m-%d")
    for rel_path, content in notebooks.items():
        full_path = os.path.join(base_dir, folder_suffix, rel_path)
        os.makedirs(os.path.dirname(full_path), exist_ok=True)
        with open(full_path, "w", encoding="utf-8") as f:
            json.dump(content, f, indent=2)

        # Git add & commit for each file
        date_str = current_date.strftime("%Y-%m-%dT12:00:00")
        subprocess.run(["git", "add", full_path])
        subprocess.run([
            "git", "commit",
            f"--date={date_str}",
            f"--author={author_name} <{author_email}>",
            "-m", f"Added notebook {rel_path} on {current_date.strftime('%Y-%m-%d')}"
        ])

    current_date += timedelta(days=2)

# One final push
subprocess.run(["git", "push", "origin", "main"])
print("✅ Notebooks created and committed for 2023.")
