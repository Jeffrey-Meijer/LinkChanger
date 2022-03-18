import requests
import json
import bs4 as bs

def get_footer():
    r = requests.get('https://tegelsensanitairbeilen.nl/wp-json/hq/v1/elementor/footer')
    # data = json.dumps(r.json()['_elementor_data'][0]).encode('utf-8').decode('unicode-escape') # Elementor footer data
    data = json.loads(r.json()['_elementor_data'][0])
    for element in data:
        # if element["editor"]
        # if element["elements"]["settings"]["editor"]:
            # print(element["elements"]["settings"]["editor"])        
        # else:
            # print(element["elements"]["elements"]["settings"]["editor"])
        print(element["elements"])
        # break
    # soup = bs.BeautifulSoup(data)

    # print(data)

def main():
    get_footer()


if __name__ == "__main__":
    main()