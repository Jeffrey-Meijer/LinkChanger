import requests
import json
import bs4 as bs

def get_footer():
    r = requests.get('http://localhost/linkscript/wp-json/hq/v1/elementor/footer')
    data = json.loads(r.json()['_elementor_data'][0])
    for element in data:
        for el in element["elements"]:
            if el["elements"]:
                for l in el["elements"]:
                    if l["settings"]["editor"]:
                        toEdit = l["settings"]["editor"]

    
    print(toEdit)

    toEdit = toEdit.replace("https://webdesignhq.nl/", "https://hqonline.nl/") # Change URL
    toEdit = toEdit.replace("Webdesignhq", "HQ Online")
    print(toEdit)


def main():
    get_footer()


if __name__ == "__main__":
    main()