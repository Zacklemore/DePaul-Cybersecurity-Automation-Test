import requests 
import re 


def scrape(homepage='http://10.14.6.10/index.php'): 
    #Quick assignment that will scrape the homepage of a site for a flag.
    #912ec803b2ce49e4a541068d4q95ab57p
    #673cc3378d0f1fbd3747d14d6b782ddb - correct length should return this guy

    url = homepage
    response = requests.get(url)
 
    print(response.text)
    regex =  r'CNS\{[a-f0-9]{32}\}'
    ans = re.findall(regex, response.text)
    print(ans[0])
    #CNS{673cc3378d0f1fbd3747d14d6b782ddb}

scrape(input("Enter ip or web adress: "))
