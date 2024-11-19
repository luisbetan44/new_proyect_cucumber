from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class LoginSteps3:

    def __init__(self, browser):
        self.browser = browser

    def navigate_to_login_page(self, url):
        self.browser.get(url)
        print("Navegó a la página de inicio de sesión")

    def enter_credentials(self, username, password):
       self.browser.find_element(By.ID, "email").send_keys(username)
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

    def click_global_search(self):
        self.browser.find_element(By.ID, "search-options").click()
        time.sleep(2)

    def enter_account_number(self, account_number):
        input_element = WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located((By.ID, "search-options")))
        input_element.send_keys(account_number)
        time.sleep(2)  # Esperar a que las opciones se carguen

    def click_suggested_option(self):
        element_to_click = WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#search-dropdown > app-accounts-list > ngx-simplebar > div.simplebar-wrapper > div.simplebar-mask > div > div > div > div > div.dropdown-sub-item.accounts-numbers")))
        self.browser.execute_script("arguments[0].style.display = 'block';", element_to_click)
        element_to_click.click()
        time.sleep(5)