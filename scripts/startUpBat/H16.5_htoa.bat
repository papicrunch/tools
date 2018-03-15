@echo off
rem houdini launcher

set "HOUDINI_VERSION=Houdini 16.5.405"

rem Arnold var
set "HTOA_BIN=X:\_MTC_CONFIG\_CONFIG_HOUDINI_\htoa\Htoa_2.24\htoa-2.2.4_re18b644_houdini-16.5.405\scripts\bin"
set "HTOA_PATH=X:\_MTC_CONFIG\_CONFIG_HOUDINI_\htoa\Htoa_2.24\htoa-2.2.4_re18b644_houdini-16.5.405\"

rem General var
set "HOUDINI_GAMEDEV=X:\_MTC_CONFIG\_CONFIG_HOUDINI_\_LIB\GameDevelopmentToolset"
set "HOUDINI_HMTC=X:\_MTC_CONFIG\_CONFIG_HOUDINI_\HMTCConfig"
set "HOUDINI_PATH=%HTOA_PATH%;%HOUDINI_GAMEDEV%;&;%HOUDINI_HMTC%"
set "HOUDINI_DIR=C:\Program Files\Side Effects Software\%HOUDINI_VERSION%\bin"
set "PATH=%HTOA_BIN%;%HOUDINI_DIR%;%PATH%"

rem ------------- Optionnal var ------------
set "HOUDINI_DSO_ERROR = 2"
set "HOUDINI_BUFFEREDSAVE=1"
set "HOUDINI_ACCESS_METHOD=2"
rem Qlib set
set "QLIB_PATH=X:\_MTC_CONFIG\_CONFIG_HOUDINI_\_LIB\qLib"
set "QLIB_OTLS=%QLIB_PATH%\otls"
rem Aelib
set "AELIB_PATH=X:\_MTC_CONFIG\_CONFIG_HOUDINI_\_LIB\Aelib"
set "AELIB_OTLS=%AELIB_PATH%\otls"
rem Set user otls
set "USER_PATH=X:\_MTC_CONFIG\_CONFIG_HOUDINI_\_LIB\users"
set "USER_OTLS=%USER_PATH\otls"
rem Set optionnal path
set "HOUDINI_OTLSCAN_PATH=&;%QLIB_OTLS%\base;%QLIB_OTLS%\future;%QLIB_OTLS%\experimental;%AELIB_OTLS%;%USER_OTLS%"
set "HOUDINI_GALLERY_PATH=&;%QLIB_PATH%\gallery;%AELIB_PATH%\gallery"
set "HOUDINI_TOOLBAR_PATH=&;%QLIB_PATH\toolbar,%AELIB_PATH%\toolbar"
set "HOUDINI_SCRIPT_PATH =&;%QLIB_PATH%\scripts;%AELIB_PATH%\scripts"
set "HOUDINI_VEX_PATH=&;%AELIB_PATH%\vex"



cd ..\..\
start houdinifx
