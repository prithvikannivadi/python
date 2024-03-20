# create a grocery list so you don't forget anything next time you go to the store!

grocery_list = {}
# prompt user for items, one per line"
while True:
    try:
        item = input("Item: ").upper()
        if item in grocery_list:
            grocery_list[item] += 1
        else:
            grocery_list[item] = 1

# control-d ends user input
    except EOFError:
# output user's grocery list in all upper, sorted alphabetically by item, prefixing each line with number of times that item was inputted

        for key in sorted(grocery_list.keys()):
            print(grocery_list[key], key)

        break
