@echo off
setlocal
chcp 65001

REM 파일 입력 하여 변환하기
cd /d "%~dp0">ddd1.txt
for /f "delims=" %%f in ('type %*') do (
echo echo "%%~f">>ddd1.txt
)

REM 배치 파일 만들기
echo @echo off > temp.txt
echo setlocal >> temp.txt
echo chcp 65001 >> temp.txt
echo. >> temp.txt
type ddd1.txt >> temp.txt

REM 음악 추가 https://cafe.daum.net/candan/GGFN/337 다운로드 받는 방법 여기 참조 하세요.
REM fmedia 설치 되어 있어야 하고 NiceAndEasy.mp3 파일이 D 드라이브에 있어야 해요.
REM NiceAndEasy.mp3 원하시는 파일 이름으로 바꾸시면 되네요. 자신이 원하는거 다운로드.
REM 랜덤으로 bat 이름 정하기 0부터 777까지 https://freve.tistory.com/83 
REM echo fmedia "d:\NiceAndEasy.mp3" --background >> temp.txt
set /a num=%random% %%778+1
echo %num%
move /y temp.txt test%num%.bat
pause