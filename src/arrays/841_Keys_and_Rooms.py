def canVisitAllRooms(rooms):

    visited = [False]*len(rooms)
    
    visited[0] = True
    stack =[0]

    while stack:
        node = stack.pop()
        for neighbor in rooms[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                stack.append(neighbor)

    return all(visited)



if __name__ =='__main__':

    rooms = [[1],[2],[3],[]] #Output: true
    print(canVisitAllRooms(rooms))

    rooms = [[1,3],[3,0,1],[2],[0]] #Output: false

    print(canVisitAllRooms(rooms))