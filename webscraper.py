import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()

url = "https://danmemo.boom-app.wiki/entry/chara-list"

driver.get(url)
driver.maximize_window()

index = 0

def getAllCharacterLinks():
    times = range(1, 701, 1)
    characterlinks = []

    for time in times:
        link = 'https://danmemo.boom-app.wiki/entry/chara-' + str(time)

        characterlinks.append(link)

    return characterlinks

def getAllImageLinks():
    characterlinks = getAllCharacterLinks()
    imgurls = []
    largerimgurls = []

    for characterlink in characterlinks:
        driver.get(characterlink)
        try:
            imageurl = driver.find_element(By.XPATH, value='//*[@id="fixed-nav-contents"]/div[1]/div[2]/div[3]/div/div/img')
            imgurl = imageurl.get_attribute('src')
            sleep(1)
        except:
            continue

        imgurls.append(imgurl)

    for imgurl in imgurls:
        newurl = imgurl.replace('w=600', 'w=1500')
        largerimgurls.append(newurl)

    return largerimgurls

def downloadimages():
    for index, imgurl in enumerate(getAllImageLinks()):
        response = requests.get(imgurl)

        file = open('D:/Danmachi/character_' + str(index + 1) + '.jpg', 'wb')
        file.write(response.content)



downloadimages()

driver.close()