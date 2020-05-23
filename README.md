# SerialExaminer
SerialExaminer is a small tool to speed up assessing tests and detecting potential fraudsters. It's easy to use, fast to use and will be long developed and improved

Ask your students to send you test responses in .txt files named after their full names, journal number, any ID numbers or anything else, that can identify them. Aks them to write answers in these files in format `<question number>.<correct answer>`, line by line. The order of questions and letter size don't matter

#### Table of Contents
- [Installation](https://github.com/Pixel48/SerialExaminer#installation)
  - [Windows](https://github.com/Pixel48/SerialExaminer#windows)
  - [Linux](https://github.com/Pixel48/SerialExaminer#linux)
- [Usage](https://github.com/Pixel48/SerialExaminer#usage)
  - [Generating an exam key](https://github.com/Pixel48/SerialExaminer#generating-an-exam-key)
  - [Importing an exam key](https://github.com/Pixel48/SerialExaminer#importing-an-exam-key)
  - [Checking tests](https://github.com/Pixel48/SerialExaminer#checking-tests)
  - [Searching for cheaters](https://github.com/Pixel48/SerialExaminer#-searching-for-cheaters)

## Installation
### Windows
To install SerialExaminer download installer from [last release](https://github.com/Pixel48/SerialExaminer/releases/latest), install it and run using fresh desktop shortcut
> For now every installer will trigger [UAC](https://en.wikipedia.org/wiki/User_Account_Control), because it's not digitally signed, because I'm just a student developing a small project and (for now) I can't afford digital certification

## Usage
### Generating an exam key

![Check button](docs/img/check_button.png)

### Importing an exam key
### Checking tests
### Searching for cheaters

## Usage (old)
### Creating exam key file
![Exam file example](docs/img/exam_file.png)
1. Run SerialExaminer from desktop shortcut and create or import exam key file (\*.exkey).
   - If you create exam key file...
     - Provide the exact number of questions and answers in the exam and hit `Create key!` button

     ![Key parameters](docs/img/key_parameters.png)
     > Now the key creator supports the number of answers from 4 to 12, future updates will gradually expand this range until they finally remove this restriction

     - Provide answers to questions about the given number. If you make a mistake you can go back using the `<` button. Window will disappear automatically after entering the last answer

     ![Key answers](docs/img/key_ans.png)

     - After key answer window vanish, hit `Done` button and provide where to save exam key for potential future use. (You dont need to import key after creating it, it's imported immediately after save).
   - If you already had created exam key file...
2. Hit `Browse` button and provide folder with files from step 1.
3. Hit `Check!` button to calculate results

![Check button](docs/img/check_button.png)
> Future updates will automate this process and remove this button

4. Use `Display` button to show test results

![Example results table](docs/img/results.png)
> Future updates will add export options and `predicted grade` column in results

###### Copyright (c) 2020 [Pixel48](https://github.com/Pixel48/) All Rights Reserved
