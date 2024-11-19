from behave import given, when, then
import time
from elements import validate_character_numeric_element,  validate_image_css_selector,  validate_text
from elements2 import validate_character_string_element
from credenciales import Credenciales
from selectores import Selectores
from textSteps import TextSteps
from loginHelper import LoginSteps3


## credenciales 
username = Credenciales.USERNAME_ADMIN_GD
password = Credenciales.PASSWORD_ADMIN_GD
account_producer = Credenciales.JUAN_DEMO_GD
account_producer = Credenciales.JUAN_DEMO_GD
deliveries_and_sales_recent = Credenciales.DELIVERIES_AND_SALES_RECENT
deliveries_recent_title = Credenciales.DELIVERIES__RECENT_TITLE
title_column_product_deliveries = Credenciales.TITLE_COLUMN_PRODUCT_DELIVERIES
value_ctgcrt = Credenciales.VALUE_TITLE_COLUMN_CTGCRT
value_kgnetos = Credenciales.VALUE_TITLE_COLUMN_KGNETOS
sales_recent_title = Credenciales.SALES__RECENT_TITLE
value_title_price = Credenciales.VALUE_TITLE_COLUMN_PRICE

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
scroll_page = TextSteps.SCROLLEAR_PAGE_DELVERIES_HOME
validate_title_page =  TextSteps.VALIDATE_TITLE_PEGE_DELIVERIES_HOME
validate_title_module = TextSteps.VALIDATEE_TITLE_MODULE_DELIVERIES_HOME
validate_title_page_product = TextSteps.VALIDATE_TITLE_PAGE_PRODCUT_DELIVERIES_HOME
velidate_img_product = TextSteps.VALIDATE_IMG_PRUDUCT_DELIVERIES_HOME  
validate_harvest = TextSteps.VALIDATE_HARVEST_DELIVERIES_HOME
validate_date = TextSteps.VALIDATE_DATE_DELIVERIES_HOME
validate_title_ctgcrt = TextSteps.VALIDATE_CTGCRT_DELIVERIES_HOME
get_value_ctgcrt = TextSteps.GET_VELUE_CTGCRT_DELIVERIES_HOME
get_value_kgnetos = TextSteps.GET_VALUE_KG_NETOS_DELIVERIES_HOME
validate_title_module_sales = TextSteps.VALIDATE_TITLE__MODULE_SALES_HOME 
validate_title_page_product_sales = TextSteps.VALIDATE_TITLE_PAGE_PRODCUT_SALES_HOME
validate_img_pruduct_sales = TextSteps.VALIDATE_IMG_PRUDUCT_SALES_HOME 
validate_harvest_sales =TextSteps.VALIDATE_HARVEST_SALES_HOME
validate_date_sales = TextSteps.VALIDATE_DATE_SALES_HOME 
validate_title_kgnetos_sales = TextSteps.VALIDATE_TITLE_KG_NETOS_SALES_HOME
validate_title_kgnetos = TextSteps.VALIDATE_TITLE_KG_NETOS_DELIVERIES_HOME
get_kgnetos_sales = TextSteps.GET_VALUE_KG_NETOS_SALES_HOME 
validate_title_price_sales = TextSteps.VALDATE_TITLE_PRICE_SALES_HOME 
get_price_sales = TextSteps.GET_VALUE_PRICE_SALES_HOME

## Selectores 

url = Selectores.PAGE_HOME_STAGING_GD_XPAHT
scroll_half_page = Selectores.SROLLE_HALF_PAGE
select_title_page_deliveries_home_xpaht = Selectores.SELECT_TITLE_PEGE_DELIVERIES_HOME_XPAHT
select_title_module_xpaht = Selectores.SELECT_TITLE_MODULE_DELIVERIES_HOME_XPAHT
select_title_page_product_deliveries_home_xpaht = Selectores.SELECT_TITLE_PEGE_PRODUCT_DELIVERIES_HOME_XPAHT
select_img_product_deliveries_home_selectores = Selectores.SELECT_IMG_PRODUCT_DELIVERIES_HOME_SELECTOR
img_grain_wheat = Selectores.IMG_GRAIN_WHEAT
img_grain_corn =Selectores.IMG_GRAIN_CORN
img_grain_soy = Selectores.IMG_GRAIN_SOY
img_grain_sunflower = Selectores.IMG_GRAIN_SUNFLOWER 
select_harvest_deliveries_home_xpaht = Selectores.SELECT_HARVEST_DELIVERIES_HOME_XPAHT  
select_value_date_deliveries_home_xpaht = Selectores.SELECT_VALUE_DATE_DELIVERIES_HOME_XPAHT  
select_value_title_ctgcrt_deliveries_home_xpaht = Selectores.SELECT_TITLE_CTGCRT_DELIVERIES_HOME_XPAH
select_value_ctgcrt_deliveries_home_xpaht = Selectores.SELECT_VALUE_CTGCRT_DELIVERIES_HOME_XPAH 
select_value_title_kgnetos_deliveries_home_xpaht = Selectores.SELECT_VALUE_TITLE_KGNETOS_DELIVERIES_HOME_XPAHT
select_value_kgnetos_deliveries_home_xpaht = Selectores.SELECT_VALUE_KGNETOS_DELIVERIES_HOME_XPAHT
select_title_module_sales_xpaht = Selectores.SELECT_TITLE_MODULE_SALES_HOME_XPAHT 
select_title_page_sales_home_xpaht = Selectores.SELECT_TITLE_PEGE_PRODUCT_SALES_HOME_XPAHT 
select_img_product_sales_home_selectores = Selectores.SELECT_IMG_PRODUCT_SALES_HOME_SELECTOR 
select_harvest_sales_home_xpaht = Selectores.SELECT_HARVEST_SALES_HOME_XPAHT 
select_value_date_sales_home_xpaht = Selectores.SELECT_VALUE_DATE_SALES_HOME_XPAHT 
select_value_title_kgnetos_sales_home_xpaht = Selectores.SELECT_VALUE_TITLE_KGNETOS_SALES_HOME_XPAHT 
select_value_kgnetos_sales_home_xpaht = Selectores.SELECT_VALUE_KGNETOS_SALES_HOME_XPAHT
select_value_title_price_sales_home_xpaht = Selectores.SELECT_VALUE_TITLE_PRICE_SALES_HOME_XPAHT
select_value_price_sales_home_xpaht = Selectores.SELECT_VALUE_PRICE_SALES_HOME_XPAHT 





   




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

