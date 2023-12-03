import http.client
import json

conn = http.client.HTTPSConnection("api.collectapi.com")
city='istanbul'
headers = {
    'content-type': "application/json",
    'authorization': "apikey"
    }
conn.request("GET", f"/weather/getWeather?data.lang=tr&data.city={city}", headers=headers)
res = conn.getresponse()
data = res.read()
j_data=json.loads(data.decode('utf-8'))
sehir_adi=j_data['city']
date = j_data['result'][0]['date']
hava_durumu = j_data['result'][0]['description']
derece = j_data['result'][0]['degree']
minimum = j_data['result'][0]['min']
maksimum = j_data['result'][0]['max']
gece = j_data['result'][0]['night']
nem = j_data['result'][0]['humidity']
statu = j_data['result'][0]['status']
icon = j_data['result'][0]['icon']
json_muco={
    'sehir':sehir_adi,
    'gun':date,
    'derece':derece,
    'nem':nem,
    'gece':gece,
    'minimum':minimum,
    'maksimum':maksimum,
    'durum':statu,
    'hava durumu':hava_durumu,
    'icon':icon
}
with open('veri.json', 'w') as create_and_write_json:
    json.dump(json_muco, create_and_write_json)
    print('Veriler Json Dosyasına Kayıt Edildi..')
