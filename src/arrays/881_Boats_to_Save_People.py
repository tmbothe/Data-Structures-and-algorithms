def numRescueBoats(people, limit):
    boats = 0
    people.sort()

    left = 0, right = len(people)-1

    while left <= right:
        if left == right:
            boats += 1
            break
        current = people[left]+people[right]

        if current <= limit:
            left += 1
        boats += 1
        right -= 1

    return boats
