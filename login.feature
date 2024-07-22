Feature: Inicio de sesion
  Como un usuario registrado
  Quiero iniciar sesion en el sistema
  Para acceder a las funciones

  @iniciarSesion
  Scenario: Inicio de sesion exitoso
    Given estoy en la pagina de inicio de sesion
    When ingreso mi nombre de usuario y credenciales correctas
    And hago clic en el boton de inicio de sesion
    Then deberia ser redirigido a la pagina principal

  @seleccionartenat
  Scenario: Selecciono el tenant
    Given selecciono el tenant donde quiero ingresar
    Then ingreso a la pagina de inicio