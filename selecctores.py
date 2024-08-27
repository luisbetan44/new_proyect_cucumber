class Selecctores:

# URL de los ambientes

  PAGE_HOME_QA_GD_XPAHT = "https://pwa-portal-qa.silohub.ag/login"

  PAGE_HOME_STAGING_GD_XPAHT = "https://pwa-portal-staging.silohub.ag/"

  PAGE_HOME_UAT_GD_XPAHT = "https://pwa-portal-gaviglio-uat.silohub.ag/login"





# selecctores de imagenes en la plataforma

  IMG_GRAIN_WHEAT = "https://pwa-portal-staging.silohub.ag/assets/images/grains/trigo.svg"
  IMG_GRAIN_CORN = "https://pwa-portal-staging.silohub.ag/assets/images/grains/maiz.svg"
  IMG_GRAIN_SOY = "https://pwa-portal-staging.silohub.ag/assets/images/grains/soja.svg"
  IMG_GRAIN_SUNFLOWER = "https://pwa-portal-staging.silohub.ag/assets/images/grains/girasol.svg"            

# insertar cantidades

  INSERT_AMOUNT_KILOS = "300"

  INSERT_AMOUNT_PRODUCT = "10" 

  INSERT_AMOUNT_PRICE = "3000"

  CLICK_CHEVRON_ONE = 3

  CLICK_CHEVRON_TWO = 6

  SCROLLHEIGHT = "window.scrollTo(0, document.body.scrollHeight);"

  SCROLLUP = "window.scrollTo(0, -500);"

  SCROLLSAMPLE = "window.scrollBy(0, 250);"

  # selectores de menu 

  SELECT_MENU_GRAIN_XPAHT = '//span[text() =" Granos"]'

# selectores de submenu

  SELECT_SUBMENU_CONTRACT_XPAHT = '//a[text()=" Contratos "]'


# selectores de la pantalla de granos contrato 

# validaciones de texto en las pantalla granos contratos
  VALIDATE_TITLE_GRAIN_CONTRACT_TEXT = "CONTRATOS"

  VALIDATE_TITLE_SUCCESSE_GRAIN_CONTRACT_TEXT = "Confirmación de venta generada con éxito."

  # cargar opción de tipo de confirmación

  SELECT_DROPDOWN_TYPE_CONFIRM_XPAHT = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-sale-confirmation-main/div/div[1]/app-contract-form/div[1]/form/div/div[1]/div[1]/div[2]/div[2]/ng-select/div/span"

  SELECT_OPTION_CONFIRM_XPAHT = "//span[text()=' (VT) Confirmación De Venta ']"


  #seleccionar cuenta en el buscador granos contratos 

  SEARCH_ACCOUNT_IN_GRAIN_CONTRACT_XPAHT = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-sale-confirmation-main/div/div[1]/app-contract-form/div[1]/form/div/div[1]/div[1]/div[3]/div[2]/div/app-customer-searcher/ng-select/div/div/div[2]/input"

  INSERT_ACCOUNT_IN_GRAIN_CONTRACT_XPAHT = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-sale-confirmation-main/div/div[1]/app-contract-form/div[1]/form/div/div[1]/div[1]/div[3]/div[2]/div/app-customer-searcher/ng-select/div/div/div[2]/input"

  SELECT_ACCOUNT_IN_GRAIN_CONTRACT_XPAHT = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-sale-confirmation-main/div/div[1]/app-contract-form/div[1]/form/div/div[1]/div[1]/div[3]/div[2]/div/app-customer-searcher/ng-select/ng-dropdown-panel/div/div[2]/div[1]/span"
               
# seleccionar especia             

  SELECT_DROPDOWN_SPECIES_GRAIN_CONTRACT_XPAHT = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-sale-confirmation-main/div/div[1]/app-contract-form/div[1]/form/div/div[1]/div[1]/div[4]/div[2]/ng-select/div/span"
  
  SELECT_OPTION_SPECIES_GRAIN_CONTRACT_XPAHT = '/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-sale-confirmation-main/div/div[1]/app-contract-form/div[1]/form/div/div[1]/div[1]/div[4]/div[2]/ng-select/ng-dropdown-panel/div/div[2]/div[14]'

  # seleccionar cosecha
  SELECT_DROPDOWN_HARVEST_GRAIN_CONTRACT_XPAHT = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-sale-confirmation-main/div/div[1]/app-contract-form/div[1]/form/div/div[1]/div[1]/div[5]/div[2]/ng-select/div/span"
  
  SELECT_OPTION_HARVEST_GRAIN_CONTRACT_XPAHT = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-sale-confirmation-main/div/div[1]/app-contract-form/div[1]/form/div/div[1]/div[1]/div[5]/div[2]/ng-select/ng-dropdown-panel/div/div[2]/div[1]/span"

