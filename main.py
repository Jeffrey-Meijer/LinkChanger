from dataclasses import replace
import requests
import json
import bs4 as bs

def replace_footer(data=None):
    # if r == None:
    r = requests.get("http://localhost/linkscript/wp-json/hq/v1/elementor/footer")
    if data is None:
        data = json.loads(r.json()["_elementor_data"][0])
    for element in data:
        if element.get('settings'):
            if element['settings'].get('editor'):
                print('exists')
                print(element["settings"]["editor"])
                toEdit = element["settings"]["editor"]
                toEdit = toEdit.replace("https://webdesignhq.nl/", "https://hqonline.nl/")
                toEdit = toEdit.replace("Webdesignhq", "HQ Online")
                # return element['settings']['editor']
                # return element
            else:
                return replace_footer(element['elements'])
        else:
            return replace_footer(element['elements'])

    return json.dumps([element])
    # print(data[0])
    # if data[0].get("editor"):
        # print("exists")
        # return replace_footer(data, r)
    # else:
        # for element in data:
        #     for el in element["elements"]:
        #         try:
        #             if el["settings"]["editor"]:
        #                 toEdit = el["settings"]["editor"]
        #                 toEdit = toEdit.replace("https://webdesignhq.nl/", "https://hqonline.nl/") # Change URL
        #                 toEdit = toEdit.replace("Webdesignhq", "HQ Online")
        #                 el["settings"]["editor"] = toEdit
        #                 return [element]
        #         except KeyError:
        #             return replace_footer(el, r)
                # else:
                    # return replace_footer(el, r)
            # if el["elements"]:
            #     for l in el["elements"]:
            #         if l["settings"]["editor"]:
            #             toEdit = l["settings"]["editor"]
            #             toEdit = toEdit.replace("https://webdesignhq.nl/", "https://hqonline.nl/") # Change URL
            #             toEdit = toEdit.replace("Webdesignhq", "HQ Online")
            #             l["settings"]["editor"] = toEdit
                        
        # return json.dumps([element])



def send_data(new_footer):
    print(new_footer.replace("\\", "\\\\"))
    obj = {
        "_elementor_data": new_footer.replace("\\", "\\\\")
    }
    # print(json.dumps(obj))
    # r = requests.post("http://localhost/linkscript/wp-json/hq/v1/elementor/footer", data=obj)
    status = r.status_code
    if status == 200:
        # print("data sent")
        print(r.text)
    else:
        print(status)


def main():
    new_footer = replace_footer()
    send_data(new_footer)


if __name__ == "__main__":
    main()