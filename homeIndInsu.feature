Feature: Home indicadores de insumos 
  validar los movimientos de insumos de los ultimo meses 12 o 6

  @iniciarSesion5
  Scenario: Inicio de sesion exitoso5
    Given estoy en la pagina de inicio de sesion5
    When ingreso mi nombre de usuario y credenciales correctas5
    And hago clic en el boton de inicio de sesion5
    Then deberia ser redirigido a la pagina principal5

  @seleccionartenat5
  Scenario: Selecciono el tenant5
    Given selecciono el tenant donde quiero ingresar5
    Then ingreso a la pagina de inicio5

  @seleccionarcuenta4
  Scenario: Seleccionar cuenta del productor5
    Given seleccionar al buscador global5
    When ingreso numero de cuenta en el buscador global5
    And hago clic en la opción desplegada correspondiente5
    And srollear hasta el centro de la pantalla5 
    

  @ValidarInsumosPendientesDeRetirar
  Scenario: validar indicador  insumos pendientes de retirar en el home
    Given validar descripcion del  primer producto 
    Then validar la cantidad del primer producto
    And validar el descripcion del segundo producto
    And validar la cantidad del segundo producto  

  @ValidarMercaderiaRemitida
  Scenario: validar mercaderia remitida en el home
    Given validar descripcion del  primer producto remitido
    Then validar la cantidad del primer producto remitido
    And validar el descripcion del segundo producto remitido
    And validar la cantidad del segundo producto remitido 

 @ValidarMercaderiaFacturada
  Scenario: validar mercaderia facturada en el home
    Given validar descripcion del  primer producto facturada
    Then validar la cantidad del primer producto facturada
    And validar el descripcion del segundo producto facturada
    And validar la cantidad del segundo producto facturada   