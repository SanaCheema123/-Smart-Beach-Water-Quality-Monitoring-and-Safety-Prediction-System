@echo off
echo Installing required libraries...
py -m pip install --upgrade pip
py -m pip install -r requirements.txt
echo Setup completed.
pause
