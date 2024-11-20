Feature: Inicio de sesion
  Como un usuario registrado, quiero validar los saldos del resumen de mis negocios

  Background:
    
    Given ingreso a la pantalla del login
    When insertar email y password
    And seleccionar boton de aceptar
    Then redireccionado a la pantalla principal
    Given hacer click sobre el tenant
    Then posicionarse en la pagina de inicio
    Given seleccionar al buscador global para el reporte de entregas y ventas
    When ingreso numero de cuenta en el buscador global para el reporte de entregas y ventas
    And seleccionar la opción desplegada correspondiente para el reporte de entregas y ventas
   

  @ValidarResumenDeMisNegocios
  Scenario: Validar los saldos del resumen de mis negocios en el home
    Given seleccionar boton del filtro del home 
    When limpiar el filtro del home 
    And seleccionar cosecha para el resumen de mis negocios 
    And seleccionar el boton de aceptar del filtro resumen de mis negocios del home
    Then validar titulo del indicador del resumen de mis negocios del home 
    And validar imagen del producto del primer movimiento del listado del resumen de mis negocios del home 
    And validar descripcion del producto del listado del resumen de mis negocios del home
    And validar la cantidad del saldo disponible del serial del resumen de mis negocios del home
    And validar titulo de entregado del resumen de mis negocios del home
    And validar la cantidad de la entrega del resumen de mis negocios del home 
    And validar el titulo pendientes de entregas del resumen de mis negocios del home 
    And validar la cantidad de pendientes de entregar del resumen de mis negocios del home
    And validar titulo fijados del resumen de mis negocios del home
    And validar cantidad de fijados del resumen de mis negocios del home 
    And validar titulo pendientes de fijar del resumen de mis negocios del home 
    And validar cantidad de pendientes de fijar del resumen de mis negocios del home 
    And validar titulo pesificado del resumen de mis negocios del home
    And validar cantidad de pesificar del resumen de mis negocios del home 
    And validar titulo pendiente de pesificar del resumen de mis negocios del home
    And validar cantidad de pendiente de pesificar del resumen de mis negocios del home  
    And validar titulo liquidado del resumen de mis negocios del home
    And validar cantidad de liquidados del resumen de mis negocios del home
    And validar titulo pendientes de liquidar del resumen de mis negocios del home
    And validar cantidad de pendientes de liquidar del resumen de mis negocios del home 
    And validar titulo pagado del resumen de mis negocios del home 
    And validar cantidad de pagado del resumen de mis negocios del home
    And validar titulo de pendientes de pagar del resumen de mis negocios del home
    And validar cantidad de pendientes de pagar del resumen de mis negocios del home 
