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
    Given seleccionar al buscador global para el reporte de entregas y ventas
    When ingreso numero de cuenta en el buscador global para el reporte de entregas y ventas
    And seleccionar la opción desplegada correspondiente para el reporte de entregas y ventas
   
    

  @ValidarEntregasRecientes
  Scenario: validar las entregas recientes en el home
    Given scrollear hasta reporte de entregas del home 
    Then validar titulo de la pagina en el home
    And validar titulo del reporte de entregas del home
    And validar descripcion del producto en el reporte de entregas del home
    And Validar imagen del producto del reporte de entregas del home
    And validar cosecha en el reporte de entregas del home
    And validar fecha del reporte de entregas del home 
    And validar titulo CTG/CRT del reporte de entregas del home
    And obtener valor CTG/CRT del reporte de entregas en el home
    And validar titulo Kg Netos del reporte de entregas en el home
    And obtener valor Kg Netos del reporte de entregas en el home

  @ValidarVentasRecientes
  Scenario: validar las ventas recientes en el home
    Given validar titulo del reporte de las ventas del home
    Then validar titulo del producto en el reporte de ventas del home
    And Validar imagen del producto del reporte de ventas del home
    And validar cosecha en el reporte de ventas del home
    And validar fecha del reporte de ventas del home 
    And validar titulo Kg Netos del reporte de ventas del home
    And obtener valor Kg Netos del reporte de ventas del home
    And validar titulo precio del reportes de ventas del home
    And obtener precio del reporte de ventas en del home
    
    