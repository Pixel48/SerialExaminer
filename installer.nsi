;SeriEx Installer
!include "MUI2.nsh"

;------------------
;Atributes
Name "SerialExaminer"
OutFile "InstallSerialExaminer.exe"
InstallDir $PROGRAMFILES\SerialExaminer
RequestExecutionLevel admin
;Unicode True

;------------------
;Icons
!define MUI_UNICON "unico.ico"
!define MUI_ICON "ico.ico"

;------------------
;Installer
!insertmacro MUI_PAGE_DIRECTORY
!insertmacro MUI_PAGE_INSTFILES

Section "SerialExaminer" SerialExaminer
  SetOutPath $INSTDIR
  File /r "dist\SerialExaminer\*"
  ;InstallDirRegKey HKLM "Software\SerialExaminer" ""

  WriteRegStr HKLM SOFTWARE\NSIS_Example2 "Install_Dir" "$INSTDIR"

  WriteRegStr HKLM "Software\SerialExaminer" "DisplayName" "SerialExaminer"
  WriteRegStr HKLM "Software\SerialExaminer" "UninstallString" '"$INSTDIR\Uninstall.exe"'
  WriteRegDWORD HKLM "Software\SerialExaminer" "NoModify" 1
  WriteRegDWORD HKLM "Software\SerialExaminer" "NoRepair" 1
  WriteUninstaller "$INSTDIR\Uninstall.exe"
SectionEnd

;------------------
;Uninstaller
!insertmacro MUI_UNPAGE_CONFIRM
!insertmacro MUI_UNPAGE_INSTFILES

Section "Uninstall"
  Delete "$INSTDIR\Uninstall.exe"
  RMDir "$INSTDIR\*"
  RMDir /r "$INSTDIR"
  DeleteRegKey HKLM "Software\SerialExaminer"
SectionEnd

Section "Desktop shortcut"
  CreateShortcut "$DESKTOP\SerialExaminer.lnk" "$INSTDIR\SerialExaminer.exe"
SectionEnd
