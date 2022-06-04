# return masked string
def maskify(cc):
    num = len(cc)
    num4 = num - 4
    anw = cc[-4:]
    while num4 > 0:
        anw = '#' + anw
        num4 -= 1

    cc_list = []
    cc_list[:] = cc
    return anw
    pass