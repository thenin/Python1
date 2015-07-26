from func import triangle_area, f_to_c

__author__ = 'kguryanov'

precision = 0.00001
fails = 0
tries = 0


def test(got, expected):
    global tries
    global fails
    tries += 1
    if got == expected:
        prefix = ' OK '
    elif close_enough(got, expected):
        prefix = ' CEOK '
    else:
        prefix = '  X '
        fails += 1
    print('%6s got: %s expected: %s ' % (prefix, repr(got), repr(expected)))


def close_enough(actual, expected):
    try:
        res = abs(actual / expected - 1)
        result = res <= precision
    except TypeError:
        result = False
    return result


def abs(value):
    result = value
    if value < 0:
        result = -value
    return result

    # test for test


test(10, "10")

# tests for triangle area
test(triangle_area(10, 10), 50)
test(triangle_area(10, 20), 100)
test(triangle_area(2, 3), 3)

# tests for F to C conversion

test(f_to_c(1), -17.2222)
test(f_to_c(1), 17.2222)
test(f_to_c(0), -17.7778)
test(f_to_c(100), 37.7778)
test(f_to_c(32), 0)
test(f_to_c(212), 100)
test(f_to_c(-459.67), -273.15)
print('%s tries, %s failes' % (repr(tries), repr(fails)))
