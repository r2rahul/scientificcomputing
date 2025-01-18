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


if __name__ == '__main__':
    num = bubble_sort([64, 34, 25, 12, 22, 11, 90])
    print(num)