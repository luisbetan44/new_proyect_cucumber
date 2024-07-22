Feature: Registro de usuarios
  Como un nuevo usuario quiero registrarme en el sistema
  para poder acceder a las funciones

  Background:
    Given estoy en el navegador chrome
  @registro
  Scenario Outline: Registro de usuario exitoso
    Given estoy en la pagina de Registro
    When completo el formulario de Registro con "<Nombre>" y ""<Apellido>
    And hago clic en el boton de registro OR presiono enter
    Then deberia ver un mensaje de bienvenida
    But me pide que confirme el correo

   
 Examples:
 |Nombre|Apellido|
 |Juan |Perez    |
 |Maria|Rodriguez|
 |Lizet|ODR      |