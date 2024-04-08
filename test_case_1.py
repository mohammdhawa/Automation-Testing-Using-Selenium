from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pytest

@pytest.fixture(scope="class")
def setup(request):
    driver = webdriver.Chrome()
    driver.get("http://127.0.0.1:8000/")
    time.sleep(2)
    driver.maximize_window()
    time.sleep(2)
    driver.implicitly_wait(10)
    # scrolling_down(driver, "slowly")
    # scrolling_up(driver, "slowly")

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
    time.sleep(1)


# İlk dosya, film türlerine göz atmayla ilgili bir test sınıfından oluşur;
# burada bu sınıftaki her işlev, belirli bir film türüne göz atmayı söyler
# ve böylece filmlere türe göre göz atmanın sitede iyi çalıştığından emin oluruz.
@pytest.mark.usefixtures("setup")
class TestGenres:

    def test_all(self):
        click_navbar_dropdown(self.driver)
        genre_button = self.driver.find_element(By.XPATH, "//a[normalize-space()='All']")
        genre_button.click()
        time.sleep(2)
        scrolling_down(self.driver)
        scrolling_up(self.driver)
        self.driver.back()
        time.sleep(1)

    def test_documentary(self):
        click_navbar_dropdown(self.driver)
        genre_button = self.driver.find_element(By.XPATH, "//a[@class='dropdown-item'][normalize-space()='Documentary']")
        genre_button.click()
        time.sleep(3)
        scrolling_down(self.driver)
        scrolling_up(self.driver)
        self.driver.back()
        time.sleep(2)

    def test_action(self):
        click_navbar_dropdown(self.driver)

        genre_button = self.driver.find_element(By.XPATH, "//a[@class='dropdown-item'][normalize-space()='Action']")
        genre_button.click()
        time.sleep(1)

        scrolling_down(self.driver)
        scrolling_up(self.driver)

    def test_adventure(self):
        click_navbar_dropdown(self.driver)

        genre_button = self.driver.find_element(By.XPATH, "//a[@class='dropdown-item'][normalize-space()='Adventure']")
        genre_button.click()
        time.sleep(1)

        scrolling_down(self.driver)
        scrolling_up(self.driver)

    def test_comedy(self):
        click_navbar_dropdown(self.driver)

        genre_button = self.driver.find_element(By.XPATH, "//a[@class='dropdown-item'][normalize-space()='Comedy']")
        genre_button.click()
        time.sleep(1)

        scrolling_down(self.driver)
        scrolling_up(self.driver)

    def test_drama(self):
        click_navbar_dropdown(self.driver)

        genre_button = self.driver.find_element(By.XPATH, "//a[@class='dropdown-item'][normalize-space()='Drama']")
        genre_button.click()
        time.sleep(1)

        scrolling_down(self.driver)
        scrolling_up(self.driver)

    def test_horror(self):
        click_navbar_dropdown(self.driver)

        genre_button = self.driver.find_element(By.XPATH, "//a[@class='dropdown-item'][normalize-space()='Horror']")
        genre_button.click()
        time.sleep(1)

        scrolling_down(self.driver)
        scrolling_up(self.driver)

    def test_romance(self):
        click_navbar_dropdown(self.driver)

        drop_down_button = self.driver.find_element(By.XPATH, "//a[@class='dropdown-item'][normalize-space()='Romance']")
        drop_down_button.click()
        time.sleep(1)

        scrolling_down(self.driver)
        scrolling_up(self.driver)

    def test_science_fiction(self):
        click_navbar_dropdown(self.driver)

        drop_down_button = self.driver.find_element(By.XPATH, "//a[@class='dropdown-item'][normalize-space()='Science fiction']")
        drop_down_button.click()
        time.sleep(1)

        scrolling_down(self.driver)
        scrolling_up(self.driver)

    def test_fantasy(self):
        click_navbar_dropdown(self.driver)

        drop_down_button = self.driver.find_element(By.XPATH, "//a[@class='dropdown-item'][normalize-space()='Fantasy']")
        drop_down_button.click()
        time.sleep(1)

        scrolling_down(self.driver)
        scrolling_up(self.driver)

    def test_historical(self):
        click_navbar_dropdown(self.driver)

        drop_down_button = self.driver.find_element(By.XPATH, "//a[@class='dropdown-item'][normalize-space()='Historical']")
        drop_down_button.click()
        time.sleep(1)

        scrolling_down(self.driver)
        scrolling_up(self.driver)

    def test_crime(self):
        click_navbar_dropdown(self.driver)

        drop_down_button = self.driver.find_element(By.XPATH, "//a[@class='dropdown-item'][normalize-space()='Crime']")
        drop_down_button.click()
        time.sleep(1)

        scrolling_down(self.driver)
        scrolling_up(self.driver)

    def test_thriller(self):
        click_navbar_dropdown(self.driver)

        drop_down_button = self.driver.find_element(By.XPATH, "//a[@class='dropdown-item'][normalize-space()='Thriller']")
        drop_down_button.click()
        time.sleep(1)

        scrolling_down(self.driver)
        scrolling_up(self.driver)

    def test_mystery(self):
        click_navbar_dropdown(self.driver)

        drop_down_button = self.driver.find_element(By.XPATH, "//a[@class='dropdown-item'][normalize-space()='Mystery']")
        drop_down_button.click()
        time.sleep(1)

        scrolling_down(self.driver)
        scrolling_up(self.driver)
