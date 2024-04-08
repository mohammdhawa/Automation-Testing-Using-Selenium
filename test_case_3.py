from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import pytest
from selenium.webdriver.support.ui import Select

@pytest.fixture(scope="class")
def setup(request):
    driver = webdriver.Chrome()
    driver.get("http://127.0.0.1:8000/")
    time.sleep(2)
    driver.maximize_window()
    time.sleep(2)
    driver.implicitly_wait(10)

    def teardown():
        driver.quit()

    request.addfinalizer(teardown)
    request.cls.driver = driver

def scrolling_down(driver, status=None):
    if status == "slowly":
        scroll_amount = 100
        current_scroll_position = 0
        while current_scroll_position < driver.execute_script("return document.body.scrollHeight"):
            driver.execute_script("window.scrollBy(0, " + str(scroll_amount) + ");")
            current_scroll_position += scroll_amount
            time.sleep(0.1)
    else:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)

def scrolling_up(driver, status=None):
    if status == "slowly":
        scroll_amount = -100
        scroll_delay = 0.1
        current_scroll_position = driver.execute_script("return document.body.scrollHeight")
        while current_scroll_position > 0:
            driver.execute_script("window.scrollBy(0, " + str(scroll_amount) + ");")
            current_scroll_position += scroll_amount
            time.sleep(scroll_delay)
    else:
        driver.execute_script("window.scrollTo(0, 0);")
    time.sleep(3)

def click_navbar_dropdown(driver):
    drop_down_button = driver.find_element(By.ID, "navbarDropdown")
    drop_down_button.click()
    time.sleep(3)


# Üçüncü dosya, filmlerin (tür, dil, ülke vb.) göre filtrelenmesini test
# eden bir işlevi ve ayrıca belirli bir filmi aramayı test eden
# bir işlevi içeren bir test sınıfdan oluşur.

@pytest.mark.usefixtures("setup")
class TestCase3:

    def test_filtering(self):
        try:
            click_navbar_dropdown(self.driver)
            all_movies = self.driver.find_element(By.XPATH, "//a[normalize-space()='All']")
            all_movies.click()
        except:
            print("Error while locating all_movies button")
        time.sleep(3)

        self.driver.execute_script("window.scrollBy(0, 800)")
        time.sleep(10)

        dropdown_element = self.driver.find_element(By.ID, "id_type")
        select = Select(dropdown_element)
        select.select_by_visible_text("Action")
        select.select_by_visible_text("Adventure")

        time.sleep(2)

        dropdown_element2 = self.driver.find_element(By.ID, "id_language")
        select2 = Select(dropdown_element2)
        select2.select_by_visible_text("English")

        time.sleep(2)

        dropdown_element3 = self.driver.find_element(By.ID, "id_country")
        select3 = Select(dropdown_element3)
        select3.select_by_visible_text("USA")

        time.sleep(3)

        filter_button = self.driver.find_element(By.XPATH, "//button[normalize-space()='Filter']")
        filter_button.click()

        scrolling_up(self.driver)
        self.driver.execute_script("window.scrollBy(0, 800)")
        time.sleep(5)

        home_button = self.driver.find_element(By.XPATH, "//a[@class='nav-link'][normalize-space()='Home']")
        home_button.click()
        time.sleep(5)

    def test_search(self):
        search_button_element = self.driver.find_element(By.XPATH, "//a[normalize-space()='Search']")
        search_button_element.click()

        time.sleep(2)

        search_input_element = self.driver.find_element(By.XPATH, "//input[@id='id_name']")
        search_input_element.send_keys("shawshank")

        time.sleep(2)

        search_input_element.send_keys(Keys.ENTER)

        time.sleep(4)




