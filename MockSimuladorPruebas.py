import tabulate

class MockAITestGenerator:
    def __init__(self, requirements):
        self.requirements = requirements
        self.test_cases = []

    def generate_test_cases(self):
        """Simula la generación de casos de prueba basada en requisitos."""
        for i, req in enumerate(self.requirements, 1):
            test_case = {
                "ID": f"TC_{i:03}",
                "Descripción de Requisito del Sistema": f"El sistema cumple con: {req}"
            }
            self.test_cases.append(test_case)
        return self.test_cases

    def detect_errors(self, code):
        """Simula la detección de errores básica en el código."""
        errors = []
        if "print(" in code and not code.endswith(")\n"):
            errors.append("Error de sintaxis: Falta paréntesis de cierre en print().")
        if "=" in code and "==" not in code and "if" in code:
            errors.append("Error lógico: Asignación en lugar de comparación en una condición if.")
        return errors if errors else ["No se detectaron errores."]

# Simulación de Requisitos
requirements = [
    "El sistema debe permitir el inicio de sesión con credenciales válidas.",
    "El usuario debe poder restablecer su contraseña mediante correo electrónico.",
    "El sistema debe registrar el historial de acceso de los usuarios."
]

# Ejecución de la IA
mock_ai = MockAITestGenerator(requirements)
test_cases = mock_ai.generate_test_cases()

# Tabulate crea la tabla para una mejor experiencia del usuario
print("\nCasos de prueba generados:")
print(tabulate.tabulate(test_cases, headers="keys", tablefmt="grid"))

# Deteccion de errores
sample_code = "print(\"Hola Mundo\""
errors = mock_ai.detect_errors(sample_code)

print("\nErrores detectados en el código:")
for error in errors:
    print(f"- {error}")
