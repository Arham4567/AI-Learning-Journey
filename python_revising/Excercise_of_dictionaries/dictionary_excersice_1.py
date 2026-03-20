"""We have the following information on countries and their population (population is in crores),

Country	Population
China	143
India	136
USA	    32
Pakistan	21

1) Using above create a dictionary of countries and its population
2) Write a program that asks user for three type of inputs,

a) print: if user enter print then it should print all countries with their population in this format,

china==>143
india==>136
usa==>32
pakistan==>21

b) add: if user input add then it should further ask for a country name to add. If country already exist in our dataset then it should print that it exist and do nothing. If it doesn't then it asks for population and add that new country/population in our dictionary and print it

c) remove: when user inputs remove it should ask for a country to remove. If country exist in our dictionary then remove it and print new dictionary using format shown above in (a). Else print that country doesn't exist!

d) query: on this again ask user for which country he or she wants to query. When user inputs that country it will print population of that country."""
from os import remove

country_population={
    "china":143,
    "india":136,
    "usa":32,
    "pakistan":21
}

def print_all_countries(country):
    for cunt,p in country.items():
        print(cunt,"==>",p)


def add_country(country):
    cunt = input("Enter country name to add: ")
    cunt=cunt.lower()
    if cunt in country:
        print("Country already exist in our dataset")
        add_country(country)
    else:
        population = int(input("Enter country population: "))
        country[cunt] = population
        print("Country population added updated data set : " )
        print_all_countries(country_population)

def remove_country(country):
    cunt = input("Enter country name to remove: ")
    cunt = cunt.lower()
    if cunt in country:
        country.pop(cunt)
        print("Country & population removed,updated data set : " )
        print_all_countries(country_population)


def query_country(country):
    cunt = input("Enter country name to query: ")
    cunt = cunt.lower()
    if cunt not in country:
        print("Country dont exist in our dataset")
        add_country(country)
    else:
        print("Population of ",cunt,"is => ",country[cunt])


def choices(country):

    if choice == "print":
        print_all_countries(country)
    elif choice == "add":
        add_country(country)
    elif choice == "remove":
        remove_country(country)
    elif choice == "query":
        query_country(country)
    else:
        print("Invalid choice")


if __name__ == '__main__':
    x="1"
    while x != "ok":
        choice = input("Enter the operation you wanna perform ,print,add,remove,and query on a given dataset ")
        choice = choice.lower()
        choices(country_population)
        if choice == "ok":
            x="ok"
            print("program terminated")
