@echo off

set PYTHON=D:\Projects\stable-diffusion-webui\venv\Scripts\python.exe
set GIT=
set VENV_DIR=
set COMMANDLINE_ARGS=--listen --disable-safe-unpickle --api

call webui.bat
