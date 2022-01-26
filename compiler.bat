@echo off
setlocal
set USR_PATH=
set SYS_PATH=
for /F "tokens=3* skip=2" %%P in ('%SystemRoot%\system32\reg.exe query "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\Environment" /v PATH') do @set "SYS_PATH=%%P %%Q"
for /F "tokens=3* skip=2" %%P in ('%SystemRoot%\system32\reg.exe query "HKCU\Environment" /v PATH') do @set "USR_PATH=%%P %%Q"
if "%SYS_PATH:~-1%"==" " set "SYS_PATH=%SYS_PATH:~0,-1%"
if "%USR_PATH:~-1%"==" " set "USR_PATH=%USR_PATH:~0,-1%"
endlocal & call set "PATH=%SYS_PATH%;%USR_PATH%"
TITLE KillOS Compiler
cls
IF EXIST killos.exe DEL /F killos.exe
IF EXIST build goto alreadymade ELSE goto makebuild
:makebuild
mkdir build
cd build
curl https://raw.githubusercontent.com/KillaMeep/aboutmething/main/killos.py -O
curl https://raw.githubusercontent.com/KillaMeep/aboutmething/main/icon.ico -O
curl https://raw.githubusercontent.com/KillaMeep/aboutmething/main/requirements.txt -O
python --version >nul 2>&1 && ( goto gotpy ) || ( goto install )



:alreadymade
cd build
goto gotpy





:install
echo Python missing, installing now.
curl https://raw.githubusercontent.com/KillaMeep/aboutmething/main/pythoninstaller.bat -O
pythoninstaller.bat
exit

:gotpy
IF EXIST pyinstaller.bat DEL /F pyinstaller.bat
echo build starting.
pip install -r requirements.txt
pip install auto-py-to-exe
del requirements.txt
pyinstaller --noconfirm --onefile -i icon.ico --console killos.py
cd dist && copy killos.exe ..\.. && cd ..\..
goto eof




:eof
rmdir /Q /S build
rmdir /Q /S build
exit