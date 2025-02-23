import pytest
from MockSimuladorPruebas import MockAITestGenerator

# Datos para la Prueba
requirements = [
    "El sistema debe permitir el inicio de sesion con credenciales validas.",
    "El usuario debe poder restablecer su contraseña mediante correo electronico."
]
mock_ai = MockAITestGenerator(requirements)

# Caso de Prueba #1: Verificacion de Generacion de Casos de Prueba
@pytest.mark.parametrize("req_index", [0, 1])
def test_generate_test_cases(req_index):
    """Verifica que los casos de prueba se generen correctamente basados en los requisitos."""
    test_cases = mock_ai.generate_test_cases()
    
    # Se espera que la cantidad de casos generados sea igual a la cantidad de requisitos
    assert len(test_cases) == len(requirements)
    
    # Se verifica que los IDs sean correctos y las descripciones correspondan a los requisitos
    assert test_cases[req_index]["ID"] == f"TC_{req_index+1:03}"
    assert test_cases[req_index]["Descripcion de Requisito del Sistema"] == "El sistema cumple con: " + requirements[req_index]

# Caso de Prueba #2: Verificacion de Deteccion de Errores en Codigo
@pytest.mark.parametrize("code, expected_error", [
    ("print(\"Hola Mundo\"", "Error de sintaxis"),
    ("if x = 5:", "Error logico"),
    ("print(\"Hola Mundo\")\nif x == 5:\n    print(\"Correcto\")", "No se detectaron errores.")
])
def test_detect_errors(code, expected_error):
    """Verifica que la deteccion de errores funcione correctamente para distintos escenarios."""
    errors = mock_ai.detect_errors(code)
    assert expected_error in errors[0]  # Se espera detectar el error correcto