def ToIntArray(path):
    returnArray = []
    with open(path) as f:
        for line in f:
            returnArray.append(int(line))

    return returnArray

def ToStringArray(path):
    returnArray = []
    with open(path) as f:
        returnArray = f.readlines()

    return returnArray