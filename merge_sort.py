# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def my_merge(left_arr, right_arr):
    i = 0
    j = 0
    m = []
    print(left_arr)
    print(right_arr)
    for k in range(2*len(left_arr)):
        print(m)
        if left_arr[i] < right_arr[j]:
            m.append(left_arr[i])
            i = i+1
            if i == len(left_arr):
                while j < len(left_arr):
                    m.append(right_arr[j])
                    j = j+1
        else:
            m.append(right_arr[j])
            j = j+1
            if j == len(right_arr):
                while i < len(left_arr):
                    m.append(left_arr[i])
                    i = i+1
    return m


def split(inp_arr):
    n = len(inp_arr)
    print(n)
    if n == 1:
        return inp_arr
    else:
        return [inp_arr[0:int(n/2)], inp_arr[int(n/2):n]]


def my_merge_sort(left_arr, right_arr):
    if len(left_arr) == 1 and len(right_arr) == 1:
        if left_arr[0] < right_arr[0]:
            return [left_arr[0], right_arr[0]]
        else:
            return [right_arr[0], left_arr[0]]
    else:
        left_split = split(left_arr)
        left_output = my_merge_sort(left_split[0], left_split[1])
        right_split = split(right_arr)
        right_output = my_merge_sort(right_split[0], right_split[1])
        return my_merge(left_output, right_output)


input_arr = [4, 3, 2, 1, 7, 6, 5, 8]
print(input_arr)
print(my_merge_sort(input_arr[0:4], input_arr[4:8]))






# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
