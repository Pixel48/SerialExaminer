# -*- coding: utf-8 -*-
# SerialExaminer.py
#   by Pixel
# Workflow:      https://trello.com/b/NcEXmMyl
# Repository:    https://github.com/Pixel48/SerialExaminer.git
# Documentation: https://github.com/Pixel48/SerialExaminer (WIP)
from tkinter import *
from tkinter import filedialog
import tkinter.font as tkFont
import os, pickle#, shutil, csv # NOTE: not used yet

versionTag = 'v0.0.0'

# SOME GLOBALS
R = 0
C = 0
INPUT_FILES = []
OUTPUT_FILE = None
KEY_FILE = None
KEY_DICT = {}
RESULT_DICT = {}
questionCount = 0
answersCount = 0

def newRow(arg = 1):
  global C, R
  R += arg
  C = 0
def newCol(arg = 1):
  global C
  C += arg
def zeroCol():
  global C, R
  C = R = 0

def splitLine(line):
  if line.split('.')[0].isdigit():
    line = line.split('.')
    line[0] = int(line[0])
    if line[1]:
      if 'a' in line[1].lower():
        line[1] = 'A'
      elif 'b' in line[1].lower():
        line[1] = 'B'
      elif 'c' in line[1].lower():
        line[1] = 'C'
      elif 'd' in line[1].lower():
        line[1] = 'D'
      else:
        line[1] = 'X'
      return line
    else:
      return [line[0], 'X']
  else:
    return [0, 'X']

