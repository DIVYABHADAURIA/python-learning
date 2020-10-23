from func import format_msg
import requests
import sys

def send(name,website=None,verbose=False):
	if website != None :
	  msg = format_msg(my_name=name,my_website=website)
	else :
		msg = format_msg(name)
	if verbose :
		print(name,website)

	r = requests.get("http://httpbin.org/json")
	if r.status_code == 200:
		return r.json()
	else :
		return "THERE WAS AN ERROR"

if __name__ == "__main__":
	print(sys.argv)
	name= "Unknown"
	if len(sys.argv) > 1:
		name = sys.argv[1]
	response = send("DIVYA",verbose=True)
	print(response)