@echo off
title University ERP Platform
echo ========================================================
echo        University ERP Platform (PBL_OS)
echo ========================================================
echo.
echo [1/2] Checking and installing dependencies...
python -m pip install -r requirements.txt
echo.
echo [2/2] Starting Flask server...
echo Server running at: http://127.0.0.1:5000
echo Press Ctrl+C to stop the server.
echo.
python app.py
pause
