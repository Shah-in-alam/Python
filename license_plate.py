import re
import morse3
from art import *

forbidden_letters = ["AAP", "AAS", "AEL", "ALA", "ANE", "ASS", "BEB", "BIT", "BOM", "BOY", "BSP",
    "BUB", "BWP", "BYT", "CAP", "CDF", "CDH", "CDV", "CON", "CSP", "CUB", "CUL",
    "CUT", "CVP", "DCD", "DIK", "DOM", "FDF", "FOK", "FOL", "FOU", "FUC", "FUK",
    "GAT", "GAY", "GEK", "GOD", "HIV", "HOL", "JEK", "KAK", "KKQ", "KUL", "KUT",
    "LAF", "LDD", "LSP", "LUL", "MAS", "MCC", "MDP", "MOR", "MOU", "MST", "NIC",
    "NIK", "NIQ", "NVA", "PDB", "PDO", "PET", "PFF", "PIK", "PIN", "PIP", "PIS",
    "PJU", "PKK", "POT", "PRL", "PSB", "PSC", "PSL", "PTB", "PUE", "PUT", "PVV",
    "PYK", "PYN", "PYP", "PYS", "ROM", "SEX", "SOA", "SOT", "SPA", "SUL", "TAK",
    "TET", "TIT", "TUE", "VCD", "VIH", "VLD", "VMO", "VNV", "ZAC", "ZAK", "ZOT"
]

forbidden_pattern = re.compile('|'.join(forbidden_letters), re.IGNORECASE)

standard_patterns = {
    "1962-1971": r"[A-Z]{2}\.\d{3}",
    "1971-1973": r"[A-Z]\.\d{3}\.[A-Z]",
    "1973-2008": r"[A-Z]{3}-\d{3}",  
    "2008-2010": r"\d{3}-[A-Z]{3}",
    "2010-now": r"\d-[A-Z]{3}-\d{3}"
}
special_patterns = {
    "king and queen": r"^[1-9]$",
    "royal family members": r"^(?:10|[2-9]\d)$",
    "official vehicles": r"^A-[1-9]\d{0,2}$",
    "diplomat ": r"^CD-[A-Z]{2}\d{3}$",
    "agriculture vehicles": r"^G-L[A-Z]{2}-\d{3}$",
    "motorcycles": r"^M-[A-Z]{3}-\d{3}$",
    "oldtimers": r"^O-[A-Z]{3}-\d{3}$",
    "trailers": r"^Q-[A-Z]{3}-\d{3}$",
    "taxis": r"^T-X[A-Z]{2}-\d{3}$",
    "test drives": r"^Y-[A-Z]{3}-\d{3}$"
}
morse_code_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 
    'Z': '--..','-': '-....-',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', 
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.'
}
def forbidden(plate):
    return bool(forbidden_pattern.search(plate))

def check(plate):
    if forbidden(plate):
        return "forbidden plate - " + plate
    
    for year_range, pattern in standard_patterns.items():
        if re.match(pattern, plate):
            return f"standard plate - {year_range}"

    for category, pattern in special_patterns.items():
        if re.match(pattern, plate):
            return f"special plate - {category}"
    
    return "invalid plate"

def nato(plate):
    nato_alphabet = {
        'A': 'Alpha', 'B': 'Bravo', 'C': 'Charlie', 'D': 'DELTA', 'E': 'Echo',
        'F': 'Foxtrot', 'G': 'Golf', 'H': 'Hotel', 'I': 'India', 'J': 'Juliett',
        'K': 'Kilo', 'L': 'Lima', 'M': 'Mike', 'N': 'November', 'O': 'OSCAR',
        'P': 'Papa', 'Q': 'QUEBEC', 'R': 'ROMEO', 'S': 'Sierra', 'T': 'TANGO',
        'U': 'Uniform', 'V': 'Victor', 'W': 'Whiskey', 'X': 'X-RAY', 'Y': 'Yankee',
        'Z': 'ZULU',
        '0':'ZERO','1':'ONE','2':'TWO','3':'THREE','4':'FOUR','5':'FIVE',
        '6':'SIX','7':'SEVEN','8':'EIGHT','9':'NINER'
        }
    translated = []
    for char in plate.upper():
        if char.isalnum():
            translated.append(nato_alphabet.get(char, '') + " ")
        elif char == '-':
            translated[-1] = translated[-1].rstrip()  
            translated.append(" - ")
    final_output = ''.join(translated).rstrip()
    return final_output.replace(" - ", " - ")

def morse(plate):
    plate_alpha_numeric = ''.join(filter(lambda x: x.isalnum() or x == '-', plate)).upper()
    morse_code = ' '.join(morse_code_dict.get(char, '') for char in plate_alpha_numeric)
    return morse_code
def ascii(plate):
    ascii_art = text2art(text)
    return ascii_art

def main():
        plate = input("Enter the license plate: ").strip()
        validity = check(plate)
        print(validity)

        if validity != "invalid plate":
         format_choice = input("Enter format: ").lower()

        if format_choice == "morse":
            print(morse(plate))
        elif format_choice == "nato":
            print(nato(plate))
        elif format_choice == "ascii":
            print(ascii(plate))
        else:
            print("Wrong format!")

if __name__ == "__main__":
    main()