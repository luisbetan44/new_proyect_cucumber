Feature: Home entregas y ventas 
  validar los movimientos de las ultimas cinco entregas y ventas 

  @iniciarSesion4
  Scenario: Inicio de sesion exitoso
    Given ingreso a la pantalla del login
    When insertar email y password
    And seleccionar boton de aceptar
    Then redireccionado a la pantalla principal

  @seleccionartenat4
  Scenario: Selecciono el tenant4
    Given hacer click sobre el tenant
    Then posicionarse en la pagina de inicio

  @seleccionarcuenta4
  Scenario: Seleccionar cuenta del productor
    Given seleccionar al buscador global
    When ingreso numero de cuenta en el buscador global
    And hago clic en la opción desplegada correspondiente
    And srollear hasta el centro de la pantalla 
    

  @ValidarEntregasRecientes
  Scenario: validar las entregas recientes en el home
    Given scrollear pantalla 
    Then validar titulo de pantalla2
    And validar titulo del modulo2
    And validar titulo de pagina de productos2
    And Validar imagen del producto2
    And validar cosecha2
    And validar fecha2 
    And validar titulo CTG/CRT2
    And obtener valor CTG/CRT2
    And validar titulo Kg Netos2
    And obtener valor Kg Netos2

  @ValidarVentasRecientes
  Scenario: validar las ventas recientes en el home
    Given validar titulo del modulo3
    And validar titulo de pagina de productos3
    And Validar imagen del producto3
    And validar cosecha3
    And validar fecha3 
    And validar titulo Kg Netos3
    And obtener valor Kg Netos3
    And validar titulo precio3
    And obtener precio3
    And obtener valor final3 
    