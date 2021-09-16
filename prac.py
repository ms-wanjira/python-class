s='python'
print(s[-1::-1])

x=[[1,2,3],
    [2,7,9]]
print(x[1][-1])


c={2,0.1,1}
print(type(c))


def FindDuplicates(elements):
    duplicates , seen =set(), set()
    for element in elements:
        if element in seen:
            duplicates.add(element)
            seen.add(element)
            return list(duplicates)
