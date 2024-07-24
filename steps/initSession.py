from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

@given('estoy en la pagina de inicio de sesion')
def step_impl(context):
    context.browser.get("https://pwa-portal-staging.silohub.ag/login")
    print("Navegó a la página de inicio de sesión")

@when('ingreso mi nombre de usuario y credenciales correctas')
def step_impl(context):
    print("Buscando campo de email")
    context.browser.find_element(By.ID, "email").send_keys("admingd@silohub.ag")
    print("Buscando campo de contraseña")
    context.browser.find_element(By.ID, "password").send_keys("G@viglio123")

@when('hago clic en el boton de inicio de sesion')
def step_impl(context):
    print("Buscando botón de inicio de sesión")
    context.browser.find_element(By.XPATH, "/html/body/app-root/app-login-main/div/div[2]/div/app-login-form/div/div/div[1]/div/div[2]/form/div[4]/app-button/button").click()
    time.sleep(2)

@then('deberia ser redirigido a la pagina principal')
def step_impl(context):
    try:
        WebDriverWait(context.browser, 10).until(EC.url_contains("home"))
        current_url = context.browser.current_url
        print("URL actual:", current_url)
        assert "home" in current_url  # Verifica que 'home' esté en la URL actual
    except Exception as e:
        print("Error:", e)
        raise AssertionError("No se redirigió a la página principal")
    
@given('selecciono el tenant donde quiero ingresar')
def step_impl(context):
    print("Buscando botón de inicio de sesión")
    context.browser.find_element(By.XPATH, "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home-main/div/div[1]/app-tenant-main/app-tenant[8]/div/div/img").click()
    time.sleep(2)

@then('ingreso a la pagina de inicio')
def step_impl(context):
    try:
        WebDriverWait(context.browser, 10).until(EC.url_contains("inicio"))
        current_url = context.browser.current_url
        print("URL actual:", current_url)
        assert "inicio" in current_url  # Verifica que 'home' esté en la URL actual
    except Exception as e:
        print("Error:", e)
        raise AssertionError("No se redirigió a la página principal")
    time.sleep(10)
    
