import undetected_chromedriver.v2 as uc
import time
import os
def read(file):
    f=open(file,"r")
    aa=f.read()
    f.close()
    return aa
chrome_options = uc.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])
chrome_options.add_argument('--disable-blink-features=AutomationControlled')
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36")
chrome_options.add_argument("--remote-debugging-port=9222")
d = uc.Chrome(options=chrome_options)
d.set_page_load_timeout(30)
d.implicitly_wait(30)
def trio():
    try:
        d.execute_script('document.getElementsByClassName("text-17 md-text-18 md-font-bold leading-18")[0].click();')
        print("ii")
        return(True)
    except:
        print("oo")
        return(False)
def test():
    try:
        d.execute_script("window.open('https://app.stormgain.com/crypto-miner/')")
        d.execute_script("window.open('https://app.stormgain.com/crypto-miner/')")
        ii=0
        while(d.current_url!="https://app.stormgain.com/crypto-miner/"):
            ii=ii+1
            print("org")
            if(ii==60):
                raise Exception("Issue")
            time.sleep(1)
        d.save_screenshot("screenshot.png")
        return (True)
    except:
        time.sleep(60)
        return (False)
def clicko():
    while(not test()):
        print("testing...")
    time.sleep(10)
    tt=True
    while tt:
        try:
            d.execute_script('document.getElementsByTagName("button")[2]')
            d.execute_script('document.getElementsByTagName("button")[1].click()')
            tt=trio()
        except:
            tt=trio()
        d.save_screenshot("screenshot.png")
        time.sleep(2)
    d.save_screenshot("screenshot.png")
toto=True
while(toto):
    try:
        d.get('https://app.stormgain.com/#modal_login')
        d.execute_script('document.getElementById("email").value="'+os.environ['email']+'"')
        d.execute_script('document.getElementById("password").value="'+os.environ['password']+'"')
        d.execute_script('document.getElementsByClassName("btn btn-mint btn-login")[0].click()')
        ii=0
        toto=False
    except:
        toto=True
while(d.current_url!="https://app.stormgain.com/"):
    print(d.current_url)
while True:
    clicko()
    time.sleep(14400)
