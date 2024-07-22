import re
from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

from elements import validate_character_numeric_element

@given('estoy en la pagina de inicio de sesion2')
def step_impl(context):
    context.browser.get("https://pwa-portal-staging.silohub.ag/login")
    print("Navegó a la página de inicio de sesión")

@when('ingreso mi nombre de usuario y credenciales correctas2')
def step_impl(context):
    print("Buscando campo de email")
    context.browser.find_element(By.ID, "email").send_keys("admingd@silohub.ag")
    print("Buscando campo de contraseña")
    context.browser.find_element(By.ID, "password").send_keys("G@viglio123")

@when('hago clic en el boton de inicio de sesion2')
def step_impl(context):
    print("Buscando botón de inicio de sesión")
    context.browser.find_element(By.XPATH, "/html/body/app-root/app-login-main/div/div[2]/div/app-login-form/div/div/div[1]/div/div[2]/form/div[4]/app-button/button").click()
    time.sleep(2)

@then('deberia ser redirigido a la pagina principal2')
def step_impl(context):
    try:
        WebDriverWait(context.browser, 10).until(EC.url_contains("home"))
        current_url = context.browser.current_url
        print("URL actual:", current_url)
        assert "home" in current_url  # Verifica que 'home' esté en la URL actual
    except Exception as e:
        print("Error:", e)
        raise AssertionError("No se redirigió a la página principal")
    
@given('selecciono el tenant donde quiero ingresar2')
def step_impl(context):
    print("Buscando botón de inicio de sesión")
    context.browser.find_element(By.XPATH, "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home-main/div/div[1]/app-tenant-main/app-tenant[8]/div/div/img").click()
    time.sleep(5)

@then('ingreso a la pagina de inicio2')
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

@given('selecciono al buscador global')
def step_impl(context):
    context.browser.find_element(By.ID, "search-options").click()
    time.sleep(2)   
    

@when('ingreso numero de cuenta en el buscador global')
def step_impl(context):
    input_element = WebDriverWait(context.browser, 10).until(EC.visibility_of_element_located((By.ID, "search-options")))
    input_element.send_keys("1023")
    time.sleep(2)  # Esperar a que las opciones se carguen

@when('hago clic en la opción desplegada correspondiente')
def step_impl(context):
    element_to_click = WebDriverWait(context.browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#search-dropdown > app-accounts-list > ngx-simplebar > div.simplebar-wrapper > div.simplebar-mask > div > div > div > div > div.dropdown-sub-item.accounts-numbers")))
    context.browser.execute_script("arguments[0].style.display = 'block';", element_to_click)
    element_to_click.click()
    time.sleep(5)

@then('el sistema muestra mensaje de bienvenida')
def step_impl(context):
    element_obtained = WebDriverWait(context.browser, 10).until(EC.visibility_of_element_located((By.XPATH, "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home/div/app-welcome-home/div/div[1]/div/p")))
    assert element_obtained.is_displayed(), "El mensaje de bienvenida no se muestra"
    expected_message = "Buen día JUAN DEMO!"  
    assert element_obtained.text == expected_message

@then('Vencido a hoy saldo en ARS')
def step_impl(context):
    select_element = WebDriverWait(context.browser, 10).until(EC.visibility_of_element_located((By.XPATH, "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home/div/div[1]/app-balances/div[2]/swiper/div/div[1]/div[1]/app-number-values-card/div/div/div/div[3]/div/h4/span")))
    valor = select_element.text
    if re.search(r'\d', valor):
        print(f'El valor es un carácter numérico. Valor: {valor}')
        assert True, "El saldo a hoy es un valor numérico"
    else:
        print(f'El valor no es un carácter numérico. Valor: {valor}')
        assert False, f"El saldo a hoy no es un valor numérico: {valor}"
    time.sleep(2)

@then('Vencido a hoy saldo en USD')
def step_impl(context):
    select_element = WebDriverWait(context.browser, 10).until(EC.visibility_of_element_located((By.XPATH, "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home/div/div[1]/app-balances/div[2]/swiper/div/div[1]/div[2]/app-number-values-card/div/div/div/div[3]/div/h4/span")))
    valor = select_element.text
    if re.search(r'\d', valor):
        print(f'El valor es un carácter numérico. Valor: {valor}')
        assert True, "El saldo a hoy es un valor numérico"
    else:
        print(f'El valor no es un carácter numérico. Valor: {valor}')
        assert False, f"El saldo a hoy no es un valor numérico: {valor}"
    time.sleep(2)

@then('A vencer saldo en USD')
def step_impl(context):
    select_element = WebDriverWait(context.browser, 10).until(EC.visibility_of_element_located((By.XPATH, "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home/div/div[1]/app-balances/div[2]/swiper/div/div[1]/div[3]/app-number-values-card/div/div/div/div[3]/div/h4/span")))
    valor = select_element.text
    if re.search(r'\d', valor):
        print(f'El valor es un carácter numérico. Valor: {valor}')
        assert True, "El saldo a hoy es un valor numérico"
    else:
        print(f'El valor no es un carácter numérico. Valor: {valor}')
        assert False, f"El saldo a hoy no es un valor numérico: {valor}"
    time.sleep(2)

@then('A vencer saldo en ARS')
def step_impl(context):
    select_element =  "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home/div/div[1]/app-balances/div[2]/swiper/div/div[1]/div[4]/app-number-values-card/div/div/div/div[3]/div/h4/span"
    validate_character_numeric_element(context.browser,select_element)
    time.sleep(2)