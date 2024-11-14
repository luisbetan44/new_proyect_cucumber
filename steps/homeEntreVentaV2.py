from behave import given, when, then
import time
from elements import validate_character_numeric_element,  validate_image_css_selector,  validate_text
from elements2 import validate_character_string_element
from selectores import Selectores
from textSteps import TextSteps
from loginHelper import LoginSteps3



star_sesion =  TextSteps.HELPER_START_SESSION
url = Selectores.PAGE_HOME_STAGING_GD_XPAHT
isert_user_pass = TextSteps.HELPER_INSERT_USERNAME_AND_PASSWORD
click_button = TextSteps.HELPER_CLICK_ON_THE_BUTTON_SESSION
redireccion_pege = TextSteps.HELPER_REDIRRECT_ME_TO_THE_MAIN_PAGE
select_tenant = TextSteps.HELPER_SELECT_TENANT_WHERE_I_WANT_TO_ENTER
enter_home_page = TextSteps.HELPER_ENTER_THE_HOME_PAGE
select_global_search = TextSteps.HELPER_SELECT_GLOBAL_SEARCH
insert_account = TextSteps.HELPER_INSERT_ACCOUNT_SEARCH
click_option = TextSteps.HELPER_CLICK_OPTION_ACCOUNT
scroll_page = TextSteps.SCROLLEAR_PAGE_DELVERIES_HOME
validate_title_page =  TextSteps.VALIDATE_TITLE_PEGE_DELIVERIES_HOME  
validate_title_module = TextSteps.VALIDATEE_TITLE_MODULE_DELIVERIES_HOME  
validate_title_page_product = TextSteps.VALIDATE_TITLE_PAGE_PRODCUT_DELIVERIES_HOME 
velidate_img_product = TextSteps.VALIDATE_IMG_PRUDUCT_DELIVERIES_HOME  
validate_harvest = TextSteps.VALIDATE_HARVEST_DELIVERIES_HOME  
validate_date = TextSteps.VALIDATE_DATE_DELIVERIES_HOME  
validate_title_ctgcrt = TextSteps.VALIDATE_CTGCRT_DELIVERIES_HOME 
get_value_ctgcrt = TextSteps.GET_VELUE_CTGCRT_DELIVERIES_HOME 
validate_title_kgnetos = TextSteps.VALIDATE_TITLE_KG_NETOS_DELIVERIES_HOME 
get_value_kgnetos = TextSteps.GET_VALUE_KG_NETOS_DELIVERIES_HOME
validate_title_module_sales = TextSteps.VALIDATE_TITLE__MODULE_SALES_HOME 
validate_title_page_product_sales = TextSteps.VALIDATE_TITLE_PAGE_PRODCUT_SALES_HOME 
validate_img_pruduct_sales = TextSteps.VALIDATE_IMG_PRUDUCT_SALES_HOME 
validate_harvest_sales =TextSteps.VALIDATE_HARVEST_SALES_HOME
validate_date_sales = TextSteps.VALIDATE_DATE_SALES_HOME 
validate_title_kgnetos_sales = TextSteps.VALIDATE_TITLE_KG_NETOS_SALES_HOME
get_kgnetos_sales = TextSteps.GET_VALUE_KG_NETOS_SALES_HOME 
validate_title_price_sales = TextSteps.VALDATE_TITLE_PRICE_SALES_HOME 
get_price_sales = TextSteps.GET_VALUE_PRICE_SALES_HOME
scroll_half_page = Selectores.SROLLE_HALF_PAGE
validate_title_page_deliveries_home_xpaht = Selectores.VALIDATE_TITLE_PEGE_DELIVERIES_HOME_XPAHT
   




@given(star_sesion)
def step_impl(context):
    login_steps = LoginSteps3(context.browser)
    login_steps.navigate_to_login_page(url)

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

@given(scroll_page)
def step_impl(context):
    context.browser.execute_script(scroll_half_page)
    time.sleep(2)


## validar entregas

