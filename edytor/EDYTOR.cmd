@echo off
rem Otwiera edytor modeli Little Townies w osobnym oknie Microsoft Edge.
set "ED=%~dp0LittleTownies-Edytor.html"
where msedge >nul 2>nul && ( start "" msedge --app="file:///%ED%" --window-size=1400,900 & exit /b )
if exist "%ProgramFiles(x86)%\Microsoft\Edge\Application\msedge.exe" ( start "" "%ProgramFiles(x86)%\Microsoft\Edge\Application\msedge.exe" --app="file:///%ED%" --window-size=1400,900 & exit /b )
if exist "%ProgramFiles%\Microsoft\Edge\Application\msedge.exe" ( start "" "%ProgramFiles%\Microsoft\Edge\Application\msedge.exe" --app="file:///%ED%" --window-size=1400,900 & exit /b )
start "" "%ED%"
