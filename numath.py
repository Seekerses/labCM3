# Ошибка, вызываемая при непрохождении условий сходимости метода
class RequirementException(Exception):
    pass
# Ошибка, вызываемая в случае выхода корня за пределы интервала
class RootOutOfRange(Exception):
    pass

# Производная функции в точке
def derivate(function, x):
    delta = 10E-6;
    return round((function(x + delta) - function(x - delta))/(2*delta), 4)

# Вторая производная функции в точке
def secDerivate(function, x):
    delta = 10E-6;
    return round(derivate(function, x + delta) - derivate(function, x - delta)/(2*delta), 4)

# Проверка на монотонность первой И второй производной функции на промежутке
def derivativeCheck(function, a, b):
    delta = abs( b - a )/10E+3
    isPositive = False
    isPositive2 = False
    i = 0
    while ( derivate(function, a + i) == 0):
        i += delta
    if ( derivate(function, a + i) > 0):
        isPositive = True
    i = 0
    while ( secDerivate(function, a + i) == 0):
        i += delta
    if ( secDerivate(function, a + i ) > 0):
        isPositive2 = True
    i = delta
    while (a + i < b):
        firstDer = derivate(function, a + i)
        secondDer = secDerivate(function, a + i)
        if ((firstDer > 0) != isPositive) and (firstDer != 0):
            return False
        if ((secondDer > 0) != isPositive2) and (secondDer != 0):
            return False
        i += delta
    return True

# Метод, контроллирующий выполнение метода хорд
def Hordes(function, a, b, acc):
    if not hordesCheck(function, a, b):
        raise RequirementException
    return HordesMethod(function, a, b, acc)

# Вычислительный метод метода хорд
def HordesMethod(function, a, b, acc):
    data = []
    f = function
    if(f(a) * secDerivate(function, a) > 0):
        prev = a
        x = b
        while (abs(f(x) - f(prev)) > acc and abs(f(x)) > acc):
            prev = x
            x = a - ((x - a)/(f(x) - f(a))) * f(a)
            data.append([a, prev, x, f(a), f(prev), f(x), abs(f(x) - f(prev))])
        return data
    else:
        prev = b
        x = a
        while (abs(f(x) - f(prev)) > acc and abs(f(x)) > acc):
            prev = x
            x = x - ((b - x)/(f(b) - f(x))) * f(x)
            data.append([a, prev, x, f(a), f(prev), f(x), abs(f(x) - f(prev))])
        return data

# Проверка условий, необходимый для выполнения метода хорд
def hordesCheck(function, a, b):
    if (function(a) * function(b) < 0 and derivativeCheck(function, a , b)):
        return True
    else:
        return False

# Метод, контроллирующий выполнения метода Ньютона
def Newton(function, a, b, approx, acc):
    if not NewtonCheck(function, a,b):
        raise RequirementException
    return NewtonMethod(function, a, b, approx, acc)

# Метод, проверяющий условия, необходимые для корректного выполнения метода Ньютона
def NewtonCheck(function, a, b):
    if (function(a) * function(b) < 0 and derivativeCheck(function, a, b)):
        i = 0;
        delta = abs(b - a)/10E+3
        while (a + i) < b:
            if(derivate(function, a + i) != 0):
                return True
            i += delta
        return False
    else:
        return False

# Вычислительный метод метода Ньютона
def NewtonMethod(function,  a, b, approx, acc):
    prev = 0
    data = []
    if (function(a) * secDerivate(function, a) > 0):
        approx = a
    elif (function(b) * secDerivate(function, b) > 0):
        approx = b
    while(abs(approx - prev) > acc and abs(function(approx)/derivate(function, approx)) > acc and abs(function(approx)) > acc):
        prev = approx
        approx = approx - function(approx)/derivate(function, approx)
        data.append([prev, function(prev), derivate(function, prev), approx, abs(approx - prev)])
    prev = approx
    approx = approx - function(approx)/derivate(function, approx)
    data.append([prev, function(prev), derivate(function, prev), approx, abs(approx - prev)])
    return data

# Метод, контроллирующий выполнение метода простых итераций
def Iteration(function, a, b, approx, acc):
    if not IterationCheck(function, a, b):
        raise RequirementException
    return IterationMethod(function, a, b, approx, acc)

# Метод для поиска максимума производной функции на отрезке
# если максимум стремится к 0, то возвращает 1 или -1 (зависит соответственно от ближайших к 0 значений)
def MaxDeriativeOnInterval(function, a, b):
    delta = abs(b - a)/1000
    i = delta
    max = -2
    dangerousPoint = 0
    maxPoint = a-1
    while(a + i) < b:
        der = derivate(function, a + i)
        if der == 0:
            dangerousPoint = a+i
        if(der > max and der != 0):
            max = der
            maxPoint = a+i
        i += delta
    if (dangerousPoint + delta == maxPoint or dangerousPoint - i == maxPoint):
        if (max > 0):
            return 1
        else:
            return -1
    return max

# Метод для поиска значения Q
def MaxQOnInterval(function, a, b):
    delta = abs(b - a)/1000
    i = delta
    max = -2
    while(a + i) < b:
        der = abs(derivate(function, a + i))
        if(der > max and der != 0):
            max = der
        i += delta
    return max

# Вычислительный метод метода простых итераций
def IterationMethod(function, a, b, approx, acc):
    maxDer = MaxDeriativeOnInterval(function, a, b)
    f = lambda x: x + function(x) * (-1/maxDer)
    prev = 1000000
    q = MaxQOnInterval(f, a, b)
    data = []
    iterCount = 0
    if (q > 0.5):
        while(abs(approx - prev) >= acc * (1-q)/(q)):
            prev = approx
            approx = f(approx)
            if (approx < a or approx > b):
                raise RootOutOfRange
            data.append([prev, approx, f(approx), function(approx), abs(approx - prev)])
    else:
        while(abs(approx - prev) >= acc):
            prev = approx
            approx = f(approx)
            if (approx < a or approx > b):
                raise RootOutOfRange
            data.append([prev, approx, f(approx), function(approx), abs(approx - prev)])
    return data

# Метод, проверяющий условия, необходимые для корректного выполнения метода простых итераций
def IterationCheck(function, a, b):
    delta = abs(b - a)/10E+3
    i = 0
    while (a + i) < b:
        der = abs(derivate(function, a+i))
        if(der > 1):
            return False
        i += delta
    return True