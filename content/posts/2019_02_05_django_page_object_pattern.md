Title: Page Object Pattern in testing Django
Date: 2019-02-05
Category: Python
Tags: python, django, testing, selenium
Slug: django-page-object-pattern
Summary: Page Object Pattern in testing Django
Status: published


## Page Object Pattern
Functional testing with usage of selenium is based on giving simple instructions to browser and comparing results with expectations. Generally we start with step by step instructions which element should be located, then what to do with them (click, read or insert value). It's working fine with simple pages but when project is growing and our test suite is getting complex as well and brittle to changes. Some id changed and bam, plenty of tests are not valid anymore. The Page Object Pattern is some special form of facade pattern where the web pages and elements of them are separated from testing procedure and provides nicer API. 


### Page Objects in action

```python
from selenium import webdriver
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from webdriver_manager.chrome import ChromeDriverManager


class BasePage(object):
    url = None

    def __init__(self, driver):
        self.driver = driver

    def fill_form(self, elem, value):
        elem.send_keys(value)

    def fill_form_by_id(self, form_element_id, value):
        elem = self.driver.find_element_by_id(form_element_id)
        return self.fill_form(elem, value)

    def navigate(self):
        self.driver.get(self.url)


class Homepage(BasePage):
    url = "http://localhost:8000"

    def getLoginform(self):
        return LogInPage(self.driver)


class LogInPage(BasePage):
    url = "http://127.0.0.1:8000/login/"

    def setUsername(self, username):
        self.fill_form_by_id("id_username", username)

    def setPassword(self, password):
        self.fill_form_by_id("id_password", password)

    def submit(self):
        self.driver.find_element_by_id("login_button").click()


class LogInTest(StaticLiveServerTestCase):
    def setUp(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--incognito")
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    def test_someone_can_login(self):
        homepage = Homepage(self.browser)
        homepage.navigate()
        signup_form = homepage.getLoginform()
        signup_form.navigate()
        signup_form.setUsername("Justin")
        signup_form.setPassword("Bieber")
        signup_form.submit()
        elem = self.browser.find_element_by_css_selector('.alert')
        self.assertIsNotNone(elem)

    def tearDown(self):
        self.browser.close()
```


<br>

----------------
#### Sources:
* [Justin Abrahms - Selenium's Page Object Pattern: The Key to Maintainable Tests](https://justin.abrah.ms/python/selenium-page-object-pattern--the-key-to-maintainable-tests.html)
