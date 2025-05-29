list1 = input("Enter the first list of numbers separated by spaces: ")
list1 = [int(x) for x in list1.split()]
list2 = input("Enter the second list of numbers separated by spaces: ")
list2 = [int(x) for x in list2.split()]

# comparing the length
if len(list1) > len(list2):
    print("The first list is longer than the second list.")
elif len(list1) < len(list2):
    print("The second list is longer than the first list.")
else:
    print("Both lists are of the same length.")

# comparing the sums
sum1 = sum(list1)
sum2 = sum(list2)

if sum1 > sum2:
    print("The sum of the first list is greater than the sum of the second list.")
elif sum1 < sum2:
    print("The sum of the second list is greater than the sum of the first list.")
else:
    print("Both lists have the same sum.")

# comparing the elements
if set(list1) == set(list2):
    print("Both lists contain the same elements.")
else:
    print("The lists contain different elements.")