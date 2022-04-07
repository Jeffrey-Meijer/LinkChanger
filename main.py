import requests
import json

url = "https://server2.webdesignhq.shockmedia.nl/~hqlinkchanger"
endpoint = "wp-json/hq/v1/elementor/footer"
def get_obj():
  """Gets the elementor footer object from the given website"""
  # r = requests.get("http://localhost/linkscript/wp-json/hq/v1/elementor/footer")
  r = requests.get(f"{url}/{endpoint}")
  # return r.json()['_elementor_data'][0])

  return r.json()
  # return json.loads(r.json())


def replace_footer(obj):
  for i in range(len(obj)):
    obj[i] = obj[i].replace("webdesignhq.nl", "hq-online.nl")
    obj[i] = obj[i].replace("Webdesignhq", "HQ Online")

  return obj
  # else:
    # print('going None')
    # return None
    # print(elements)
      # obj = obj['elements']
      # return get_footer(obj)
    # return get_footer(obj['elements'])
  # else:
    # if obj['settings']:
      # if obj['settings'].get('editor'):
        # return obj['settings']['editor']

# TO DO, Werkt niet als er een inner section in zit waar de footer niet in zit. Ook werkt het niet als hij niet in de eerste sectie zit
# def replace_footer(obj, main_element=None, count=0, return_point=None):
#   """
#   Tries to find the footer element in the given object and replace it with the new website url and name
#   """
#   # print(obj)
#   if count == 0:
#       main_element = obj
#       count += 1
#   for element in obj:
#       # for child_element in element:
#         # print(child_element)
#       return get_footer(element)
#       element_copy = element
#       # print(element['isInner'])
#       # print(element_copy)
#       # print(element)
#       if element_copy['elType'] in ['section', 'column']:
#           element_copy = element_copy['elements']
#           return replace_footer(element_copy,main_element,count)
#       # elif element['elType'] in ['section', 'column'] and element['isInner'] == True:
#       #   return_point = element
#       #   print(return_point)
#       #   element = element['elements']
#       #   return replace_footer(element,main_element,count,return_point)
#       else:
#           if element_copy['settings']:
#               if element_copy['settings'].get('editor'):
#                   # print(element['settings']['editor'])
#                   original = json.dumps(element['settings']['editor'])
#                   toEdit = original
#                   toEdit = toEdit.replace("https://webdesignhq.nl/", "https://hq-online.nl/")
#                   toEdit = toEdit.replace("Webdesignhq", "HQ Online")
                  
#                   main_element = json.dumps(main_element)
#                   main_element = main_element.replace(original, toEdit)
#                   main_element = main_element.replace("\\", "\\\\")
#                   return main_element
      
#       # if return_point != None:
#       #   # print('test')
#       #   temp = return_point
#       #   return_point = None
#         # return replace_footer(temp, main_element, count, return_point)
#       # return replace_footer(element, None, count, None)
#       # return None

def send_data(new_footer):
  """
  Sends the new footer to the website. This is done using the exposed rest api.
  """
  obj = {
      "footer": new_footer
  }
  r = requests.post(f"{url}/{endpoint}", data=obj)
  status = r.status_code
  if status == 200:
    # pass
      print(r.text)
  else:
    # pass
    print(status)


def main():
  """
  Main execution point
  """
  # print(get_obj())
  new_footer = replace_footer(get_obj())
  # print(new_footer)
  if new_footer != None:
      send_data(new_footer)
      print('Header changed!')
  else:
      print('Header failed to change!')


if __name__ == "__main__":
    main()