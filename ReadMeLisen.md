For this task, you create a script called "license_plate.py" that checks the validity of a Belgian license plate. Once the user inputs a license plate, the script needs to verify its validity. If the license plate is valid, the user will be prompted to select a format to display the license plate in. The available formats are the NATO alphabet, Morse code or ASCII art

Special license plates:
1-9: vehicle from king and/or queen (output kind and queen)
10-99: vehicles from other royal family members (output royal)
A-1 → A-999: official (vehicles)
CD-AA111 → CD-ZZ999: diplomat (vehicles)
G-LAA-111 → G-LZZ-999: agriculture  (vehicles)
M-AAA-000 → M-ZZZ-999: motorcycle(s)
O-AAA-111 → O-ZZZ-999: oldtimer(s)
Q-AAA-000 → Q-ZZZ-999: trailer(s)
T-XAA-000 → T-XZZ-999: taxi(s)
Y-AAA-000 → Y-ZZZ-999: test (drives)
Standard license plates are categorized according to the corresponding years
1962-1971: AA.001 → ZZ.999
1971-1973: A.001.A → Z.999.Z
1973-2008: AAA-001 → ZZZ-999
2008-2010: 001-AAA → 999-CFQ
2010-now: 1-AAA-001 → 7-ZZZ-999
Also, take into account a list of forbidden letter combinations.
AAP AAS AEL ALA ANE ASS BEB BIT BOM BOY BSP BUB BWP BYT CAP CDF CDH CDV CON CSP CUB CUL CUT CVP DCD DIK DOM FDF FOK FOL FOU FUC FUK GAT GAY GEK GOD HIV HOL JEK KAK KKQ KUL KUT LAF LDD LSP LUL MAS MCC MDP MOR MOU MST NIC NIK NIQ NVA PDB PDO PET PFF PIK PIN PIP PIS PJU PKK POT PRL PSB PSC PSL PTB PUE PUT PVV PYK PYN PYP PYS ROM SEX SOA SOT SPA SUL TAK TET TIT TUE VCD VIH VLD VMO VNV ZAC ZAK ZOT
Create (at least) these functions:
forbidden(plate) which returns a boolean True if the plate holds a forbidden letter combination and False if not
check(plate) which can return the following strings:
invalid plate
forbidden plate - <forbidden combination>
standard plate - <year range>
special plate - <special category>
nato(plate) which returns the plate (without nonalphabetical characters) in NATO phonetic alphabetLinks to an external site. (package phonetic-alphabetLinks to an external site. already in CodeGrade)
morse(plate) which returns the plate (without nonalphabetical characters) in morse code Links to an external site.(package morse3Links to an external site. already in CodeGrade)Links to an external site.
ascii(plate) which returns the plate in ASCII artLinks to an external site. (package artLinks to an external site. already in CodeGrade)
main() which calls all functions as needed
Write this all in a script that should call the main() function from an if __name__ == "__main__": block!

Important: you are only allowed to use 2 out of the 3 suggested packages (so you will have to code at least one function yourself) and you are not allowed to install any additional packages!
If you do use all 3 packages or any others, your grade will be deduced!

Example usage:

$ python3 script.py 
Enter license plate: Y.456.T
standard plate - 1971-1973
Enter format: morse
-.-- ....- ..... -.... - 


Enter license plate: CD-AT654
special plate - diplomat
Enter format: blabla
Wrong format!


Enter license plate: G-UIO-100
standard plate - 1973-2008
Enter format: ascii
  ____         _   _  ___   ___          _   ___    ___  
 / ___|       | | | ||_ _| / _ \        / | / _ \  / _ \ 
| |  _  _____ | | | | | | | | | | _____ | || | | || | | |
| |_| ||_____|| |_| | | | | |_| ||_____|| || |_| || |_| |
 \____|        \___/ |___| \___/        |_| \___/  \___/ 

Enter license plate: 6
special plate - king and queen
Enter format: nato
SIX
      