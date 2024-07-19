# TEMPERATURE CONVERSION: PROGRAM TO CONVERT FAHRENHEIT INTO CELSIUS

from nada_dsl import *
def nada_main():
    party1 = Party(name="Party1")
    # v = SecretInteger(Input(name="v", party=party1))
    f = SecretInteger(Input(name="f", party=party1))
    # th = SecretInteger(Input(name="th", party=party1))
    n = SecretInteger(Input(name="n", party=party1))
    c = (Integer(5)*(f-Integer(32)))/n
    # c = v*(f-th)/n
    return [Output(c, "c", party1)]


##################################################################################################
# LINEAR SEARCH

'''
from nada_dsl import *
def nada_main():
    party1 = Party(name="Party1")
    a = SecretInteger(Input(name="a", party=party1))
    b = SecretInteger(Input(name="b", party=party1))
    c = SecretInteger(Input(name="c", party=party1))
    # found = SecretInteger(Input(name="found", party=party1))
    notfound = SecretInteger(Input(name="notfound", party=party1))
    sequence: list[SecretInteger] = []
    sequence.append(a)
    sequence.append(b)
    sequence.append(c)
    d = SecretInteger(Input(name="d", party=party1))  # search item
    found = a + b + c + d
    for i in range(3):
        if sequence[i]==d:
            return [Output(found, "found", party=party1)]
    return [Output(notfound, "notfound", party=party1)]
'''

##################################################################################################
# SUM OF ELEMENTS OF LIST

'''
from nada_dsl import *
def nada_main():
    party1 = Party(name="Party1")
    a = SecretInteger(Input(name="a", party=party1))
    b = SecretInteger(Input(name="b", party=party1))
    c = SecretInteger(Input(name="c", party=party1))
    result = SecretInteger(Input(name="result", party=party1))
    sequence: list[SecretInteger] = []
    sequence.append(a)
    sequence.append(b)
    sequence.append(c)
    for i in range(3):
        result+=sequence[i]
    return [Output(result, "result", party1)]
'''

##################################################################################################
# Simple arithmetic program1

'''
from nada_dsl import *
def nada_main():
    party1 = Party(name="Party1")
    party2 = Party(name="Party2")
    party3 = Party(name="Party3")
    a = SecretInteger(Input(name="A", party=party1))
    b = SecretInteger(Input(name="B", party=party2))
    result = a + b
    return [Output(result, "my_output", party3)]
'''

##################################################################################################
# Simple arithmetic program2

'''
from nada_dsl import *
def nada_main():
    party1 = Party(name="Party1")
    A = SecretInteger(Input(name="A", party=party1))
    B = SecretInteger(Input(name="B", party=party1))
    C = SecretInteger(Input(name="C", party=party1))
    TMP1 = A + B
    D = TMP1 * C
    return [Output(D, "D", party1)]
'''


