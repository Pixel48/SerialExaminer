# SerialExaminer
  SerialExaminer is a small tool to speed up assessing tests and detecting potential fraudsters. It's easy to use, fast to use and will be long developed and improved

  Ask your students to send you test responses in .txt files named after their full names, journal number, any ID numbers or anything else, that can identify them. Aks them to write answers in these files in format `<question number>.<question answer>`, line by line. The order of questions and letter size don't matter

#### Table of Contents
  - [Installation](https://github.com/Pixel48/SerialExaminer#installation)
    - [Windows](https://github.com/Pixel48/SerialExaminer#windows)
    - [Linux](https://github.com/Pixel48/SerialExaminer#linux)
  - [Usage](https://github.com/Pixel48/SerialExaminer#usage)
    - [Generating an exam key](https://github.com/Pixel48/SerialExaminer#generating-an-exam-key)
    - [Importing an exam key](https://github.com/Pixel48/SerialExaminer#importing-an-exam-key)
    - [Checking tests](https://github.com/Pixel48/SerialExaminer#checking-tests)
    - [Searching for cheaters](https://github.com/Pixel48/SerialExaminer#searching-for-cheaters)

## Installation
  Download the latest [SerialExaminer installer](https://github.com/Pixel48/SerialExaminer/releases/latest)
  > For now, downloading the installer will launch [UAC](https://en.wikipedia.org/wiki/User_Account_Control) *Unknown publisher* alert because it is not digitally signed - I'm just a student developing a small project and I can't afford digital certification

## Usage
  How to use SerialExaminer interface

  ![Main window dummy](./docs/img/main_window.png)

### Generating an exam key
  1. Provide the exact number of questions and answers in the exam and hit `Create key!` button

  ![Key parameters](./docs/img/key_parameters.png)

  2. Provide answers to questions about the given number. If you make a mistake you can go back using the `<` button. Window will disappear automatically after entering the last answer

  ![Key parameters](./docs/img/key_parameters.png)
  > Now the key creator supports the number of answers from 4 to 12, future updates will gradually expand this range until they finally remove this restriction

  3. After key answer window vanish, hit `Done` button and provide where to save exam key for potential future use. (You dont need to import key after creating it, it's imported immediately after save).

### Checking tests
  1. Create or import correct exam key
  2. Hit `Browse` button and provide folder with files written by your students
  3. Hit `Check!` button to calculate results
  4. Hit `Display` button to show test results
  > Future updates will add export options and `predicted grade` column in results

### Searching for cheaters
  1. Hit `Import` button
  2. In new dialog change file extension to ***Plain text (\*.txt)***
  3. Select the source file to which you want to check the similarity in other tests
  4. Hit `Browse` button and provide folder with other tests
  5. Hit `Check!` button to calculate results
  6. Hit `Display` button to show similarity of other tests to source test

###### Copyright (c) 2020 [Pixel48](https://github.com/Pixel48/) All Rights Reserved
