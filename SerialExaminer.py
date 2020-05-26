# -*- coding: utf-8 -*-
# SerialExaminer.py
#   by Pixel
# Repository:    https://github.com/Pixel48/SerialExaminer.git
from tkinter import *
from tkinter import filedialog
from functools import partial
import tkinter.font as tkFont
import os, pickle

versionTag = '0.4-alpha.0'

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
      line[1] = line[1].strip('\n')
      line[1] = line[1].strip(' ')[:1].upper()
      return line
    else:
      return [line[0], '#']
  else:
    return [0, '#']

class MainWindow(object):
  """Creator for main apilcation window"""
  def __init__(self, master):
    self.master = master
    self.master.resizable(width=False, height=False) # lock window resize
    self.master.iconbitmap(r'./ico.ico') # icon
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
    KEY_FILE = filedialog.askopenfilename(
      title = "Select exam key file",
      initialdir = './keys',
      filetypes =(("Exam key file", "*.exkey"),
                  ("Plain text", "*.txt"),
                 )
    )
    self.keyButtonImport['state'] = NORMAL
    self.keyButtonCreate['state'] = NORMAL
    if '.exkey' in KEY_FILE or '.txt' in KEY_FILE:
      global questionCount, KEY_DICT
      if '.exkey' in KEY_FILE:
        with open(KEY_FILE, 'rb') as keyf:
          KEY_DICT = pickle.load(keyf)
      elif '.txt' in KEY_FILE:
        with open(KEY_FILE, 'r') as keyf:
          for line in keyf:
            line = splitLine(line)
            KEY_DICT[line[0]] = line[1]
      questionCount = len(KEY_DICT.keys())
      self.inputButton['state'] = NORMAL
  def browseExams(self):
    global INPUT_FILES
    testDir = filedialog.askdirectory(
    title = "Examination txt files location",
    initialdir = '.',
    )
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
    self.outputButtonExport['state'] = NORMAL
    self.outputButtonDsiplay['state'] = NORMAL
  def resultDisplay(self):
    self.masterResultDisplayWindow = Toplevel(self.master)
    self.appResultDisplayWindow = ResultDisplayWindow(self.masterResultDisplayWindow, self)
  def resultExport(self):
    # NOTE: RESULT_DICT format: {<Filename>: ['<points>/<maxPoints', '<goodAnswersIn%>%']}
    global RESULT_DICT
    EXPOT_FILE = filedialog.asksaveasfilename(
      title = "Save test result",
      initialdir = '.',
      defaultextension = '.csv',
      filetypes =(
                  ("CSV file", "*.csv"),
                 )
    )
    if EXPOT_FILE[-4:] == '.csv':
      with open(EXPOT_FILE, 'w') as export:
        export.write(';FILENAME;'+'POINTS (max '+RESULT_DICT[list(RESULT_DICT.keys())[0]][0].split('/')[1]+');RESULT IN %\n')
        i = 1
        for key in RESULT_DICT:
          export.write(key+';'+RESULT_DICT[key][0].split('/')[0]+';'+RESULT_DICT[key][1][:-1].replace('.',',')+'\n')
          i += 1
        export.close()

