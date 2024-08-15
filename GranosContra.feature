Feature: flujo de granos contratos 

  @iniciarSesion6
  Scenario: Inicio de sesion exitoso8
    Given estoy en la pagina de inicio de sesion8
    When ingreso mi nombre de usuario y credenciales correctas8
    And hago clic en el boton de inicio de sesion8
    Then deberia ser redirigido a la pagina principal8

  @seleccionartenat6
  Scenario: Selecciono el tenant8
    Given selecciono el tenant donde quiero ingresar8
    Then ingreso a la pagina de inicio8

  

  
  