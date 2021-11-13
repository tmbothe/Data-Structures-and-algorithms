import itertools


def flatten(nums):
    """flatten a list: [1,2,[3,4. [5],[6,7,[8,[9]]]]]
    """
    result = []
    for num in nums:
        print(result)
        if type(num) is list:
            for i in num:
                if type(i) is list:
                    result.extend(i)
                else:
                    result.append(i)
        else:
            result.append(num)

    return result


def flatten(L):

    if len(L) == 1:

        if type(L[0]) == list:

            result = flatten(L[0])

        else:

            result = L

    elif type(L[0]) == list:

        result = flatten(L[0]) + flatten(L[1:])

    else:

        result = [L[0]] + flatten(L[1:])

    return result


def flatten_without_rec(non_flat):

    flat = []

    while non_flat:  # runs until the given list is empty.

        e = non_flat.pop()

        if type(e) == list:  # checks the type of the poped item.

            non_flat.extend(e)  # if list extend the item to given list.
        else:

            flat.append(e)  # if not list then add it to the flat list.

    flat.sort()

    return flat


if __name__ == '__main__':
    from iteration_utilities import deepflatten
    nums = [1, 2, [3, 4., [5], [6, 7, [8, [9]]]]]

    print(flatten(nums))

    # print(joinedlist=list(itertools.chain(*nums)))

    flatten_list = list(deepflatten(nums))

    print(flatten_list)

    print(flatten(nums))

    print(flatten_without_rec(nums))
