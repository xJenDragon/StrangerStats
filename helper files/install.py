# install.py
import os

packages = [
    "pandas",
    "numpy",
    "matplotlib",
    "seaborn",
    "scikit-learn",
    "openpyxl"
]

for pkg in packages:
    os.system(f"pip install {pkg}")
