# Rupert
Wrapper for DNS recon tools to automatically fingerprint subdomain takeovers

![Screenshot of Rupert CLI](https://i.imgur.com/y7FQIG2.png)


# Install
`pip3 install -r requirements.txt`

`chmod +x subfinder/subfinder`

`tar -xvf subfinder/subfinder_2.3.8_linux_amd64.tar.gz -C subfinder`
https://github.com/projectdiscovery/subfinder/releases/download/v2.3.8/subfinder_2.3.8_checksums.txt)


# Usage
> python3 rupert.py [domain] [flags]


# Syntax
-v, --verbose
> verbosity mode

-f [FILE], --file [FILE]
> Read list of domains from file into Rupert

-s [n], --skip [n]
> Number of lines to skip (if any) when reading from file

-c [n], --cap [n]
> Set a cap to how many subdomains Rupert will scan. If too many are enumerated, abort.


# Resources
* https://github.com/projectdiscovery/subfinder
* https://github.com/EdOverflow/can-i-take-over-xyz
