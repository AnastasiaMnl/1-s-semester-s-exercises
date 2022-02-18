import json
import urllib.request 
from urllib.request import Request, urlopen

req = Request('https://drand.cloudflare.com/public/latest', headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20130401 Firefox/31.0'})
data = urlopen(req).read()
data = str(data)

splitted = []
splitted = data.split("'")
dict = json.loads(splitted[1])
value = dict.get("randomness")

separated = [value[i:i+2] for i in range(0, len(value), 2)]

#INTEGERS MODULO 80
modulo80 = []
int_list = []
for i in range (len(separated)):   
    separated[i]= "0x" + separated[i]
    int_list.append(int(separated[i],16))
    modulo80.append(int_list[i] % 80)

#KEEPING ELEMENTS ONCE
unique_list = []
for x in modulo80:
    if x not in unique_list:
            unique_list.append(x)
print ("unique_list : ",unique_list)

#DATA FROM OPAP
url = 'https://api.opap.gr/draws/v3.0/1100/last-result-and-active '
response = urllib.request.urlopen(url)
html = response.read()
data = html.decode()
kino = json.loads(data)
print("winningNumbers : ",kino['last']["winningNumbers"]['list'])

#COMMON NUMBERS
common_list = set(unique_list).intersection(kino['last']["winningNumbers"]['list'])
print ("COMMON NUMBERS IN unique_list AND winningNumbers : ",common_list)
