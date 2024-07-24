from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from elements import scroll_to_element, validate_character_numeric_element, validate_character_numeric_element_selector, validate_image_xpaht, validate_strt
from loginHelper import LoginSteps3




@given('estoy en la pagina de inicio de sesion4')
def step_impl(context):
    login_steps = LoginSteps3(context.browser)
    login_steps.navigate_to_login_page("https://pwa-portal-staging.silohub.ag/login")

@when('ingreso mi nombre de usuario y credenciales correctas4')
def step_impl(context):
    login_steps = LoginSteps3(context.browser)
    login_steps.enter_credentials("admingd@silohub.ag", "G@viglio123")

@when('hago clic en el boton de inicio de sesion4')
def step_impl(context):
    login_steps = LoginSteps3(context.browser)
    login_steps.click_login_button()

@then('deberia ser redirigido a la pagina principal4')
def step_impl(context):
    login_steps = LoginSteps3(context.browser)
    login_steps.verify_redirection_to_home()

@given('selecciono el tenant donde quiero ingresar4')
def step_impl(context):
    login_steps = LoginSteps3(context.browser)
    login_steps.select_tenant()

@then('ingreso a la pagina de inicio4')
def step_impl(context):
    login_steps = LoginSteps3(context.browser)
    login_steps.verify_redirection_to_inicio()

@given('seleccionar al buscador global4')
def step_impl(context):
    login_steps = LoginSteps3(context.browser)
    login_steps.click_global_search()

@when('ingreso numero de cuenta en el buscador global4')
def step_impl(context):
    login_steps = LoginSteps3(context.browser)
    login_steps.enter_account_number("1023")

@when('hago clic en la opción desplegada correspondiente4')
def step_impl(context):
    login_steps = LoginSteps3(context.browser)
    login_steps.click_suggested_option()
    time.sleep(5)

@when('srollear hasta el centro de la pantalla')
def step_impl(context):
    element_scroll = "//span[text()='Entregas Recientes ']"
    scroll_to_element(context.browser, element_scroll)
    

@given('validar imagen del producto entregado')
def step_impl(context):
    img_obtained = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home/div/div[3]/app-recent-grain-movements/div[2]/div[1]/app-recent-deliveries/app-responsive-table-multiple-items/div/table/tbody/tr[1]/td[1]/div/div/div[1]/img"
    img_expected = ["https://pwa-portal-staging.silohub.ag/assets/images/grains/trigo.svg",
                    "https://pwa-portal-staging.silohub.ag/assets/images/grains/maiz.svg",
                    "https://pwa-portal-staging.silohub.ag/assets/images/grains/girasol.svg",
                    "https://pwa-portal-staging.silohub.ag/assets/images/grains/soja.svg"]
    validate_image_xpaht(context.browser, img_obtained, img_expected)

@then('validar descripcion y cosecha del producto a entregar')
def step_impl(context):
    description_delivery = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home/div/div[3]/app-recent-grain-movements/div[2]/div[1]/app-recent-deliveries/app-responsive-table-multiple-items/div/table/tbody/tr[1]/td[1]/div/div/div[2]/div[1]/span"
    validate_strt(context.browser, description_delivery)

@then('validar la fecha de la entrega')
def step_impl(context):
    value_date = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home/div/div[3]/app-recent-grain-movements/div[2]/div[1]/app-recent-deliveries/app-responsive-table-multiple-items/div/table/tbody/tr[1]/td[1]/div/div/div[2]/div[2]/span"
    validate_character_numeric_element(context.browser, value_date)
    time.sleep(2)

@then('validar el numero de CTG/CRT de la entrega')
def step_impl(context):
    value_CTG_CRT = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home/div/div[3]/app-recent-grain-movements/div[2]/div[1]/app-recent-deliveries/app-responsive-table-multiple-items/div/table/tbody/tr[1]/td[2]/div/div/span"
    validate_character_numeric_element(context.browser, value_CTG_CRT)
    time.sleep(2)

@then('validar kilos a entregar')
def step_impl(context):
    value_KL_delivery = '//*[@id="layout-wrapper"]/div/div/div/app-home/div/div[3]/app-recent-grain-movements/div[2]/div[1]/app-recent-deliveries/app-responsive-table-multiple-items/div/table/tbody/tr[1]/td[3]/div/div/span'
    validate_character_numeric_element(context.browser, value_KL_delivery)
    time.sleep(2)

@given('validar imagen del producto vender')
def step_impl(context):
    img_obtained = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home/div/div[3]/app-recent-grain-movements/div[2]/div[2]/app-recent-sales/app-responsive-table-multiple-items/div/table/tbody/tr[1]/td[1]/div/div/div[1]/img"
    img_expected = ["https://pwa-portal-staging.silohub.ag/assets/images/grains/trigo.svg",
                    "https://pwa-portal-staging.silohub.ag/assets/images/grains/maiz.svg",
                    "https://pwa-portal-staging.silohub.ag/assets/images/grains/girasol.svg",
                    "https://pwa-portal-staging.silohub.ag/assets/images/grains/soja.svg"]
    validate_image_xpaht(context.browser, img_obtained, img_expected)

@then('validar descripcion y cosecha del producto a vender')
def step_impl(context):
    description_sales = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home/div/div[3]/app-recent-grain-movements/div[2]/div[2]/app-recent-sales/app-responsive-table-multiple-items/div/table/tbody/tr[1]/td[1]/div/div/div[2]/div[1]/span"
    validate_strt(context.browser, description_sales)

@then('validar la fecha de la vender')
def step_impl(context):
    value_date_sales = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home/div/div[3]/app-recent-grain-movements/div[2]/div[2]/app-recent-sales/app-responsive-table-multiple-items/div/table/tbody/tr[1]/td[1]/div/div/div[2]/div[2]/span"
    validate_character_numeric_element(context.browser, value_date_sales)
    time.sleep(2)

@then('validar el cantidad kilos de la venta')
def step_impl(context):
    value_KL_sales = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home/div/div[3]/app-recent-grain-movements/div[2]/div[2]/app-recent-sales/app-responsive-table-multiple-items/div/table/tbody/tr[1]/td[2]/div/div/span"
    validate_character_numeric_element(context.browser, value_KL_sales)
    time.sleep(2)

@then('validar precio de las ventas')
def step_impl(context):
    value_price = "#layout-wrapper > div > div > div > app-home > div > div:nth-child(4) > app-recent-grain-movements > div:nth-child(2) > div:nth-child(2) > app-recent-sales > app-responsive-table-multiple-items > div > table > tbody > tr:nth-child(1) > td:nth-child(3) > div > div > span:nth-child(2)"
    validate_character_numeric_element_selector(context.browser, value_price)
    time.sleep(2)

