Feature: flujo de insumos producto
generar un pedido de insumos

  @iniciarSesion6
  Scenario: Inicio de sesion exitoso7
    Given estoy en la pagina de inicio de sesion7
    When ingreso mi nombre de usuario y credenciales correctas7
    And hago clic en el boton de inicio de sesion7
    Then deberia ser redirigido a la pagina principal7

  @seleccionartenat6
  Scenario: Selecciono el tenant7
    Given selecciono el tenant donde quiero ingresar7
    Then ingreso a la pagina de inicio7

  @IngresarinsumosProdcuto
  Scenario: Seleccionar menu de insumos
    Given ingreso al menu de insumos
    When ingreso al submenu de producto
    And validar titulo de pagina de productos
    
    

  @BuscarAgregarProducto
  Scenario: Ingresar y seleccionar producto
    Given ingresar descripcion del producto en el buscador 
    When seleccionar campo condiciones de pago
    And ingresar condicion de pago 
    And hacer click boton buscar
    And hacer click en el boton de precio del segundo producto 
    And hacer click sobre el checbox de la descripcon del precio
    And agregar prodcuto al carrito
    And ingresar al carrito 

  @IngresarCuentaProductModificarcantidad
  Scenario: Ingresar cuenta y modificar cantidad de prodcutos
    Given ingreso cuenta prodcutor
    When selecciono cuenta productor
    And seleccionar campo cantidad de producto
    And limpiar campo cantidad de producto
    And ingresar nueva cantidad
    And hacer click boton continuar 
    And seleccionar sucursal
    And seleccionar deposito
    And seleccionar tipo de comprobamte
    And hacer click boton crear orden
    And hacer click popup confirmar
    And hacer click popup aceptar

  @ValidarOrdenCreada
  Scenario: Validar orden creada
    Given ingreso al submenu de ordenes
    When ingreso al detalle de la orden
    Then validar fecha actual de la orden
    And validar cliente
    When salir del detalle 