@given(scroll_page)
def step_impl(context):
    context.browser.execute_script(scroll_half_page)
    time.sleep(2)


## validar entregas

@then(validate_title_page)
def step_impl(context):
    titlle_value1 = select_title_page_deliveries_home_xpaht
    value_expected1 = deliveries_and_sales_recent
    validate_text(context.browser,titlle_value1, value_expected1)

@then(validate_title_module)
def step_impl(context):
    titlle_value2 = select_title_module_xpaht
    value_expected2 = deliveries_recent_title
    validate_text(context.browser, titlle_value2, value_expected2 )

@then(validate_title_page_product)
def step_impl(context):
    titlle_value3 = select_title_page_product_deliveries_home_xpaht
    value_expected3 = title_column_product_deliveries
    validate_text(context.browser,titlle_value3,value_expected3 )


@then(velidate_img_product)
def step_impl(context):
    image_1 = select_img_product_deliveries_home_selectores
    image_1_expected = [
           img_grain_wheat,
           img_grain_corn,
           img_grain_soy,
           img_grain_soy
        ]
    validate_image_css_selector(context.browser, image_1, image_1_expected)

@then(validate_harvest)
def step_impl(context):
    element1 = select_harvest_deliveries_home_xpaht
    validate_character_string_element(context.browser, element1  )

@then(validate_date)
def step_impl(context):
    element2 = select_value_date_deliveries_home_xpaht
    validate_character_numeric_element(context.browser, element2  )
    time.sleep(2)

@then(validate_title_ctgcrt)
def step_impl(context):
    titlle_value4 = select_value_title_ctgcrt_deliveries_home_xpaht
    value_expected4 = value_ctgcrt
    validate_text(context.browser, titlle_value4, value_expected4)

@then(get_value_ctgcrt)
def step_impl(context):
    element3 = select_value_ctgcrt_deliveries_home_xpaht
    validate_character_numeric_element(context.browser, element3  )
    time.sleep(2)

@then(validate_title_kgnetos)
def step_impl(context):
    titlle_value5 = select_value_title_kgnetos_deliveries_home_xpaht
    value_expected5 = value_kgnetos
    validate_text(context.browser, titlle_value5, value_expected5)


@then(get_value_kgnetos)
def step_impl(context):
    element4 = select_value_kgnetos_deliveries_home_xpaht
    validate_character_numeric_element(context.browser, element4  )



## validar ventas 

@given(validate_title_module_sales)
def step_impl(context):
    titlle_value6 = select_title_module_sales_xpaht
    value_expected6 = sales_recent_title
    validate_text(context.browser, titlle_value6, value_expected6)

@then(validate_title_page_product_sales)
def step_impl(context):
    titlle_value7 = select_title_page_sales_home_xpaht
    value_expected7 = title_column_product_deliveries
    validate_text(context.browser, titlle_value7, value_expected7)


@then(validate_img_pruduct_sales)
def step_impl(context):
    image_2 = select_img_product_sales_home_selectores
    image_2_expected = [
           img_grain_wheat,
           img_grain_corn,
           img_grain_soy,
           img_grain_soy
        ]
    validate_image_css_selector(context.browser, image_2, image_2_expected)
    

@then(validate_harvest_sales)
def step_impl(context):
    element5 = select_harvest_sales_home_xpaht
    validate_character_string_element(context.browser, element5  )
    time.sleep(2)


@then(validate_date_sales)
def step_impl(context):
    element6 = select_value_date_sales_home_xpaht
    validate_character_numeric_element(context.browser, element6  )

    
@then(validate_title_kgnetos_sales)
def step_impl(context):
    titlle_value8 = select_value_title_kgnetos_sales_home_xpaht
    value_expected8 = value_kgnetos
    validate_text(context.browser, titlle_value8, value_expected8)
    

@then(get_kgnetos_sales)
def step_impl(context):
    element7 = select_value_kgnetos_sales_home_xpaht
    validate_character_numeric_element(context.browser, element7  )
    

@then(validate_title_price_sales)
def step_impl(context):
    titlle_value9 = select_value_title_price_sales_home_xpaht
    value_expected9 = value_title_price
    validate_text(context.browser, titlle_value9, value_expected9)

@then(get_price_sales)
def step_impl(context):
    element8 = select_value_price_sales_home_xpaht 
    validate_character_string_element(context.browser, element8  )



    