# seleccionar input de cantidad 

  SELECT_INPUT_AMOUNT_KILOS_GRAIN_CONTRACT_XPAHT = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-sale-confirmation-main/div/div[1]/app-contract-form/div[1]/form/div/div[1]/div/app-input-for-long-form[1]/div/div[2]/div/input"

# seleccionar tipo de moneda 
#   
  SELECT_DROPDOWN_TYPE_MONEY_GRAIN_CONTRACT_XPAHT = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-sale-confirmation-main/div/div[1]/app-contract-form/div[1]/form/div/div[1]/div[1]/div[6]/div[2]/ng-select/div/span"

  SELECT_OPTION_TYPE_MONEY_GRAIN_CONTRACT_XPAHT = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-sale-confirmation-main/div/div[1]/app-contract-form/div[1]/form/div/div[1]/div[1]/div[6]/div[2]/ng-select/ng-dropdown-panel/div/div[2]/div[1]/span"

# ingresar precio 

  SELECT_INPUT_PRICE_GRAIN_CONTRACT_XPAHT = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-sale-confirmation-main/div/div[1]/app-contract-form/div[1]/form/div/div[1]/div[1]/app-input-for-long-form[2]/div/div[2]/div/input"

# seleccionar pizarra 

  SELECT_DROPDOWN_BOARD_GRAIN_CONTRACT_XPAHT = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-sale-confirmation-main/div/div[1]/app-contract-form/div[1]/form/div/div[1]/div[1]/div[7]/div[2]/ng-select/div/span"

  SELECT_OPTION_BOARD_GRAIN_CONTRACT_XPAHT = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-sale-confirmation-main/div/div[1]/app-contract-form/div[1]/form/div/div[1]/div[1]/div[7]/div[2]/ng-select/ng-dropdown-panel/div/div[2]/div[2]/span"

# seleccionar codigo estandar

  SELECT_DROPDOWN_CODE_STANDARD_GRAIN_CONTRACT_XPAHT = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-sale-confirmation-main/div/div[1]/app-contract-form/div[1]/form/div/div[1]/div[1]/div[8]/div[2]/ng-select/div/span"

  SELECT_OPTION_CODE_STANDARD_GRAIN_CONTRACT_XPAHT = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-sale-confirmation-main/div/div[1]/app-contract-form/div[1]/form/div/div[1]/div[1]/div[8]/div[2]/ng-select/ng-dropdown-panel/div/div[2]/div/span"

# seleccionar fecha de pago 

  SELECT_CALENDAR_DATA_PAY_GRAIN_CONTRACT_XPAHT = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-sale-confirmation-main/div/div[1]/app-contract-form/div[1]/form/div/div[1]/div[2]/div[2]/app-date-picker/div/input[2]"

  SELECT_DAY_CALENDAR_GRAIN_CONTRACT_XPAHT = "//div[contains(@class, 'flatpickr-calendar')]" 

  #seleccionar fecha entrega 

  SELECT_CALENDAR_DELIVERY_GRAIN_CONTRACT_XPAHT = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-sale-confirmation-main/div/div[1]/app-contract-form/div[1]/form/div/div[2]/div[2]/div/div[1]/div[2]/app-date-picker/div/input[2]"

  SELECT_ARROW_CALENDAR_GRAIN_CONTRACT_XPAHT = "/html/body/div[5]/div[1]/span[2]"

  SELECT_DATE_CALENDAR_DELIVERY_ONE = '/html/body/div[5]/div[2]/div/div[2]/div/span[4]'
 
  SELECT_DATE_CALENDAR_DELIVERY_TWO = '/html/body/div[5]/div[2]/div/div[2]/div/span[33]'

  # seleccionar otras opciones 

  SELECT_OTHERS_OPTION_CHEVRON_GRAIN_CONTRACT_XPAHT = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-sale-confirmation-main/div/div[1]/app-contract-form/div[1]/div/app-select-premiun/div/div/button/img"

  SELECT_PREMIUMS_GRAIN_CONTRACT_XPAHT = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-sale-confirmation-main/div/div[1]/app-contract-form/div[1]/div/app-select-premiun/div/div/div/li[1]/a"

  SELECT_DROPDOWN_PREMIUMS_GRAIN_CONTRACT_XPAHT = "/html/body/ngb-modal-window/div/div/app-modal-contract-premiun/div[2]/div[2]/div/form/div[1]/div[1]/app-premiun-list/ng-select/div/div/div[2]/input"

  SELECT_OPTION_PREMIUMS_GRAIN_CONTRACT_XPAHT = "/html/body/ngb-modal-window/div/div/app-modal-contract-premiun/div[2]/div[2]/div/form/div[1]/div[1]/app-premiun-list/ng-select/ng-dropdown-panel/div/div[2]/div[2]/span"

  SELECT_MONEY_PREMIUMS_GRAIN_CONTRACT_XPAHT = "/html/body/ngb-modal-window/div/div/app-modal-contract-premiun/div[2]/div[2]/div/form/div[1]/div[2]/ng-select/div/span"

  INSERT_MONEY_PREMIUMS_GRAIN_CONTRACT_XPAHT = "/html/body/ngb-modal-window/div/div/app-modal-contract-premiun/div[2]/div[2]/div/form/div[1]/div[2]/ng-select/ng-dropdown-panel/div/div[2]/div[2]"

  INSERT_AMOUNT_VALUE_GRAIN_CONTRACT_XPAHT = "/html/body/ngb-modal-window/div/div/app-modal-contract-premiun/div[2]/div[2]/div/form/div[1]/div[3]/input"

  ADD_PREMIUMS_GRAIN_CONTRACT_XPAHT = "/html/body/ngb-modal-window/div/div/app-modal-contract-premiun/div[2]/div[2]/div/form/div[1]/div[4]/button/img"

  ACCEPT_PREMIUMS_GRAIN_CONTRACT_XPAHT = "/html/body/ngb-modal-window/div/div/app-modal-contract-premiun/div[2]/div[2]/div/div/div/div/app-button[2]/button"

