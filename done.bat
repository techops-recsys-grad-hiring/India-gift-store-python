@echo off

REM Reset the repository to the latest commit and remove untracked files
git reset HEAD --hard
git clean -f

REM Deactivate the virtual environment
deactivate