def display(list):
    count = 0
    for item in list:
        count+=1
        print(count, item)

def length(list):
    return len(list)


def create():

    list = []

    how_many_items = input("How many items do you need? ")
    how_many_items = int(how_many_items)

    for item_number in range(how_many_items):
        item = input("New item: ")
        list.append(item)

    return list
