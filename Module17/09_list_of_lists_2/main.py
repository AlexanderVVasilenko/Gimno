nice_list = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]],
             [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]

very_nice_list = [x for each_list in nice_list for each_list2 in each_list for x in each_list2]
print(very_nice_list)
