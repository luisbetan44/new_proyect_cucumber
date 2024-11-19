
from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from elements import validate_character_numeric_element,validate_image_xpaht, validate_values_text
from credenciales import Credenciales
from loginHelper import LoginSteps3
from textSteps import TextSteps
from selectores import Selectores

## credenciales 
username = Credenciales.USERNAME_ADMIN_GD
password = Credenciales.PASSWORD_ADMIN_GD
account_producer = Credenciales.JUAN_DEMO_GD
account_producer = Credenciales.JUAN_DEMO_GD

## pasos 
star_sesion =  TextSteps.HELPER_START_SESSION
isert_user_pass = TextSteps.HELPER_INSERT_USERNAME_AND_PASSWORD
click_button = TextSteps.HELPER_CLICK_ON_THE_BUTTON_SESSION
redireccion_pege = TextSteps.HELPER_REDIRRECT_ME_TO_THE_MAIN_PAGE
select_tenant = TextSteps.HELPER_SELECT_TENANT_WHERE_I_WANT_TO_ENTER
enter_home_page = TextSteps.HELPER_ENTER_THE_HOME_PAGE
select_global_search = TextSteps.HELPER_SELECT_GLOBAL_SEARCH
insert_account = TextSteps.HELPER_INSERT_ACCOUNT_SEARCH
click_option = TextSteps.HELPER_CLICK_OPTION_ACCOUNT


## Selectores 

url = Selectores.PAGE_HOME_STAGING_GD_XPAHT
scroll_half_page = Selectores.SROLLE_HALF_PAGE


@given(star_sesion)
def step_impl(context):
    login_steps = LoginSteps3(context.browser)
    login_steps.navigate_to_login_page(url)

@when(isert_user_pass)
def step_impl(context):
    login_steps = LoginSteps3(context.browser)
    login_steps.enter_credentials(username, password)

@when(click_button)
def step_impl(context):
    login_steps = LoginSteps3(context.browser)
    login_steps.click_login_button()

@then(redireccion_pege)
def step_impl(context):
    login_steps = LoginSteps3(context.browser)
    login_steps.verify_redirection_to_home()

@given(select_tenant)
def step_impl(context):
    login_steps = LoginSteps3(context.browser)
    login_steps.select_tenant()

@then(enter_home_page)
def step_impl(context):
    login_steps = LoginSteps3(context.browser)
    login_steps.verify_redirection_to_inicio()

@given(select_global_search)
def step_impl(context):
    login_steps = LoginSteps3(context.browser)
    login_steps.click_global_search()

@when(insert_account)
def step_impl(context):
    login_steps = LoginSteps3(context.browser)
    login_steps.enter_account_number(account_producer)

@when(click_option)
def step_impl(context):
    login_steps = LoginSteps3(context.browser)
    login_steps.click_suggested_option()
    time.sleep(5)




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

def after_scenario(context, scenario):
  if context.browser:
        print("Cerrando el navegador")
        context.browser.quit()
