from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from elements import delete_element, displace_element, find_elements, find_elements_id, find_send_element, search_and_select_option, select_option_click, send_element, validate_text,validate_text_by_text
from elements2 import verify_todate
from loginSample import LoginSteps2





@given('estoy en la pagina de inicio de sesion7')
def step_impl(context):
    login_steps = LoginSteps2(context.browser)
    login_steps.navigate_to_login_page("https://pwa-portal-staging.silohub.ag/login")

@when('ingreso mi nombre de usuario y credenciales correctas7')
def step_impl(context):
    login_steps = LoginSteps2(context.browser)
    login_steps.enter_credentials("comercialgd@silohub.ag", "G@viglio123")

@when('hago clic en el boton de inicio de sesion7')
def step_impl(context):
    login_steps = LoginSteps2(context.browser)
    login_steps.click_login_button()

@then('deberia ser redirigido a la pagina principal7')
def step_impl(context):
    login_steps = LoginSteps2(context.browser)
    login_steps.verify_redirection_to_home()

@given('selecciono el tenant donde quiero ingresar7')
def step_impl(context):
    login_steps = LoginSteps2(context.browser)
    login_steps.select_tenant()

@then('ingreso a la pagina de inicio7')
def step_impl(context):
    login_steps = LoginSteps2(context.browser)
    login_steps.verify_redirection_to_inicio()

@given('ingreso al menu de insumos')
def step_impl(context):
    select_supplies = "/html/body/app-root/app-layout/app-vertical/div/app-sidebar/div[1]/div[3]/div[1]/ngx-simplebar/div[1]/div[2]/div/div/div/ul/li[4]/a"
    displace_element(context.browser,select_supplies )
    time.sleep(5)

@when('ingreso al submenu de producto')
def step_impl(context):
    select_menu_product = "/html/body/app-root/app-layout/app-vertical/div/app-sidebar/div[1]/div[3]/div[1]/ngx-simplebar/div[1]/div[2]/div/div/div/ul/li[4]/div/ul/li[1]/a"
    find_elements(context.browser,select_menu_product )
    time.sleep(5)

@when('validar titulo de pagina de productos')
def step_impl(context):   
    title_page_product_obtained = "/html/body/app-root/app-layout/app-vertical/div/div/div/app-header-for-screen/div/div/span"
    title_page_product_expected = "PRODUCTOS"
    validate_text(context.browser, title_page_product_obtained, title_page_product_expected)

@given('ingresar descripcion del producto en el buscador')
def step_impl(context):
    add_product = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-supplies/app-supplies-searcher/div/div[1]/input"
    send_product = "herbicida"
    find_send_element(context.browser, add_product, send_product )
    time.sleep(2)

@when('seleccionar campo condiciones de pago')
def step_impl(context):
    select_condition = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-supplies/app-supplies-searcher/div/div[2]/app-supplies-price-list-selector/button"
    find_elements(context.browser,select_condition )

@when('ingresar condicion de pago')
def step_impl(context):
    xpath_search_input = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-supplies/app-supplies-searcher/div/div[2]/app-supplies-price-list-selector/ul/input"
    xpath_search_result = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-supplies/app-supplies-searcher/div/div[2]/app-supplies-price-list-selector/ul/div/div[10]/input"
    value_to_search = "30 días"
    search_and_select_option(context.browser, xpath_search_input, xpath_search_result, value_to_search)

@when('hacer click boton buscar')
def step_impl(context):
    button_search = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-supplies/app-supplies-searcher/div/div[3]/button/div"
    find_elements(context.browser, button_search )
    time.sleep(3)

@when('hacer click en el boton de precio del segundo producto')
def step_impl(context):
    select_price_product = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-supplies/app-supplies-product-price-list/div/app-supplies-product-price-list-item[2]/div/div/div/div[2]/button[2]/strong"
    find_elements(context.browser, select_price_product )
    time.sleep(3)

@when('hacer click sobre el checbox de la descripcon del precio')
def step_impl(context):
    select_product_list = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-supplies/app-supplies-product-price-list/div/app-supplies-product-price-list-item[2]/div/div/app-supplies-product-price-list-item-price/div[2]/app-supplies-product-price-list-item-price-item/div/div[1]/input"
    find_elements(context.browser, select_product_list )
    time.sleep(3)

@when('agregar prodcuto al carrito')
def step_impl(context):
    add_button = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-supplies/app-supplies-product-price-list/div/app-supplies-product-price-list-item[2]/div/div/app-supplies-product-price-list-item-price/app-supplies-product-price-list-item-price-add-share-buttons/div/button[2]"
    find_elements(context.browser,  add_button )
    time.sleep(3)

@when('ingresar al carrito')
def step_impl(context):
    select_car = "shipment"
    find_elements_id(context.browser,select_car )
    time.sleep(3)

@given('ingreso cuenta prodcutor')
def step_impl(context):
    select_account = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-supplies-cart/div/div[2]/app-supplies-customer-info/div/div[1]/div/div[2]/app-customer-searcher/ng-select/div/div/div[2]/input"
    send_account = "1023"
    find_send_element(context.browser, select_account, send_account )

