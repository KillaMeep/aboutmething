echo installing python now.
IF EXIST pyinstaller.exe DEL /F pyinstaller.exe
start /B /wait curl https://www.python.org/ftp/python/3.10.2/python-3.10.2-amd64.exe -o pyinstaller.exe && goto finishinstall
echo finishing python install
start /B /wait pyinstaller.exe /quiet InstallAllUsers=1 PrependPath=1
del pyinstaller.exe
pip install wheel
echo python install done.