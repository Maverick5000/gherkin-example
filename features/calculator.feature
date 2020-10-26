Feature: Test Calculadora
    Scenario: Suma
        Given Iniciamos la calculadora
        When Le paso "2 + 3" a la calculadora
        Then Obtengo el resultado "5"
    Scenario: Resta
        Given Iniciamos la calculadora
        When Le paso "5 - 2" a la calculadora
        Then Obtengo el resultado "3"
    Scenario: Multiplicacion
        Given Iniciamos la calculadora
        When Le paso "6 * 3" a la calculadora
        Then Obtengo el resultado "18"
    Scenario: Numeros negativos
        Given Iniciamos la calculadora
        When Le paso "3 - 5" a la calculadora
        Then Obtengo el resultado "-2"