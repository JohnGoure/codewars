def linear_search(arr, val):
    for x in range(len(arr) - 1, -1, -1):
        print("Comparing " + str(arr[x]) + " with " + str(val) + ".")
        if arr[x] == val:
            return True
    return None
searchfor = input("Please give me a number to search for: ")
print(linear_search([1, 2, 3, 4, 5, 6], int(searchfor)))