class MainWindow(object):
  """Creator for main apilcation window"""
  def __init__(self, master):
    self.master = master
    self.frame = Frame(self.master)
    self.build(self.frame)
    self.frame.grid()
  def build(self, frame):
    zeroCol()
    # signature stuff #
    self.signatureFont = tkFont.Font(size = 7)
    self.gh = Label(frame, font = self.signatureFont)
    self.gh['text'] = "GitHub.com/Pixel48/SerialExaminer"
    self.gh['fg'] = 'grey'
    self.gh.grid(row = 99, column = 0, columnspan = 3, sticky = 'e')
    # version #
    global versionTag
    self.version = Label(frame, font = self.signatureFont)
    self.version['text'] = versionTag
    self.version.grid(row = 99, column = 0, sticky = 'w')
    # main #
    # label
    self.mainFont = tkFont.Font(size=20)
    self.mainLabel = Label(frame, font = self.mainFont)
    self.mainLabel['text'] = "SerialExaminer"
    self.mainFont['size'] = 15
    self.mainLabel.grid(row = R, column = C, columnspan = 3)
    # exam key files #
    # label
    newRow()
    self.keyLabel = Label(frame)
    self.keyLabel['text'] = "Exam key file"
    self.keyLabel.grid(row = R, column = C)
    # create button
    newCol()
    self.keyButtonCreate = Button(frame)
    self.keyButtonCreate['text'] = "Create"
    self.keyButtonCreate['command'] = self.createKey
    self.keyButtonCreate.grid(row = R, column = C)
    # import button
    newCol()
    self.keyButtonImport = Button(frame)
    self.keyButtonImport['text'] = "Import"
    self.keyButtonImport['command'] = self.importKey
    self.keyButtonImport.grid(row = R, column = C)
    # input files #
    # label
    newRow()
    self.inputLabel = Label(frame)
    self.inputLabel['text'] = "Testing files directory"
    self.inputLabel.grid(row = R, column = C, columnspan = 1)
    # button
    newCol()
    self.inputButton = Button(frame)
    self.inputButton['text'] = "Browse"
    self.inputButton['command'] = self.browseExams
    self.inputButton['state'] = DISABLED
    self.inputButton.grid(row = R, column = C, columnspan = 2, sticky = 'we')
    # serial examinition #
    # button
    newRow()
    self.examinateButtonFont = tkFont.Font(size=15)
    self.examinateButton = Button(frame, font = self.examinateButtonFont)
    self.examinateButton['text'] = "Check!"
    self.examinateButton['command'] = self.examinate
    self.examinateButton['state'] = DISABLED
    self.examinateButton.grid(row = R, column = C, columnspan = 3, sticky = 'we')
    # output files #
    # label
    newRow()
    self.outputLabel = Label(frame)
    self.outputLabel['text'] = "Retsults"
    self.outputLabel.grid(row = R, column = C)
    # button display
    newCol()
    self.outputButtonDsiplay = Button(frame)
    self.outputButtonDsiplay['text'] = "Display"
    self.outputButtonDsiplay['command'] = self.resultDisplay
    self.outputButtonDsiplay['state'] = DISABLED
    self.outputButtonDsiplay.grid(row = R, column = C)
    # button export
    newCol()
    self.outputButtonExport = Button(frame)
    self.outputButtonExport['text'] = "Export"
    self.outputButtonExport['command'] = self.resultExport
    self.outputButtonExport['state'] = DISABLED
    self.outputButtonExport.grid(row = R, column = C)

  def createKey(self):
    self.masterWindowCreateKey = Toplevel(self.master)
    self.appWindowCreateKey = KeyCreatorWindow(self.masterWindowCreateKey, self)
  def importKey(self):
    global KEY_FILE
    self.keyButtonImport['state'] = DISABLED
    self.keyButtonCreate['state'] = DISABLED
    KEY_FILE = os.path.normpath(filedialog.askopenfilename(
      title = "Select exam key file",
      initialdir = '.',
      filetypes =(("Exam Key File", "*.exkey"),
                  # ("Csv files", "*.csv"), # TODO: add csv key import
                  # ("Excel sheets", "*.xml"), # TODO: add xml key import
                  ("All files", "*.*"))
    ))
    self.keyButtonImport['state'] = NORMAL
    self.keyButtonCreate['state'] = NORMAL
    if ".exkey" in KEY_FILE:
      global questionCount, KEY_DICT
      with open(KEY_FILE, 'rb') as keyf:
        KEY_DICT = pickle.load(keyf)
      questionCount = len(KEY_DICT.keys())
      self.inputButton['state'] = NORMAL
  def browseExams(self):
    global INPUT_FILES
    testDir = os.path.normpath(filedialog.askdirectory(
    title = "Examination txt files location",
    initialdir = '.',
    ))
    testFiles = os.listdir(testDir)
    buffer = []
    for file in testFiles:
      buffer.append(os.path.join(testDir, file))
    for file in buffer:
      if '.txt' in file:
        INPUT_FILES.append(file)
    if INPUT_FILES:
      self.examinateButton['state'] = NORMAL
  def examinate(self):
    global questionCount
    for testFile in INPUT_FILES:
      with open(testFile, 'r') as examinateFile:
        answersDict = {}
        points = 0
        for line in examinateFile:
          line = splitLine(line)
          answersDict[line[0]] = line[1]
        for question in answersDict.keys():
          if question in KEY_DICT.keys():
            if answersDict[question] == KEY_DICT[question]:
              points += 1
        resultName = os.path.basename(testFile).split('.')[0]
        RESULT_DICT[resultName] = [str(points) + '/' + str(questionCount), str(round(points*100/questionCount, 2)) + '%']
        # NOTE: Result format: {<Filename>: ['<points>/<maxPoints', '<goodAnswersIn%>%']}
        # print(resultName + ':', RESULT_DICT[resultName])
    self.outputButtonDsiplay['state'] = NORMAL
    self.outputButtonExport['state'] = NORMAL
  def resultDisplay(self):
    self.masterResultDisplayWindow = Toplevel(self.master)
    self.appResultDisplayWindow = ResultDisplayWindow(self.masterResultDisplayWindow, self)
  def resultExport(self):
    pass

