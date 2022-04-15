cls
@echo off
title "Google Colab Local Server by @abhimanyus1997"

@REM echo "Opening a new Google Colab in Brave"
@REM set %url% = "https://colab.research.google.com/#create=true"
@REM start brave %url%

echo "Starting Jupyter NB Server "
jupyter notebook --NotebookApp.allow_origin='https://colab.research.google.com' \
--port=9090 --no-browser
echo "Jupyter NB Server Launched"
pause
