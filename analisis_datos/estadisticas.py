# estadisticas.py
def media(compras):
    return sum([valor for _,valor in compras])/len(compras)  

def mediana(compras):
    precios = [valor for _,valor in compras]
    precios.sort()
    if len(precios) % 2 == 0:
        print(precios)
        medio = int(len(precios)/2)
        return precios[medio] + precios[medio-1]
    else :
        print(precios)
        return precios[int(len(precios)/2)]   