class KeyCreatorWindow(object):
  """Creator for CreateKey Window"""
  def __init__(self, master, above):
    global questionCount, answersCount
    questionCount = 40
    answersCount = 4
    self.master = master
    self.above = above
    self.frame = Frame(self.master)
    self.build(self.frame)
    self.frame.grid()
  def build(self, frame):
    zeroCol()
    # window name #
    # label
    self.mainFont = tkFont.Font(size = 14)
    self.mainLabel = Label(frame, font = self.mainFont)
    self.mainLabel['text'] = "Serial Examiner\nKey Creator"
    self.mainLabel.grid(row = R, column = C, columnspan = 6)
    # question quantinity #
    # label
    newRow()
    self.questionLabel = Label(frame)
    self.questionLabel['text'] = "Question quantinity"
    self.questionLabel.grid(row = R, column = C)
    # button -10
    newCol()
    self.questionButtonMinus10 = Button(frame)
    self.questionButtonMinus10['text'] = "<<"
    self.questionButtonMinus10['width'] = 3
    self.questionButtonMinus10['command'] = self.questionCountMinus10
    self.questionButtonMinus10.grid(row = R, column = C)
    # button -1
    newCol()
    self.questionButtonMinus1 = Button(frame)
    self.questionButtonMinus1['text'] = "<"
    self.questionButtonMinus1['width'] = 3
    self.questionButtonMinus1['command'] = self.questionCountMinus1
    self.questionButtonMinus1.grid(row = R, column = C)
    # countLabel
    newCol()
    self.questionLabelCount = Label(frame)
    self.questionLabelCount['text'] = questionCount
    self.questionLabelCount['width'] = 3
    self.questionLabelCount.grid(row = R, column = C)
    # button +1
    newCol()
    self.questionButtonPlus1 = Button(frame)
    self.questionButtonPlus1['text'] = ">"
    self.questionButtonPlus1['width'] = 3
    self.questionButtonPlus1['command'] = self.questionCountPlus1
    self.questionButtonPlus1.grid(row = R, column = C)
    # button +10
    newCol()
    self.questionButtonPlus10 = Button(frame)
    self.questionButtonPlus10['text'] = ">>"
    self.questionButtonPlus10['width'] = 3
    self.questionButtonPlus10['command'] = self.questionCountPlus10
    self.questionButtonPlus10.grid(row = R, column = C)
    # # posible answears quantinity # # NOTE: conented for now, i'll use it leater
    # # label
    # newRow()
    # self.answersQuantinity = Label(frame)
    # self.answersQuantinity['text'] = "Posible answears quantinity"
    # self.answersQuantinity.grid(row = R, column = C)
    # # 2 radio
    # newCol()
    # self.answers2 = Radiobutton(frame)
    # self.answers2['variable'] = self.answersCount
    # self.answers2['text'] = "2"
    # self.answers2['value'] = 2
    # self.answers2.deselect()
    # self.answers2.grid(row = R, column = C, columnspan = 2)
    # # 4
    # newCol()
    # newCol()
    # self.answers4 = Radiobutton(frame)
    # self.answers4['variable'] = self.answersCount
    # self.answers4['text'] = "4"
    # self.answers4['value'] = 4
    # self.answers4.select()
    # self.answers4.grid(row = R, column = C, columnspan = 2)
    # main key creator init button #
    newRow()
    self.nextWindowFont = tkFont.Font(size = 14)
    self.nextWindow = Button(frame, font = self.nextWindowFont)
    self.nextWindow['text'] = "Create Key!"
    self.nextWindow['command'] = self.mainKeyCreator
    self.nextWindow.grid(row = R, column = C, columnspan = 6, sticky = 'we')
    # key config done button #
    newRow()
    self.keyDone = Button(frame, font = self.nextWindowFont)
    self.keyDone['text'] = "Done"
    self.keyDone['command'] = self.die
    self.keyDone['state'] = DISABLED
    self.keyDone.grid(row = R, column = C, columnspan = 6, sticky = 'we')

  def questionCountMinus10(self):
    global questionCount
    questionCount -= 10
    if questionCount < 1:
      questionCount = 100
    self.questionLabelCount['text'] = questionCount
  def questionCountMinus1(self):
    global questionCount
    questionCount -= 1
    if questionCount < 1:
      questionCount = 100
    self.questionLabelCount['text'] = questionCount
  def questionCountPlus1(self):
    global questionCount
    questionCount += 1
    if questionCount > 100:
      questionCount = 1
    self.questionLabelCount['text'] = questionCount
  def questionCountPlus10(self):
    global questionCount
    questionCount += 10
    if questionCount > 100:
      questionCount = 10
    self.questionLabelCount['text'] = questionCount
  def mainKeyCreator(self):
    self.masterMainWindowCreateKey = Toplevel(self.master)
    self.appWindowCreateKey = MainKeyCreatorWindow(self.masterMainWindowCreateKey, self)
  def exportKeyFile(self, file):
    with open(file, 'wb') as keyFile:
      pickle.dump(KEY_DICT, keyFile)

  def die(self):
    global KEY_FILE
    KEY_FILE = os.path.normpath(filedialog.asksaveasfilename(
      title = "Select exam key file",
      initialdir = '.',
      filetypes =(("Exam Key File", "*.exkey"),)
    ))
    if '.exkey' not in KEY_FILE:
      KEY_FILE += '.exkey'
    if KEY_FILE is '':
      return # if no filename provided, don't proceed
    self.exportKeyFile(KEY_FILE)
    self.above.inputButton['state'] = NORMAL
    self.master.destroy()

