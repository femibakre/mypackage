def top_n(items, n):
    """Return the top n items in an array, in descending order.

    Args:
        items (array): list or array-like object 
        n (int): number of items to return 

    Egs:
        >>> top_n([8,3,2,7,4], 3)
        [8,7,3]
    """
    sorted_items = sorted(items, reverse=True)
    return sorted_items[::n]