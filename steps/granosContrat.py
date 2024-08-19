
import time
from behave import given, when, then
from elements import calendar_todate, calendar_todate_retro, find_elements, find_send_element,search_and_displace_account, select_option_click, validate_text_by_text
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
selectSpecies = Selecctores.SELECT_DROPDOWN_SPECIES_GRAIN_CONTRACT_XPAHT
selectOptionSpecies = Selecctores.SELECT_OPTION_SPECIES_GRAIN_CONTRACT_XPAHT
selectHarvest = Selecctores.SELECT_DROPDOWN_HARVEST_GRAIN_CONTRACT_XPAHT
selectOptionHarvest = Selecctores.SELECT_OPTION_HARVEST_GRAIN_CONTRACT_XPAHT
selectInputKilos = Selecctores.SELECT_INPUT_AMOUNT_KILOS_GRAIN_CONTRACT_XPAHT
insertAmount = Selecctores.INSERT_AMOUNT_KILOS
selectTypeMoney = Selecctores.SELECT_DROPDOWN_TYPE_MONEY_GRAIN_CONTRACT_XPAHT
selectOptionMoney = Selecctores.SELECT_OPTION_TYPE_MONEY_GRAIN_CONTRACT_XPAHT
selectInputPrice = Selecctores.SELECT_INPUT_PRICE_GRAIN_CONTRACT_XPAHT
insertPrice = Selecctores.INSERT_AMOUNT_PRICE
selectDropBoard = Selecctores.SELECT_DROPDOWN_BOARD_GRAIN_CONTRACT_XPAHT
selectOptionBoard = Selecctores.SELECT_OPTION_BOARD_GRAIN_CONTRACT_XPAHT
selectDropCodeStandard = Selecctores.SELECT_DROPDOWN_CODE_STANDARD_GRAIN_CONTRACT_XPAHT
selectOptionCodeStandard = Selecctores.SELECT_OPTION_CODE_STANDARD_GRAIN_CONTRACT_XPAHT
selectCalendarDatePay = Selecctores.SELECT_CALENDAR_DATA_PAY_GRAIN_CONTRACT_XPAHT
selectDayCalendar = Selecctores.SELECT_DAY_CALENDAR_GRAIN_CONTRACT_XPAHT
scrollElement = Selecctores.SCROLLSAMPLE
scrollup = Selecctores.SCROLLUP
selectDateDelivery = Selecctores.SELECT_CALENDAR_DELIVERY_GRAIN_CONTRACT_XPAHT
selectArrowCalendar = Selecctores.SELECT_ARROW_CALENDAR_GRAIN_CONTRACT_XPAHT
clickChevron = Selecctores.CLICK_CHEVRON_ONE
selectTodateDelivery = Selecctores.SELECT_DATE_CALENDAR_DELIVERY

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
    time.sleep(4)

@when ("seleccionar la especie")
def step_impl(context):
    button_dopdown2 = selectSpecies
    option_desired2 = selectOptionSpecies
    select_option_click(context.browser, button_dopdown2, option_desired2, )
    time.sleep(2)

@when ("seleccionar cosecha")
def step_impl(context):
    button_dopdown3 = selectHarvest
    option_desired3 = selectOptionHarvest
    select_option_click(context.browser, button_dopdown3, option_desired3, )
    time.sleep(2)

@when ("ingresar cantidad")
def step_impl(context):
    select_input_amount = selectInputKilos
    send_amount = insertAmount 
    find_send_element(context.browser,select_input_amount,send_amount )
    time.sleep(2)

@when ("seleccionar modena")
def step_impl(context):
     button_dopdown4 = selectTypeMoney
     option_desired4 = selectOptionMoney
     select_option_click(context.browser, button_dopdown4, option_desired4, )
     time.sleep(2)

@when("scrollear la pantalla")
def step_impl(context):
    driver = context.browser
    driver.execute_script(scrollElement)


@when("ingresar precio")
def step_impl(context):
    insert_price = selectInputPrice
    send_price = insertPrice
    find_send_element(context.browser, insert_price, send_price )
    time.sleep(2)

@when ("seleccionar pizarra")
def step_impl(context):
     button_dopdown5 = selectDropBoard
     option_desired5 = selectOptionBoard
     select_option_click(context.browser, button_dopdown5, option_desired5  )
     time.sleep(2)
        

@when ("seleccionar codigo standar")
def step_impl(context):
    button_dopdown6 = selectDropCodeStandard
    option_desired6 = selectOptionCodeStandard
    select_option_click(context.browser, button_dopdown6, option_desired6 )
    time.sleep(2)

@when ("seleccionar fecha de pago")
def step_impl(context):
     select_data_day = selectCalendarDatePay
     popup_calendar1 = selectDayCalendar
     calendar_todate(context.browser, select_data_day, popup_calendar1)
     time.sleep(2)

@given ("scrollear hacia principio de la pantalla")
def step_impl(context):
    driver = context.browser
    driver.execute_script(scrollup) 

@when("ingresar fecha de entrega")
def step_impl(context):
    select_calendar = selectDateDelivery
    popup_xpath = selectTodateDelivery
    select_chevron = selectArrowCalendar
    popup_xpath2 = selectTodateDelivery
    click_chevron = clickChevron
    calendar_todate_retro(context.browser, select_calendar, popup_xpath, select_chevron, popup_xpath2, clicks=click_chevron)
    time.sleep(2)


 
 