class MainKeyCreatorWindow(object):
  """Window to create exam key"""
  def __init__(self, master, above):
    global KEY_DICT
    KEY_DICT = {}
    self.master = master
    self.above = above
    self.frame = Frame(self.master)
    self.questionNo = 1
    self.build(self.frame)
    self.frame.grid()
  def build(self, frame):
    zeroCol()
    # main label #
    # label/counter
    self.mainFont = tkFont.Font(size = 14)
    self.mainLabel = Label(frame, font = self.mainFont)
    self.mainLabelUpdate()
    self.mainLabel.grid(row = R, column = C, columnspan = 5)
    # question/answer buttons
    # back button
    newRow()
    self.backButton = Button(frame)
    self.backButton['width'] = 3
    self.backButton['text'] = "<"
    self.backButton['command'] = self.backQuestion
    self.backButton.grid(row = R, column = C)
    # A
    newCol()
    self.aButton = Button(frame)
    self.aButton['width'] = 3
    self.aButton['text'] = "A"
    self.aButton['command'] = self.aAnswer
    self.aButton.grid(row = R, column = C)
    # B
    newCol()
    self.bButton = Button(frame)
    self.bButton['width'] = 3
    self.bButton['text'] = "B"
    self.bButton['command'] = self.bAnswer
    self.bButton.grid(row = R, column = C)
    # C
    newCol()
    self.cButton = Button(frame)
    self.cButton['width'] = 3
    self.cButton['text'] = "C"
    self.cButton['command'] = self.cAnswer
    self.cButton.grid(row = R, column = C)
    # D
    newCol()
    self.dButton = Button(frame)
    self.dButton['width'] = 3
    self.dButton['text'] = "D"
    self.dButton['command'] = self.dAnswer
    self.dButton.grid(row = R, column = C)

  def backQuestion(self):
    self.questionNo -= 1
    if self.questionNo < 1:
      self.questionNo = 1
    self.mainLabelUpdate()
  def aAnswer(self):
    self.bindAnswer(self.questionNo, "A")
    self.questionNo += 1
    self.mainLabelUpdate()
  def bAnswer(self):
    self.bindAnswer(self.questionNo, "B")
    self.questionNo += 1
    self.mainLabelUpdate()
  def cAnswer(self):
    self.bindAnswer(self.questionNo, "C")
    self.questionNo += 1
    self.mainLabelUpdate()
  def dAnswer(self):
    self.bindAnswer(self.questionNo, "D")
    self.questionNo += 1
    self.mainLabelUpdate()
  def bindAnswer(self, questionNumber, questionAnswer):
    global KEY_DICT
    KEY_DICT[questionNumber] = questionAnswer # NOTE: that should work...
  def mainLabelUpdate(self):
    self.mainLabel['text'] = "Question " + str(self.questionNo)
    if self.questionNo > questionCount:
      self.above.keyDone['state'] = NORMAL
      self.above.nextWindow['text'] = "ReCreate Key!"
      self.die()
  def die(self):
    self.master.destroy()

class ResultDisplayWindow(object):
  """Pop-up with test results from RESULT_DICT"""
  def __init__(self, master, above):
    self.master = master
    self.above = above
    self.frame = Frame(self.master)
    self.build(self.frame)
    self.frame.grid()
  def build(self, frame):
    pass

  def die(self):
    self.master.destroy()

def main():
  root = Tk()
  root.title("SeriEx")
  root.resizable(width=False, height=False) # lock window resize
  ws = root.winfo_screenwidth()
  hs = root.winfo_screenheight()
  x = (ws/20)*10
  y = (hs/20)*9
  root.iconbitmap(r'./ico.ico') # icon
  # root.geometry('+%d+%d'%(x, y)) # set position
  app = MainWindow(root)
  root.mainloop()

if __name__ == '__main__':
  main()
