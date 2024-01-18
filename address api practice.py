address_api ={
"status": "success",
"country": "Canada",
"countryCode": "CA",
"region": "QC",
"regionName": "Quebec",
"city": "Montreal",
"zip": "H3C",
"lat": 45.4978,
"lon": -73.5485,
"timezone": "America/Toronto",
"isp": "Le Groupe Videotron Ltee",
"org": "Videotron Ltee",
"as": "AS5769 Videotron Telecom Ltee",
"query": "24.48.0.1"
}
ip = address_api['query']
country = address_api['country']
status = address_api['status']
country_code =address_api['countryCode']
region = address_api['region']
print(status)
# ip address 24.48.0.1 is located country is Canada.The conncetion's current status is success. And the country code is CA and its region is QC.
print(f'ip address {ip} is located country is {country}.The conncetion\'s current status is {status}. And the country code is {country_code} and its region is {region}.')
