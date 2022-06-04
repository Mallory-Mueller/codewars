seconds=665
m, s = divmod(seconds, 60)
h, m = divmod(m, 60)
print('{:d}:{:02d}:{:02d}'.format(h, m, s))


def make_readable(seconds):
    m, s = divmod(seconds, 60)
    h, m = divmod(m, 60)
    return('{:00}:{:00}:{:00}'.format(h, m, s))