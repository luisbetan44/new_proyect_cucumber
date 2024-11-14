
import time
from behave import given, when, then
from elements import calendar_todate, displace_element, find_and_click_element, find_elements,find_send_element,search_and_displace_account, select_option_click, validate_text, validate_text_by_text
from textSteps import TextSteps
from selectores import Selectores
from loginSample import LoginSteps2
from credenciales import Credenciales  
 
startSession = TextSteps.START_SESSION
insertUsermanePassword = TextSteps.INSERT_USERNAME_AND_PASSWORD
clickOnTheButtonSession = TextSteps.CLICK_ON_THE_BUTTON_SESSION
redirrectMeToMainPage = TextSteps.REDIRRECT_ME_TO_THE_MAIN_PAGE
selectTenantWhereIwantToEnter = TextSteps.SELECT_TENANT_WHERE_I_WANT_TO_ENTER
enterTheHomePage = TextSteps.ENTER_THE_HOME_PAGE 
username = Credenciales.USERNAME_COMERCIAL_GD
password = Credenciales.PASSWORD_COMERCIAL_GD
url = Selectores.PAGE_HOME_STAGING_GD_XPAHT
menuGrain = Selectores.SELECT_MENU_GRAIN_XPAHT
submenuContract = Selectores.SELECT_SUBMENU_CONTRACT_XPAHT
textValue = Selectores.VALIDATE_TITLE_GRAIN_CONTRACT_TEXT
selectDropConfirm = Selectores.SELECT_DROPDOWN_TYPE_CONFIRM_XPAHT
selectOptionConfirm = Selectores.SELECT_OPTION_CONFIRM_XPAHT
searchAccount = Selectores.SEARCH_ACCOUNT_IN_GRAIN_CONTRACT_XPAHT
insertAccount = Selectores.INSERT_ACCOUNT_IN_GRAIN_CONTRACT_XPAHT
valueAccount =  Credenciales.JUAN_DEMO_GD
selectAccount = Selectores.SELECT_ACCOUNT_IN_GRAIN_CONTRACT_XPAHT
selectSpecies = Selectores.SELECT_DROPDOWN_SPECIES_GRAIN_CONTRACT_XPAHT
selectOptionSpecies = Selectores.SELECT_OPTION_SPECIES_GRAIN_CONTRACT_XPAHT
selectHarvest = Selectores.SELECT_DROPDOWN_HARVEST_GRAIN_CONTRACT_XPAHT
selectOptionHarvest = Selectores.SELECT_OPTION_HARVEST_GRAIN_CONTRACT_XPAHT
selectInputKilos = Selectores.SELECT_INPUT_AMOUNT_KILOS_GRAIN_CONTRACT_XPAHT
insertAmount = Selectores.INSERT_AMOUNT_KILOS
selectTypeMoney = Selectores.SELECT_DROPDOWN_TYPE_MONEY_GRAIN_CONTRACT_XPAHT
selectOptionMoney = Selectores.SELECT_OPTION_TYPE_MONEY_GRAIN_CONTRACT_XPAHT
selectInputPrice = Selectores.SELECT_INPUT_PRICE_GRAIN_CONTRACT_XPAHT
insertPrice = Selectores.INSERT_AMOUNT_PRICE
selectDropBoard = Selectores.SELECT_DROPDOWN_BOARD_GRAIN_CONTRACT_XPAHT
selectOptionBoard = Selectores.SELECT_OPTION_BOARD_GRAIN_CONTRACT_XPAHT
selectDropCodeStandard = Selectores.SELECT_DROPDOWN_CODE_STANDARD_GRAIN_CONTRACT_XPAHT
selectOptionCodeStandard = Selectores.SELECT_OPTION_CODE_STANDARD_GRAIN_CONTRACT_XPAHT
selectCalendarDatePay = Selectores.SELECT_CALENDAR_DATA_PAY_GRAIN_CONTRACT_XPAHT
selectDayCalendar = Selectores.SELECT_DAY_CALENDAR_GRAIN_CONTRACT_XPAHT
scrollElement = Selectores.SCROLLSAMPLE
scrollup = Selectores.SCROLLUP
scrollHeight = Selectores.SCROLLHEIGHT
selectDateDelivery = Selectores.SELECT_CALENDAR_DELIVERY_GRAIN_CONTRACT_XPAHT
selectArrowCalendar = Selectores.SELECT_ARROW_CALENDAR_GRAIN_CONTRACT_XPAHT
clickChevron = Selectores.CLICK_CHEVRON_ONE
selectTodateDelivery1 = Selectores.SELECT_DATE_CALENDAR_DELIVERY_ONE
selectTodateDelivery2 = Selectores.SELECT_DATE_CALENDAR_DELIVERY_TWO
selectOthersOption = Selectores.SELECT_OTHERS_OPTION_CHEVRON_GRAIN_CONTRACT_XPAHT
selectPremiums = Selectores.SELECT_PREMIUMS_GRAIN_CONTRACT_XPAHT
selectDropdowPremiums = Selectores.SELECT_DROPDOWN_PREMIUMS_GRAIN_CONTRACT_XPAHT
selectOptionPremiums = Selectores.SELECT_OPTION_PREMIUMS_GRAIN_CONTRACT_XPAHT
selectMoneyPremiums = Selectores.SELECT_MONEY_PREMIUMS_GRAIN_CONTRACT_XPAHT
insertMoneyPremiums = Selectores.INSERT_MONEY_PREMIUMS_GRAIN_CONTRACT_XPAHT
insertAmountPremiums = Selectores.INSERT_AMOUNT_VALUE_GRAIN_CONTRACT_XPAHT
add_premiums =  Selectores.ADD_PREMIUMS_GRAIN_CONTRACT_XPAHT
accept_premiums = Selectores.ACCEPT_PREMIUMS_GRAIN_CONTRACT_XPAHT
selectInputPlant =  Selectores.SELECT_PLANT_GRAIN_CONTRACT_XPAHT
selectOptionPlant = Selectores.SELECT_OPTION_PLANT_GRAIN_CONTRACT_XPAHT
selectInputOrigin = Selectores.SELECT_ORIGIN_GRAIN_CONTRACT_XPAHT
selectOptionOrigin = Selectores.SELECT_OPTION_ORIGIN_GRAIN_CONTRACT_XPAHT
selectInputDestination = Selectores.SELECT_DESTINATION_GRAIN_CONTRACT_XPAHT
selectOptionDestination = Selectores.SELECT_OPTION_DESTINATION_GRAIN_CONTRACT_XPAHT
selectDateFixationFrom = Selectores.SELECT_CALENDAR_FIXATION_FROM_GRAIN_CONTRACT_XPAHT
selectTodateFixationFrom = Selectores.SELECT_TODATE_FIXATION_FROM_GRAIN_CONTRACT_XPAHT
selectDateFixationUntil = Selectores.SELECT_CALENDAR_FIXATION_UNTIL_GRAIN_CONTRACT_XPAHT
selectTodateFixationUntil = Selectores.SELECT_TODATE_FIXATION_UNTIL_GRAIN_CONTRACT_XPAHT
selectButtonCreate = Selectores.SELECT_BUTTON_CREATE_XPAHT
selectButtonConfirm = Selectores.SELECT_BUTTON_CONFIRM
selectResponseMessege = Selectores.SELECT_RESPONSE_MESSAGE
validateTitleSuccesse = Selectores.VALIDATE_TITLE_SUCCESSE_GRAIN_CONTRACT_TEXT
selectButtonAccept = Selectores.SELECT_BUTTON_ACCEPT

 



