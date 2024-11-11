from behave import given, when, then
import time
from elements import validate_character_numeric_element,  validate_image_css_selector,  validate_text
from elements2 import validate_character_string_element
from textSteps import TextSteps
from loginHelper import LoginSteps3



star_sesion =  TextSteps.HELPER_START_SESSION
isert_user_pass = TextSteps.HELPER_INSERT_USERNAME_AND_PASSWORD
click_button = TextSteps.HELPER_CLICK_ON_THE_BUTTON_SESSION
redireccion_pege = TextSteps.HELPER_REDIRRECT_ME_TO_THE_MAIN_PAGE
select_tenant = TextSteps.HELPER_SELECT_TENANT_WHERE_I_WANT_TO_ENTER
enter_home_page = TextSteps.HELPER_ENTER_THE_HOME_PAGE
select_global_search = TextSteps.HELPER_SELECT_GLOBAL_SEARCH
insert_account = TextSteps.HELPER_INSERT_ACCOUNT_SEARCH
click_option = TextSteps.HELPER_CLICK_OPTION_ACCOUNT




@given(star_sesion)
def step_impl(context):
    login_steps = LoginSteps3(context.browser)
    login_steps.navigate_to_login_page("https://pwa-portal-staging.silohub.ag/login")

@when(isert_user_pass)
def step_impl(context):
    login_steps = LoginSteps3(context.browser)
    login_steps.enter_credentials("admingd@silohub.ag", "G@viglio123")

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
    login_steps.enter_account_number("1023")

@when(click_option)
def step_impl(context):
    login_steps = LoginSteps3(context.browser)
    login_steps.click_suggested_option()
    time.sleep(5)

@given('scrollear pantalla')
def step_impl(context):
    context.browser.execute_script("window.scrollTo(0, 1000);")
    time.sleep(2)


## validar entregas

@then('validar titulo de pantalla2')
def step_impl(context):
    titlle_value1 = '/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home-switch/app-home-v2/div/div[3]/app-recent-grain-movements/div[1]/p'
    value_expected1= "Entregas y Ventas Recientes"
    validate_text(context.browser,titlle_value1, value_expected1)

@then('validar titulo del modulo2')
def step_impl(context):
    titlle_value2 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home-switch/app-home-v2/div/div[3]/app-recent-grain-movements/div[2]/div[1]/app-recent-deliveries/app-responsive-table-multiple-items/div/div/span[1]"
    value_expected2 = "Entregas Recientes"
    validate_text(context.browser, titlle_value2, value_expected2 )

@then('validar titulo de pagina de productos2')
def step_impl(context):
    titlle_value3 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home-switch/app-home-v2/div/div[3]/app-recent-grain-movements/div[2]/div[1]/app-recent-deliveries/app-responsive-table-multiple-items/div/table/thead/tr/th[1]"
    value_expected3 = "Producto"
    validate_text(context.browser,titlle_value3,value_expected3 )


@then('Validar imagen del producto2')
def step_impl(context):
    image_1 = "#layout-wrapper > div > div > div > app-home-switch > app-home-v2 > div > div:nth-child(4) > app-recent-grain-movements > div:nth-child(2) > div:nth-child(1) > app-recent-deliveries > app-responsive-table-multiple-items > div > table > tbody > tr:nth-child(1) > td:nth-child(1) > div > div > div.me-2 > img"
    image_1_expected = [
           "https://pwa-portal-staging.silohub.ag/assets/images/grains/trigo.svg",
           "https://pwa-portal-staging.silohub.ag/assets/images/grains/maiz.svg",
           "https://pwa-portal-staging.silohub.ag/assets/images/grains/girasol.svg",
           "https://pwa-portal-staging.silohub.ag/assets/images/grains/soja.svg"
        ]
    validate_image_css_selector(context.browser, image_1, image_1_expected)

@then('validar cosecha2')
def step_impl(context):
    element1 = '/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home-switch/app-home-v2/div/div[3]/app-recent-grain-movements/div[2]/div[1]/app-recent-deliveries/app-responsive-table-multiple-items/div/table/tbody/tr[1]/td[1]/div/div/div[2]/div[1]/span'
    validate_character_string_element(context.browser, element1  )

@then('validar fecha2')
def step_impl(context):
    element2 = '/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home-switch/app-home-v2/div/div[3]/app-recent-grain-movements/div[2]/div[1]/app-recent-deliveries/app-responsive-table-multiple-items/div/table/tbody/tr[1]/td[1]/div/div/div[2]/div[2]/span'
    validate_character_numeric_element(context.browser, element2  )
    time.sleep(2)

@then('validar titulo CTG/CRT2')
def step_impl(context):
    titlle_value4 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home-switch/app-home-v2/div/div[3]/app-recent-grain-movements/div[2]/div[1]/app-recent-deliveries/app-responsive-table-multiple-items/div/table/thead/tr/th[2]"
    value_expected4 = "CTG/CRT"
    validate_text(context.browser, titlle_value4, value_expected4)

@then('obtener valor CTG/CRT2')
def step_impl(context):
    element3 = '/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home-switch/app-home-v2/div/div[3]/app-recent-grain-movements/div[2]/div[1]/app-recent-deliveries/app-responsive-table-multiple-items/div/table/tbody/tr[1]/td[2]/div/div/span'
    validate_character_numeric_element(context.browser, element3  )
    time.sleep(2)

