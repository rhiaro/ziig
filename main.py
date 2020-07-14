import requests
from bs4 import BeautifulSoup


def get_spec(url):
    r = requests.get(url)
    if r.ok:
        return r.content
    else:
        return False

def parse_spec(url):
    spec = get_spec(url)
    if spec:
        doc = BeautifulSoup(spec, features="lxml")
        ziigs = doc.find_all("em", {"class":"rfc2119"})
        for ziig in ziigs:
            section = ziig.find_parent("section")
            print(section.get("class"))
    else:
        print("No spec at {}".format(url))

url = "https://www.w3.org/TR/did-core"
parse_spec(url)