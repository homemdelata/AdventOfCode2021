def ToIntArray(path):
    returnArray = []
    with open(path) as f:
        for line in f:
            returnArray.append(int(line))

    return returnArray