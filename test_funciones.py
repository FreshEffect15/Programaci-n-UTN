import pytest

from TP_Variables_Dimensionadas.py import comprobar_dni, comprobar_frase, comprobar_nombres, comprobar_divisibilidad


def test_comprobar_dni_valido():
    assert comprobar_dni("12345678") == "Su DNI es correcto"

def test_comprobar_dni_invalido():
    assert comprobar_dni("1234") == "Su DNI no es válido"


def test_comprobar_frase():
    assert comprobar_frase("Esta es una frase de prueba") == "La palabra final de la frase es: prueba"


def test_comprobar_nombres():
    assert comprobar_nombres("John Doe") == ("John", "Doe")


def test_comprobar_divisibilidad_multiplo():
    assert comprobar_divisibilidad(10, 5) == True

def test_comprobar_divisibilidad_no_multiplo():
    assert comprobar_divisibilidad(7, 3) == False



if __name__ == "__main__":
    pytest.main()