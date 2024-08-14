from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from elements import calendar_todate, calendar_todate_retro,find_elements,find_send_element, search_and_displace_account,select_option_click, validate_text,validate_text_by_text
from features.selecctores import INSERT_ACCOUNT_IN_GRAIN_CONTRACT_XPAHT, INSERT_AMOUNT_KILOS, INSERT_AMOUNT_PRICE, JUAN_DEMO, PAGE_HOME_STAGING_GD_XPAHT, PASSWORD_COMERCIAL,SCROLLHEIGHT, SCROLLUP, SEARCH_ACCOUNT_IN_GRAIN_CONTRACT_XPAHT, SELECT_ACCOUNT_IN_GRAIN_CONTRACT_XPAHT, SELECT_ARROW_NEXT_CALENDAR_DATA_DELIVERY_GRAIN_CONTRACT_SELECCTOR, SELECT_BUTTON_ACCEPT_GRAIN_CONTRACT_XPAHT, SELECT_BUTTON_CONFIRM_GRAIN_CONTRACT_XPAHT, SELECT_BUTTON_CONTINUE_GRAIN_CONTRACT_XPAHT, SELECT_CALENDAR_DATA_DELIVERY_GRAIN_CONTRACT_XPAHT, SELECT_DATA_CALENDAR_GRAIN_CONTRACT_XPAHT, SELECT_DATA_DAY_DELIVERY_GRAIN_CONTRACT_XPAHT, SELECT_DATA_FROM_FIXATION_GRAIN_CONTRACT_XPAHT, SELECT_DATA_UNTIL_FIXATION_GRAIN_CONTRACT_XPAHT, SELECT_DROPDOWN_BOARD_GRAIN_CONTRACT_XPAHT, SELECT_DROPDOWN_DESTINATION_GRAIN_CONTRACT_XPAHT, SELECT_DROPDOWN_HARVEST_GRAIN_CONTRACT_XPAHT, SELECT_DROPDOWN_MONEY_GRAIN_CONTRACT_XPAHT, SELECT_DROPDOWN_ORIGIN_GRAIN_CONTRACT_XPAHT, SELECT_DROPDOWN_PLANT_GRAIN_CONTRACT_XPAHT, SELECT_DROPDOWN_SPECIES_GRAIN_CONTRACT_XPAHT, SELECT_DROPDOWN_STANDARD_CODE_GRAIN_CONTRACT_XPAHT, SELECT_DROPDOWN_TYPE_CONFIRM_XPAHT, SELECT_INPUT_AMOUNT_KILOS_GRAIN_CONTRACT_XPAHT, SELECT_INPUT_AMOUNT_PRICE_GRAIN_CONTRACT_XPAHT, SELECT_MENU_GRAIN_XPAHT, SELECT_OPTION_BOARD_GRAIN_CONTRACT_XPAHT, SELECT_OPTION_CONFIRM_XPAHT, SELECT_OPTION_DATA_DAY_GRAIN_CONTRACT_XPAHT, SELECT_OPTION_DESTINATION_GRAIN_CONTRACT_XPAHT, SELECT_OPTION_HARVEST_GRAIN_CONTRACT_XPAHT, SELECT_OPTION_MONEY_GRAIN_CONTRACT_XPAHT, SELECT_OPTION_ORIGIN_GRAIN_CONTRACT_XPAHT, SELECT_OPTION_PLANT_GRAIN_CONTRACT_XPAHT, SELECT_OPTION_SPECIES_GRAIN_CONTRACT_XPAHT, SELECT_OPTION_STANDARD_CODE_GRAIN_CONTRACT_XPAHT,  SELECT_SUBMENU_CONTRACT_XPAHT, USERNAME_COMERCIAL, VALIDATE_RESPONSE_GRAIN_CONTRACT_TEXT, VALIDATE_TITLE_GRAIN_CONTRACT_TEXT, VALUE_TEXT_RESPONSE_GRAIN_CONTRACT_XPAHT
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
    select_grain = SELECT_MENU_GRAIN_XPAHT
    find_elements(context.browser,select_grain)
    time.sleep(2)

