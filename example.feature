Feature: Iniciar

@examples
Scenario: Usuario valido para iniciar sesion
     Given el usuario tiene una cuenta
     When el usuario incia session con credenciales validas
     Then el usuario debe ser redirigido al panal de control