@given(startSession)
def step_impl(context):
    login_steps = LoginSteps2(context.browser)
    login_steps.navigate_to_login_page(url)

@when(insertUsermanePassword)
def step_impl(context):
    login_steps = LoginSteps2(context.browser)
    login_steps.enter_credentials(username,password)

@when(clickOnTheButtonSession)
def step_impl(context):
    login_steps = LoginSteps2(context.browser)
    login_steps.click_login_button()

@then(redirrectMeToMainPage)
def step_impl(context):
    login_steps = LoginSteps2(context.browser)
    login_steps.verify_redirection_to_home()

@given(selectTenantWhereIwantToEnter)
def step_impl(context):
    login_steps = LoginSteps2(context.browser)
    login_steps.select_tenant()

@then(enterTheHomePage)
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

@when ("scrollear hacia principio de la pantalla")
def step_impl(context):
    driver = context.browser
    driver.execute_script(scrollup)
    time.sleep(2) 


@given ("seleccionar chevron")
def step_impl(context):
    select_others_data = selectOthersOption
    find_elements(context.browser, select_others_data)
    time.sleep(1)

@when ("seleccionar opcion prima de contrato")
def step_impl(context):
    option_premiums = selectPremiums
    find_elements(context.browser, option_premiums)
    time.sleep(1)

