def contrived_func(val):
    """
    :param val: input value
    :type val: int
    :return: True or False
    :rtype: boolean
    """
    if val < 150 and val > 100:
        return True
    elif val * 5 < 361 and val / 2 < 24:
        if val == 6:
            return False
        else:
            return True
    elif (val > 75 or val / 8 < 10) and val ** val % 5 == 0:
        return True
    else:
        return False