@when ('ingreso al submenu de contratos')
def step_impl(context):
    select_confir_sales = SELECT_SUBMENU_CONTRACT_XPAHT
    find_elements(context.browser,select_confir_sales)
    time.sleep(2)

@then ('validar titulo de pagina')
def step_impl(context):
    text_expected = VALIDATE_TITLE_GRAIN_CONTRACT_TEXT
    validate_text_by_text(context.browser, text_expected)

@given ('seleccionar tipo de confirmacion de venta')
def step_impl(context):
    button_dopdown = SELECT_DROPDOWN_TYPE_CONFIRM_XPAHT
    option_desired = SELECT_OPTION_CONFIRM_XPAHT
    select_option_click(context.browser, button_dopdown, option_desired)
    time.sleep(2)

@when ('ingresar la cuenta del productor')
def step_impl(context):
    located_element = SEARCH_ACCOUNT_IN_GRAIN_CONTRACT_XPAHT
    select_input = INSERT_ACCOUNT_IN_GRAIN_CONTRACT_XPAHT
    account_number = JUAN_DEMO
    search_and_displace_account(context.browser, account_number, select_input, located_element )

@when ('seleccionar cuenta del productor')
def step_impl(context):
    select_account = SELECT_ACCOUNT_IN_GRAIN_CONTRACT_XPAHT
    find_elements(context.browser,select_account)
    time.sleep(2)

@when ('seleccionar especie')
def step_impl(context):
    button_dopdown2 = SELECT_DROPDOWN_SPECIES_GRAIN_CONTRACT_XPAHT
    option_desired2 = SELECT_OPTION_SPECIES_GRAIN_CONTRACT_XPAHT
    select_option_click(context.browser, button_dopdown2, option_desired2, )

@when ('seleccionar cosecha')
def step_impl(context):
    button_dopdown3 = SELECT_DROPDOWN_HARVEST_GRAIN_CONTRACT_XPAHT
    option_desired3 = SELECT_OPTION_HARVEST_GRAIN_CONTRACT_XPAHT 
    select_option_click(context.browser, button_dopdown3, option_desired3, )

@when ('ingresar cantidad de kilos')
def step_impl(context):
    insert_amount = SELECT_INPUT_AMOUNT_KILOS_GRAIN_CONTRACT_XPAHT
    send_amount = INSERT_AMOUNT_KILOS
    find_send_element(context.browser,insert_amount,send_amount )

@when ('seleccionar moneda')
def step_impl(context):
    button_dopdown4 = SELECT_DROPDOWN_MONEY_GRAIN_CONTRACT_XPAHT
    option_desired4 =  SELECT_OPTION_MONEY_GRAIN_CONTRACT_XPAHT
    select_option_click(context.browser, button_dopdown4, option_desired4, ) 

@when ('ingresar precio') 
def step_impl(context):
    insert_price = SELECT_INPUT_AMOUNT_PRICE_GRAIN_CONTRACT_XPAHT
    send_price = INSERT_AMOUNT_PRICE
    find_send_element(context.browser, insert_price, send_price )
    time.sleep(3)

@when ('scrollear en la pantalla')
def step_impl(context):
    context.browser.execute_script(SCROLLHEIGHT)

@when ('seleccionar pizarra') 
def step_impl(context):
    button_dopdown4 = SELECT_DROPDOWN_BOARD_GRAIN_CONTRACT_XPAHT
    option_desired4 = SELECT_OPTION_BOARD_GRAIN_CONTRACT_XPAHT
    select_option_click(context.browser, button_dopdown4, option_desired4  )

@when ('seleccionar codigo estandar')
def step_impl(context):
    button_dopdown5 = SELECT_DROPDOWN_STANDARD_CODE_GRAIN_CONTRACT_XPAHT
    option_desired5 = SELECT_OPTION_STANDARD_CODE_GRAIN_CONTRACT_XPAHT
    select_option_click(context.browser, button_dopdown5, option_desired5 )


