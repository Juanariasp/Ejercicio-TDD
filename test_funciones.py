from funciones import encontrar_minimo

def test_encontrar_minimo():
    assert encontrar_minimo([1,2,3,4]) == 1
    assert encontrar_minimo([5,8,11,35]) == 5
    assert encontrar_minimo([10,20,88,6]) == 6
    