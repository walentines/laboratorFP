def validate_id_year(id):
    try:
        id = int(id)
        return True
    except:
        print("Introdu un integer valid!")
        return False


def validate_cnp(cnp):
    try:
        cnp = int(cnp)
    except:
        print("Introdu un integer valid!")
        return False
    if (cnp // 10000000000000 == 0 and cnp // 1000000000000 != 0):
        return True
    print("Introdu un cnp valid!")
    return False
