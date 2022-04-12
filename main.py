import requests

url = "https://server2.webdesignhq.shockmedia.nl/~hqlinkchanger"
endpoint = "wp-json/hq/v1/elementor/footer"
def get_obj():
  """Gets the elementor footer object from the given website"""
  r = requests.get(f"{url}/{endpoint}")

  return r.json()


def replace_footer(obj):
  for i in range(len(obj)):
    obj[i] = obj[i].replace("webdesignhq.nl", "hq-online.nl")
    obj[i] = obj[i].replace("Webdesignhq", "HQ Online")

  return obj

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
      print(r.text)
  else:
    print(status)


def main():
  """
  Main execution point
  """
  new_footer = replace_footer(get_obj())
  if new_footer != None:
      send_data(new_footer)
      print('Header changed!')
  else:
      print('Header failed to change!')


if __name__ == "__main__":
    main()