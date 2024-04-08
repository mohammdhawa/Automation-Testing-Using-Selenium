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
    scrolling_down(driver, "slowly")

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


# İkinci dosya, hesap oluşturmayı, oturum açmayı, oturumu kapatmayı
# ve profil bilgilerini doldurmayı test eden işlevleri içerdiğinden,
# hesap kimlik doğrulamasıyla ilgili bir test sınıfından oluşur.
@pytest.mark.usefixtures("setup")
class TestUserAuthentication:

    def test_signup(self):
        scrolling_down(self.driver)
        try:
            login_button = self.driver.find_element(By.ID, "loggin_id")
            login_button.click()
        except:
            print("The element login button not found")
        time.sleep(3)
        try:
            signup_button = self.driver.find_element(By.XPATH, "//a[normalize-space()='Sign Up']")
            signup_button.click()
        except:
            print("The element signup button not found")

        time.sleep(3)

        try:
            username_input = self.driver.find_element(By.XPATH, "//input[@id='id_username']")
            username_input.send_keys("test2")

            time.sleep(2)

            email_input = self.driver.find_element(By.XPATH, "//input[@id='id_email']")
            email_input.send_keys("test2@gmail.com")

            time.sleep(2)

            password_input = self.driver.find_element(By.ID, "id_password1")
            password_input.send_keys("MoH.1822")

            time.sleep(2)

            password_input2 = self.driver.find_element(By.ID, "id_password2")
            password_input2.send_keys("MoH.1822")

            time.sleep(2)

            signup_button = self.driver.find_element(By.XPATH, "//button[normalize-space()='Signup']")
            signup_button.click()

            time.sleep(3)

            try:
                try:
                    first_name_input = self.driver.find_element(By.ID, "id_first_name")
                    first_name_input.clear()
                    first_name_input.send_keys("Mohammad")
                except:
                    print("Error while locating first_name_input")

                time.sleep(2)

                try:
                    last_name_input = self.driver.find_element(By.ID, "id_last_name")
                    last_name_input.clear()
                    last_name_input.send_keys("Hawa")
                except:
                    print("Error while locating the last_name_input")

                time.sleep(2)

                try:
                    phone_input = self.driver.find_element(By.ID, "id_phone_number")
                    phone_input.clear()
                    phone_input.send_keys("+905377944478")
                except:
                    print("Error while locating the phone_input")

                time.sleep(2)

                try:
                    address_input = self.driver.find_element(By.ID, "id_address")
                    address_input.clear()
                    address_input.send_keys("Any Random Address")
                except:
                    print("Error while locating the address_input")

                time.sleep(2)

                try:
                    image_input = self.driver.find_element(By.ID, "id_image")
                    image_input.send_keys("/home/mhawa/Downloads/profile_photo.jpeg")
                except:
                    print("Error while locating the image_input")

                time.sleep(2)

                try:
                    job_input = self.driver.find_element(By.ID, "id_job")
                    job_input.clear()
                    job_input.send_keys("Software Engineer")
                except:
                    print("Error while locating job_input")

                time.sleep(2)

                try:
                    save_button = self.driver.find_element(By.XPATH, "//button[normalize-space()='Save Changes']")
                    save_button.click()
                except:
                    print("Error while locating save_button")
                time.sleep(5)
            except:
                print("Something wrong while locating (firstname - lastname - phone - address - image - job - savebutton) elements")
        except:
            print("Error in finding an element (username input - email_input - password_input - password_input2 - signup_button)")

        try:
            home_button = self.driver.find_element(By.XPATH, "//a[@class='nav-link'][normalize-space()='Home']")
            home_button.click()
        except:
            print("Something wrong while locating home button")

        time.sleep(5)

    def test_logout(self):
        scrolling_down(self.driver)

        try:
            logout_button = self.driver.find_element(By.ID, "logout_id")
            logout_button.click()
            time.sleep(4)
        except:
            print("Something wrong while locating logout button")

    def test_login(self):
        try:
            username_input = self.driver.find_element(By.ID, "id_username")
            username_input.send_keys("test2")

            time.sleep(2)

            password_input = self.driver.find_element(By.ID, "id_password")
            password_input.send_keys("MoH.1822")

            time.sleep(2)

            login_button = self.driver.find_element(By.XPATH, "//button[normalize-space()='login']")
            login_button.click()
        except:
            print("Something wrong while locating (username_input - password_input - login_button)")
        time.sleep(5)
