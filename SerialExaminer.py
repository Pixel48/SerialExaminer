# -*- coding: utf-8 -*-
# SerialExaminer.py
#   by Pixel
# Workflow:      https://trello.com/b/NcEXmMyl
# Repository:    https://github.com/Pixel48/SerialExaminer.git
# Documentation: https://github.com/Pixel48/SerialExaminer (WIP)

from tkinter import *
from tkinter import filedialog
import tkinter.font as tkFont
import os#, shutil, pickle, csv # NOTE: not used yet

# SOME GLOBALS
R = 0
C = 0
INPUT_FILES = None
OUTPUT_FILE = None
KEY_FILE = None

def newRow(arg = 1):
  global C, R
  R += arg
  C = 0
def newCol(arg = 1):
  global C
  C += arg

class MainWindow(object):
  """Creator for main apilcation window"""
  def __init__(self, master):
    self.master = master
    self.frame = Frame(self.master)
    self.build()

  def build(self):
    """Create widgets"""
    # signature stuff #
    self.signatureFont = tkFont.Font(size =7)
    self.gh = Label(font = self.signatureFont)
    self.gh['text'] = "GitHub.com/Pixel48/SerialExaminer"
    self.gh['fg'] = 'grey'
    self.gh.grid(row = 99, column = 0, columnspan = 3, sticky = 'e')
    #/signature stuff/#
    # main #
    # label
    self.mainFont = tkFont.Font(size=20)
    self.mainLabel = Label(font = self.mainFont)
    self.mainLabel['text'] = "SerialExaminer v0.1.0"
    self.mainFont['size'] = 15
    self.mainLabel.grid(row = R, column = C, columnspan = 3)
    # exam key files #
    # label
    newRow()
    self.keyLabel = Label()
    self.keyLabel['text'] = "Exam key file"
    self.keyLabel.grid(row = R, column = C)
    # TODO: exam key generate window/button
    # create button
    newCol()
    self.keyButtonCreate = Button()
    self.keyButtonCreate['text'] = "Create"
    self.keyButtonCreate['command'] = self.createKey
    self.keyButtonCreate.grid(row = R, column = C)
    # import button
    newCol()
    self.keyButtonImport = Button()
    self.keyButtonImport['text'] = "Import"
    self.keyButtonImport['command'] = self.createKey
    self.keyButtonImport.grid(row = R, column = C)
    # input files #
    # label
    newRow()
    self.inputLabel = Label()
    self.inputLabel['text'] = "Testing files directory"
    self.inputLabel.grid(row = R, column = C, columnspan = 1)
    # button
    newCol()
    self.inputButton = Button()
    self.inputButton['text'] = "Browse"
    self.inputButton['command'] = self.browseExams
    self.inputButton['state'] = DISABLED
    self.inputButton.grid(row = R, column = C, columnspan = 2, sticky = 'we')
    # serial examinition #
    # button
    newRow()
    self.examinateButtonFont = tkFont.Font(size=15)
    self.examinateButton = Button(font = self.examinateButtonFont)
    self.examinateButton['text'] = "Check!"
    self.examinateButton['command'] = self.examinate
    self.examinateButton['state'] = DISABLED
    self.examinateButton.grid(row = R, column = C, columnspan = 3, sticky = 'we')
    # output files #
    # label
    newRow()
    self.outputLabel = Label()
    self.outputLabel['text'] = "Retsults"
    self.outputLabel.grid(row = R, column = C)
    # button display
    newCol()
    self.outputButtonDsiplay = Button()
    self.outputButtonDsiplay['text'] = "Display"
    self.outputButtonDsiplay['command'] = self.resultDisplay
    self.outputButtonDsiplay['state'] = DISABLED
    self.outputButtonDsiplay.grid(row = R, column = C)
    # button export
    newCol()
    self.outputButtonExport = Button()
    self.outputButtonExport['text'] = "Export"
    self.outputButtonExport['command'] = self.resultExport
    self.outputButtonExport['state'] = DISABLED
    self.outputButtonExport.grid(row = R, column = C)

  def browseExams(self):
    global INPUT_FILES
    INPUT_FILES = os.path.normpath(filedialog.askdirectory())
  def createKey(self):
    # TODO: createKey dialog
    pass
  def resultDisplay(self):
    pass
  def resultExport(self):
    pass
  def examinate(self):
    pass

def main():
  root = Tk()
  root.title("SeriEx")
  # root.resizable(width=False, height=False) # lock window resize
  ws = root.winfo_screenwidth()
  hs = root.winfo_screenheight()
  x = (ws/20)*10
  y = (hs/20)*9
  root.geometry('+%d+%d'%(x, y)) # set position
  root.iconbitmap(r'./ico.ico') # icon
  app = MainWindow(root)
  root.mainloop()

if __name__ == '__main__':
  main()
