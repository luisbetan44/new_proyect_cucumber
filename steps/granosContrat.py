
import time
from behave import given, when, then
from elements import find_elements, search_and_displace_account, select_option_click, validate_text_by_text
from selecctores import Selecctores
from loginSample import LoginSteps2
from credenciales import Credenciales   

username = Credenciales.USERNAME_COMERCIAL_GD
password = Credenciales.PASSWORD_COMERCIAL_GD
url = Selecctores.PAGE_HOME_STAGING_GD_XPAHT
menuGrain = Selecctores.SELECT_MENU_GRAIN_XPAHT
submenuContract = Selecctores.SELECT_SUBMENU_CONTRACT_XPAHT
textValue = Selecctores.VALIDATE_TITLE_GRAIN_CONTRACT_TEXT
selectDropConfirm = Selecctores.SELECT_DROPDOWN_TYPE_CONFIRM_XPAHT
selectOptionConfirm = Selecctores.SELECT_OPTION_CONFIRM_XPAHT
searchAccount = Selecctores.SEARCH_ACCOUNT_IN_GRAIN_CONTRACT_XPAHT
insertAccount = Selecctores.INSERT_ACCOUNT_IN_GRAIN_CONTRACT_XPAHT
valueAccount =  Credenciales.JUAN_DEMO_GD
selectAccount = Selecctores.SELECT_ACCOUNT_IN_GRAIN_CONTRACT_XPAHT

@given('estoy en la pagina de inicio de sesion8')
def step_impl(context):
    login_steps = LoginSteps2(context.browser)
    login_steps.navigate_to_login_page(url)

@when('ingreso mi nombre de usuario y credenciales correctas8')
def step_impl(context):
    login_steps = LoginSteps2(context.browser)
    login_steps.enter_credentials(username,password)

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
    time.sleep(2)

@given ("seleccionar menu de granos")
def step_impl(context):
    select_grain = menuGrain
    find_elements(context.browser,select_grain)
    time.sleep(2)


@when ("seleccionar submenu de contratos")
def step_impl(context):
    select_confir_sales = submenuContract
    find_elements(context.browser,select_confir_sales)
    time.sleep(2)


@then ("velidar titulo de la pagina")
def step_impl(context):
    text_expected = textValue
    validate_text_by_text(context.browser, text_expected)

@given ('seleccionar tipo de confirmacion')
def step_impl(context):
    button_dopdown = selectDropConfirm
    option_desired = selectOptionConfirm
    select_option_click(context.browser, button_dopdown, option_desired)
    time.sleep(2)

@when ('ingresar cuenta productor')
def step_impl(context):
    located_element = searchAccount
    select_input = insertAccount
    account_number = valueAccount
    search_and_displace_account(context.browser, account_number, select_input, located_element )

@when ('seleccionar cuenta productor')
def step_impl(context):
    select_account = selectAccount
    find_elements(context.browser,select_account)
    time.sleep(2)





 
 
