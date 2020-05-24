;SeriEx Installer
!include "MUI2.nsh"

;------------------
;Atributes
Name "SerialExaminer"
OutFile "SerialExaminerSetup.exe"
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
  CreateDirectory "$INSTDIR\keys"

  WriteRegStr HKLM "SOFTWARE\SerialExaminer" "InstallPath" "$INSTDIR"
  WriteRegStr HKLM "Software\SerialExaminer" "DisplayName" "SerialExaminer"
  WriteRegStr HKLM "Software\SerialExaminer" "UninstallString" '"$INSTDIR\Uninstall.exe"'

  WriteUninstaller "$INSTDIR\Uninstall.exe"
SectionEnd

Section "Desktop shortcut"
  CreateShortcut "$DESKTOP\SerialExaminer.lnk" "$INSTDIR\SerialExaminer.exe"
SectionEnd

;------------------
;Uninstaller
!insertmacro MUI_UNPAGE_CONFIRM
!insertmacro MUI_UNPAGE_INSTFILES

Section "Uninstall"
  Delete "$DESKTOP\SerialExaminer.lnk"
  Delete "$INSTDIR\Uninstall.exe"
  RMDir /r "$INSTDIR"
  DeleteRegKey HKLM "Software\SerialExaminer"
SectionEnd
