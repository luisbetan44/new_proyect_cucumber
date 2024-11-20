
from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from elements import find_elements, validate_character_numeric_element,validate_image_xpaht, validate_text, validate_values_text
from credenciales import Credenciales

from textSteps import TextSteps
from selectores import Selectores

## credenciales 
username = Credenciales.USERNAME_ADMIN_GD
password = Credenciales.PASSWORD_ADMIN_GD
account_producer = Credenciales.JUAN_DEMO_GD
account_producer = Credenciales.JUAN_DEMO_GD
value_title_modal_summary_business = Credenciales.VALUE_TITLE_MODAL_SUMMARY_BUSINESS
value_title_column_deliveries = Credenciales.VALUE_TITLE_COLUMN_DELIVERIES
value_title_column_pending = Credenciales.VALUE_TITLE_COLUMN_PENDING
value_title_column_fixed = Credenciales.VALUE_TITLE_COLUMN_FIXED
value_title_column_weighed = Credenciales.VALUE_TITLE_COLUMN_WEIGHED
value_title_column_liquidated = Credenciales.VALUE_TITLE_COLUMN_LIQUIDATED
value_title_column_paid = Credenciales.VALUE_TITLE_COLUMN_PAID
grain_soy = Credenciales.GRAIN_SOY

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
select_button_filter_campaign = TextSteps.SELECT_BUTTON_FILTER_CAMPAIGN_SUMMARY_BUSINESS_HOME
clean_filter_campaign = TextSteps.CLEAN_FILTER_CAMPAIGN_SUMMARY_BUSINESS_HOME
select_harvest_filter = TextSteps.SELECT_HARVEST_SUMMARY_BUSINESS_HOME
select_button_accept_filter = TextSteps.SELECT_BUTTON_ACCEPT_SUMMARY_BUSINESS_HOME
validate_title_summary_business_home = TextSteps.VALIDATE_TITLE_SUMMARY_BUSINESS_HOME
validate_img_product_summary_business_home = TextSteps.VALIDATE_IMG_PRODUCT_SUMMARY_BUSINESS_HOME
validate_description_product_summary_business_home = TextSteps.VALIDATE_DESCRIPTION_PRODUCT_SUMMARY_BUSINESS_HOME
validate_balance_available_summary_business_home = TextSteps.VALIDATE_BALANCE_AVAILABLE_SUMMARY_BUSINESS_HOME
validate_title_delivery_summary_business_home = TextSteps.VALIDATE_TITLE_DELIVERY_SUMMARY_BUSINESS_HOME
validate_amount_delivery_summary_business_home = TextSteps.VALIDATE_AMOUNT_DELIVERY_SUMMARY_BUSINESS_HOME
validate_title_pending_delivery_summary_business_home = TextSteps.VALIDATE_TITLE_PENDING_DELIVERY_SUMMARY_BUSINESS_HOME
validate_amount_pending_delivery_summary_business_home = TextSteps.VALIDATE_AMOUNT_PENDING_DELIVERY_SUMMARY_BUSINESS_HOME
validate_title_fixed_summary_business_home = TextSteps.VALIDATE_TITLE_FIXED_SUMMARY_BUSINESS_HOME
validate_amount_fixed_summary_business_home = TextSteps.VALIDATE_AMOUNT_FIXED_SUMMARY_BUSINESS_HOME
validate_title_pending_fixed_summary_business_home = TextSteps.VALIDATE_TITLE__PENDING_FIXED_SUMMARY_BUSINESS_HOME
validate_amount_pending_fixed_summary_business_home = TextSteps.VALIDATE_AMOUNT_PENDING_FIXED_SUMMARY_BUSINESS_HOME
validate_title_weighed_summary_business_home = TextSteps.VALIDATE_TITLE_WEIGHED_SUMMARY_BUSINESS_HOME
validate_amount_weighed_summary_business_home = TextSteps.VALIDATE_AMOUNT_WEIGHED_SUMMARY_BUSINESS_HOME
validate_title_pending_weighed_summary_business_home = TextSteps.VALIDATE_TITLE__PENDING_WEIGHED_SUMMARY_BUSINESS_HOME
validate_amount_pending_weighed_summary_business_home = TextSteps.VALIDATE_AMOUNT_PENDING_WEIGHED_SUMMARY_BUSINESS_HOME
validate_title_liquidated_summary_business_home = TextSteps.VALIDATE_TITLE_LIQUIDATED_SUMMARY_BUSINESS_HOME
validate_amount_liquidated_summary_business_home = TextSteps.VALIDATE_AMOUNT_LIQUIDATED_SUMMARY_BUSINESS_HOME
validate_title_pending_liquidated_summary_business_home = TextSteps.VALIDATE_TITLE__PENDING_LIQUIDATED_SUMMARY_BUSINESS_HOME
validate_amount_pending_liquidated_summary_business_home = TextSteps.VALIDATE_AMOUNT_PENDING_LIQUIDATED_SUMMARY_BUSINESS_HOME
validate_title_paid_summary_business_home = TextSteps.VALIDATE_TITLE_PAID_SUMMARY_BUSINESS_HOME
validate_amount_paid_summary_business_home = TextSteps.VALIDATE_AMOUNT_PAID_SUMMARY_BUSINESS_HOME
validate_title_pending_paid_summary_business_home = TextSteps.VALIDATE_TITLE_PENDING__PAID_SUMMARY_BUSINESS_HOME
validate_amount_pending_paid_summary_business_home = TextSteps.VALIDATE_AMOUNT_PENDING__PAID_SUMMARY_BUSINESS_HOME



