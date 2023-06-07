import requests

def print_town(town):
    payload = {'3':"", 'n':"", 'T':"", 'M':"", 'q':"", 'lang': 'ru'}
    adres = requests.get('https://wttr.in/' + town, params=payload)
    response = requests.get(adres.url)
    response.raise_for_status()
    print(response.text)

def main():
    towns = ['London','SVO','Череповец']

    for town in towns:
        print_town(town)

if __name__ == '__main__':
    main()