# from nada_dsl import *

# def nada_main():
#     party1 = Party(name="Party1")
#     party2 = Party(name="Party2")
#     party3 = Party(name="Party3")
#     a = SecretInteger(Input(name="A", party=party1))
#     b = SecretInteger(Input(name="B", party=party2))

#     result = a + b

#     return [Output(result, "my_output", party3)]

# from nada_dsl import *

# def nada_main():
#     party1 = Party(name="Party1")
#     A = SecretInteger(Input(name="A", party=party1))
#     B = SecretInteger(Input(name="B", party=party1))
#     C = SecretInteger(Input(name="C", party=party1))

#     TMP1 = A + B
#     D = TMP1 * C

#     return [Output(D, "D", party1)]

from nada_dsl import *
def nada_main():
    party1 = Party(name="Party1")
    v = SecretInteger(Input(name="v", party=party1))
    f = SecretInteger(Input(name="f", party=party1))
    th = SecretInteger(Input(name="th", party=party1))
    n = SecretInteger(Input(name="n", party=party1))
    c = v*(f-th)/n
    return [Output(c, "c", party1)]
