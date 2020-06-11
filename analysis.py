import json
import requests
from termcolor import colored
from urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

import modules.config as config



#load fingerprint data into memory
with open("config/fingerprints.json", "r") as file:
	fingerprints = json.load(file)





#is pointing to a hijackable service?
def check_if_hijackable(page_content):

	#check if takeover fingerprint exists in page
	for engine in fingerprints['subdomain_takeover_data']:
		if fingerprints['subdomain_takeover_data'][engine] in page_content:
			return engine



#prepare whitespace for console
def whitespace(url):
	#make output all purdy
	whitespace = ""
	whitespace_length = 45 - len(url)
	
	for i in range(whitespace_length):
		whitespace += " "

	return whitespace





#discern if service is vulnerable
def is_yoinkable(url):

	try:
		r = requests.get(url, verify=False, timeout=4)

		#check if subdomain takeover fingerprint exists in page
		subdomain_takeover = check_if_hijackable(r.text)


		#print to console
		if subdomain_takeover:
			print(colored(url, 'cyan'), colored("%s%s",'white') % (whitespace(url), subdomain_takeover))


		if config.verbose:
			print(colored(url, 'green'))



	except Exception as e:
		return False
