import os 
import csv 
from datetime import datetime
from collections import defaultdict
from zipfile import ZipFile 
import pathlib

def calculate_age(birth, death=''):
    try:
        birth_date =datetime.strptime(birth, '%d %B %Y')
        if death:
            death_date =datetime.strptime(death, '%d %B %Y')
            return (death_date - birth_date).days // 365
        else:
            today =datetime.now()
            return (today -birth_date).days // 365
    except ValueError:
        return "Cannot calculate age with given date format."

def mentions(book, text):
    book_path =f'Harry Potter {book}.csv'
    mentions_count =0
    characters = defaultdict(list)
    with open(book_path, newline='', encoding='uft-8') as csvfile:
        reader =csv.reader(csvfile)
        for i, row in enumerate(reader, 1):
            if text in row[0]:
                mentions_count+=1
                characters[row[1]].append(i)
    print(f'{mentions_count} appearances of {text} in book {book_path}\n')
    for character, lines in characters.items():
        print(f'{character} on line(s) {", ".join(map(str, lines))}')
    return characters

def character(name):
    with open('Characters.csv', newline='', encoding='uft-8') as csvfile:
        reader =csv.DictReader(csvfile)
        for row in reader:
            if row['Name'] == name:
                age =calculate_age(row['Birth'], row.get('Death', ''))
                print(f"{row['Name']}\n{row['House']}\n{age} years old.\n")
                break


def spell(text):
    with open('Spells.csv',newline='', encoding='uft-8') as csvfile:
        reader =csv.DictReader(csvfile)
        for row in reader: 
            if row ['Name'] == text:
                print(f"SPELL {text}\n")
                for key, value in row.items():
                    print(f"{key}: {value}")
                break

def potion(text):
    with open('Potions.csv', newline='', encoding='uft-8') as csvfile:
        reader =csv.DictReader(csvfile)
        for row in reader:
            if row['Name'] == text:
                print(f"POTION {text}\n")
                for key, value in row.items():
                    print(f"{key}: {value}")
                break


def main():
    book =input("Enter boook: ")
    text =input("Enter spell/potion: ")


if __name__ == "__main__":
  main()