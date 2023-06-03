import requests

def print_town(town):
    payload = {'days': '3', 'version': 'n' 'color': 'T', 'wind': 'M', 'quiet': 'q'}#, 'lang': 'lang=ru'}
    adres = requests.get('https://wttr.in/' + town, params=payload)
    # url = 'https://wttr.in/' + town + '?3?n?T?M?q&lang=ru'
    print(adres.url)
    response = requests.get(adres.url)
    # response = requests.get('https://wttr.in/' + town + '?3?n?T?M?q&lang=ru')
    response.raise_for_status()
    print(response.text)

def main():
    towns = ['san%20francisco','SVO','Череповец']

    for town in towns:
        print_town(town)


# Предыдущее задание: 

    # url = 'https://wttr.in/san%20francisco?nTqu&lang=en'
    # response = requests.get(url)
    # response.raise_for_status()
    # print(response.text)   

    # url = 'https://wttr.in/London?3?n?T'
    # response = requests.get(url)
    # response.raise_for_status()
    # print(response.text)

    # url = 'https://wttr.in/Череповец?3?n?T'
    # response = requests.get(url)
    # response.raise_for_status()
    # print(response.text)

    # url = 'https://wttr.in/SVO?3?n?T'
    # response = requests.get(url)
    # response.raise_for_status()
    # print(response.text)

    # url = 'https://wttr.in/Череповец?3?n?T?M?q&lang=ru'
    # response = requests.get(url)
    # response.raise_for_status()
    # print(response.text)

# Конец предедыщего задания

if __name__ == '__main__':
    main()