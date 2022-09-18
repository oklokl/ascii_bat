@echo off

chcp 65001 > nul
cd /d "%~dp0"

for /f "delims=" %%a in ('type "%1"') do (
echo echo ^"%%a^">>"TMP%~nx1"
)

copy /y "TMP%~nx1" "%1"
del /q "TMP%~nx1"
