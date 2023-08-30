@echo off
REM Create virtual environment
python -m venv env

REM Activate virtual environment
call env\Scripts\activate

REM Install requirements
pip install -r requirements.txt

REM Deactivate virtual environment
deactivate
