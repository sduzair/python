from pprint import pprint 
import requests


def getUsers():
  res = requests.get("https://dummyjson.com/users")
  if res.ok:
    return res.json()
  else:
    return "Request failed!"


pprint(getUsers())