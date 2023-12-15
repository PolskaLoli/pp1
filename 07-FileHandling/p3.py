array=[[3,7,2,],
       [4,2,5],
       [5,2,1]] 


row_sum=[sum(row) for row in array]
column_sum=[sum(column) for column in zip(*array)]

if row_sum==column_sum:
    print(True)
else:
    print(False)
