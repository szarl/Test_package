##### Authpr: Karol Rutkowski
##### Data: 25.11.2021

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

PATH = Service(ChromeDriverManager().install())


class SourcefulTest:
    driver = webdriver.Chrome(service=PATH)

    userSender = {
        'fullName': "Mobiesense Monika Mazurek",
        'streetName': "Olszewskiego",
        'streetNumberBlock': "6",
        'streetNumberFlat': "313",
        'postalCode': "25-663",
        'cityName': "Kielce",
        'numberNIP': "6572441180",
        'phoneNumber': "664540929",
        'directionalNumber': "+48",
        'email': "monika@sourceful.nl"
    }
    userReceiver = {
        'fullName': "Natalia Ivanova",
        'streetName': "Lenina St",
        'streetNumberBlock': "1",
        'streetNumberFlat': "1",
        'postalCode': "",
        'cityName': "Chornobai",
        'phoneNumber': "505032236",
        'directionalNumber': "+48",
        'email': "natalia@ivanova.pl"
    }
    chocolateInfo = {
        'name': "Czekoladki",
        'amount': "2",
        'weight': "10",
        'cost': "20"
    }

    cupInfo = {
        'name': "Kubek",
        'amount': "1",
        'weight': "2",
        'cost': "5"
    }

    def assertEqual(self, value, valeuHtml):
        if value == valeuHtml:
            print("Test Ok")
            # return true
        else:
            print("Test nie Ok")
            # return false

    # i've got some problems with selenium, dont know why i am not able to use functions like find_element_by ... proparly so i used find_element
    # there were also problem with the version, becouse in the past i used to work with web driver version number 86 and know it is on 96 and my coputer had
    # some problems with that i guess

    if __name__ == '__main__':
        try:
            driver.get("https://paczkadoukrainy.pl/")
            driver.maximize_window()
            driver.find_element(By.CSS_SELECTOR,
                                'div:nth-child(3) div div div div div:nth-child(4)  div:nth-child(2) div input').send_keys(
                "10")
            driver.find_element(By.CSS_SELECTOR, 'div:nth-child(3) div div div div button').click()
            # there is no such a element as 'w punkcie ruchu ' on the website so i decided to choose inpost
            time.sleep(1)
            driver.find_element(By.CSS_SELECTOR, 'button:nth-child(3)').click()
            time.sleep(1)
            driver.find_element(By.XPATH,
                                '//*[@id="collapseTwoAndHalf"]/div/div/div/fieldset/div/div[2]/div/label').click()

            # way of searching == // but couldnt have found the correct adress as in exercise, so it wont me allow to go next step
            # option_pane = []
            # for place in driver.find_element(By.CSS_SELECTOR,'section:nth-child(2) div:nth-child(2) div div div div:nth-child(2) div div div').find_element_by_tag_name("option"):
            #     option_pane.append(place)
            #     if place.text.rfind("19901"):
            #     place.click()

            time.sleep(4)
            # bettter to use WebDriverWait expiressions but still something doesnt work properly and I have to figure it out

            driver.find_element(By.CSS_SELECTOR, 'section:nth-child(2) div:nth-child(2) div div div div input').click()
            driver.find_element(By.CSS_SELECTOR,
                                'section:nth-child(2) div:nth-child(2) div div div div input').send_keys("19901",
                                                                                                         Keys.TAB)

            # SendingUser data
            driver.find_element(By.CSS_SELECTOR, 'fieldset div div:nth-child(4) div div div div input').send_keys(
                userSender.get('fullName'))
            driver.find_element(By.CSS_SELECTOR,
                                'fieldset div div:nth-child(4) div div div div:nth-child(2) input').send_keys(
                userSender.get('postalCode'))
            driver.find_element(By.ID, 'senderCity').send_keys(userSender.get('cityName'))
            driver.find_element(By.CSS_SELECTOR,
                                'fieldset div div:nth-child(4) div div div div:nth-child(4) input').send_keys(
                userSender.get('streetName'))
            driver.find_element(By.CSS_SELECTOR,
                                'fieldset div div:nth-child(4) div div div div:nth-child(5) input').send_keys(
                userSender.get('streeNumberBlock'))
            driver.find_element(By.CSS_SELECTOR,
                                'fieldset div div:nth-child(4) div div div div:nth-child(6) input').send_keys(
                userSender.get('streetNumberFlat'))
            driver.find_element(By.CSS_SELECTOR,
                                'fieldset div div:nth-child(4) div div div div:nth-child(7) input').send_keys(
                userSender.get('phoneNumber'))
            driver.find_element(By.CSS_SELECTOR,
                                'fieldset div div:nth-child(4) div div div div:nth-child(8) input').send_keys(
                userSender.get('email'))
            driver.find_element(By.CSS_SELECTOR,
                                'fieldset div div:nth-child(4) div div div:nth-child(2) div:nth-child(3) input').send_keys(
                userReceiver.get('fullName'))
            driver.find_element(By.CSS_SELECTOR,
                                'fieldset div div:nth-child(4) div div div:nth-child(2) div:nth-child(8) input').send_keys(
                userReceiver.get('phoneNumber'))
            driver.find_element(By.CSS_SELECTOR,
                                'fieldset div div:nth-child(4) div div div:nth-child(2) div:nth-child(8) span').clear()
            driver.find_element(By.CSS_SELECTOR,
                                'fieldset div div:nth-child(4) div div div:nth-child(2) div:nth-child(8) span').send_keys(
                userReceiver.get('directionNumber'))
            driver.find_element(By.CSS_SELECTOR,
                                'fieldset div div:nth-child(4) div div div:nth-child(2) div:nth-child(9) input').send_keys(
                userReceiver.get('email'))

            # package1 info
            driver.find_element(By.NAME, '#parcelItemDescription').send_keys(chocolateInfo.get('name'))
            driver.find_element(By.ID, 'parcelItemQuantity').send_keys(chocolateInfo.get('amount'))
            driver.find_element(By.ID, 'parcelItemWeight').send_keys(chocolateInfo.get('weight'))
            driver.find_element(By.ID, 'parcelItemValueClientCurrency').send_keys(chocolateInfo.get('cost'))

            driver.find_element(By.CSS_SELECTOR, 'div div:nth-child(4) div button').click()
            # package2 info
            driver.find_element(By.CSS_SELECTOR,
                                'fieldset div div:nth-child(5) div:nth-child(2) div div:nth-child(2) div:nth-child(2) input').send_keys(
                cupInfo.get('name'))
            driver.find_element(By.CSS_SELECTOR,
                                'fieldset div div:nth-child(5) div:nth-child(2) div div:nth-child(2) div:nth-child(3) input').send_keys(
                cupInfo.get('amount'))
            driver.find_element(By.CSS_SELECTOR,
                                'fieldset div div:nth-child(5) div:nth-child(2) div div:nth-child(2) div:nth-child(4) input').send_keys(
                cupInfo.get('weight'))
            driver.find_element(By.CSS_SELECTOR,
                                'fieldset div div:nth-child(5) div:nth-child(2) div div:nth-child(2) div:nth-child(5) input').send_keys(
                cupInfo.get('cost'))
            driver.find_element(By.CSS_SELECTOR,
                                'div div.row.mt-4 div.col-lg-5 div div.col-lg-6.duty-item__cross-icon-container.ml-lg-0.pl-lg-0 div.input-group input').clear()
            driver.find_element(By.CSS_SELECTOR,
                                'div div.row.mt-4 div.col-lg-5 div div.col-lg-6.duty-item__cross-icon-container.ml-lg-0.pl-lg-0 div.input-group input').send_keys(
                '12')
            # clicked 4 squares instead of 3
            driver.find_element(By.CSS_SELECTOR, '#anchorOrderForm fieldset div:nth-child(2) div div label').click()
            driver.find_element(By.CSS_SELECTOR, '#anchorOrderForm fieldset div:nth-child(3) div div label').click()
            driver.find_element(By.CSS_SELECTOR, '#anchorOrderForm fieldset div:nth-child(4) div div label').click()
            driver.find_element(By.CSS_SELECTOR, '#anchorOrderForm fieldset div:nth-child(5) div div label').click()

            driver.find_element(By.XPATH, '//*[@id="btn_next_step"]').click()

            # testing values on the web with the values given at the begining

            assertEqual(userSender.get('name'), driver.find_element(By.CSS_SELECTOR,
                                                                    'div:nth-child(3) div:nth-child(1) div div p:nth-child(1) span:nth-child(2)').text)
            assertEqual(userSender.get('postalCode'), driver.find_element(By.CSS_SELECTOR,
                                                                          'div:nth-child(3) div:nth-child(1) div div p:nth-child(2) span:nth-child(2)').text)
            assertEqual(userSender.get('cityName'), driver.find_element(By.CSS_SELECTOR,
                                                                        'div:nth-child(3) div:nth-child(1) div div p:nth-child(3) span:nth-child(2)').text)
            assertEqual(userSender.get('streetName'), driver.find_element(By.CSS_SELECTOR,
                                                                          'div:nth-child(3) div:nth-child(1) div div p:nth-child(4) span:nth-child(2)').text)
            assertEqual(userSender.get('streetNumberFlat'), driver.find_element(By.CSS_SELECTOR,
                                                                                'div:nth-child(3) div:nth-child(1) div div p:nth-child(5) span:nth-child(2)').text)
            assertEqual(userSender.get('streetNumberBlock'), driver.find_element(By.CSS_SELECTOR,
                                                                                 'div:nth-child(3) div:nth-child(1) div div p:nth-child(6) span:nth-child(2)').text)
            assertEqual(userSender.get('phoneNumber'), driver.find_element(By.CSS_SELECTOR,
                                                                           'div:nth-child(3) div:nth-child(1) div div p:nth-child(7) span:nth-child(2)').text)
            assertEqual(userSender.get('email'), driver.find_element(By.CSS_SELECTOR,
                                                                     'div:nth-child(3) div:nth-child(1) div div p:nth-child(8) span:nth-child(2)').text)
        finally:
            raise Exception('Something went wrong')
