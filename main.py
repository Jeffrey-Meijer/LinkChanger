# from dataclasses import replace
import requests
import json
# import bs4 as bs

# def recursive_search(data, count=0):
#     print(data)
#     if count == 0:
#         toEdit = None
#         count += 1
#     if isinstance(data, list):
#         for x in data:
#             if x.get('settings'):
#                 if x['settings'].get('editor'):
#                     print('exists')
#                     toEdit = x["settings"]["editor"]
#                     element_to_change = json.dumps(toEdit)
#                     toEdit = toEdit.replace("https://webdesignhq.nl/", "https://hqonline.nl/")
#                     toEdit = toEdit.replace("Webdesignhq", "HQ Online")
#                 else:
#                     return recursive_search(x["elements"], count)
#             else:
#                 return recursive_search(x["elements"], count)
#     else:
#         if data.get('settings'):
#             if data['settings'].get('editor'):
#                 print('exists')
#                 toEdit = data["settings"]["editor"]
#                 element_to_change = json.dumps(toEdit)
#                 toEdit = toEdit.replace("https://webdesignhq.nl/", "https://hqonline.nl/")
#                 toEdit = toEdit.replace("Webdesignhq", "HQ Online")
#             else:
#                 return recursive_search(data["elements"], count)
#         else:
#             return recursive_search(data["elements"], count)

#     return toEdit

def replace_footer(count=0, data=None, main_element="", element_to_change=""):
    # if r == None:
    r = requests.get("http://localhost/linkscript/wp-json/hq/v1/elementor/footer")
    if data is None:
        data = json.loads(r.json()["_elementor_data"][0])

    # test = getattr(data[0], 'editor')
    # print(dict(data))
    # return
    for element in data:
        if count == 0:
            main_element = json.dumps([element])
            count += 1
        if element.get('settings'):
            if element['settings'].get('editor'):
                print('exists')
                print(element["settings"]["editor"])
                toEdit = element["settings"]["editor"]
                element_to_change = json.dumps(toEdit)
                toEdit = toEdit.replace("https://webdesignhq.nl/", "https://hqonline.nl/")
                toEdit = toEdit.replace("Webdesignhq", "HQ Online")
                print(toEdit)
                # return element['settings']['editor']
                # return element
            else:
                return replace_footer(count,element['elements'],main_element,element_to_change)
        else:
            return replace_footer(count,element['elements'],main_element,element_to_change)
        
        # result = recursive_search(element)
        
        # if result != None:
            # break
    # print(previous_elements)
    # print(main_element)
    # element_to_change = element_to_change.replace("\\", "\\\\")
    # element = json.dumps(element).replace("\\", "\\\\")
    # print(main_element)
    # print(element_to_change)
    # print(toEdit)
    # print(result)
    main_element = main_element.replace(element_to_change, json.dumps(toEdit).replace("\\", "\\\\"))
    return main_element
    # return main_element
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
    # print(new_footer.replace("\\", "\\\\"))
    # print(new_footer)
    obj = {
        "_elementor_data": new_footer
    }
    # print(json.dumps(obj).replace("\\", "\\\\"))
    r = requests.post("http://localhost/linkscript/wp-json/hq/v1/elementor/footer", data=obj)
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