class KeyCreatorWindow(object):
  """Creator for CreateKey Window"""
  def __init__(self, master, above):
    global questionCount, answersCount
    questionCount = 40
    answersCount = 4
    self.master = master
    self.master.resizable(width=False, height=False) # lock window resize
    self.master.iconbitmap(r'./ico.ico') # icon
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
    self.mainLabel.grid(row = R, column = C, columnspan = 7)
    # question quantity #
    # label
    newRow()
    self.questionLabel = Label(frame)
    self.questionLabel['text'] = "Question quantity"
    self.questionLabel.grid(row = R, column = C)
    # questions button -10
    newCol()
    self.questionButtonMinus10 = Button(frame)
    self.questionButtonMinus10['text'] = "<<"
    self.questionButtonMinus10['width'] = 3
    self.questionButtonMinus10['command'] = self.questionCountMinus10
    self.questionButtonMinus10.grid(row = R, column = C)
    # questions button -1
    newCol()
    self.questionButtonMinus1 = Button(frame)
    self.questionButtonMinus1['text'] = "<"
    self.questionButtonMinus1['width'] = 3
    self.questionButtonMinus1['command'] = self.questionCountMinus1
    self.questionButtonMinus1.grid(row = R, column = C)
    # questionsCountLabel
    newCol()
    self.questionLabelCount = Label(frame)
    self.questionLabelCount['text'] = questionCount
    self.questionLabelCount['width'] = 3
    self.questionLabelCount.grid(row = R, column = C)
    # questions button +1
    newCol()
    self.questionButtonPlus1 = Button(frame)
    self.questionButtonPlus1['text'] = ">"
    self.questionButtonPlus1['width'] = 3
    self.questionButtonPlus1['command'] = self.questionCountPlus1
    self.questionButtonPlus1.grid(row = R, column = C)
    # questions button +10
    newCol()
    self.questionButtonPlus10 = Button(frame)
    self.questionButtonPlus10['text'] = ">>"
    self.questionButtonPlus10['width'] = 3
    self.questionButtonPlus10['command'] = self.questionCountPlus10
    self.questionButtonPlus10.grid(row = R, column = C)
    # button 0
    newCol()
    self.questionButton0 = Button(frame)
    self.questionButton0['text'] = "|<-"
    self.questionButton0['width'] = 3
    self.questionButton0['command'] = self.question0
    self.questionButton0.grid(row = R, column = C)
    # answers quantity #
    # label
    newRow()
    self.answerLabel = Label(frame)
    self.answerLabel['text'] = "Answers quantinity"
    self.answerLabel.grid(row = R, column = C)
    # answers button -10
    newCol()
    self.answerButtonMinus4 = Button(frame)
    self.answerButtonMinus4['text'] = "<<"
    self.answerButtonMinus4['width'] = 3
    self.answerButtonMinus4['command'] = self.answerCountMinus4
    self.answerButtonMinus4.grid(row = R, column = C)
    # answers button -1
    newCol()
    self.answerButtonMinus1 = Button(frame)
    self.answerButtonMinus1['text'] = "<"
    self.answerButtonMinus1['width'] = 3
    self.answerButtonMinus1['command'] = self.answerCountMinus1
    self.answerButtonMinus1.grid(row = R, column = C)
    # answersCountLabel
    newCol()
    self.answerLabelCount = Label(frame)
    self.answerLabelCount['text'] = answersCount
    self.answerLabelCount['width'] = 3
    self.answerLabelCount.grid(row = R, column = C)
    # answers button +1
    newCol()
    self.answerButtonPlus1 = Button(frame)
    self.answerButtonPlus1['text'] = ">"
    self.answerButtonPlus1['width'] = 3
    self.answerButtonPlus1['command'] = self.answerCountPlus1
    self.answerButtonPlus1.grid(row = R, column = C)
    # answers button +10
    newCol()
    self.answerButtonPlus4 = Button(frame)
    self.answerButtonPlus4['text'] = ">>"
    self.answerButtonPlus4['width'] = 3
    self.answerButtonPlus4['command'] = self.answerCountPlus4
    self.answerButtonPlus4.grid(row = R, column = C)
    # Main buttons #
    newRow()
    self.nextWindowFont = tkFont.Font(size = 14)
    self.nextWindow = Button(frame, font = self.nextWindowFont)
    self.nextWindow['text'] = "Create Key!"
    self.nextWindow['command'] = self.mainKeyCreator
    self.nextWindow.grid(row = R, column = C, columnspan = 7, sticky = 'we')
    # key config done button #
    newRow()
    self.keyDone = Button(frame, font = self.nextWindowFont)
    self.keyDone['text'] = "Done"
    self.keyDone['command'] = self.die
    self.keyDone['state'] = DISABLED
    self.keyDone.grid(row = R, column = C, columnspan = 7, sticky = 'we')

  def question0(self):
    global questionCount
    questionCount = 40
    self.questionLabelCount['text'] = questionCount
  def questionCountMinus10(self):
    global questionCount
    questionCount -= 10
    if questionCount < 1:
      questionCount = 1
    self.questionLabelCount['text'] = questionCount
  def questionCountMinus1(self):
    global questionCount
    questionCount -= 1
    if questionCount < 1:
      questionCount = 1
    self.questionLabelCount['text'] = questionCount
  def questionCountPlus1(self):
    global questionCount
    questionCount += 1
    self.questionLabelCount['text'] = questionCount
  def questionCountPlus10(self):
    global questionCount
    questionCount += 10
    self.questionLabelCount['text'] = questionCount

  def answerCountMinus4(self):
      global answersCount
      answersCount -= 4
      if answersCount < 4:
        answersCount = 12
      self.answerLabelCount['text'] = answersCount
  def answerCountMinus1(self):
      global answersCount
      answersCount -= 1
      if answersCount < 4:
        answersCount = 12
      self.answerLabelCount['text'] = answersCount
  def answerCountPlus1(self):
      global answersCount
      answersCount += 1
      if answersCount > 12:
        answersCount = 4
      self.answerLabelCount['text'] = answersCount
  def answerCountPlus4(self):
      global answersCount
      answersCount += 4
      if answersCount > 12:
        answersCount = 4
      self.answerLabelCount['text'] = answersCount

  def mainKeyCreator(self):
    self.masterMainWindowCreateKey = Toplevel(self.master)
    self.appWindowCreateKey = MainKeyCreatorWindow(self.masterMainWindowCreateKey, self)
  def exportKeyFile(self, file):
    with open(file, 'wb') as keyFile:
      pickle.dump(KEY_DICT, keyFile)

  def die(self):
    global KEY_FILE
    KEY_FILE = filedialog.asksaveasfilename(
      title = "Select exam key file",
      initialdir = './keys',
      filetypes =(("Exam Key File", "*.exkey"),)
    )
    if '.exkey' not in KEY_FILE:
      KEY_FILE += '.exkey'
    if KEY_FILE != '..exkey': # if no filename provided, don't proceed
      self.exportKeyFile(KEY_FILE)
      self.above.inputButton['state'] = NORMAL
      self.master.destroy()