@then ('seleccionar fecha de pago')
def step_impl(context):
    select_calendar = SELECT_DATA_CALENDAR_GRAIN_CONTRACT_XPAHT
    select_data_day = SELECT_OPTION_DATA_DAY_GRAIN_CONTRACT_XPAHT
    calendar_todate(context.browser, select_data_day, select_calendar)


@when('scrollear hacia arriba de la pantalla')
def step_impl(context):
    context.browser.execute_script(SCROLLUP)



@when ('seleccionar fecha de entrega')
def step_impl(context):
    select_calendar = SELECT_CALENDAR_DATA_DELIVERY_GRAIN_CONTRACT_XPAHT
    popup_xpath = SELECT_DATA_DAY_DELIVERY_GRAIN_CONTRACT_XPAHT
    select_chevron = SELECT_ARROW_NEXT_CALENDAR_DATA_DELIVERY_GRAIN_CONTRACT_SELECCTOR
    popup_xpath2 = SELECT_DATA_DAY_DELIVERY_GRAIN_CONTRACT_XPAHT
    click_chevron = 6
    calendar_todate_retro(context.browser, select_calendar, popup_xpath, select_chevron, popup_xpath2, clicks=click_chevron)
    time.sleep(2)



@when ('seleccionar planta')
def step_impl(context):
    button_dopdown6 = SELECT_DROPDOWN_PLANT_GRAIN_CONTRACT_XPAHT
    option_desired6 = SELECT_OPTION_PLANT_GRAIN_CONTRACT_XPAHT
    select_option_click(context.browser, button_dopdown6, option_desired6 )



@when ('seleccionar procedencia')
def step_impl(context):
    button_dopdown7 = SELECT_DROPDOWN_ORIGIN_GRAIN_CONTRACT_XPAHT
    option_desired7 = SELECT_OPTION_ORIGIN_GRAIN_CONTRACT_XPAHT
    select_option_click(context.browser, button_dopdown7, option_desired7 )

@when ('seleccionar destino')
def step_impl(context):
    button_dopdown8 = SELECT_DROPDOWN_DESTINATION_GRAIN_CONTRACT_XPAHT
    option_desired8 = SELECT_OPTION_DESTINATION_GRAIN_CONTRACT_XPAHT
    select_option_click(context.browser, button_dopdown8, option_desired8 )

@when ('seleccionar fecha de fijacion desde')
def step_impl(context):
    select_calendar = SELECT_DATA_FROM_FIXATION_GRAIN_CONTRACT_XPAHT
    select_data_day = SELECT_OPTION_DATA_DAY_GRAIN_CONTRACT_XPAHT
    calendar_todate(context.browser, select_data_day, select_calendar)
    

@when ('seleccionar fecha de fijacion hasta')
def step_impl(context):
    select_calendar = SELECT_DATA_UNTIL_FIXATION_GRAIN_CONTRACT_XPAHT
    select_data_day = SELECT_OPTION_DATA_DAY_GRAIN_CONTRACT_XPAHT
    calendar_todate(context.browser, select_data_day, select_calendar)
   
@given ('seleccionar boton crear')
def step_impl(context):
    select_button_continue = SELECT_BUTTON_CONTINUE_GRAIN_CONTRACT_XPAHT
    find_elements(context.browser, select_button_continue)
    time.sleep(2)
    
@when ('seleccionar boton confirmar')
def step_impl(context):
    select_button_confirm = SELECT_BUTTON_CONFIRM_GRAIN_CONTRACT_XPAHT
    find_elements(context.browser, select_button_confirm)
    time.sleep(2)

@then ('validar mensaje de finalizacion')
def step_impl(context):  
    element_text = VALUE_TEXT_RESPONSE_GRAIN_CONTRACT_XPAHT 
    text_expected = VALIDATE_RESPONSE_GRAIN_CONTRACT_TEXT
    validate_text(context.browser, element_text, text_expected )
    time.sleep(2) 


@when('seleccionar boton aceptar')
def step_impl(context):
    select_finish = SELECT_BUTTON_ACCEPT_GRAIN_CONTRACT_XPAHT
    find_elements(context.browser, select_finish)
    time.sleep(3)


    


