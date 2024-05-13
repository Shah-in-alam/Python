import pandas as pd
import requests
from bs4 import BeautifulSoup
from datetime import datetime
from dateutil.parser import parse
import threading
import calendar

data = pd.read_csv('data.csv')
data['date'] = pd.to_datetime(data['date'], format='%m/%d/%Y')

def zodiac(day, month):
    zodiac_signs = [
        ((3, 21), (4, 19), "Aries"), ((4, 20), (5, 20), "Taurus"),
        ((5, 21), (6, 20), "Gemini"), ((6, 21), (7, 22), "Cancer"),
        ((7, 23), (8, 22), "Leo"), ((8, 23), (9, 22), "Virgo"),
        ((9, 23), (10, 22), "Libra"), ((10, 23), (11, 21), "Scorpio"),
        ((11, 22), (12, 21), "Sagittarius"), ((12, 22), (1, 19), "Capricorn"),
        ((1, 20), (2, 18), "Aquarius"), ((2, 19), (3, 20), "Pisces")
    ]
    for start, end, sign in zodiac_signs:
        if (month == start[0] and day >= start[1]) or (month == end[0] and day <= end[1]):
            print(f"Zodiac sign:",sign)
    

def percentage(day, month):
    total_births = data['births'].sum()
    daily_births = data[(data['date'].dt.month == month) & (data['date'].dt.day == day)]['births'].sum()
    percent =round((daily_births / total_births) * 100, 2)
    print(f"Percentage of people born on same day:",percent ,"%")
 

def age(day,month,year):
    birthdate = datetime(year, month, day)
    today = datetime.today()
    ag=today.year - birthdate.year - ((today.month, today.day) < (month, day))
    print(f"\nToday {ag} years old!") 

def historical(day,month):
    api_url = f"https://api.api-ninjas.com/v1/historicalevents?month={month}&day={day}"
    try:
        response = requests.get(api_url, headers={'X-Api-Key': 'sUxIFLk8PRz9olfC+RNvKg==vectXLQ63uuZDpa4'})
        response.raise_for_status()
        events = response.json()
        print(f"Historical events:")
        for event in events[:10]:
            print(f"{event['year']} - {event['event']}")
    except requests.exceptions.HTTPError as errh:
        print(f"HTTP Error: {errh}")
    except requests.exceptions.ConnectionError as errc:
        print(f"Error Connecting: {errc}")
    except requests.exceptions.Timeout as errt:
        print(f"Timeout Error:", errt)
    except requests.exceptions.RequestException as err:
        print(f"OOps: Something Else", err)
        
def wikipedia(day,month):
    month_name = datetime(year=1, month=month, day=1).strftime('%B')
    url = f'https://en.wikipedia.org/wiki/{month_name}_{day}'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    birthdays = []
    for li in soup.select('ul > li'):
        if "–" in li.text:
            birthdays.append(li.text.split('–', 1)[1].strip())
    filename = f"{month_name}_{day}.txt"
    with open(filename, 'w', encoding='utf-8') as f:
        for birthday in birthdays:
            f.write(birthday + '\n')
    print(f"File save as: {filename}")

def one(day,month,year):
    # url =f"https://www.onthisday.com/date/{year}/{month}/{day}"
    # response =requests.get(url)
    # if response.status_code !=200:
    #     print(f"Failed to retrieve data: {response.status_code}")
    # soup= BeautifulSoup(response.text,'html.parser')
    # event_list =soup.find('ul',class_='event_li')
    # if not event_list:
    #     print("No events list found.")
    # hit_song =event_list.find('li',class_='event')
    # if not hit_song:
    #     print("No hit song found on this date.")
    # song_details =[b.get_text(strip =True) for b in hit_song.find_all('b')]
    # if len(song_details)>=2:
    #     song =song_details[0]
    #     description =song_details[1]
    #     print("{song} - {description}")
    # else:
    #     print("Song destails are not found are incomplete")
   return
    
def main():
    date_input =input()
    status = input()
    parsed_date = parse(date_input)
    day = parsed_date.day
    month = parsed_date.month
    year = parsed_date.year

    
    age(day,month,year)
    zodiac(day, month)
    percentage(day, month)
    historical(day,month)
    wikipedia(day,month)
    #print(one(day,month,year))

if __name__ == "__main__":
    main()
