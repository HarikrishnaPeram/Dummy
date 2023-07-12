from selenium.webdriver.common.by import By


class BasicInfo:

    def __init__(self, driver):
        self.driver = driver

    firstname = (By.Xpath, "//input[@name='firstname']")
    surname = (By.XPATH, "//input[@id='u_0_d_my']")
    mobileoremail = (By.XPATH, "//input[@id='u_0_g_MR']")
    newpassword = (By.XPATH, "//input[@id='password_step_input']")
    day = (By.XPATH, "#day")
    month = (By.XPATH, "#month")
    year = (By.XPATH, "#year")
    gender = (By.CSS_SELECTOR, "#u_0_5_hS")
    signup = (By.CSS_SELECTOR, "#u_0_s_9H")


    def getfirstname(self):
        return self.driver.find_element(*BasicInfo.firstname)
    def getsurname(self):
        return self.driver.find_element(*BasicInfo.surname)

    def getmobileoremail(self):
        return self.driver.find_element(*BasicInfo.mobileoremail)

    def getnewpassword(self):
        return self.driver.find_element(*BasicInfo.newpassword)

    def getday(self):
        return self.driver.find_element(*BasicInfo.day)

    def getmonth(self):
        return self.driver.find_element(*BasicInfo.month)

    def getyear(self):
        return self.driver.find_element(*BasicInfo.year)
    def getgender(self):
        return self.driver.find_element(*BasicInfo.gender)
    def getsignup(self):
        return self.driver.find_element(*BasicInfo.signup)


