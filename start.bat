@echo off

REM Reset the repository to the latest commit and remove untracked files
git checkout . && git clean  -f

REM Update your local repository with changes from the remote repository
git pull -r

REM Create a virtual environment and activate it
python -m venv .\.app && .\.app\Scripts\activate

REM Run the unit tests
python -m unittest

echo To run tests execute
echo python -m unittest