@then(validate_title_page)
def step_impl(context):
    titlle_value1 = validate_title_page_deliveries_home_xpaht
    value_expected1= "Entregas y Ventas Recientes"
    validate_text(context.browser,titlle_value1, value_expected1)

@then(validate_title_module)
def step_impl(context):
    titlle_value2 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home-switch/app-home-v2/div/div[3]/app-recent-grain-movements/div[2]/div[1]/app-recent-deliveries/app-responsive-table-multiple-items/div/div/span[1]"
    value_expected2 = "Entregas Recientes"
    validate_text(context.browser, titlle_value2, value_expected2 )

@then(validate_title_page_product)
def step_impl(context):
    titlle_value3 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home-switch/app-home-v2/div/div[3]/app-recent-grain-movements/div[2]/div[1]/app-recent-deliveries/app-responsive-table-multiple-items/div/table/thead/tr/th[1]"
    value_expected3 = "Producto"
    validate_text(context.browser,titlle_value3,value_expected3 )


@then(velidate_img_product)
def step_impl(context):
    image_1 = "#layout-wrapper > div > div > div > app-home-switch > app-home-v2 > div > div:nth-child(4) > app-recent-grain-movements > div:nth-child(2) > div:nth-child(1) > app-recent-deliveries > app-responsive-table-multiple-items > div > table > tbody > tr:nth-child(1) > td:nth-child(1) > div > div > div.me-2 > img"
    image_1_expected = [
           "https://pwa-portal-staging.silohub.ag/assets/images/grains/trigo.svg",
           "https://pwa-portal-staging.silohub.ag/assets/images/grains/maiz.svg",
           "https://pwa-portal-staging.silohub.ag/assets/images/grains/girasol.svg",
           "https://pwa-portal-staging.silohub.ag/assets/images/grains/soja.svg"
        ]
    validate_image_css_selector(context.browser, image_1, image_1_expected)

@then(validate_harvest)
def step_impl(context):
    element1 = '/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home-switch/app-home-v2/div/div[3]/app-recent-grain-movements/div[2]/div[1]/app-recent-deliveries/app-responsive-table-multiple-items/div/table/tbody/tr[1]/td[1]/div/div/div[2]/div[1]/span'
    validate_character_string_element(context.browser, element1  )

@then(validate_date)
def step_impl(context):
    element2 = '/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home-switch/app-home-v2/div/div[3]/app-recent-grain-movements/div[2]/div[1]/app-recent-deliveries/app-responsive-table-multiple-items/div/table/tbody/tr[1]/td[1]/div/div/div[2]/div[2]/span'
    validate_character_numeric_element(context.browser, element2  )
    time.sleep(2)

@then(validate_title_ctgcrt)
def step_impl(context):
    titlle_value4 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home-switch/app-home-v2/div/div[3]/app-recent-grain-movements/div[2]/div[1]/app-recent-deliveries/app-responsive-table-multiple-items/div/table/thead/tr/th[2]"
    value_expected4 = "CTG/CRT"
    validate_text(context.browser, titlle_value4, value_expected4)

@then(get_value_ctgcrt)
def step_impl(context):
    element3 = '/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home-switch/app-home-v2/div/div[3]/app-recent-grain-movements/div[2]/div[1]/app-recent-deliveries/app-responsive-table-multiple-items/div/table/tbody/tr[1]/td[2]/div/div/span'
    validate_character_numeric_element(context.browser, element3  )
    time.sleep(2)

@then(validate_title_kgnetos)
def step_impl(context):
    titlle_value5 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home-switch/app-home-v2/div/div[3]/app-recent-grain-movements/div[2]/div[1]/app-recent-deliveries/app-responsive-table-multiple-items/div/table/thead/tr/th[3]"
    value_expected5 = "Kg Netos"
    validate_text(context.browser, titlle_value5, value_expected5)


@then(get_value_kgnetos)
def step_impl(context):
    element4 = '/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home-switch/app-home-v2/div/div[3]/app-recent-grain-movements/div[2]/div[1]/app-recent-deliveries/app-responsive-table-multiple-items/div/table/tbody/tr[1]/td[3]/div/div/span'
    validate_character_numeric_element(context.browser, element4  )



