#!/usr/bin/python3

import sys
import json
import argparse
from termcolor import colored
from multiprocessing import Pool


#import rupert modules
import modules.config as config
import modules.analysis as analysis
import modules.recon as recon


domains = []
subdomains = []
cap = False

#parse command line arguments
parser = argparse.ArgumentParser()
parser.add_argument('-v', '--verbose', default=False, action='store_true')
parser.add_argument('-f', '--file', default=False)
parser.add_argument('-sf', '--subfile', default=False)
parser.add_argument('-s', '--skip', default=False)
parser.add_argument('-c', '--cap', default=False)
parser.add_argument('-reporting', '--reporting', default=False)
args, domains = parser.parse_known_args()

if args.verbose:
	config.verbose = True
if args.file:
	config.from_file = args.file
if args.subfile:
	config.subfile = args.subfile
if args.skip:
	config.skip = args.skip
if args.cap:
	cap = args.cap
if args.reporting:
	config.reporting = json.loads(str(args.reporting).lower())






#create HTTP links to try from list of subdomains
def generate_http_services(unchecked_subdomains):
	http_services = []


    
	#gather list of http services to check
	for subdomain in unchecked_subdomains:

		#probe default ports for HTTP services
		http_services.append("http://" + subdomain)
		http_services.append("https://" + subdomain)

	return http_services




def check_services_for_subdomain_takeovers(http_services):
	#open resource pool to check services
	p = Pool(processes=20)
	result = p.map(analysis.is_yoinkable, http_services)
	p.close()




def turn_file_into_list(file):
	lines = []

	for line in open(config.subfile, "r").readlines():
		lines.append(line.rstrip('\n').lower())

	return lines




#check subdomains directly from file
if config.subfile:
	subdomains = turn_file_into_list(config.subfile)
	http_services = generate_http_services(subdomains)
	check_services_for_subdomain_takeovers(http_services)


#read domains from file
if config.from_file:
	domains = turn_file_into_list(config.from_file)



loop = 0

#iterate through the list of domains
for domain in domains:

	#used to skip domains in a list
	if config.skip:
		if loop <= int(config.skip):
			loop +=1
			continue



	#gather subdomains
	unchecked_subdomains = recon.gather_subdomains(domain)


	print(colored('Total: %s domains found', 'white') % str(len(unchecked_subdomains)))
	print('')


	http_services = generate_http_services(unchecked_subdomains)


	#if services exceeds reasonable cap abort process
	if cap:
		if len(http_services) > int(cap):
			print('Aborted... exceeded cap...')
			continue


	check_services_for_subdomain_takeovers(http_services)
	
