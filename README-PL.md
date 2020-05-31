# SerialExaminer [![readme translation](https://img.shields.io/badge/tłumaczenie%20pliku-polski-red?color=f00&logo=google-translate&logoColor=fff&style=for-the-badge)][readme-pl] [![translate to english](https://img.shields.io/badge/-english-blue?color=00f&style=for-the-badge)][readme-en]
  [![license](https://img.shields.io/github/license/Pixel48/SerialExaminer?color=brown&label=licencja)](https://github.com/Pixel48/SerialExaminer/blob/master/LICENSE)
  [![last release](https://img.shields.io/github/v/release/Pixel48/SerialExaminer?color=brightgreen&label=wersja)](https://github.com/Pixel48/SerialExaminer/releases/latest)
  [![GitHub commit activity](https://img.shields.io/github/commit-activity/m/Pixel48/SerialExaminer?color=informational&logo=github)](https://github.com/Pixel48/SerialExaminer/commits/develop)

## Table of Contents
  - [Wprowadzenie](#wprowadzenie)
  - [Instalacja](#instalacja)
    - [Windows](#windows)
    - [Linux](#linux)
  - [Instrukcja obsługi](#instrukcja-obsługi)
    - [Zbieranie odpowiedzi](#zbieranie-odpowiedzi)
    - [Generowanie klucza odpowiedzi](#generowanie-klucza-odpowiedzi)
    - [Importowanie klucza odpowiedzi](#Importowanie-klucza-odpowiedzi)
    - [Sprawdzanie odpowiedzi](#sprawdzanie-odpowiedzi)
  - [Feedback](#feedback)

## Wprowadzenie
  Większość nauczycieli sprawdza wiedzę swoich uczniów za pomocą listy pytań z kilkoma opcjami odpowiedzi. Ta metoda jest w porządku, ale generuje dużo pracy. Godziny pracy. Dzięki SerialExaminer godziny te mogą stać się sekundami, zwracając zmarnowany czas

## Instalacja

### Windows
  Aby uruchomić ten projekt na komputerze, pobierz i uruchom odpowiedni instalator z [ostatniej wersji][latest-release] projektu

  `SerialExaminerSetup.exe` jest 32-bitowy. W przypadku systemów 64-bitowych pobierz `SerialExaminerSetup-x64.exe`
  Aby sprawdzić, ile bitów ma Twój system, sprawdź informacje o systemie w _Ustawieniach systemu_
  > Uruchomienie pobranego instalatora uruchomi __[UAC](https://en.wikipedia.org/wiki/User_Account_Control) *Nieznany wydawca*__, ponieważ nie jest podpisany cyfrowo - na razie nie stać mnie na cyfrową certyfikację. Możesz użyć srtony [Virustotal](https://www.virustotal.com/gui/home/upload), aby upewnić się, że instalator jest czysty

### Linux
  Aby uruchomić ten projekt na swoim niesamowitym systemie, użyj następującego kodu
  > Najpierw upewnij się, że na twoim systemie został zainstalowany [Python3](https://www.python.org)

  ```bash
  cd ~/Desktop
  git clone https://github.com/Pixel48/SerialExaminer.git
  cd SerialExaminer
  python3 SerialExaminer.py
  ```

## Instrukcja obsługi
  Krótki przewodnik na temat korzystania z SerialExaminer

### Zbieranie odpowiedzi
  Uczniowie powinni przesłąć odpowiedzi testowe w plikach **.txt** nazwane ich imieniem i nzawiskiem, numerem dziennika, dowolnym numerem identyfikacyjnym lub czymkolwiek innym, co może ich zidentyfikować. Uczniowie muszą zapisać odpowiedzi w formacie `<numer pytania>. <wybrana odpowiedź>`, wiersz po wierszu. Kolejność pytań i wielkość liter nie mają znaczenia

### Generowanie klucza odpowiedzi
  1. Podaj dokładną liczbę pytań, opcji odpowiedzi na pytanie i naciśnij przycisk `Create key`
  2. Podaj odpowiedzi na pytania o podanym numerze. W razie popełnienia błędu, możesz wrócić do poprzedniego pytania za pomocą przycisku `<`. Okno zniknie automatycznie po wprowadzeniu ostatniej odpowiedzi
  3. Po zniknięciu okna odpowiedzi, w poprzednim oknie naciśnij przycisk `Done` i podaj ścierzkę zapisu nowego klucza odpowiedzi do potencjalnego wykorzystania w przyszłości. Klucz jest automatycznie importowany po jego utworzeniu

### Importowanie klucza odpowiedzi
  1. Naciśnij przycisk `Import`
  2. W nowym oknie dialogowym wybierz plik klucza, który chcesz zaimportować

  Możesz zaimportować klucz z pliku _.txt_, jeśli został on sformatowany jako odpowiedź na egzamin

### Sprawdzanie odpowiedzi
  1. Utwórz lub zaimportuj poprawny klucz odpowiedzi
  2. Naciśnij przycisk `Browse` i wskarz folder z plikami odpowiedzi zapisanymi przez uczniów
  3. Naciśnij przycisk `Check`, aby obliczyć wyniki
  4. Naciśnij przycisk `Display`, aby wyświetlić wyniki testu (pierwsze 270 rekordów)
  5. Naciśnij przycisk Eksportuj, jeśli chcesz wygenerować plik raportu z tabelą wyników w wybranym formacie
  > Przyszłe aktualizacje dodadzą opcje eksportu i kolumnę przewidywanej oceny w wynikach

## Feedback
  [![GitHub issues open](https://img.shields.io/github/issues-raw/Pixel48/SerialExaminer?color=yellow&label=otwarte%20wątki)][issues]
  [![GitHub issues closed](https://img.shields.io/github/issues-closed-raw/Pixel48/SerialExaminer?color=red&label=zamknięte%20wątki)][issues]

  Jeśli korzystałeś z programu, czuj się zaproszony do otwarcia wątku na [stronie problemów][issues] projektu, aby pomóc mi ulepszyć moją pracę

---
###### Copyright (c) 2020 [Pixel48](https://github.com/Pixel48/) All Rights Reserved
  [readme-en]: ./README.md "English translation"
  [readme-pl]: ./README-PL.md "Polskie tłumaczenie"
  [latest-release]: https://github.com/Pixel48/SerialExaminer/releases/latest
  [issues]: https://github.com/Pixel48/SerialExaminer/issues