## Selectores 

url = Selectores.PAGE_HOME_STAGING_GD_XPAHT
scroll_half_page = Selectores.SROLLE_HALF_PAGE
select_button_filter_campaign_xpaht = Selectores.SELECT_BUTTON_FILTER_CAMPAIGN_SUMMARY_BUSINESS_HOME_XPAHT
select_button_clean_filter_xpaht = Selectores.SELECT_BUTTON_CLEAN_FILTER_CAMPAIGN_SUMMARY_BUSINESS_HOME_XPAHT
select_harvest_xpaht = Selectores.SELECT_HARVEST_SUMMARY_BUSINESS_HOME_XPAHT
select_button_accept_filter_xpaht = Selectores.SELECT_BUTTON_ACCEPT_SUMMARY_BUSINESS_HOME_XPAHT
select_value_title_summary_business_home_xpaht = Selectores.SELECT_VALUE_TITLE_SUMMARY_BUSINESS_HOME_XPAHT
select_img_product_summary_business_home_xpaht = Selectores.SELECT_IMG_PRODUCT_SUMMARY_BUSINESS_HOME_XPAHT
img_grain_wheat =Selectores.IMG_GRAIN_WHEAT 
img_grain_corn = Selectores.IMG_GRAIN_CORN 
img_grain_soy = Selectores.IMG_GRAIN_SOY 
img_grain_sunflower = Selectores.IMG_GRAIN_SUNFLOWER
select_value_description_product_summary_business_home_xpaht = Selectores.SELECT_VALUE_DESCRIPTION_PRODUCT_SUMMARY_BUSINESS_HOME_XPAHT
select_value_balance_available_summary_business_home_xpaht = Selectores.SELECT_VALUE_BALANCE_AVAILABLE_SUMMARY_BUSINESS_HOME_XPAHT
select_value_title_delivery_summary_business_home_xpaht = Selectores.SELECT_VALUE_TITLE_DELIVERY_SUMMARY_BUSINESS_HOME_XPAHT
select_value_amount_delivery_summary_business_home_xpaht = Selectores.SELECT_VALUE_AMOUNT_DELIVERY_SUMMARY_BUSINESS_HOME_XPAHT
select_value_title_pending_delivery_summary_business_home_xpaht = Selectores.SELECT_VALUE_TITLE_PENDING_DELIVERY_SUMMARY_BUSINESS_HOME_XPAHT
select_value_amount_pending_delivery_summary_business_home_xpaht = Selectores.SELECT_VALUE_AMOUNT_PENDING_DELIVERY_SUMMARY_BUSINESS_HOME_XPAHT
select_value_title_fixed_summary_business_home_xpaht = Selectores.SELECT_VALUE_TITLE_FIXED_SUMMARY_BUSINESS_HOME_XPAHT
select_value_amount_fixed_summary_business_home_xpaht = Selectores.SELECT_VALUE_AMOUNT_FIXED_SUMMARY_BUSINESS_HOME_XPAHT
select_value_title_pending_fixed_summary_business_home_xpaht = Selectores.SELECT_VALUE_TITLE__PENDING_FIXED_SUMMARY_BUSINESS_HOME_XPAHT
select_value_amount_pending_fixed_summary_business_home_xpaht = Selectores.SELECT_VALUE_AMOUNT_PENDING_FIXED_SUMMARY_BUSINESS_HOME_XPAHT
select_value_title_weighed_summary_business_home_xpaht = Selectores.SELECT_VALUE_TITLE_WEIGHED_SUMMARY_BUSINESS_HOME_XPAHT
select_value_amount_weighed_summary_business_home_xpaht = Selectores.SELECT_VALUE_AMOUNT_WEIGHED_SUMMARY_BUSINESS_HOME_XPAHT
select_value_title_pending_weighed_summary_business_home_xpaht = Selectores.SELECT_VALUE_TITLE__PENDING_WEIGHED_SUMMARY_BUSINESS_HOME_XPAHT
select_value_amount_pending_weighed_summary_business_home_xpaht = Selectores.SELECT_VALUE_AMOUNT_PENDING_WEIGHED_SUMMARY_BUSINESS_HOME_XPAHT
select_value_title_liquidated_summary_business_home_xpaht = Selectores.SELECT_VALUE_TITLE_LIQUIDATED_SUMMARY_BUSINESS_HOME_XPAHT
select_value_amount_liquidated_summary_business_home_xpaht = Selectores.SELECT_VALUE_AMOUNT_LIQUIDATED_SUMMARY_BUSINESS_HOME_XPAHT
select_value_title_pending_liquidated_summary_business_home_xpaht = Selectores.SELECT_VALUE_TITLE__PENDING_LIQUIDATED_SUMMARY_BUSINESS_HOME_XPAHT
select_value_amount_pending_liquidated_summary_business_home_xpaht = Selectores.SELECT_VALUE_AMOUNT_PENDING_LIQUIDATED_SUMMARY_BUSINESS_HOME_XPAHT
select_value_title_paid_summary_business_home_xpaht = Selectores.SELECT_VALUE_TITLE_PAID_SUMMARY_BUSINESS_HOME_XPAHT
select_value_amount_paid_summary_business_home_xpaht = Selectores.SELECT_VALUE_AMOUNT_PAID_SUMMARY_BUSINESS_HOME_XPAHT
select_value_title_pending_paid_summary_business_home_xpaht = Selectores.SELECT_VALUE_TITLE_PENDING__PAID_SUMMARY_BUSINESS_HOME_XPAHT
select_value_amount_pending_paid_summary_business_home_xpaht = Selectores.SELECT_VALUE_AMOUNT_PENDING__PAID_SUMMARY_BUSINESS_HOME_XPAHT





