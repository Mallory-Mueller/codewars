def xo(s):
    x=s.lower()
    count_x= x.count("x")
    count_o= x.count("o")

    if count_x ==count_o:
        return True
    else:
        return False
    