## validar ventas 

@given(validate_title_module_sales)
def step_impl(context):
    titlle_value6 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home-switch/app-home-v2/div/div[3]/app-recent-grain-movements/div[2]/div[2]/app-recent-sales/app-responsive-table-multiple-items/div/div/span[1]"
    value_expected6 = "Ventas Recientes"
    validate_text(context.browser, titlle_value6, value_expected6)

@then(validate_title_page_product_sales)
def step_impl(context):
    titlle_value7 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home-switch/app-home-v2/div/div[3]/app-recent-grain-movements/div[2]/div[2]/app-recent-sales/app-responsive-table-multiple-items/div/table/thead/tr/th[1]"
    value_expected7 = "Producto"
    validate_text(context.browser, titlle_value7, value_expected7)


@then(validate_img_pruduct_sales)
def step_impl(context):
    image_2 = "#layout-wrapper > div > div > div > app-home-switch > app-home-v2 > div > div:nth-child(4) > app-recent-grain-movements > div:nth-child(2) > div:nth-child(2) > app-recent-sales > app-responsive-table-multiple-items > div > table > tbody > tr:nth-child(1) > td:nth-child(1) > div > div > div.me-2 > img"
    image_2_expected = [
           "https://pwa-portal-staging.silohub.ag/assets/images/grains/trigo.svg",
           "https://pwa-portal-staging.silohub.ag/assets/images/grains/maiz.svg",
           "https://pwa-portal-staging.silohub.ag/assets/images/grains/girasol.svg",
           "https://pwa-portal-staging.silohub.ag/assets/images/grains/soja.svg"
        ]
    validate_image_css_selector(context.browser, image_2, image_2_expected)
    

@then(validate_harvest_sales)
def step_impl(context):
    element5 = '/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home-switch/app-home-v2/div/div[3]/app-recent-grain-movements/div[2]/div[2]/app-recent-sales/app-responsive-table-multiple-items/div/table/tbody/tr[1]/td[1]/div/div/div[2]/div[1]/span'
    validate_character_string_element(context.browser, element5  )
    time.sleep(2)


@then(validate_date_sales)
def step_impl(context):
    element6 = '/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home-switch/app-home-v2/div/div[3]/app-recent-grain-movements/div[2]/div[2]/app-recent-sales/app-responsive-table-multiple-items/div/table/tbody/tr[1]/td[1]/div/div/div[2]/div[2]/span'
    validate_character_numeric_element(context.browser, element6  )

    
@then(validate_title_kgnetos_sales)
def step_impl(context):
    titlle_value8 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home-switch/app-home-v2/div/div[3]/app-recent-grain-movements/div[2]/div[2]/app-recent-sales/app-responsive-table-multiple-items/div/table/thead/tr/th[2]"
    value_expected8 = "Kg Netos"
    validate_text(context.browser, titlle_value8, value_expected8)
    

@then(get_kgnetos_sales)
def step_impl(context):
    element7 = '/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home-switch/app-home-v2/div/div[3]/app-recent-grain-movements/div[2]/div[2]/app-recent-sales/app-responsive-table-multiple-items/div/table/tbody/tr[1]/td[2]/div/div/span'
    validate_character_numeric_element(context.browser, element7  )
    

@then(validate_title_price_sales)
def step_impl(context):
    titlle_value9 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home-switch/app-home-v2/div/div[3]/app-recent-grain-movements/div[2]/div[2]/app-recent-sales/app-responsive-table-multiple-items/div/table/thead/tr/th[3]"
    value_expected9 = "Precio"
    validate_text(context.browser, titlle_value9, value_expected9)

@then(get_price_sales)
def step_impl(context):
    element8 = '/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-home-switch/app-home-v2/div/div[3]/app-recent-grain-movements/div[2]/div[2]/app-recent-sales/app-responsive-table-multiple-items/div/table/tbody/tr[1]/td[3]/div/div/span[1]'
    validate_character_string_element(context.browser, element8  )



    