@then('validar titulo Kg Netos2')
def step_impl(context):
    titlle_value5 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home-switch/app-home-v2/div/div[3]/app-recent-grain-movements/div[2]/div[1]/app-recent-deliveries/app-responsive-table-multiple-items/div/table/thead/tr/th[3]"
    value_expected5 = "Kg Netos"
    validate_text(context.browser, titlle_value5, value_expected5)


@then('obtener valor Kg Netos2')
def step_impl(context):
    element4 = '/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home-switch/app-home-v2/div/div[3]/app-recent-grain-movements/div[2]/div[1]/app-recent-deliveries/app-responsive-table-multiple-items/div/table/tbody/tr[1]/td[3]/div/div/span'
    validate_character_numeric_element(context.browser, element4  )



## validar ventas 

@given('validar titulo del modulo3')
def step_impl(context):
    titlle_value6 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home-switch/app-home-v2/div/div[3]/app-recent-grain-movements/div[2]/div[2]/app-recent-sales/app-responsive-table-multiple-items/div/div/span[1]"
    value_expected6 = "Ventas Recientes"
    validate_text(context.browser, titlle_value6, value_expected6)

@then('validar titulo de pagina de productos3')
def step_impl(context):
    titlle_value7 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home-switch/app-home-v2/div/div[3]/app-recent-grain-movements/div[2]/div[2]/app-recent-sales/app-responsive-table-multiple-items/div/table/thead/tr/th[1]"
    value_expected7 = "Producto"
    validate_text(context.browser, titlle_value7, value_expected7)


@then('Validar imagen del producto3')
def step_impl(context):
    image_2 = "#layout-wrapper > div > div > div > app-home-switch > app-home-v2 > div > div:nth-child(4) > app-recent-grain-movements > div:nth-child(2) > div:nth-child(2) > app-recent-sales > app-responsive-table-multiple-items > div > table > tbody > tr:nth-child(1) > td:nth-child(1) > div > div > div.me-2 > img"
    image_2_expected = [
           "https://pwa-portal-staging.silohub.ag/assets/images/grains/trigo.svg",
           "https://pwa-portal-staging.silohub.ag/assets/images/grains/maiz.svg",
           "https://pwa-portal-staging.silohub.ag/assets/images/grains/girasol.svg",
           "https://pwa-portal-staging.silohub.ag/assets/images/grains/soja.svg"
        ]
    validate_image_css_selector(context.browser, image_2, image_2_expected)
    

@then(' validar cosecha3')
def step_impl(context):
    element5 = '/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home-switch/app-home-v2/div/div[3]/app-recent-grain-movements/div[2]/div[2]/app-recent-sales/app-responsive-table-multiple-items/div/table/tbody/tr[1]/td[1]/div/div/div[2]/div[1]/span'
    validate_character_string_element(context.browser, element5  )
    time.sleep(2)


@then('validar fecha3')
def step_impl(context):
    element6 = '/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home-switch/app-home-v2/div/div[3]/app-recent-grain-movements/div[2]/div[2]/app-recent-sales/app-responsive-table-multiple-items/div/table/tbody/tr[1]/td[1]/div/div/div[2]/div[2]/span'
    validate_character_numeric_element(context.browser, element6  )

    
@then('validar titulo Kg Netos3')
def step_impl(context):
    titlle_value8 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home-switch/app-home-v2/div/div[3]/app-recent-grain-movements/div[2]/div[2]/app-recent-sales/app-responsive-table-multiple-items/div/table/thead/tr/th[2]"
    value_expected8 = "Kg Netos"
    validate_text(context.browser, titlle_value8, value_expected8)
    

@then('obtener valor Kg Netos3')
def step_impl(context):
    element7 = '/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home-switch/app-home-v2/div/div[3]/app-recent-grain-movements/div[2]/div[2]/app-recent-sales/app-responsive-table-multiple-items/div/table/tbody/tr[1]/td[2]/div/div/span'
    validate_character_numeric_element(context.browser, element7  )
    

@then('validar titulo precio3')
def step_impl(context):
    titlle_value9 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home-switch/app-home-v2/div/div[3]/app-recent-grain-movements/div[2]/div[2]/app-recent-sales/app-responsive-table-multiple-items/div/table/thead/tr/th[3]"
    value_expected9 = "Precio"
    validate_text(context.browser, titlle_value9, value_expected9)

@then(' obtener precio3')
def step_impl(context):
    element8 = '/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home-switch/app-home-v2/div/div[3]/app-recent-grain-movements/div[2]/div[2]/app-recent-sales/app-responsive-table-multiple-items/div/table/tbody/tr[1]/td[3]/div/div/span[1]'
    validate_character_string_element(context.browser, element8  )


@then('obtener valor final3')
def step_impl(context):
    element9 = '/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home-switch/app-home-v2/div/div[3]/app-recent-grain-movements/div[2]/div[2]/app-recent-sales/app-responsive-table-multiple-items/div/table/tbody/tr[1]/td[3]/div/div/span[2]'
    validate_character_numeric_element(context.browser, element9  )

    