class MainKeyCreatorWindow(object):
  """Window to create exam key"""
  def __init__(self, master, above):
    global KEY_DICT
    KEY_DICT = {}
    self.master = master
    self.master.resizable(width=False, height=False) # lock window resize
    self.master.iconbitmap(r'./ico.ico') # icon
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
    self.mainLabel['width'] = 20
    self.mainLabelUpdate()
    self.mainLabel.grid(row = R, column = C, columnspan = 5, sticky = 'we')
    # question/answer buttons #
    # back button
    newRow()
    self.backButton = Button(frame)
    # self.backButton['width'] = 3
    self.backButton['text'] = "<"
    self.backButton['command'] = self.backQuestion
    rs = 1
    if answersCount > 4:
      rs += 1
    if answersCount > 8:
      rs += 1
    self.backButton.grid(row = R, column = C, rowspan = rs, sticky = 'nesw')
    newCol()
    self.aButton = Button(frame)
    self.aButton['text'] = "A"
    self.aButton['command'] = partial(self.bindAnswer, "A")
    self.aButton.grid(row = R, column = C, sticky = 'we')
    newCol()
    self.bButton = Button(frame)
    self.bButton['text'] = "B"
    self.bButton['command'] = partial(self.bindAnswer, "B")
    self.bButton.grid(row = R, column = C, sticky = 'we')
    newCol()
    self.cButton = Button(frame)
    self.cButton['text'] = "C"
    self.cButton['command'] = partial(self.bindAnswer, "C")
    self.cButton.grid(row = R, column = C, sticky = 'we')
    newCol()
    self.dButton = Button(frame)
    self.dButton['text'] = "D"
    self.dButton['command'] = partial(self.bindAnswer, "D")
    self.dButton.grid(row = R, column = C, sticky = 'we')
    if answersCount > 4:
      newRow()
      if answersCount > 4:
        newCol()
        self.eButton = Button(frame)
        self.eButton['text'] = "E"
        self.eButton['command'] = partial(self.bindAnswer, "E")
        self.eButton.grid(row = R, column = C, sticky = 'we')
      if answersCount > 5:
        newCol()
        self.fButton = Button(frame)
        self.fButton['text'] = "F"
        self.fButton['command'] = partial(self.bindAnswer, "F")
        self.fButton.grid(row = R, column = C, sticky = 'we')
      if answersCount > 6:
        newCol()
        self.gButton = Button(frame)
        self.gButton['text'] = "G"
        self.gButton['command'] = partial(self.bindAnswer, "G")
        self.gButton.grid(row = R, column = C, sticky = 'we')
      if answersCount > 7:
        newCol()
        self.hButton = Button(frame)
        self.hButton['text'] = "H"
        self.hButton['command'] = partial(self.bindAnswer, "H")
        self.hButton.grid(row = R, column = C, sticky = 'we')
    if answersCount > 8:
      newRow()
      if answersCount > 8:
        newCol()
        self.iButton = Button(frame)
        self.iButton['text'] = "I"
        self.iButton['command'] = partial(self.bindAnswer, "I")
        self.iButton.grid(row = R, column = C, sticky = 'we')
      if answersCount > 9:
        newCol()
        self.jButton = Button(frame)
        self.jButton['text'] = "J"
        self.jButton['command'] = partial(self.bindAnswer, "J")
        self.jButton.grid(row = R, column = C, sticky = 'we')
      if answersCount > 10:
        newCol()
        self.kButton = Button(frame)
        self.kButton['text'] = "K"
        self.kButton['command'] = partial(self.bindAnswer, "K")
        self.kButton.grid(row = R, column = C, sticky = 'we')
      if answersCount > 11:
        newCol()
        self.lButton = Button(frame)
        self.lButton['text'] = "L"
        self.lButton['command'] = partial(self.bindAnswer, "L")
        self.lButton.grid(row = R, column = C, sticky = 'we')

  def backQuestion(self):
    self.questionNo -= 1
    if self.questionNo < 1:
      self.questionNo = 1
    self.mainLabelUpdate()
  def bindAnswer(self, questionAnswer):
    global KEY_DICT
    KEY_DICT[self.questionNo] = questionAnswer
    self.questionNo += 1
    self.mainLabelUpdate()
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
    self.master.resizable(width=False, height=False) # lock window resize
    self.master.iconbitmap(r'./ico.ico') # icon
    self.above = above
    self.frame = Frame(self.master)
    self.build(self.frame)
    self.frame.grid()
  def build(self, frame):
    global RESULT_DICT
    zeroCol()
    # legend #
    Label(frame,
          text = "Name",
          fg = 'blue',
          width = 15).grid(row = R, column = C)
    newCol()
    Label(frame,
          text = "Points",
          fg = 'blue',
          width = 10).grid(row = R, column = C)
    newCol()
    Label(frame,
          text = "Result",
          fg = 'red').grid(row = R, column = C)
    # results #
    for filename in RESULT_DICT:
      newRow()
      Label(frame,
            text = filename).grid(row = R, column = C)
      newCol()
      Label(frame,
            text = RESULT_DICT[filename][0]).grid(row = R, column = C)
      newCol()
      Label(frame,
            text = RESULT_DICT[filename][1]).grid(row = R, column = C)

def main():
  root = Tk()
  root.title("SeriEx")
  ws = root.winfo_screenwidth()
  hs = root.winfo_screenheight()
  app = MainWindow(root)
  root.mainloop()

if __name__ == '__main__':
  main()
