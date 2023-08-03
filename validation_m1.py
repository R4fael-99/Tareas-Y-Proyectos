def valInt(arg, interval=None):
    if not isinstance(arg, int):
        return False

    if interval is None:
        return True
    elif isinstance(interval, (tuple, list)):
        if len(interval) == 2 and all(isinstance(val, (int, float)) for val in interval):
            if interval[0] < interval[1]:
                return interval[0] < arg < interval[1] if isinstance(interval, tuple) else interval[0] <= arg <= interval[1]
            else:
                raise ValueError("(ValueError) El intervalo debe estar ordenado de manera creciente.")
        else:
            raise ValueError("(ValueError) El intervalo debe contener exactamente dos valores numéricos.")
    else:
        raise TypeError("(TypeError) El segundo argumento debe ser una lista o una tupla de dos valores numéricos.")

def valFloat(arg, interval=None):
    if isinstance(arg, int) or isinstance(arg, float):
        if interval is None:
            return isinstance(arg, float)
        elif isinstance(interval, (tuple, list)):
            if len(interval) == 2 and all(isinstance(val, (int, float)) for val in interval):
                if interval[0] < interval[1]:
                    return interval[0] < arg < interval[1] if isinstance(interval, tuple) else interval[0] <= arg <= interval[1]
                else:
                    raise ValueError("(ValueError) El intervalo debe estar ordenado de manera creciente.")
            else:
                raise ValueError("(ValueError) El intervalo debe contener exactamente dos valores numéricos.")
        else:
            raise TypeError("(TypeError) El segundo argumento debe ser una lista o una tupla de dos valores numéricos.")
    else:
        return False

def valComplex(arg, interval=None):
    if isinstance(arg, complex):
        if interval is None:
            return True
        elif isinstance(interval, (tuple, list)):
            if len(interval) == 2 and all(isinstance(val, (int, float)) for val in interval):
                if interval[0] < interval[1]:
                    return interval[0] < abs(arg) < interval[1] if isinstance(interval, tuple) else interval[0] <= abs(arg) <= interval[1]
                else:
                    raise ValueError("(ValueError): El intervalo debe estar ordenado de manera creciente.")
            else:
                raise ValueError("(ValueError): El intervalo debe contener exactamente dos valores numéricos.")
        else:
            raise TypeError("(TypeError): El segundo argumento debe ser una lista o una tupla de dos valores numéricos.")
    else:
        return False

def valList(arg1, arg2=None, arg3=None):
    if arg2 is None and arg3 is None:
        return isinstance(arg1, list)

    if arg2 is not None and arg3 == 'len':
        if isinstance(arg1, list) and isinstance(arg2, int):
            return len(arg1) == arg2
        else:
            raise TypeError("(TypeError): Los tipos de argumentos no son válidos para la opción 'len'.")
    
    if arg2 is not None and arg3 == 'value':
        if isinstance(arg1, list) and isinstance(arg2, list):
            return arg1 == arg2
        else:
            raise TypeError("(TypeError): Los tipos de argumentos no son válidos para la opción 'value'.")
    
    raise ValueError("(ValueError): El tercer argumento debe ser 'len' o 'value'.")
    