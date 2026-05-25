import sympy
from typing import Dict
# Controlla il file readme.md per i dettagli su ciascun sub-task

def calcola_derivata(espressione: str, variabile: str)-> sympy.Expr:
    try:
        # Crea il simbolo della variabile
        var = sympy.symbols(variabile)

        # Parsing dell'espressione in forma simbolica
        expr = sympy.sympify(espressione)

        # Calcolo della derivata
        derivata = sympy.diff(expr, var)

        # Restituisce il risultato come stringa
        return str(derivata)

    except Exception as e:
        raise ValueError(f"Errore nel parsing o nel calcolo: {e}")


def calcola_integrale_definito(espressione: str, variabile: str, estremo_inf: float, estremo_sup: float)-> sympy.Expr :
    """Sub-task 2: Calcolare un Integrale Definito."""

    try:
        var = sympy.symbols(variabile)
        expr =sympy.sympify(espressione)

        # integrale definito
        risultato = sympy.integrate(expr, (var, estremo_inf, estremo_sup))

        return risultato

    except Exception as e:
        raise ValueError(f"Errore nel calcolo dell'integrale: {e}")



def calcola_limite(espressione: str, variabile: str, punto: str) -> sympy.Expr:
    """Sub-task 3: Calcolare un Limite."""
    pass

def calcola_polinomio_taylor(espressione: str, variabile: str, punto: float, ordine: int) -> sympy.Expr:
    """Sub-task 4: Calcolare una Serie di Taylor."""
    pass

def risolvi_sistema_lineare(eq1: str, eq2: str, var1: str, var2: str) -> Dict[sympy.Symbol, sympy.Expr]:
    """Sub-task 5: Risolvere un Sistema Lineare."""
    pass

def main():
    print("Sub-task 1:", calcola_derivata("x**3 + 2*x", "x"))
    print("Sub-task 2:", calcola_integrale_definito("x**2", "x", 0, 3))
    print("Sub-task 3:", calcola_limite("sin(x)/x", "x", "0"))
    print("Sub-task 4:", calcola_polinomio_taylor("exp(x)", "x", 0.0, 4))
    print("Sub-task 5:", risolvi_sistema_lineare("x + y - 3", "x - y - 1", "x", "y"))

if __name__ == "__main__":
    main()
