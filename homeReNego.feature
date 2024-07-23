Feature: Inicio de sesion
  Como un usuario registrado y validar los saldos del resumen de mis negocios

  @iniciarSesion3
  Scenario: Inicio de sesion exitoso3
    Given estoy en la pagina de inicio de sesion3
    When ingreso mi nombre de usuario y credenciales correctas3
    And hago clic en el boton de inicio de sesion3
    Then deberia ser redirigido a la pagina principal3

  @seleccionartenat3
  Scenario: Selecciono el tenant3
    Given selecciono el tenant donde quiero ingresar3
    Then ingreso a la pagina de inicio3

  @seleccionarcuenta3
  Scenario: Seleccionar cuenta del productor3
    Given seleccionar al buscador global3
    When ingreso numero de cuenta en el buscador global3
    And hago clic en la opción desplegada correspondiente3
    Then el sistema muestra mensaje de bienvenida3
    

  @ValidarResumenDeMisNegocios
  Scenario: validar los saldos del resumen de mis negocios en el home
    Given validar imagen del producto
    Then validar descripcion del producto
    And validar la cantidad entregada
    And validar la cantidad pendiente de entregar
    And validar cantidad fijada
    And validar cantidad pendiente de fijar
    And validar cantidad pesificada
    And validar cantidad pendiente de pesificar
    And validar cantidad liquidada
    And validar cantidad pendiente de liquidar