@given(select_button_filter_campaign)
def step_impl(context):
    Filter_campaign = select_button_filter_campaign_xpaht
    find_elements(context.browser, Filter_campaign)
    time.sleep(1)
   

@when(clean_filter_campaign)
def step_impl(context):
    delete_campaign = select_button_clean_filter_xpaht
    find_elements(context.browser, delete_campaign)
    time.sleep(2)

@when(select_harvest_filter)
def step_impl(context):
    select_campaign = select_harvest_xpaht
    find_elements(context.browser, select_campaign)

@when(select_button_accept_filter)
def step_impl(context):
    selecct_button_aplicar = select_button_accept_filter_xpaht
    find_elements(context.browser, selecct_button_aplicar)
    time.sleep(6)

@then(validate_title_summary_business_home)
def step_impl(context):
  title_expected = select_value_title_summary_business_home_xpaht
  title_obtained = value_title_modal_summary_business
  validate_text(context.browser, title_expected,title_obtained)

@then(validate_img_product_summary_business_home)
def step_impl(context):
   image_1 = select_img_product_summary_business_home_xpaht
   image_1_expected = [ img_grain_wheat, 
                        img_grain_corn, 
                        img_grain_soy, 
                        img_grain_sunflower 
            ] 
   validate_image_xpaht(context.browser, image_1, image_1_expected)


@then(validate_description_product_summary_business_home )
def step_impl(context):
    titlle_value1 = select_value_description_product_summary_business_home_xpaht
    value_expected1 = grain_soy
    validate_text(context.browser, titlle_value1, value_expected1)

@then(validate_balance_available_summary_business_home)
def step_impl(context):
     element1 = select_value_balance_available_summary_business_home_xpaht
     validate_character_numeric_element(context.browser, element1  )




@then(validate_title_delivery_summary_business_home)
def step_impl(context):
    titlle_value2 = select_value_title_delivery_summary_business_home_xpaht
    value_expected2 = value_title_column_deliveries
    validate_text(context.browser, titlle_value2, value_expected2)

@then(validate_amount_delivery_summary_business_home)
def step_impl(context):    
    element2 = select_value_amount_delivery_summary_business_home_xpaht
    validate_character_numeric_element(context.browser, element2  )

