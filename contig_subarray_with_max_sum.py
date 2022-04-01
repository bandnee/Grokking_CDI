

#First express in language
'''
sliding window    max_cur_sum = [sw_sum + cur_ele > cur_ele keep]       m
1                                             1
1 -2  [-1>-2 keep]                               1
1 -2 1 [0<1 drop]                             1
1,3    [4>3 keep]                             4
1,3,4 [8>3 keep]                              8
1,3,4,-7 [8+-7>-7 keep]                          8
1,3,4,-7,6 [7>6 keep]                         8
'''
arr1 = [1,-2,1,3,-3,4,-7,6,-1,2]
#Start with the first element and keep increasing the index 
max_sum = arr1[0]
max_cur_sum = arr1[0]
for i in range(1,len(arr1)):
    max_cur_sum = max(arr1[i],  max_cur_sum + arr1[i])
    max_sum = max(max_cur_sum,max_sum)

print max_sum
