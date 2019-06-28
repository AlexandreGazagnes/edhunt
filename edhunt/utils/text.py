def handle_none_values(l):
    return [(i, (j if j else "-")) for i, j in l]