# seleccionar planta 

  SELECT_PLANT_GRAIN_CONTRACT_XPAHT = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-sale-confirmation-main/div/div[1]/app-contract-form/div[1]/form/div/div[2]/div[2]/div/div[2]/div[2]/app-search-selector/ng-select"

  SELECT_OPTION_PLANT_GRAIN_CONTRACT_XPAHT = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-sale-confirmation-main/div/div[1]/app-contract-form/div[1]/form/div/div[2]/div[2]/div/div[2]/div[2]/app-search-selector/ng-select/ng-dropdown-panel/div/div[2]/div[2]/span"
  
  SELECT_ORIGIN_GRAIN_CONTRACT_XPAHT = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-sale-confirmation-main/div/div[1]/app-contract-form/div[1]/form/div/div[2]/div[2]/div/div[3]/div[2]/app-search-selector/ng-select/div/div/div[2]/input"

  SELECT_OPTION_ORIGIN_GRAIN_CONTRACT_XPAHT = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-sale-confirmation-main/div/div[1]/app-contract-form/div[1]/form/div/div[2]/div[2]/div/div[3]/div[2]/app-search-selector/ng-select/ng-dropdown-panel/div/div[2]/div[3]/span"

  SELECT_DESTINATION_GRAIN_CONTRACT_XPAHT = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-sale-confirmation-main/div/div[1]/app-contract-form/div[1]/form/div/div[2]/div[2]/div/div[4]/div[2]/app-search-selector/ng-select/div/div/div[2]/input"

  SELECT_OPTION_DESTINATION_GRAIN_CONTRACT_XPAHT = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-sale-confirmation-main/div/div[1]/app-contract-form/div[1]/form/div/div[2]/div[2]/div/div[4]/div[2]/app-search-selector/ng-select/ng-dropdown-panel/div/div[2]/div[6]/span"

  # seleccionar fecha de fijacion 

  SELECT_CALENDAR_FIXATION_FROM_GRAIN_CONTRACT_XPAHT = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-sale-confirmation-main/div/div[1]/app-contract-form/div[1]/form/div/div[2]/div[4]/div[2]/app-date-picker/div/input[2]"
   
  SELECT_TODATE_FIXATION_FROM_GRAIN_CONTRACT_XPAHT = "/html/body/div[2]/div[2]/div/div[2]/div/span[30]" 

  SELECT_CALENDAR_FIXATION_UNTIL_GRAIN_CONTRACT_XPAHT = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-sale-confirmation-main/div/div[1]/app-contract-form/div[1]/form/div/div[2]/div[5]/div[2]/app-date-picker/div/input[2]"
  
  SELECT_TODATE_FIXATION_UNTIL_GRAIN_CONTRACT_XPAHT = "/html/body/div[3]/div[2]/div/div[2]/div/span[31]" 

  SELECT_BUTTON_CREATE_XPAHT = "/html/body/app-root/app-layout/app-vertical/div/div/div/div/app-sale-confirmation-main/div/div[1]/app-contract-form/div[2]/app-button[2]/button"

  SELECT_BUTTON_CONFIRM = "/html/body/div[6]/div/div[6]/button[3]"

  SELECT_RESPONSE_MESSAGE = "/html/body/div[6]/div/h2"

  SELECT_BUTTON_ACCEPT = "/html/body/div[6]/div/div[6]/button[1]"