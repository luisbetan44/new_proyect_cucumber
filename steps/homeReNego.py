from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from elements import validate_character_numeric_element,validate_image_xpaht, validate_text, validate_values_text

@given('estoy en la pagina de inicio de sesion3')
def step_impl(context):
    context.browser.get("https://pwa-portal-staging.silohub.ag/login")
    print("Navegó a la página de inicio de sesión")

@when('ingreso mi nombre de usuario y credenciales correctas3')
def step_impl(context):
    print("Buscando campo de email")
    context.browser.find_element(By.ID, "email").send_keys("admingd@silohub.ag")
    print("Buscando campo de contraseña")
    context.browser.find_element(By.ID, "password").send_keys("G@viglio123")

@when('hago clic en el boton de inicio de sesion3')
def step_impl(context):
    print("Buscando botón de inicio de sesión")
    context.browser.find_element(By.XPATH, "/html/body/app-root/app-login-main/div/div[2]/div/app-login-form/div/div/div[1]/div/div[2]/form/div[4]/app-button/button").click()
    time.sleep(2)

@then('deberia ser redirigido a la pagina principal3')
def step_impl(context):
    try:
        WebDriverWait(context.browser, 10).until(EC.url_contains("home"))
        current_url = context.browser.current_url
        print("URL actual:", current_url)
        assert "home" in current_url  # Verifica que 'home' esté en la URL actual
    except Exception as e:
        print("Error:", e)
        raise AssertionError("No se redirigió a la página principal")
    
@given('selecciono el tenant donde quiero ingresar3')
def step_impl(context):
    print("Buscando botón de inicio de sesión")
    context.browser.find_element(By.XPATH, "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home-main/div/div[1]/app-tenant-main/app-tenant[8]/div/div/img").click()
    time.sleep(2)

@then('ingreso a la pagina de inicio3')
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


@given('seleccionar al buscador global3')
def step_impl(context):
    context.browser.find_element(By.ID, "search-options").click()
    time.sleep(2)   
    

@when('ingreso numero de cuenta en el buscador global3')
def step_impl(context):
    input_element = WebDriverWait(context.browser, 10).until(EC.visibility_of_element_located((By.ID, "search-options")))
    input_element.send_keys("1023")
    time.sleep(2)  # Esperar a que las opciones se carguen

@when('hago clic en la opción desplegada correspondiente3')
def step_impl(context):
    element_to_click = WebDriverWait(context.browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#search-dropdown > app-accounts-list > ngx-simplebar > div.simplebar-wrapper > div.simplebar-mask > div > div > div > div > div.dropdown-sub-item.accounts-numbers")))
    context.browser.execute_script("arguments[0].style.display = 'block';", element_to_click)
    element_to_click.click()
    time.sleep(5)

@then('el sistema muestra mensaje de bienvenida3')
def step_impl(context):
    element_obtained = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home/div/app-welcome-home/div/div[1]/div/p"
    expected_message = "Buen día JUAN DEMO!"  
    validate_text(context.browser, element_obtained, expected_message)

@given('validar imagen del producto')
def step_impl(context):
    img_obtained = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home/div/div[2]/app-business-indicators/div[2]/swiper[1]/div/div[1]/div[1]/div/img"
    img_expected = ["https://pwa-portal-staging.silohub.ag/assets/images/grains/trigo.svg",
                    "https://pwa-portal-staging.silohub.ag/assets/images/grains/maiz.svg",
                    "https://pwa-portal-staging.silohub.ag/assets/images/grains/girasol.svg",
                    "https://pwa-portal-staging.silohub.ag/assets/images/grains/soja.svg"]
    validate_image_xpaht(context.browser, img_obtained, img_expected)

@then('validar descripcion del producto')
def step_impl(context):
    description_obtained = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home/div/div[2]/app-business-indicators/div[2]/swiper[1]/div/div[1]/div[1]/div/span"
    description_expected = ["Soja","Maiz","Trigo"]
    validate_values_text(context.browser, description_obtained, description_expected)

@then('validar la cantidad entregada')
def step_impl(context):
    value_delivery = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home/div/div[2]/app-business-indicators/div[2]/swiper[1]/div/div[1]/div[2]/app-indicator-card/div/div[2]/div[1]/div[2]"
    validate_character_numeric_element(context.browser, value_delivery)
    time.sleep(2)

@then('validar la cantidad pendiente de entregar')
def step_impl(context):
    value_delivery_pending = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home/div/div[2]/app-business-indicators/div[2]/swiper[1]/div/div[1]/div[2]/app-indicator-card/div/div[2]/div[2]/div[2]"
    validate_character_numeric_element(context.browser, value_delivery_pending)
    time.sleep(2)

@then('validar cantidad fijada')
def step_impl(context):
    value_fixed = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home/div/div[2]/app-business-indicators/div[2]/swiper[1]/div/div[1]/div[3]/app-indicator-card/div/div[2]/div[1]/div[2]"
    validate_character_numeric_element(context.browser, value_fixed)
    time.sleep(2)

@then('validar cantidad pendiente de fijar')
def step_impl(context):
    value_fixed_pending = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home/div/div[2]/app-business-indicators/div[2]/swiper[1]/div/div[1]/div[3]/app-indicator-card/div/div[2]/div[2]/div[2]"
    validate_character_numeric_element(context.browser, value_fixed_pending)
    time.sleep(2)

@then('validar cantidad pesificada')
def step_impl(context):
    value_pesificado = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home/div/div[2]/app-business-indicators/div[2]/swiper[1]/div/div[1]/div[4]/app-indicator-card/div/div[2]/div[1]/div[2]"
    validate_character_numeric_element(context.browser, value_pesificado)
    time.sleep(2)

@then('validar cantidad pendiente de pesificar')
def step_impl(context):
    value_pesificado_pending = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home/div/div[2]/app-business-indicators/div[2]/swiper[1]/div/div[1]/div[4]/app-indicator-card/div/div[2]/div[2]/div[2]"
    validate_character_numeric_element(context.browser, value_pesificado_pending)
    time.sleep(2)

@then('validar cantidad liquidada')
def step_impl(context):
    value_liquidated = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home/div/div[2]/app-business-indicators/div[2]/swiper[1]/div/div[1]/div[5]/app-indicator-card/div/div[2]/div[1]/div[2]"
    validate_character_numeric_element(context.browser, value_liquidated)
    time.sleep(2)

@then('validar cantidad pendiente de liquidar')
def step_impl(context):
    value_liquidated_pending = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home/div/div[2]/app-business-indicators/div[2]/swiper[1]/div/div[1]/div[5]/app-indicator-card/div/div[2]/div[2]/div[2]"
    validate_character_numeric_element(context.browser, value_liquidated_pending)
    time.sleep(2)

