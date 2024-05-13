In this task, we explore the world of Harry Potter's spells and potions. You should download the zip file HarryPotter.zip Download HarryPotter.zip, which contains various files: characters, potions, spells, and the first three books. In your code, you should be able to unzip the entire file and start from there.

The goal is to search for the characters who use a specific spell or potion based on a book, spell, or potion.

Create the following functions:
mentions(book, text) this function searches for the number of times a specific spell or potion appears in a book. It prints the count and also returns a dictionary of the character who used it and a list of line numbers.
character(name): this function prints the full name, house, and age of today or at the time of their death. 
calculate_age(birth,death=''): this helper function calculates a person's age based on their date of birth and date of death (if found). If the dates are not given in the format 'dd month yyyy' (sometimes with a comma before the year), the age cannot be calculated.
spell(text): this function searches for a specific spell and returns an overview of its characteristics as key-value pairs.
potion(text): this function searches for a specific potion and returns an overview of its characteristics as key-value pairs.
Write this all in a script "spells.py" that should call the main() function from an if __name__ == "__main__": block!

Important: you are not allowed to use pandas or to install extra packages!
Your're allowed to use os, pathlib, zipfile, csv, datetime and collections

Example usage:

$ python3 script.py 

Enter book: 1
Enter spell/potion: Alohomora

4 apperances of Alohomora in book Harry Potter 1.csv

Hermione on line(s) 724, 1337
Hermione Jean Granger
Gryffindor
Hermione is today 43 years old.

Ron on line(s) 726, 1396 
Ronald Bilius Weasley Gryffindor 
Ron is today 43 years old.  

SPELL Alohomora 
Name: Unlocking Charm 
Incantation: Alohomora 
Type: Charm 
Effect: Unlocks target 
Light: Invisible, blue, yellow, or purple
