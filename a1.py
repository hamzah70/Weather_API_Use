"""
NAME : MOHAMMAD HAMZAH AKHTAR
ROLL NO. : 2018051
SECTION : A
GROUP : 3

"""

from urllib.request import *
from datetime import *
# function to get weather response
def weather_response(location, API_key):
	# write your code
	url = urlopen('http://api.openweathermap.org/data/2.5/forecast?q=%s&APPID=%s' %(location,API_key))
	html = str(url.read())
	return html

# function to check for valid response 
def has_error(location,json):
	# write your code 
	if (json.find(location) != -1):
		return False
	else:
		return True	
	


# function to get attributes on nth day
def get_temperature(json, n, t):

	# write your code 
	date_index = json.index(str(date.today() + timedelta(n)))
	time_index = json.index(str(t),date_index)
	temp_index = json.rfind('"temp"',0,time_index)
	temp = json[temp_index+7:temp_index+12]
	return float(temp)

def get_humidity(json, n, t):
	# write your code 
	date_index = json.index(str(date.today()+timedelta(n)))
	time_index = json.index(str(t),date_index)
	humidity_index = json.rfind('"humidity"',0,time_index)
	humidity = json[humidity_index+11:humidity_index+13]
	return float(humidity)

def get_pressure(json, n, t):
	# write your code 
	date_index = json.index(str(date.today()+timedelta(n)))
	time_index = json.index(str(t),date_index)
	pressure_index = json.rfind('"pressure"',0,time_index)
	pressure = json[pressure_index+11:pressure_index+13]
	return float(pressure) 

def get_wind(json, n, t):
	# write your code 
	date_index = json.index(str(date.today()+timedelta(n)))
	time_index = json.index(str(t),date_index)
	wind_index = json.rfind('"speed"',0,time_index)
	wind = json[wind_index+8:wind_index+12]
	return float(wind)

def get_sealevel(json, n, t):
	# write your code
	date_index = json.index(str(date.today()+timedelta(n)))
	time_index = json.index(str(t),date_index)
	sealevel_index = json.rfind('"sea_level"',0,time_index)
	sealevel = json[sealevel_index+12:sealevel_index+18]
	return float(sealevel)

if __name__ == '__main__':
	x = weather_response('Delhi', '65ff78135854500cd7853fe3860b5569')
	print(get_temperature(x,0,'15:00:00'))



