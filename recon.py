import modules.config as config
import time
import subprocess


#wrapper for subdomain functions
def gather_subdomains(domain):

	#gather subdomains
	subdomains = subfinder(domain)
	return subdomains




#organically gather subdomains
def subfinder(domain):
	subdomains = subprocess.check_output('./subfinder/subfinder -silent -d %s' % (domain), shell=True)
	return subdomains.decode('utf-8').split('\n')[:-1]