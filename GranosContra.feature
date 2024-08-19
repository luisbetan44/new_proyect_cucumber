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

  @seleccionarMenuGranosContratos
  Scenario: Ingresar en el menu de granos contratos
    Given seleccionar menu de granos
    When seleccionar submenu de contratos
    Then velidar titulo de la pagina
  
  @IngresarDatosFormularioIzquierdo
  Scenario:
    Given seleccionar tipo de confirmacion 
    When ingresar cuenta productor
    And seleccionar cuenta productor
    And seleccionar la especie
    And seleccionar cosecha
    And ingresar cantidad 
    And seleccionar modena
    And scrollear la pantalla
    And ingresar precio
    And seleccionar pizarra
    And seleccionar codigo standar
    And seleccionar fecha de pago  
  
  @IngresarDatosFormularioDerecho
  Scenario:
    Given scrollear hacia principio de la pantalla 
    When ingresar fecha de entrega 
    

  

  
  