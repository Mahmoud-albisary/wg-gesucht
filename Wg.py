import requests
from bs4 import BeautifulSoup
import winsound 
import time
  
c= 0 

while True:
    try:
        URL = "https://www.wg-gesucht.de/wg-zimmer-in-Munchen.90.0.1.0.html?csrf_token=12ce0965385777b54a76cc581aef910d8f2d1ff2&offer_filter=1&city_id=90&noDeact=1&dFr=1656626400&categories%5B%5D=0&rent_types%5B%5D=2&rMax=550"
        r = requests.get(URL)
        
        soup = BeautifulSoup(r.content, 'html5lib') # If this line causes an error, run 'pip install html5lib' or install html5lib\
        table = soup.find('div',attrs = {'id':'master_wrapper'})
        table = table.find('div',attrs = {'id':'site_wrapper'})
        table = table.find('div',attrs = {'id':'main_content'})
        table = table.find('div',attrs = {'id':'main_column'})
        count = table.findAll('div',attrs = {'class':'wgg_card offer_list_item'})[0].get('id')
        with open('IdWg.txt') as f:
            lines = f.readlines()
        f.close()
        if lines[0] != count:
                # frequency is set to 500Hz
            freq = 500 
            print(lines[0])
            # duration is set to 100 milliseconds             
            dur = 10000
                        
            winsound.Beep(freq, dur)
            with open('IdWg.txt', 'w') as f:
                f.write(count)
            f.close()
        if c >= 5:
            print("careful there is a problem")
        time.sleep(50)
    except:
        c =c + 1
        if c >= 5:
            print("careful there is a problem")