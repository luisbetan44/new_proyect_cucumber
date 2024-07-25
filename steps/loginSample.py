
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class LoginSteps2:

    def __init__(self, browser):
        self.browser = browser

    def navigate_to_login_page(self, url):
        self.browser.get(url)
        print("Navegó a la página de inicio de sesión")

    def enter_credentials(self, username, password):
        print("Buscando campo de email")
        self.browser.find_element(By.ID, "email").send_keys(username)
        print("Buscando campo de contraseña")
        self.browser.find_element(By.ID, "password").send_keys(password)

    def click_login_button(self):
        print("Buscando botón de inicio de sesión")
        self.browser.find_element(By.XPATH, "/html/body/app-root/app-login-main/div/div[2]/div/app-login-form/div/div/div[1]/div/div[2]/form/div[4]/app-button/button").click()
        time.sleep(2)

    def verify_redirection_to_home(self):
        try:
            WebDriverWait(self.browser, 10).until(EC.url_contains("home"))
            current_url = self.browser.current_url
            print("URL actual:", current_url)
            assert "home" in current_url  # Verifica que 'home' esté en la URL actual
        except Exception as e:
            print("Error:", e)
            raise AssertionError("No se redirigió a la página principal")

    def select_tenant(self):
        print("Buscando botón de inicio de sesión")
        self.browser.find_element(By.XPATH, "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home-main/div/div[1]/app-tenant-main/app-tenant[8]/div/div/img").click()
        time.sleep(2)

    def verify_redirection_to_inicio(self):
        try:
            WebDriverWait(self.browser, 10).until(EC.url_contains("inicio"))
            current_url = self.browser.current_url
            print("URL actual:", current_url)
            assert "inicio" in current_url  # Verifica que 'home' esté en la URL actual
        except Exception as e:
            print("Error:", e)
            raise AssertionError("No se redirigió a la página principal")
        time.sleep(10)