from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys

pp=0
k=0
"""
c# kullandığım zaman textboxa yazılan inputlar txt dosyasına kaydediliyo ve alttaki input kısmı şöyle gözüküyo:

dosya = open(r"C:\Users\ÖMER\Desktop\InstagramCommentScrapper\logs\1.txt","r")
logs = dosya.read().split()
dosya.close()

hesap = str(logs[0])
post_sayisi =int(logs[1])

"""
hesap = str(input("Account link\n-->"))
post_sayisi =int(input("How many ig post to scrape\n-->"))
browser = webdriver.Firefox()
browser.get(hesap)
sleep(7)

username=browser.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
password=browser.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')


username.send_keys('botiye__')
password.send_keys('xxtrax55')
sleep(1)
password.send_keys(Keys.RETURN)
sleep(7)
try:
    simdi_deil=browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button')
    simdi_deil.click()
    sleep(10)
except:
    pass

post=browser.find_elements_by_xpath('//div[@class="v1Nh3 kIKUG  _bz0w"]')

while pp<post_sayisi:
    if pp>0:
        s=len(post)
        newposts = browser.find_elements_by_xpath('//div[@class="v1Nh3 kIKUG  _bz0w"]')
        for x in newposts:
            if x not in post:
                post.append(x)
        k = len(post) - s
    for x in range(k,len(post)):
        if pp ==post_sayisi:
            browser.quit()
            break
        try:
            post[x].click()
            sleep(7)


            comment=browser.find_elements_by_class_name('C4VMK')
            for a in range(0,len(comment)):
                print(comment[a].text)
            clo = browser.find_element_by_css_selector(".BI4qX > button:nth-child(1)")
            clo.click()
            pp+=1

        except:
            pass
print("finised")


