def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair


def car(cons):
    def left(a, b):
        return a
    return cons(left)


def cdr(cons):
    def right(a, b):
        return b
    return cons(right)


print(car(cons(3,4)))

print(cdr(cons(3, 4)))