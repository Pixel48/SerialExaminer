# SerialExaminer [![readme translation](https://img.shields.io/badge/readme%20translation-polski-red?color=f00&logo=google-translate&logoColor=fff&style=for-the-badge)][readme-pl] [![translate to polish](https://img.shields.io/badge/-angielski-blue?color=00f&style=for-the-badge)][readme-en]
  [![license](https://img.shields.io/github/license/Pixel48/SerialExaminer?color=brown)](https://github.com/Pixel48/SerialExaminer/blob/master/LICENSE)
  [![last release](https://img.shields.io/github/v/release/Pixel48/SerialExaminer?color=brightgreen&label=version)](https://github.com/Pixel48/SerialExaminer/releases/latest)
  [![GitHub commit activity](https://img.shields.io/github/commit-activity/m/Pixel48/SerialExaminer?color=informational&logo=github)]()

## Table of Contents
  - [Introduction](#introduction)
    - [Description](#description)
    - [Example of use](#example-of-use)
  - [Setup](#setup)
    - [Windows](#windows)
    - [Linux](#linux)
  - [Usage](#usage)
    - [Generating test answer key](#generating-test-answer-key)
    - [Importing test answer key](#importing-test-answer-key)
    - [Checking test answers](#chacking-test-answers)
    - [Exporting test results](#exporting-test-results)
  - [Feedback](#feedback)

## Introduction
### Description
### Example of use
## Setup

### Windows
  To launch this project on your computer download and run proper installer form [last release][latest-release]

  `SerialExaminerSetup.exe` is 32-bit. For 64-bit systems, download `SerialExaminerSetup-x64.exe`
  To check how many bit your system is, check the system information in _System Settings_

  > Running downloaded installer will launch __[UAC](https://en.wikipedia.org/wiki/User_Account_Control) *Unknown publisher* alert__ because it is not digitally signed - for now I can't afford digital certification. You can use [Virustotal](https://www.virustotal.com/gui/home/upload) to make sure that installer is clean

### Linux
  To launch this project on your awesome system use following code
  > First make sure your system  has installed [Python3](https://www.python.org)

  ```bash
  cd ~/Desktop
  git clone https://github.com/Pixel48/SerialExaminer.git
  cd SerialExaminer
  python3 SerialExaminer.py
  ```

## Usage
How to use SerialExaminer

### Generating answer key
  1. Provide the exact number of questions and answers in the exam and Press `Create key` button
  2. Provide answers to questions about the question with given number. If you make a mistake you can go back using the `<` button. Window will disappear automatically after entering the last answer
  3. After key answer window vanish, press `Done` button and provide filename to save answer key for potential future use. Key is automatically imported after saving

### Importing answer key
  1. Press `Import` button
  2. In new dialog select key file you want to import

  You can import key from _.txt_ file, if it's formatted as a exam response

### Checking answers
  1. Create or import correct answer key
  2. Press Browse button and provide folder with files written by your students
  3. Press Check button to calculate results
  4. Press Display button to show test results
  5. Press Export button, if you want to generate report file with result table in selected format
  > Future updates will add export options and predicted grade column in results

### Exporting results

## Feedback
  [![GitHub issues open](https://img.shields.io/github/issues-raw/Pixel48/SerialExaminer?color=yellow)][issues]
  [![GitHub issues closed](https://img.shields.io/github/issues-closed-raw/Pixel48/SerialExaminer?color=red)][issues]

  If you have used the program, feel free to leave feedback on the project's [issues page][issues] to help me improve my work

---
###### Copyright (c) 2020 [Pixel48](https://github.com/Pixel48/) All Rights Reserved
  [readme-en]: ./README.md "English translation"
  [readme-pl]: ./README-PL.md "Polskie tłumaczenie"
  [latest-release]: https://github.com/Pixel48/SerialExaminer/releases/latest
  [issues]: https://github.com/Pixel48/SerialExaminer/issues