@then(validate_title_pending_delivery_summary_business_home)
def step_impl(context):
    titlle_value3 = select_value_title_pending_delivery_summary_business_home_xpaht
    value_expected3 =value_title_column_pending
    validate_text(context.browser, titlle_value3, value_expected3)

@then(validate_amount_pending_delivery_summary_business_home)
def step_impl(context):    
    element3 = select_value_amount_pending_delivery_summary_business_home_xpaht
    validate_character_numeric_element(context.browser, element3  )

       
@then(validate_title_fixed_summary_business_home)
def step_impl(context):       
    titlle_value4 = select_value_title_fixed_summary_business_home_xpaht
    value_expected4 =value_title_column_fixed
    validate_text(context.browser, titlle_value4, value_expected4)
   
        
@then(validate_amount_fixed_summary_business_home)
def step_impl(context):
    element4 = select_value_amount_fixed_summary_business_home_xpaht
    validate_character_numeric_element(context.browser, element4  )

@then(validate_title_pending_fixed_summary_business_home)
def step_impl(context):    
    titlle_value5 = select_value_title_pending_fixed_summary_business_home_xpaht
    value_expected5 = value_title_column_pending
    validate_text(context.browser, titlle_value5, value_expected5)


@then(validate_amount_pending_fixed_summary_business_home)
def step_impl(context):
    element5 = select_value_amount_pending_fixed_summary_business_home_xpaht
    validate_character_numeric_element(context.browser, element5  )
     
@then(validate_title_weighed_summary_business_home)
def step_impl(context):        
    titlle_value6 = select_value_title_weighed_summary_business_home_xpaht
    value_expected6 = value_title_column_weighed
    validate_text(context.browser, titlle_value6, value_expected6)
        
@then(validate_amount_weighed_summary_business_home)
def step_impl(context): 
    element6 = select_value_amount_weighed_summary_business_home_xpaht
    validate_character_numeric_element(context.browser, element6  )
        
@then(validate_title_pending_weighed_summary_business_home)
def step_impl(context):       
    titlle_value7 = select_value_title_pending_weighed_summary_business_home_xpaht
    value_expected7 = value_title_column_pending
    validate_text(context.browser, titlle_value7, value_expected7)

        
@then(validate_amount_pending_weighed_summary_business_home)
def step_impl(context):        
    element7 = select_value_amount_pending_weighed_summary_business_home_xpaht
    validate_character_numeric_element(context.browser, element7  )

@then(validate_title_liquidated_summary_business_home)
def step_impl(context):        
    titlle_value8 = select_value_title_liquidated_summary_business_home_xpaht
    value_expected8 = value_title_column_liquidated
    validate_text(context.browser, titlle_value8, value_expected8)


@then(validate_amount_liquidated_summary_business_home)
def step_impl(context):   
    element8 = select_value_amount_liquidated_summary_business_home_xpaht
    validate_character_numeric_element(context.browser, element8  )


@then(validate_title_pending_liquidated_summary_business_home)
def step_impl(context):
    titlle_value9 = select_value_title_pending_liquidated_summary_business_home_xpaht
    value_expected9 = value_title_column_pending
    validate_text(context.browser, titlle_value9, value_expected9)


@then(validate_amount_pending_liquidated_summary_business_home)
def step_impl(context):
    element9 = select_value_amount_pending_liquidated_summary_business_home_xpaht
    validate_character_numeric_element(context.browser, element9  )

@then(validate_title_paid_summary_business_home)
def step_impl(context):        
    titlle_value10 = select_value_title_paid_summary_business_home_xpaht
    value_expected10 = value_title_column_paid
    validate_text(context.browser, titlle_value10, value_expected10)
   
@then(validate_amount_paid_summary_business_home)
def step_impl(context):
    element10 = select_value_amount_paid_summary_business_home_xpaht
    validate_character_numeric_element(context.browser, element10  )

        
@then(validate_title_pending_paid_summary_business_home)
def step_impl(context):
    titlle_value11 = select_value_title_pending_paid_summary_business_home_xpaht
    value_expected11 = value_title_column_pending
    validate_text(context.browser, titlle_value11, value_expected11)
   
@then(validate_amount_pending_paid_summary_business_home)
def step_impl(context):   
    element11 = select_value_amount_pending_paid_summary_business_home_xpaht
    validate_character_numeric_element(context.browser, element11  )


def after_scenario(context, scenario):
  if context.browser:
        print("Cerrando el navegador")
        context.browser.quit()
