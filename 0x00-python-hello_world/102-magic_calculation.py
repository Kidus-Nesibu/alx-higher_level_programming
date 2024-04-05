import dis
def magic_calculation(a, b):
    result = 98
    result = a + b ** result
    return result
dis.dis(magic_calculation)
