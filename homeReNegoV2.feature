Feature: Inicio de sesion
  Como un usuario registrado y validar los saldos del resumen de mis negocios

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
   
    

  @ValidarResumenDeMisNegocios
  Scenario: validar los saldos del resumen de mis negocios en el home
    Given seleccionar boton del filtro del home 
    When limpiar el filtro del home 
    And seleccionar cosecha para el resumen de mis negocios 
    And seleccionar el boton de acptar del filtro del home
    Then validar titulo del indicador del resumen de negocios del home 
    And validar imagen del producto del primer movimiento del listado del resumen de mis negocios
    And validar cantidad pesificada
    And validar cantidad pendiente de pesificar
    And validar cantidad liquidada
    And validar cantidad pendiente de liquidar
