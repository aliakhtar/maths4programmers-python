def standard_form(v1, v2):
    x1, y1 = v1
    x2, y2 = v2

    a = y2 - y1
    b = x1 - x2
    c = (x1 * y2) - (x2 * y1)

    return a, b, c
