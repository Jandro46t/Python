from selenium import webdriver 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By
import pyautogui
import pymsgbox
driver_path = "C:\\Selenium\\chromedriver"
browser = webdriver.Chrome(executable_path=driver_path)
browser.get("https://web.whatsapp.com")
kisi = pymsgbox.prompt(text="Göndericeniz kişi",title="Kişi",default="")
mesaj = pymsgbox.prompt(text="İletmek istediğiniz mesaj",title="Mesaj",default="")
mesaj_sayisi = pymsgbox.prompt(text="Kaç tane mesaj yollayacaksınız",title="Adet",default="")
onaylama = pymsgbox.confirm(text="QR code yi okuttuysanız ok butonuna basınız",title="Onay",buttons=["Ok"])
if onaylama == "Ok":
    kisi_yeri = browser.find_element_by_xpath('//span[@title = "{}"]'.format(kisi))
    kisi_yeri.click()
    mesajalani = browser.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[2]/div/div[2]")
    x = 1
    while x <= int(mesaj_sayisi):
        mesajalani.send_keys(mesaj+Keys.ENTER)
        x+=1
