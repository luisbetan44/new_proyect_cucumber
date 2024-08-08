from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from elements import delete_element, displace_element, find_elements, find_elements_id, find_send_element, search_and_displace_account, search_and_select_option, select_option_click, send_element, validate_text,validate_text_by_text
from elements2 import verify_todate
from features.credenciales import JUAN_DEMO, PASSWORD_COMERCIAL, USERNAME_COMERCIAL
from features.selecctores import INSERT_ACCOUNT_IN_GRAIN_CONTRACT, PAGE_HOME_STAGING_GD_XPAHT, SEARCH_ACCOUNT_IN_GRAIN_CONTRACT, SELECT_ACCOUNT_IN_GRAIN_CONTRACT, SELECT_DROPDOWN_TYPE_CONFIRM, SELECT_MENU_GRAIN, SELECT_OPTION_CONFIRM, SELECT_SUBMENU_CONTRACT, VALIDATE_TITLE_GRAIN_CONTRACT
from loginSample import LoginSteps2





@given('estoy en la pagina de inicio de sesion8')
def step_impl(context):
    login_steps = LoginSteps2(context.browser)
    login_steps.navigate_to_login_page(PAGE_HOME_STAGING_GD_XPAHT)

@when('ingreso mi nombre de usuario y credenciales correctas8')
def step_impl(context):
    login_steps = LoginSteps2(context.browser)
    login_steps.enter_credentials(USERNAME_COMERCIAL, PASSWORD_COMERCIAL)

@when('hago clic en el boton de inicio de sesion8')
def step_impl(context):
    login_steps = LoginSteps2(context.browser)
    login_steps.click_login_button()

@then('deberia ser redirigido a la pagina principal8')
def step_impl(context):
    login_steps = LoginSteps2(context.browser)
    login_steps.verify_redirection_to_home()

@given('selecciono el tenant donde quiero ingresar8')
def step_impl(context):
    login_steps = LoginSteps2(context.browser)
    login_steps.select_tenant()

@then('ingreso a la pagina de inicio8')
def step_impl(context):
    login_steps = LoginSteps2(context.browser)
    login_steps.verify_redirection_to_inicio()
 
@given( 'ingreso al menu de granos')
def step_impl(context):
    select_grain = SELECT_MENU_GRAIN
    find_elements(context.browser,select_grain)
    time.sleep(2)

@when ('ingreso al submenu de contratos')
def step_impl(context):
    select_confir_sales = SELECT_SUBMENU_CONTRACT
    find_elements(context.browser,select_confir_sales)
    time.sleep(2)

@then ('validar titulo de pagina')
def step_impl(context):
    text_expected = VALIDATE_TITLE_GRAIN_CONTRACT
    validate_text_by_text(context.browser, text_expected)

@given ('seleccionar tipo de confirmacion de venta')
def step_impl(context):
    button_dopdown = SELECT_DROPDOWN_TYPE_CONFIRM
    option_desired = SELECT_OPTION_CONFIRM
    select_option_click(context.browser, button_dopdown, option_desired)
    time.sleep(2)

@when ('ingresar la cuenta del productor')
def step_impl(context):
    located_element = SEARCH_ACCOUNT_IN_GRAIN_CONTRACT
    select_input = INSERT_ACCOUNT_IN_GRAIN_CONTRACT
    account_number = JUAN_DEMO
    search_and_displace_account(context.browser, account_number, select_input, located_element )

@when ('seleccionar cuenta del productor')
def step_impl(context):
    select_account = SELECT_ACCOUNT_IN_GRAIN_CONTRACT
    find_elements(context.browser,select_account)
    time.sleep(2)

