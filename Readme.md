Elke had her birthday last weekend #hooray and that was the inspiration for a whole exercise about dates! You read a birthdate and find out what the zodiac sign is, the age, the radio hit, which historical events took place on that one day of the month, what percentage of people were also born on that day, and so on... and let's face it, how fun is it to gather all that information about your own birthday?

In this exercise, you will work with files and an API, and you will also do some web scraping... all of this using a single or multi-threaded approach!

For this assignment, you will need to create six functions as follows:
zodiac(day, month) prints the right zodiac sign based on a day and a month
percentage(day, month) finds the percentage (rounded by 2 digits) of people born on the same day. You use for this task the file data.csv Download data.csv(file already in CC) which contains records of daily births from 2000 to 2014, including the year, month, day of the month, day of the week, number of births, and date in the format of month/day/year. Since we have data from 14 years, we can say that we have reasonably good information. And the good news: you are allowed to use pandas!
historical(day, month) prints a list of 10 historical events that took place on that day of the month, use the API https://api-ninjas.com/api/historicaleventsLinks to an external site. for this task!
one(day, month, year) prints the number one hit in the US! Scrape the information from this website https://www.onthisday.com/Links to an external site. (ex: on my birthdate asked Blondie to Call her ;) https://www.onthisday.com/date/1980/april/23)Links to an external site. 
wikipedia(day, month) creates a file of all famous birthdays scraped from Wikipedia (hint: take a good look at the url, days are always formatted like this). The function prints out the name of the file created (ex: https://en.wikipedia.org/wiki/April_23Links to an external site. --> April_23.txt Download April_23.txt)
 age(day, month, year) prints the age (easy ;))
You must be able to read in different date formats (eg: "04/23/1980", "1980/04/23", "Apr 23, 1980" etc...), and once they are correctly formatted, you will also determine whether the functions should be executed in a single or multi-threaded manner. Don't panic if the order of execution differs (which may happen), and that's why in the multithreading tests in CC, only partial output is verified.

Write this all in a script "birthday.py" that calls the main() function from an if __name__ == "__main__": block!
Note you are allowed to use the external packages pandas, beautifulsoup, requests and dateutil (and also take a close look at the built-in module calendar)!



OUTPUT:
$ python3 birthday.py 
23-04-1980
single

Today 44 years old!
Zodiac sign: Taurus
Percentage of people born on same day: 0.27 %
Historical events:
-0215 - A temple is built on the Capitoline Hill dedicated to Venus Erycina to commemorate the Roman defeat at Lake Trasimene.
0599 - Maya king Uneh Chan of Calakmul attacks rival city-state Palenque in southern Mexico, defeating queen Yohl Ik'nal and sacking the city.
0711 - Dagobert III succeeds his father King Childebert III as King of the Franks.
1014 - Battle of Clontarf: High King of Ireland Brian Boru defeats Viking invaders, but is killed in battle.
1016 - Edmund Ironside succeeds his father Æthelred the Unready as King of England.
1343 - St. George's Night Uprising commences in the Duchy of Estonia.
1348 - The founding of the Order of the Garter by King Edward III is announced on St. George's Day.
1500 - Portuguese explorer Pedro Alvarez Cabral reaches new coastline (Brazil).
1516 - The Munich Reinheitsgebot (regarding the ingredients of beer) takes effect in all of Bavaria.
1521 - Battle of Villalar: King Charles I of Spain defeats the Comuneros.
File saved as April_23.txt
Number one hit: Call Me - Blondie


2 May 2013
multi

Today 10 years old!
Zodiac sign: Taurus
Percentage of people born on same day: 0.28 %
Number one hit: Just Give Me A Reason - P!nk Featuring Nate Ruess
Historical events:
1194 - King Richard I of England gives Portsmouth its first Royal Charter.
1230 - William de Braose is hanged by Prince Llywelyn the Great.
1536 - Anne Boleyn, Queen of England, is arrested and imprisoned on charges of adultery, incest, treason and witchcraft.
1559 - John Knox returns from exile to Scotland to become the leader of the nascent Scottish Reformation.
1568 - Mary, Queen of Scots, escapes from Loch Leven Castle.
1611 - The King James Version of the Bible is published for the first time in London, England, by printer Robert Barker.
1625 - Afonso Mendes, appointed by Pope Gregory XV as Latin Patriarch of Ethiopia, arrives at Beilul from Goa.
1670 - King Charles II of England grants a permanent charter to the Hudson's Bay Company to open up the fur trade in North America.
1808 - Outbreak of the Peninsular War: The people of Madrid rise up in rebellion against French occupation. Francisco de Goya later memorializes this event in his painting The Second of May 1808.
1812 - The Siege of Cuautla during the Mexican War of Independence ends with both sides claiming victory after Mexican rebels under José María Morelos y Pavón abandon the city after 72 days under siege by royalist Spanish troops under Félix María Calleja.
File saved as May_2.txt