; SeriEx Installer
!include "MUI2.nsh"

;------------------
; defines
!define PROGRAM_NAME "SerialExaminer"
!define UNINST_KEY "SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\${PROGRAM_NAME}"
!define INST_KEY "SOFTWARE\${PROGRAM_NAME}"

;------------------
; Atributes
Name "SerialExaminer"
OutFile "SerialExaminerSetup.exe"
InstallDir "$PROGRAMFILES32\${PROGRAM_NAME}"
RequestExecutionLevel admin
; Unicode True

;------------------
; Icons
!define MUI_UNICON "unico.ico"
!define MUI_ICON "ico.ico"

;------------------
; Installer
!insertmacro MUI_PAGE_DIRECTORY
!insertmacro MUI_PAGE_INSTFILES

Section "SerialExaminer" SerialExaminer
  SetOutPath $INSTDIR
  File /r "dist\SerialExaminer\*"
  CreateDirectory "$INSTDIR\keys"

  WriteRegStr HKLM "${INST_KEY}" "InstallDir" "$INSTDIR"
  WriteRegStr HKLM "${INST_KEY}" "DisplayName" "SerialExaminer"
  WriteRegStr HKLM "${INST_KEY}" "DisplayVersion" "0.4.1"
  WriteRegStr HKLM "${INST_KEY}" "DisplayIcon" "$\"$INSTDIR\ico.ico$\""
  WriteRegStr HKLM "${INST_KEY}" "Publisher" "GitHub.com/Pixel48"
  WriteRegStr HKLM "${INST_KEY}" "UninstallString" "$INSTDIR\Uninstall.exe"

  WriteUninstaller "$INSTDIR\Uninstall.exe"

  WriteRegStr HKLM "${UNINST_KEY}" "InstallDir" "$INSTDIR"
  WriteRegStr HKLM "${UNINST_KEY}" "DisplayName" "${PROGRAM_NAME}"
  WriteRegStr HKLM "${UNINST_KEY}" "DisplayVersion" "0.4.1"
  WriteRegStr HKLM "${UNINST_KEY}" "DisplayIcon" "$\"$INSTDIR\ico.ico$\""
  WriteRegStr HKLM "${UNINST_KEY}" "Publisher" "GitHub.com/Pixel48"
  WriteRegStr HKLM "${UNINST_KEY}" "UninstallString" "$\"$INSTDIR\Uninstall.exe$\""
  WriteRegDWORD HKLM "${UNINST_KEY}" "NoModify" 1
  WriteRegDWORD HKLM "${UNINST_KEY}" "NoRepair" 1
SectionEnd

Section "Desktop shortcut"
  CreateShortcut "$DESKTOP\SerialExaminer.lnk" "$INSTDIR\SerialExaminer.exe"
SectionEnd

;------------------
; Uninstaller
!insertmacro MUI_UNPAGE_CONFIRM
!insertmacro MUI_UNPAGE_INSTFILES

Section "Uninstall"
  Delete "$DESKTOP\SerialExaminer.lnk"
  RMDir /r "$INSTDIR"
  DeleteRegKey HKLM "${INST_KEY}"
  DeleteRegKey HKLM "${UNINST_KEY}"
SectionEnd
