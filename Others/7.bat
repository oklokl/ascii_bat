@echo off
setlocal
cd /d "%~dp0">ddd1.txt
for /f "delims=" %%f in ('type dddd.txt') do (
echo echo "%%~f">>ddd1.txt
)

pause