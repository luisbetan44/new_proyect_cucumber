Feature: flujo de granos contratos 

  @iniciarSesion8
  Scenario: Inicio de sesion exitoso8
    Given estoy en la pagina de inicio de sesion8
    When ingreso mi nombre de usuario y credenciales correctas8
    And hago clic en el boton de inicio de sesion8
    Then deberia ser redirigido a la pagina principal8

  @seleccionartenat8
  Scenario: Selecciono el tenant8
    Given selecciono el tenant donde quiero ingresar8
    Then ingreso a la pagina de inicio8

  @IngresargranosContratos
  Scenario: Seleccionar menu de granos
    Given ingreso al menu de granos
    When ingreso al submenu de contratos
    Then validar titulo de pagina
    
    

  @IgresarDatosEnFormulario
  Scenario: Ingresar datos en todos los campos requeridos
    Given seleccionar tipo de confirmacion de venta 
    When ingresar la cuenta del productor
    And seleccionar cuenta del productor
    And seleccionar especie
    And seleccionar cosecha
    And ingresar cantidad de kilos
    And seleccionar moneda
    And ingresar precio
    And scrollear en la pantalla 
    And seleccionar pizarra
    And seleccionar codigo estandar
    And seleccionar fecha de pago 
    And scrollear hacia arriba de la pantalla 
    And seleccionar fecha de entrega
    And seleccionar planta
    And seleccionar procedencia
    And seleccionar destino
    And seleccionar fecha de fijacion desde 
    And seleccionar fecha de fijacion hasta

  @SelectButtonAccept
  Scenario: seleccionar todos los botones para generar el contyrato
    Given seleccionar boton crear
    When seleccionar boton confirmar
    Then validar mensaje de finalizacion
    When seleccionar boton aceptar
       

  