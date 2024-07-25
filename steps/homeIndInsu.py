from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from elements import scroll_to_element, validate_strt,validate_values_text
from loginHelper import LoginSteps3




@given('estoy en la pagina de inicio de sesion5')
def step_impl(context):
    login_steps = LoginSteps3(context.browser)
    login_steps.navigate_to_login_page("https://pwa-portal-staging.silohub.ag/login")

@when('ingreso mi nombre de usuario y credenciales correctas5')
def step_impl(context):
    login_steps = LoginSteps3(context.browser)
    login_steps.enter_credentials("admingd@silohub.ag", "G@viglio123")

@when('hago clic en el boton de inicio de sesion5')
def step_impl(context):
    login_steps = LoginSteps3(context.browser)
    login_steps.click_login_button()

@then('deberia ser redirigido a la pagina principal5')
def step_impl(context):
    login_steps = LoginSteps3(context.browser)
    login_steps.verify_redirection_to_home()

@given('selecciono el tenant donde quiero ingresar5')
def step_impl(context):
    login_steps = LoginSteps3(context.browser)
    login_steps.select_tenant()

@then('ingreso a la pagina de inicio5')
def step_impl(context):
    login_steps = LoginSteps3(context.browser)
    login_steps.verify_redirection_to_inicio()

@given('seleccionar al buscador global5')
def step_impl(context):
    login_steps = LoginSteps3(context.browser)
    login_steps.click_global_search()

@when('ingreso numero de cuenta en el buscador global5')
def step_impl(context):
    login_steps = LoginSteps3(context.browser)
    login_steps.enter_account_number("1023")

@when('hago clic en la opción desplegada correspondiente5')
def step_impl(context):
    login_steps = LoginSteps3(context.browser)
    login_steps.click_suggested_option()
    time.sleep(5)

@when('srollear hasta el centro de la pantalla5')
def step_impl(context):
    element_scroll = "//div[text()='Insumos Pendientes de Retirar']"
    scroll_to_element(context.browser, element_scroll)

@given('validar descripcion del  primer producto')
def step_impl(context):
    element_obtained = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home/div/div[4]/app-supplies-goods-indicators/div[2]/swiper/div/div[1]/div[1]/app-supplies-indicator/div/div[3]/div[1]/div[2]"
    element_expected = ["Fertilizante","Agroquimico","Balanceado", "Semillas Hibrida"]
    validate_values_text(context.browser, element_obtained,element_expected)
    time.sleep(2)

@then('validar la cantidad del primer producto')
def step_impl(context):
    selecct_element = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home/div/div[4]/app-supplies-goods-indicators/div[2]/swiper/div/div[1]/div[1]/app-supplies-indicator/div/div[3]/div[1]/div[3]"
    validate_strt(context.browser, selecct_element )
    time.sleep(2)

@then('validar el descripcion del segundo producto')
def step_impl(context):
    element_obtained = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home/div/div[4]/app-supplies-goods-indicators/div[2]/swiper/div/div[1]/div[1]/app-supplies-indicator/div/div[3]/div[2]/div[2]"
    element_expected = ["Fertilizante","Agroquimico","Balanceado", "Semillas Hibrida", "Semillas Forrajeras", "Otros"]
    validate_values_text(context.browser, element_obtained,element_expected)
    time.sleep(2)

@then('validar la cantidad del segundo producto')
def step_impl(context):
    selecct_element = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home/div/div[4]/app-supplies-goods-indicators/div[2]/swiper/div/div[1]/div[1]/app-supplies-indicator/div/div[3]/div[2]/div[3]"
    validate_strt(context.browser, selecct_element )
    time.sleep(2)


@given('validar descripcion del  primer producto remitido')
def step_impl(context):
    element_obtained = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home/div/div[4]/app-supplies-goods-indicators/div[2]/swiper/div/div[1]/div[2]/app-supplies-indicator/div/div[3]/div[1]/div[2]"
    element_expected = ["Fertilizantes","Agroquimicos","Balanceados", "Semillas Hibrida", "Semillas Forrajeras", "Otros"]
    validate_values_text(context.browser, element_obtained,element_expected)
    time.sleep(2)

@then('validar la cantidad del primer producto remitido')
def step_impl(context):
    selecct_element = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home/div/div[4]/app-supplies-goods-indicators/div[2]/swiper/div/div[1]/div[2]/app-supplies-indicator/div/div[3]/div[1]/div[3]"
    validate_strt(context.browser, selecct_element )
    time.sleep(2)

@then('validar el descripcion del segundo producto remitido')
def step_impl(context):
    element_obtained = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home/div/div[4]/app-supplies-goods-indicators/div[2]/swiper/div/div[1]/div[2]/app-supplies-indicator/div/div[3]/div[2]/div[2]"
    element_expected = ["Fertilizantes","Agroquimicos","Balanceados", "Semillas Hibrida", "Semillas Forrajeras", "Otros"]
    validate_values_text(context.browser, element_obtained,element_expected)
    time.sleep(2)

@then('validar la cantidad del segundo producto remitido')
def step_impl(context):
    selecct_element = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home/div/div[4]/app-supplies-goods-indicators/div[2]/swiper/div/div[1]/div[2]/app-supplies-indicator/div/div[3]/div[2]/div[3]"
    validate_strt(context.browser, selecct_element )
    time.sleep(2)

@given('validar descripcion del  primer producto facturada')
def step_impl(context):
    element_obtained = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home/div/div[4]/app-supplies-goods-indicators/div[2]/swiper/div/div[1]/div[3]/app-supplies-indicator/div/div[3]/div[1]/div[2]"
    element_expected = ["Fertilizante","Agroquimico","Balanceado", "Semillas Hibrida", "Semillas Forrajeras", "Otros"]
    validate_values_text(context.browser, element_obtained,element_expected)
    time.sleep(2)

@then('validar la cantidad del primer producto facturada')
def step_impl(context):
    selecct_element = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home/div/div[4]/app-supplies-goods-indicators/div[2]/swiper/div/div[1]/div[3]/app-supplies-indicator/div/div[3]/div[1]/div[3]"
    validate_strt(context.browser, selecct_element )
    time.sleep(2)

@then('validar el descripcion del segundo producto facturada')
def step_impl(context):
    element_obtained = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home/div/div[4]/app-supplies-goods-indicators/div[2]/swiper/div/div[1]/div[3]/app-supplies-indicator/div/div[3]/div[2]/div[2]"
    element_expected = ["Fertilizante","Agroquimico","Balanceado", "Semillas Hibrida", "Semillas Forrajeras", "Otros"]
    validate_values_text(context.browser, element_obtained,element_expected)
    time.sleep(2)

@then('validar la cantidad del segundo producto facturada')
def step_impl(context):
    selecct_element = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home/div/div[4]/app-supplies-goods-indicators/div[2]/swiper/div/div[1]/div[3]/app-supplies-indicator/div/div[3]/div[2]/div[3]"
    validate_strt(context.browser, selecct_element )
    time.sleep(2)