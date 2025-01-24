import bubble_sort, selection_sort, insertion_sort, quick_sort, merge_sort, heap_sort


def perform_sorting(sorting_method, array_to_sort):
    if sorting_method == 'bubble':
        return bubble_sort.improved_bubble_sort(array_to_sort)
    elif sorting_method == 'selection':
        return selection_sort.selection_sort(array_to_sort)
    elif sorting_method == 'insertion':
        return insertion_sort.insertion_sort(array_to_sort)
    elif sorting_method == 'quick':
        return quick_sort.quick_sort(array_to_sort)
    elif sorting_method == 'merge':
        return merge_sort.merge_sort(array_to_sort)
    elif sorting_method == 'heap':
        return heap_sort.heap_sort(array_to_sort)
    else:
        bubble_sort.improved_bubble_sort(array_to_sort)
        selection_sort.selection_sort(array_to_sort)
        insertion_sort.insertion_sort(array_to_sort)
        quick_sort.quick_sort(array_to_sort)
        merge_sort.merge_sort(array_to_sort)
        heap_sort.heap_sort(array_to_sort)
        return 'Sorting using all the algorithm is done, to check the output call them individually.'



if __name__ == '__main__':
    sorting_method_to_use='megrge'
    array_to_sort = [4,3,7,1,9,10,2,5]
    print(perform_sorting(sorting_method_to_use, array_to_sort))
