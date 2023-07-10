import requests
import argparse
import sys

logo = """ \033[1;34m 
                   _         _                       _       
         ___ _   _| |__   __| | ___  _ __ ___   __ _(_)_ __  
        / __| | | | '_ \ / _` |/ _ \| '_ ` _ \ / _` | | '_ \ 
        \__ \ |_| | |_) | (_| | (_) | | | | | | (_| | | | | |
        |___/\__,_|_.__/ \__,_|\___/|_| |_| |_|\__,_|_|_| |_|

        [+] Exm : 
            - python subdomain_enum.py example.com -f list-subdomain.txt
            \033[0;31m- Exiting the program .... [Cutrl +C]\033[0;39m
\033[1;39m"""

print(logo)

parser = argparse.ArgumentParser(description='Subdomain Enumeration Tool')
parser.add_argument('host', help='Target host')
parser.add_argument('-f', '--file', help='Path to list subdomain file', required=True)
args = parser.parse_args()

host = args.host

with open(args.file, 'r') as f:
    subdomains = f.read().splitlines()

for subdomain in subdomains:
    domain = f'http://{subdomain}.{host}'
    print(domain)
    try:
        response = requests.get(domain)
        if response.status_code == 200:
            print(f'\033[0;33m[+] Discovered subdomain: {domain}\033[0;39m')
    
    except requests.ConnectionError:
        pass
    
    except KeyboardInterrupt:
        print('\033[0;31m\nExiting the program...\033[0;39m')
        sys.exit()
