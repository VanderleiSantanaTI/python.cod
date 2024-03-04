def calcular(valor, *args):
    print(args)
    total_iposto = sum(valor * item for item in args)
    return total_iposto


print(calcular(1000, 0.275, 0.05, 0.0375, 0.03))


def calcular_2(valor, **kwargs):
    # print(kwargs)
    # print(kwargs['perc_ir'])
    # kwargs vem de keyword, a diferença são os dois ** especificar a entrada
    total_iposto = sum(valor * item for item in kwargs.values())
    return total_iposto

# print(calcular_2(1000, perc_ir=0.275, perc_iss=0.05, perce_csll=0.0375, perce_pis=0.03))
