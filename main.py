import requests
import json

def get_obj():
    r = requests.get("http://localhost/linkscript/wp-json/hq/v1/elementor/footer")
    return json.loads(r.json()["_elementor_data"][0])

# TO DO, Werkt alleen met 1 extra inner section, meer zorgt ervoor dat ie hem niet vind
def replace_footer(obj, main_element=None, count=0):
    if count == 0:
        main_element = obj
        count += 1
    for element in obj:
        if element['elType'] in ['section', 'column']:
            element = element['elements']
            return replace_footer(element,main_element,count)
        else:
            if element['settings']:
                if element['settings'].get('editor'):
                    print(element['settings']['editor'])
                    original = json.dumps(element['settings']['editor'])
                    toEdit = original
                    toEdit = toEdit.replace("https://webdesignhq.nl/", "https://hqonline.nl/")
                    toEdit = toEdit.replace("Webdesignhq", "HQ Online")
                    
                    main_element = json.dumps(main_element)
                    main_element = main_element.replace(original, toEdit)
                    main_element = main_element.replace("\\", "\\\\")
                    return main_element

def send_data(new_footer):
    obj = {
        "_elementor_data": new_footer
    }
    r = requests.post("http://localhost/linkscript/wp-json/hq/v1/elementor/footer", data=obj)
    status = r.status_code
    if status == 200:
        print(r.text)
    else:
        print(status)


def main():
    new_footer = replace_footer(get_obj())
    if new_footer != None:
        send_data(new_footer)
        print('Header changed!')
    else:
        print('Header failed to change!')


if __name__ == "__main__":
    main()