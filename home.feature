Feature: ingreso al home y selecciono cuenta en el buscador global visualizar informacion en indicadores 

   @iniciarSesion2
  Scenario: Inicio de sesion exitoso2
    Given estoy en la pagina de inicio de sesion2
    When ingreso mi nombre de usuario y credenciales correctas2
    And hago clic en el boton de inicio de sesion2
    Then deberia ser redirigido a la pagina principal2

  @seleccionartenat2
  Scenario: Selecciono el tenant2
    Given selecciono el tenant donde quiero ingresar2
    Then ingreso a la pagina de inicio2

  @seleccionarcuenta
  Scenario: Seleccionar cuenta del productor
    Given selecciono al buscador global
    When ingreso numero de cuenta en el buscador global
    And hago clic en la opción desplegada correspondiente
    Then el sistema muestra mensaje de bienvenida
    And Vencido a hoy saldo en ARS
    And Vencido a hoy saldo en USD
    And A vencer saldo en ARS
    And A vencer saldo en USD 
 

  
