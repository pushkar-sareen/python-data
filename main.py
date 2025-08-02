data = [23,2,4,5,3,7,0,9,1,8,21]

def merge_sort(lst):
    if len(lst) <= 1:
        return lst
    
    mid = len(lst)//2
    left_side = merge_sort(lst[:mid])
    right_side = merge_sort(lst[mid:])
    return merge(left_side, right_side)

def merge(lst1, lst2):
    sorted_list = []
    i = 0
    j = 0
    while i < len(lst1) and j < len(lst2):
        if lst1[i] <= lst2[j]:
            sorted_list.append(lst1[i])
            i += 1
        else:
            sorted_list.append(lst2[j])
            j += 1
    sorted_list.extend(lst1[i:])
    sorted_list.extend(lst2[j:])
    return sorted_list


print(merge_sort(data))