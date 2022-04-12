import json
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
  # NIET VERLIEZEN
  f = open('config.json')
  data = json.load(f)

  jwt_token = data["jwt_token"]
  encoded_jwt_token = data["encoded_jwt_token"]

  obj = {
      "footer": new_footer,
      "jwt_token": jwt_token,
      "encoded_jwt_token": encoded_jwt_token
  }
  r = requests.post(f"{url}/{endpoint}", data=obj)
  status = r.status_code
  if status == 200:
      if r.text:
        message = json.loads(json.loads(r.text))
        if message.get("message"):
          print(message["message"])
          return False
      
      return True
  else:
    print(status)


def main():
  """
  Main execution point
  """
  new_footer = replace_footer(get_obj())
  if new_footer != None:
      req = send_data(new_footer)
      if req:
        print('Header changed!')
      else:
        print("Header failed to change!")
  else:
      print('Header failed to change!')


if __name__ == "__main__":
    main()