from selenium import webdriver
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


# Dördüncü dosya, bir filmi değerlendirme ve onun hakkında inceleme
# yazma sürecini test eden bir işlevi içeren bir sınıfdan oluşur.
@pytest.mark.usefixtures("setup")
class TestCommenting:

    def test_rating_movie(self):
        scrolling_down(self.driver)
        self.driver.find_element(By.XPATH, "//a[normalize-space()='Login']").click()
        username_input = self.driver.find_element(By.ID, "id_username")
        username_input.clear()
        username_input.send_keys("test2")

        # time.sleep(2)

        password_input = self.driver.find_element(By.ID, "id_password")
        password_input.clear()
        password_input.send_keys("MoH.1822")

        # time.sleep(2)

        login_button = self.driver.find_element(By.XPATH, "//button[normalize-space()='login']")
        login_button.click()
        # time.sleep(3)
        # time.sleep(2)
        movie = self.driver.find_element(By.XPATH, "//div[@class='w3l-populohny-grids']//div[1]//div[1]//a[1]")
        movie.click()
        scrolling_down(self.driver)
        # time.sleep(2)

        comment_input = self.driver.find_element(By.XPATH, "//textarea[@id='id_comment']")
        comment_input.send_keys("This is the best movie I've ever seen.")

        time.sleep(2)

        comment_button = self.driver.find_element(By.XPATH, "//button[normalize-space()='Post comment']")
        comment_button.click()

        scrolling_down(self.driver)
        self.driver.execute_script("window.scrollBy(0, -500);")
        # scrolling_down(self.driver, 'slowly')

        time.sleep(5)
