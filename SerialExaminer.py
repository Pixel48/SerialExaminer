#
# -*- coding: utf-8 -*-
# SerialExaminer.py
#   by Pixel
from tkinter import *

class MainWindow(object):
  """Creator for main apilcation window"""
  def __init__(self, master):
    self.master = master
    self.frame = Frame(self.master)
    pass # TODO: Design interface

def main():
  root = Tk()
  app = MainWindow(root)

if __name__ == '__main__':
  main()
