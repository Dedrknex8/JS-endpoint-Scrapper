import re
import requests
from bs4 import  BeautifulSoup
from urllib.parse import urljoin

def extract_endpoints(js_content):
    pattern = r'\/[a-zA-Z0-9\/\-_\.]*[a-zA-Z0-9\/]'
    return re.findall(pattern,js_content)


def scrap_js_endpoints(url):
    if not url.startswith(('http://', 'https://')):
        url = "https://" + url

    try:
        response = requests.get(url,timeout=5)
        if response.status_code != 200:
                print(f"Unable to access url {url}")
                return
            
        soup =  BeautifulSoup(response.text,'html.parser')
        scripts = soup.find_all('script')

        js_links = []

        #find src in every scritp
        for script in scripts:
            src = script.get('src')
            if src:
                full_url = urljoin(url,src)
                js_links.append(full_url)

        if not js_links:
            print(" No js files found")
            return
        
        found_endoints = set()

        print(f"Found {len(js_links)} Js files. Extracting endpoints ...")

        for js_link in js_links:
            try:
                js_res = requests.get(js_link, timeout=1)
                endpoints = extract_endpoints(js_res.text)
                for endpoint in endpoints :
                    found_endoints.add(endpoint)
            except Exception as e:
                print(f" Error fetching {js_links} : {e}")
                    
        if not found_endoints:
            print(f'No endpoint in js files')
            return 
                    
               
        print(f'\n Found {len(found_endoints)} unique endpoints')

        for endpoint in found_endoints:
            full_endpoint = urljoin(url,endpoint)

            try:
                            check = requests.get(full_endpoint,timeout=5)
                            if check.status_code == 200 : 
                                print(f" {full_endpoint} [ALIVE]")
                            else:
                                print(f"{full_endpoint} [Status : {check.status_code}]")
            except Exception as e :
                            print(f"Failed to access {full_endpoint}: {e}")

    except Exception as e : 
            print(f" Error {e}")


if __name__ == "__main__":
    target = input("Enter the website URL: ")
    scrap_js_endpoints(target)
