@echo off
setlocal

REM 파일 입력 하여 변환하기
cd /d "%~dp0">ddd1.txt
for /f "delims=" %%f in ('type %*') do (
echo echo "%%~f">>ddd1.txt
)

REM 배치 파일 만들기
echo @echo off > temp.txt
echo setlocal >> temp.txt
type ddd1.txt >> temp.txt
move /y temp.txt test.bat

pause