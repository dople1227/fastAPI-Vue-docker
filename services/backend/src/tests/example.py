import webbrowser
import requests
# import json
# from urllib.request import urlopen

print("find old website")
site = input("Type a website URL:")
era = input("Type a year, month, day like 20150613:")
url = "http://archive.org/wayback/available?url=%s&timestamp=%s" % (site, era)
response = requests.get(url)
data = response.json()
# response = urlopen(url)
# contents = response.read()
# text = contents.decode("utf-8")
# data = json.loads(text)
try:
    old_site = data["archived_snapshots"]["closest"]["url"]
    print("Found this copy: ", old_site)
    print("It should appear in your browser now")
    webbrowser.open(old_site)
except:
    print("cant finding", site)