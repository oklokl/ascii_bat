@echo off
chcp 65001
setLocal EnableDelayedExpansion
for /f "tokens=* delims= " %%a in (txt.txt) do (
set /a N+=1
echo ^echo "%%a">>output.txt
)