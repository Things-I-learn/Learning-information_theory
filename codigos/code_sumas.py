# input binario
# cadena separada
# Generamos las sumas 
# Vemos su resultado


def encoder_verificacion(bits:str):
    bits = [int(i) for i in bits]
    e1 = bits[0] ^ bits[1] ^ bits[2] 
    e2 = bits[0] ^ bits[1] ^ bits[3]
    e3 = bits[1] ^ bits[2] ^ bits[3]

    return e1, e2, e3

# 1100 , 1000-001
# 1+1+0 = 0, 1+0+0 = 0
# 1+1+0 = 0, 1+0+0 = 0
# 1+0+0 = 1, 0+0+0 = 0

# 