@when('selecciono cuenta productor')
def step_impl(context):
    select_account_tenant = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-supplies-cart/div/div[2]/app-supplies-customer-info/div/div[1]/div/div[2]/app-customer-searcher/ng-select/ng-dropdown-panel/div/div[2]/div[2]/span"
    find_elements(context.browser,  select_account_tenant)
    time.sleep(7)

@when('seleccionar campo cantidad de producto')
def step_impl(context):
    select_input_amount2 = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-supplies-cart/div/div[1]/div/app-supplies-selected-products/app-supplies-selected-products-item/div/div/app-supplies-selected-products-item-price-item/div/div[2]/div/div[2]/input"
    find_elements(context.browser, select_input_amount2)
    time.sleep(2)

@when('limpiar campo cantidad de producto')
def step_impl(context):
    cleam_account = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-supplies-cart/div/div[1]/div/app-supplies-selected-products/app-supplies-selected-products-item/div/div/app-supplies-selected-products-item-price-item/div/div[2]/div/div[2]/input"
    delete_element(context.browser, cleam_account)
    time.sleep(2)


@when('ingresar nueva cantidad')
def step_impl(context):
    select_input_amount = '/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-supplies-cart/div/div[1]/div/app-supplies-selected-products/app-supplies-selected-products-item/div/div/app-supplies-selected-products-item-price-item/div/div[2]/div/div[2]/input'
    send_account = '10'
    send_element(context.browser, select_input_amount,send_account )

@when('hacer click boton continuar')
def step_impl(context):
    continue_button = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-supplies-cart/div/div[2]/app-supplies-customer-info/div/app-supplies-customer-info-share-continuous/div/div[2]/button"
    find_elements(context.browser, continue_button )

@when('seleccionar sucursal')
def step_impl(context):
    select_branch = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-supplies-cart/div/div[1]/app-supplies-customer-info-branch-office/div/div/div/div[1]/select"
    select_option = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-supplies-cart/div/div[1]/app-supplies-customer-info-branch-office/div/div/div/div[1]/select/option[4]"
    select_option_click(context.browser, select_branch, select_option )


@when('seleccionar deposito')
def step_impl(context):
    select_deposit = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-supplies-cart/div/div[1]/app-supplies-customer-info-branch-office/div/div/div/div[2]/select"
    select_option = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-supplies-cart/div/div[1]/app-supplies-customer-info-branch-office/div/div/div/div[2]/select/option[3]"
    select_option_click(context.browser, select_deposit, select_option )

@when('seleccionar tipo de comprobamte')
def step_impl(context):
    select_voucher = '//*[@id="layout-wrapper"]/div/div/div/app-supplies-cart/div/div[1]/app-supplies-customer-info-branch-office/div/div/div/div[3]/select'
    select_option = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-supplies-cart/div/div[1]/app-supplies-customer-info-branch-office/div/div/div/div[3]/select/option[2]"
    select_option_click(context.browser, select_voucher, select_option )

@when('hacer click boton crear orden')
def step_impl(context):
    create_order = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-supplies-cart/div/div[2]/app-supplies-customer-info/div/app-supplies-customer-info-share-continuous/div/div[2]/button"
    find_elements(context.browser, create_order )

@when('hacer click popup confirmar')
def step_impl(context):
    confirm_order = "/html/body/div/div/div[6]/button[3]"
    find_elements(context.browser, confirm_order )
    time.sleep(2)

@when('hacer click popup aceptar')
def step_impl(context):
    accept_button = "/html/body/div/div/div[6]/button[3]"
    find_elements(context.browser, accept_button )
    time.sleep(2)

@given('ingreso al submenu de ordenes')
def step_impl(context):
    select_list_order = "/html/body/app-root/app-layout/app-vertical/div/app-sidebar/div[1]/div[3]/div[1]/ngx-simplebar/div[1]/div[2]/div/div/div/ul/li[4]/div/ul/li[3]/a"
    find_elements(context.browser, select_list_order )
    time.sleep(3)

@when('ingreso al detalle de la orden')
def step_impl(context):
    select_detail_order = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-orders/app-responsive-table/div/div/table/tbody/tr[1]/td[3]"
    find_elements(context.browser, select_detail_order )
    time.sleep(3)


@then('validar fecha actual de la orden')
def step_impl(context):
    select_todate = "#layout-wrapper > div > div > div > app-detail-orders > div > div.col-md-8.col-sm-12 > section:nth-child(1) > div > div > div:nth-child(2) > div.mt-1"
    verify_todate(context.browser,select_todate)
    time.sleep(2)

@then('validar cliente')
def step_impl(context):
    client_obtaired = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-detail-orders/div/div[1]/section[1]/div/div/div[3]/div[2]"
    client_expected = "(1023) JUAN DEMO"
    validate_text(context.browser,client_obtaired, client_expected )


@when('salir del detalle')
def step_impl(context):
    got_to_page = "/html/body/app-root/app-layout/app-vertical/div/div/div/app-header-for-screen/div/div/div/a"
    find_elements(context.browser, got_to_page)
    time.sleep(3)


    