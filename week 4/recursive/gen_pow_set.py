def generatePowerSet(arr: list, result = None, realist = None):
    if result is None:
        result = []
    if realist is None:
        realist = []
    if not arr:
        realist.append(result)
        return realist
    first = arr[0]
    rest = arr[1:]
    
    generatePowerSet(rest, result, realist)
    generatePowerSet(rest, result + [first], realist)
    
    return realist

print(generatePowerSet([1, 2]))