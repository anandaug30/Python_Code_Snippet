"""display given RxC in spiral model"""

def spiral_display(matrix):
    result = []
    if len(matrix) == 0:
        return result
    else:
        col_index = len(matrix[0])-1
        row = 0
        col = 0
        row_index = len(matrix)-1
        while row <= col_index and col <= col_index:
            # left to right
            print("")
            for i in range(row, col_index+1):
                result.append(matrix[row][i])
                print(matrix[row][i], end=" ")
            col += 1
            # top to bottom
            print("")
            for i in range(col, row_index+1):
                result.append(matrix[i][col_index])
                print(matrix[i][col_index], end=" ")
            col_index -= 1
            # right to left
            print("")
            if col <= row_index:
                for i in range(col_index, row-1):
                    result.append(matrix[row_index][i])
                    print(matrix[row_index][i], end=" ")

                row_index -= 1
            # bottom to top
            print("")
            if row <= col_index:
                for i in range(row_index, col-1, -1):
                    result.append(matrix[i][row])
        return result

my_list = [
    list(range(1, 5)), list(range(5, 9)), list(range(9, 13)), list(range(13, 17))]

for row in my_list:
    for col in row:
        print(col, end="  ")
    print("")

result = spiral_display(my_list)
print(result)
