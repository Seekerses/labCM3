class RequirementException(Exception):
    pass


class BadParamsExceptions(Exception):
    pass


def validate(func, a, b, min_intervals, max_intervals):
    if b < a:
        raise BadParamsExceptions
    if max_intervals < min_intervals:
        raise BadParamsExceptions
    if min_intervals < 1:
        raise BadParamsExceptions
    if round(min_intervals) != min_intervals or round(max_intervals) != max_intervals:
        raise BadParamsExceptions
    return True


def rectangles_left(func, a, b, accuracy, min_intervals, max_intervals):
    if not validate(func, a, b, min_intervals, max_intervals):
        return
    prev_int_sum = accuracy * 2
    int_sum = 0
    n = min_intervals / 2
    while abs(int_sum - prev_int_sum) > accuracy and n < max_intervals:
        n *= 2
        prev_int_sum = int_sum
        int_sum = 0
        delta = (b - a) / n
        x = a
        while x < b:
            int_sum += func(x) * delta
            x += delta
    return [[round(int_sum, digit_count(accuracy)), n]]


def rectangles_right(func, a, b, accuracy, min_intervals, max_intervals):
    if not validate(func, a, b, min_intervals, max_intervals):
        return
    prev_int_sum = accuracy * 2
    int_sum = 0
    n = min_intervals / 2
    while abs(int_sum - prev_int_sum) > accuracy and n < max_intervals:
        n *= 2
        prev_int_sum = int_sum
        int_sum = 0
        delta = (b - a) / n
        x = a
        while x < b:
            int_sum += func(x + delta) * delta
            x += delta
    return [[round(int_sum, digit_count(accuracy)), n]]


def rectangles_middle(func, a, b, accuracy, min_intervals, max_intervals):
    if not validate(func, a, b, min_intervals, max_intervals):
        return
    prev_int_sum = accuracy * 2
    int_sum = 0
    n = min_intervals / 2
    while abs(int_sum - prev_int_sum) > accuracy and n < max_intervals:
        n *= 2
        prev_int_sum = int_sum
        int_sum = 0
        delta = (b - a) / n
        x = a
        while x < b:
            int_sum += func(x + delta / 2) * delta
            x += delta
    return [[round(int_sum, digit_count(accuracy)), n]]


def trapeze(func, a, b, accuracy, min_intervals, max_intervals):
    if not validate(func, a, b, min_intervals, max_intervals):
        return
    prev_int_sum = accuracy * 2
    int_sum = 0
    n = min_intervals / 2
    while abs(int_sum - prev_int_sum) > accuracy and n < max_intervals:
        n *= 2
        prev_int_sum = int_sum
        int_sum = 0
        delta = (b - a) / n
        x = a
        while x < b:
            int_sum += (func(x) + func(x + delta)) / 2 * delta
            x += delta
    return [[round(int_sum, digit_count(accuracy)), n]]


def simpson(func, a, b, accuracy, min_intervals, max_intervals):
    if not validate(func, a, b, min_intervals, max_intervals):
        return
    prev_int_sum = accuracy * 2
    int_sum = 0
    if min_intervals % 2 == 0:
        n = min_intervals / 2
    else:
        n = (min_intervals - 1) / 2
    while abs(int_sum - prev_int_sum) > accuracy and n < max_intervals:
        n *= 2
        prev_int_sum = int_sum
        int_sum = 0
        delta = (b - a) / n
        x = a
        while x + delta < b:
            int_sum += (func(x) + 4 * func(x + delta) + func(x + 2 * delta)) * delta / 3
            x += delta * 2
    return [[round(int_sum, digit_count(accuracy)), n]]


def digit_count(val):
    exponential = "{:e}".format(val)
    exponential = exponential.split("e")
    exponential = exponential[1]
    exponential = exponential[1: len(exponential)]
    return int(exponential)
