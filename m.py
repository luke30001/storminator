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
d = uc.Chrome(options=chrome_options)
d.set_page_load_timeout(30)
d.implicitly_wait(30)
def trio():
    try:
        d.execute_script('document.getElementsByClassName("text-17 md-text-18 md-font-bold leading-18")[0].click();')
        return(True)
    except:
        print("oo")
        return(False)
def test():
    try:
        d.get("https://app.stormgain.com/crypto-miner/")
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
d.get('https://app.stormgain.com/#modal_login')
d.execute_script('document.getElementById("email").value="'+os.environ['email']+'"')
d.execute_script('document.getElementById("password").value="'+os.environ['password']+'"')
d.execute_script('document.getElementsByClassName("btn btn-mint btn-login")[0].click()')
ii=0
while(d.current_url!="https://app.stormgain.com/"):
    print("waiting...")
while True:
    clicko()
    time.sleep(14400)
