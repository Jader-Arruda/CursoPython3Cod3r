import requests
from bs4 import BeautifulSoup
import json
import re 

url = "https://tableau.ons.org.br/t/ONS_Publico/views/DemandaMxima/HistricoDemandaMxima"

r = requests.get(
    url,
    params = {
        ":embed":"y",
        ":showAppBanner":"false",
        ":showShareOptions":"true",
        ":display_count":"no",
        "showVizHome": "no"     
    }
)

soup = BeautifulSoup(r.text, "html.parser")

tableauData = json.loads(soup.find("textarea",{"id": "tsConfigContainer"}).text)

dataUrl = f'https://tableau.ons.org.br{tableauData["vizql_root"]}/bootstrapSession/sessions/{tableauData["sessionid"]}'

r = requests.post(dataUrl, data= {
    "sheet_id": tableauData["sheetId"],
})

dataReg = re.search('\d+;({.*})\d+;({.*})', r.text, re.MULTILINE)
info = json.loads(dataReg.group(1))*
data = json.loads(dataReg.group(2))

print(data["secondaryInfo"]["presModelMap"]["dataDictionary"]["presModelHolder"]["genDataDictionaryPresModel"]["dataSegments"]["0"]["dataColumns"])