import os
os.system("git pull")
os.system("pip install --upgrade pip")
os.system("rm -rf .cache .venv .pytest_cache")
os.system("pytest --cov-report=xml --cov=SchoolProject")
