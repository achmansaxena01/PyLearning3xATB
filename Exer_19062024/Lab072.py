numbers = [1, 2, 3]


# Collection of Items
def do_something(pramod_list):
    pramod_list.append(4)
    pramod_list.append(100)
    pramod_list[0] += 5
    return pramod_list


numbers.append(10)
l = do_something(numbers)
print(l)
