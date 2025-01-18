def bubble_sort(my_list):
    """
    Sorts a list in ascending order using the bubble sort algorithm.

    Args:
    my_list (list): The input list to be sorted.

    Returns:
    list: The sorted list in ascending order.

    Time complexity: O(n^2), where n is the number of elements in the list.
    Space complexity: O(1), as sorting is done in-place.

    Note:
    - If the input list is empty, an empty list is returned.
    - This implementation modifies the original list in-place.

    Example:
    >>> bubble_sort([64, 34, 25, 12, 22, 11, 90])
    [11, 12, 22, 25, 34, 64, 90]
    """
    if not my_list:
        return []
    n = len(my_list)
    for i in range(n):
        for j in range(n - i - 1):
            if(my_list[j] > my_list[j + 1]):
                my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]
    return my_list

def insertion_sort(my_list):
    """
    Sorts a list using the insertion sort algorithm.

    Args:
    my_list (list): The input list to be sorted.

    Returns:
    list: The sorted list in ascending order.

    Time complexity: O(n^2), where n is the number of elements in the list.
    Space complexity: O(1), as sorting is done in-place.

    Note:
    This implementation modifies the original list in-place.
    """
    for i in range(len(my_list)):
        temp = my_list[i]
        j = i - 1
        while (temp < my_list[j]) and j > -1:
            my_list[j + 1] = my_list[j]
            my_list[j] = temp
            j -= 1
    return my_list

def selection_sort(my_list):
    """
    Sorts a list using the selection sort algorithm.

    Args:
    my_list (list): The input list to be sorted.

    Returns:
    list: The sorted list in ascending order.

    Time complexity: O(n^2), where n is the number of elements in the list.
    Space complexity: O(1), as sorting is done in-place.

    Note:
    This implementation modifies the original list in-place.
    """
    for i in range(len(my_list)-1):
        min_index = i
        for j in range(i+1, len(my_list)):
            if my_list[j] < my_list[min_index]:
                min_index = j
        if i != min_index:
            my_list[i], my_list[min_index] = my_list[min_index], my_list[i]
    return my_list

def swap(my_list, index1, index2):
    """
    Swaps two elements in a list.

    Args:
    my_list (list): The list containing elements to be swapped.
    index1 (int): The index of the first element to swap.
    index2 (int): The index of the second element to swap.

    Returns:
    list: The list with the swapped elements.

    Note:
    This function modifies the original list in-place.
    """
    my_list[index1], my_list[index2] = my_list[index2], my_list[index1]
    return my_list

def pivot(my_list, pivot_index, end_index):
    """
    Partitions a list around a pivot element.

    Args:
    my_list (list): The list to be partitioned.
    pivot_index (int): The starting index of the pivot element.
    end_index (int): The ending index of the partition range.

    Returns:
    int: The final position of the pivot element after partitioning.

    Note:
    This function modifies the original list in-place.
    """
    swap_index = pivot_index
    for i in range(pivot_index + 1, end_index + 1):
        if my_list[i] < my_list[pivot_index]:
            swap_index += 1
            swap(my_list, swap_index, i)
    swap(my_list, pivot_index, swap_index)   
    return swap_index

def quick_sort_helper(my_list, left, right):
    """
    Recursive helper function for quick sort algorithm.

    Args:
    my_list (list): The list to be sorted.
    left (int): The starting index of the current partition.
    right (int): The ending index of the current partition.

    Returns:
    list: The sorted list.

    Note:
    This function modifies the original list in-place.
    """
    if left < right:
        pivot_index = pivot(my_list, left, right)
        quick_sort_helper(my_list, left, pivot_index - 1)
        quick_sort_helper(my_list, pivot_index + 1, right)
    return my_list

def quick_sort(my_list):
    """
    Sorts a list using the quick sort algorithm.

    Args:
    my_list (list): The input list to be sorted.

    Returns:
    list: The sorted list.

    Time complexity: O(n log n) average case, O(n^2) worst case.
    Space complexity: O(log n) average case for call stack.

    Note:
    This function modifies the original list in-place.
    """
    return quick_sort_helper(my_list, 0, len(my_list) - 1)

def merge(list1, list2):
    """
    Merges two sorted lists into a single sorted list.

    Args:
    list1 (list): The first sorted list.
    list2 (list): The second sorted list.

    Returns:
    list: A new sorted list containing all elements from list1 and list2.

    Time complexity: O(n + m), where n and m are the lengths of list1 and list2 respectively.
    Space complexity: O(n + m) for the new combined list.

    Note:
    This function assumes that both input lists are already sorted in ascending order.
    """
    combined = []
    i = 0
    j = 0

    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            combined.append(list1[i])
            i += 1
        else:
            combined.append(list2[j])
            j += 1
    while i < len(list1):
        combined.append(list1[i])
        i += 1
    while j < len(list2):
        combined.append(list2[j])
        j += 1
    return combined


def merge_sort(my_list):
    """
    Sorts a list using the merge sort algorithm.

    Args:
    my_list (list): The input list to be sorted.

    Returns:
    list: A new sorted list containing all elements from the input list.

    Time complexity: O(n log n), where n is the number of elements in the list.
    Space complexity: O(n) due to the creation of new lists in the recursive calls.

    Note:
    This implementation does not modify the original list. Instead, it returns a new sorted list.
    """
    if len(my_list) == 1:
        return my_list
    mid_index = int(len(my_list) / 2)
    left = merge_sort(my_list[:mid_index])
    right = merge_sort(my_list[mid_index:])
    return merge(left, right)


if __name__ == '__main__':
    print("***********Bubble Sort***********")
    num = bubble_sort([64, 34, 25, 12, 22, 11, 90])
    print(num)
    print("***********End Bubble Sort***********")
    print("***********Insertion Sort***********")
    num = insertion_sort([64, 34, 25, 12, 22, 11, 90])
    print(num)
    print("***********End Insertion Sort***********")
    print("***********Selection Sort***********")
    num = selection_sort([64, 34, 25, 12, 22, 11, 90])
    print(num)
    print("***********End Selection Sort***********")
    print("***********Merge Sort***********")
    num = merge_sort([64, 34, 25, 12, 22, 11, 90])
    print(num)
    print("***********End Merge Sort***********")
    print("***********Quick Sort***********")
    num = quick_sort([64, 34, 25, 12, 22, 11, 90])
    print(num)
    print("***********End Quick Sort***********")