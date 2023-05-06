import argparse
import requests
import socket
import whois
from bs4 import BeautifulSoup

def get_website_title(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        title = soup.find('title').get_text()
        print(f"Website Title: {title}")
    except requests.exceptions.RequestException:
        print("Failed to retrieve website title.")

def get_website_ip(url):
    try:
        ip_address = socket.gethostbyname(url)
        print(f"IP Address: {ip_address}")
    except socket.gaierror:
        print("Invalid domain or DNS lookup failed.")

def get_whois_info(url):
    try:
        domain = url.split("//")[-1].split("/")[0]
        w = whois.whois(domain)
        print("WHOIS Information:")
        print(f"Registrar: {w.registrar}")
        print(f"Creation Date: {w.creation_date}")
        print(f"Expiration Date: {w.expiration_date}")
        print(f"Name Servers: {w.name_servers}")
    except whois.parser.PywhoisError:
        print("Failed to fetch WHOIS information.")

# Help and usage information
help_message = "Website OSINT Tool - Perform OSINT on a website."
usage_message = "python osint_tool.py <url>"

# Set up the argument parser
parser = argparse.ArgumentParser(description=help_message)
parser.add_argument("url", help="URL of the website")
args = parser.parse_args()

# Run the website OSINT tool
get_website_title(args.url)
get_website_ip(args.url)
get_whois_info(args.url)