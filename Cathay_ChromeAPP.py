import time
import os
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class Cathay_APP():
    def __init__(self):
        self.driverExist = False  # check driver exist or not
        self.ChromeOption = webdriver.ChromeOptions()

    def driver(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=self.ChromeOption)
        self.driverExist = True

    def add_experimental_option(self, name, value):
        self.ChromeOption.add_experimental_option(name, value)

    def wait(self, by, param, seconds=5):
        WebDriverWait(self.driver, seconds).until(EC.presence_of_element_located((by, param)))

    def findElement(self, by, param):
        return self.driver.find_element(by, param) # by -> id, class name, xpath, name, ....

    def wait_findElement(self,by, param):
        self.wait(by, param)
        return self.findElement(by, param)

    def findElements(self, by, param):
        return self.driver.find_elements(by, param)

    def wait_findElements(self, by, param):
        self.wait(by, param)
        return self.driver.find_elements(by, param)

    def close(self):
        self.driver.close()

    def quit(self):
        self.driver.quit()
        self.driverExist = False

    def toPage(self, url):
        self.driver.get(url)

    def getScreenShot(self, FilePath):
        self.driver.get_screenshot_as_file(FilePath)


#可分開到其他檔案 ex: driver.py, TestCase.py...
    def firstTestCapture(self):
        """後續可判斷是哪段出錯/對的要留那些資訊 並加入Result"""
        try:
            self.wait('class name', 'cubre-o-indexKv__title')
            self.getScreenShot('First.jpg')
            # cv2.imread(file_name) 可以新增其他驗證機制
            return 'First Test Pass'
        except:
            return 'First TestCase Fail'

    def secondTestCountItems(self):
        """後續可判斷是哪段出錯/對的要留那些資訊 並加入Result"""
        try:
            self.wait_findElement('class name', 'cubre-o-header__burger').click()
            self.findCorrectItem('class name', 'cubre-o-channel__item', '') #個人金融
            self.findCorrectItem('class name', 'cubre-o-menu__item', '產品介紹', True)
            self.findCorrectItem('class name', 'cubre-o-menuLinkList__item', '信用卡', True)
            CreditList = self.wait_findElement('class name', 'cubre-o-menuLinkList__item.is-L2open')
            print(self.secondTest_CountTotalItems(CreditList))
            self.getScreenShot('Second.jpg')
            return 'Second Test Pass'
        except:
            return 'First TestCase Fail'

    def secondTest_CountTotalItems(self, elements):
        CreditList = elements.text.split('\n')
        return len(CreditList)-2

    def findCorrectItem(self, by, param, target, click=False):
        menuList = self.wait_findElements(by, param)
        for x in menuList:
            if x.text == target:
                if click == True:
                    x.click()
        return menuList

    def thirdTest_CountCapture(self):
        """後續可判斷是哪段出錯/對的要留那些資訊 並加入Result"""
        try:
            self.toPage('https://www.cathaybk.com.tw/cathaybk/personal/product/credit-card/cards/')
            print(self.wait_findElements('class name', 'cubre-o-anchorBlock.cubre-o-block.-iconTitle'))
            stopcard = self.wait_findElements('class name', 'cubre-o-anchorBlock.cubre-o-block.-iconTitle')
            element_quantity = self.countStopCard(stopcard)
            self.captureStopCard()
            picture_quantity = os.listdir('StopCard') #folder picture
            if element_quantity == len(picture_quantity):
                return 'Third Test Pass'
            else:
                return 'Third Test Fail - Picture Quantity Not Same'
        except:
            return 'Third TestCase Fail'
    def countStopCard(self, stopcard):
        for stopcard in stopcard:
            if '停發卡' in stopcard.text:
                stopcardDiv = stopcard.find_element('class name', 'swiper-wrapper').find_elements('tag name', 'div')
                stopcard_total = 0
                for Div in stopcardDiv:
                    if '已停止申辦' in Div.text:
                        stopcard_total += 1
                return stopcard_total-1 #total stop cards

    def captureStopCard(self):
        for x in range(1,1000):
            try:
                self.findElement('xpath', '/html/body/div[1]/main/article/section[6]/div/div[2]/div/div[2]/span[%d]'%x).click()
                time.sleep(1) #or get JS == 335 then ScreenShot
                self.getScreenShot('StopCard/StopCard%d.jpg'%x)
            except:
                print('No More Stop Card')
                break

if __name__ == '__main__':
    #建立物件/設定選項
    Cathay_ChromeAPP = Cathay_APP()
    mobile_emulation = {'deviceName': 'iPhone 6'}
    Cathay_ChromeAPP.add_experimental_option("mobileEmulation", mobile_emulation)
    Cathay_ChromeAPP.driver()
    Cathay_ChromeAPP.toPage('https://www.cathaybk.com.tw/cathaybk/')

    TestResut = [] #也可加入self直接呼叫

    #測試開始&存入結果
    """也可寫個function 知道目前做到哪個function 錯在哪個function"""
    TestResut.append(Cathay_ChromeAPP.firstTestCapture())
    TestResut.append(Cathay_ChromeAPP.secondTestCountItems())
    TestResut.append(Cathay_ChromeAPP.thirdTest_CountCapture())

    print('Test-Result:', TestResut)

