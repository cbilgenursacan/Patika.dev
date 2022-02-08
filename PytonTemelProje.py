#Q1)
flat_list = list()
def flatter(ls):
    for layer in ls:
        if type(layer) == list:
            flatter(layer)
        else:
            flat_list.append(layer)
            
ex = [[1, 'a', ['cat'], 2], [[[3]]], 'dog', 4, 5]
flatter(ex)
print(f"First Answer: {flat_list}")

print("***************************************************")

#Q2)
reverse_list = list()
def reverser(ls):
    for layer in sorted(ls, reverse=True):
        reverse_list.append(sorted(layer, reverse=True))
ex2 = [[1, 2], [3, 4], [5, 6, 7]]
reverser(ex2)
print(f"Second Answer: {reverse_list}")