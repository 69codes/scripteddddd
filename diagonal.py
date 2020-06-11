def diagonalDifference(arr):
    # let a be equal to the first figure since the first figure is the number of rows and wont be included in the calculations
    a = arr[0]
    # let b be equal to the amount of numbers left in the matrix which is just the square of the amount of rows, since its a square matrix
    b = a * a
    #then i delete the first number.. this is so that i am left with only what i will use in the calculation
    del(arr[0])
   # the first list is the first diagonal, starting ffrom index 0, the python notation is [start: stop : step] so in the case of list_1, we have 
   # start = 0 , stop = the index of the last number + 1, step = the number of row + 1.. 
                    1    2     3
                    4    5     6
                    7    8     9
      so list_1 for this example is (1 + 5 + 9)    which is    list_1 = sum(arr[0 : 10 : 4]
    list_1 =sum( arr[0 : (b+1) : (a+1)])
    ##   list_2 is the second diagonal, according to the example above will be, (3 + 5 + 7)    list_2 = sum(arr[2 : 7 : 2]) .. which follows
    the same explanation as above.
    
    list_2= sum (arr[(a-1): (b-a+1): (a-1)])
    # list_3 is the positive difference between list_1 and list_2
    list_3 = abs(list_1 - list_2)
    return (list_3)
