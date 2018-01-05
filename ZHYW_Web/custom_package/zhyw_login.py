class Login():

    def yw_login(self, driver, name, pword):
        driver.get("http://192.168.0.208:8200/ioms/")
        driver.find_element_by_id("userName").clear()
        driver.find_element_by_id("userName").send_keys(name)
        driver.find_element_by_id("passWord").clear()
        driver.find_element_by_id("passWord").send_keys(pword)
        driver.find_element_by_id("login_button").click()

    def is_login_sucess(self, driver):
        try:
            text = driver.find_element_by_id("userName").text
            print(text)
            return True
        except:
            return False