@when ("seleccionar tipo prima de contrato")
def step_impl(context):
    button_dopdown7 = selectDropdowPremiums
    option_desired7 = selectOptionPremiums
    select_option_click(context.browser, button_dopdown7, option_desired7 )
    time.sleep(2)


@when ("seleccionar tipo de moneda")
def step_impl(context):
    button_dopdown8 = selectMoneyPremiums
    option_desired8 = insertMoneyPremiums
    select_option_click(context.browser, button_dopdown8, option_desired8 )

@when ("ingresar importe")
def step_impl(context):
    insert_price = insertAmountPremiums
    send_price = insertPrice
    find_send_element(context.browser, insert_price, send_price )
    time.sleep(2)

@when ("agreagr prima")
def step_impl(context):
    insert_premiums = add_premiums
    find_elements(context.browser, insert_premiums)
    time.sleep(1)


@when ("aceptar ingreso de prima")
def step_impl(context):
    accept_button = accept_premiums
    find_elements(context.browser, accept_button )
    time.sleep(1)



@given("ingresar fecha de entrega")
def step_impl(context):
     select_calendar = selectDateDelivery
     displace_element(context.browser, select_calendar)
     time.sleep(2)

     select_calendar = selectTodateDelivery1
     find_elements(context.browser, select_calendar)
     time.sleep(1)

     select_arrow2 = selectArrowCalendar
     clicks = clickChevron
     find_and_click_element(context.browser, select_arrow2, clicks) 
     time.sleep(2)

     select_calendar = selectTodateDelivery2
     find_elements(context.browser, select_calendar)
     time.sleep(1)

@when ("seleccionar planta")
def step_impl(context):
    button_dopdown9 = selectInputPlant
    option_desired9 = selectOptionPlant
    select_option_click(context.browser, button_dopdown9, option_desired9 )
    time.sleep(2)

@when ("seleccionar procedencia")
def step_impl(context):
    button_dopdown10 = selectInputOrigin
    option_desired10 = selectOptionOrigin
    select_option_click(context.browser, button_dopdown10, option_desired10 )
    time.sleep(2)

@when ("seleccionar destino")
def step_impl(context):
    button_dopdown11 = selectInputDestination
    option_desired11 = selectOptionDestination
    select_option_click(context.browser, button_dopdown11, option_desired11 )
    time.sleep(2)  

@when ("seleccionar fecha de fijacion desde")
def step_impl(context):
    select_data_day2 = selectDateFixationFrom
    find_elements(context.browser, select_data_day2)
    popup_calendar2 = selectTodateFixationFrom
    find_elements(context.browser, popup_calendar2)
    time.sleep(2)

@when ("seleccionar fecha de fijacion hasta")
def step_impl(context):
    select_data_day3 = selectDateFixationUntil
    find_elements(context.browser, select_data_day3)
    popup_calendar3 = selectTodateFixationUntil
    find_elements(context.browser, popup_calendar3)
    time.sleep(2)

@when ("scrollear hasta el boton crear")
def step_impl(context):
    driver = context.browser
    driver.execute_script(scrollHeight)
    time.sleep(2) 

@when ("hacer click boton crear confirm de venta")
def step_impl(context):
    select_button_create = selectButtonCreate
    find_elements(context.browser, select_button_create)
    time.sleep(2)

@when ("hacer click boton confirmar")
def step_impl(context):
    select_button_confirm = selectButtonConfirm
    find_elements(context.browser, select_button_confirm)
    time.sleep(2)

@when ("hacer click boton aceptar la confirmacion")
def step_impl(context):
    select_finish = selectButtonAccept
    find_elements(context.browser, select_finish)
    time.sleep(5)

@then ("validar mensaje de extito")
def step_impl(context):
    element_text_2 = selectResponseMessege
    text_expected_2 = validateTitleSuccesse
    validate_text(context.browser, element_text_2, text_expected_2 )
    time.sleep(2)




     
     
     
 
 
