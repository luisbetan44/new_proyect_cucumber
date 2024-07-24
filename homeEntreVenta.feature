Feature: Home entregas y ventas 
  validar los movimientos de las ultimas cinco entregas y ventas 

  @iniciarSesion4
  Scenario: Inicio de sesion exitoso4
    Given estoy en la pagina de inicio de sesion4
    When ingreso mi nombre de usuario y credenciales correctas4
    And hago clic en el boton de inicio de sesion4
    Then deberia ser redirigido a la pagina principal4

  @seleccionartenat4
  Scenario: Selecciono el tenant4
    Given selecciono el tenant donde quiero ingresar4
    Then ingreso a la pagina de inicio4

  @seleccionarcuenta4
  Scenario: Seleccionar cuenta del productor4
    Given seleccionar al buscador global4
    When ingreso numero de cuenta en el buscador global4
    And hago clic en la opción desplegada correspondiente4
    And srollear hasta el centro de la pantalla 
    

  @ValidarEntregasRecientes
  Scenario: validar las entregas recientes en el home
    Given validar imagen del producto entregado
    Then validar descripcion y cosecha del producto a entregar
    And validar la fecha de la entrega
    And validar el numero de CTG/CRT de la entrega
    And validar kilos a entregar   

  @ValidarVentasRecientes
  Scenario: validar las ventas recientes en el home
    Given validar imagen del producto vender
    Then validar descripcion y cosecha del producto a vender
    And validar la fecha de la vender
    And validar el cantidad kilos de la venta
    And validar precio de las ventas
    