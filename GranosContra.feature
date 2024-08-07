Feature: flujo de granos contratos 

  @iniciarSesion6
  Scenario: Inicio de sesion exitoso5
    Given estoy en la pagina de inicio de sesion6
    When ingreso mi nombre de usuario y credenciales correctas6
    And hago clic en el boton de inicio de sesion6
    Then deberia ser redirigido a la pagina principal6

  @seleccionartenat6
  Scenario: Selecciono el tenant6
    Given selecciono el tenant donde quiero ingresar6
    Then ingreso a la pagina de inicio6

  @IngresargranosContratos6
  Scenario: Seleccionar menu de granos
    Given ingreso al menu de granos
    When ingreso al submenu de contratos
    And validar titulo de pagina
    
    

  @IgresarDatosEnFormulario
  Scenario: Ingresar datos en todos los campos requeridos
    Given seleccionar tipo de confirmacion de venta 
    When ingresar y seleccionar cuenta del productor 
    And seleccionar especie
    And seleccionar cosecha
    And ingresar cantidad de kilos
    And seleccionar moneda
    And ingresar precio
    And 

  