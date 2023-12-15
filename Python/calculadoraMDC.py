
## To work better, A > B
def mdc(a, b):
    if b == 0:
        return a
    return mdc(b, a % b)





