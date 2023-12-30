# My App Daemon Instance

## Prerequisites:

I use VS Code for my coding needs. 

- Download VS Code, Python, Git, SSH Server/Client etc.
- Install Extensions Docker, Python, Remote-SSH

## Configure git:

```
git config --global user.name NAME
git config --global user.email EMAIL

# Confirm
git config --global user.name
git config --global user.email
```

## Setup VS Code:

Ctrl + Shift + P -> Command Palette
- Python: Create Environment...
- venv
- python 3.10.12
- **NB1:** change directory if needed e.g. `cd /appdaemon/conf`
- **NB1:** Activate the environment with `source .venv/bin/activate`
- `(.venv) smithy@myserver:/path/to/conf$`

## Setup Virtual Environment

Install packages `pip install xyz`
- appdaemon
- appdaemon-testing
- pytest

This Tutorial walks through testing custom apps:
https://pypi.org/project/appdaemon-testing/
