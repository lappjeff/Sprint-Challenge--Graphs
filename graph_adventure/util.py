class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

class Stack():
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)

# does a fairly standard BFS on the current_path dict passed to it
def not_visited(current_path, room_id, player):
    # set of visited vertexs
    visited = set()

    # queue for storage
    q = Queue()
    # assign starting path to be an int array [0]
    path = [room_id]
    # enqueue the path to queue
    q.enqueue(path)

    # while queue still has items in it
    while q.size() > 0:
        # assign var p to be dequeue queue int array
        # [0]
        p = q.dequeue()
        # assign v to the first item of int array p
        # 0
        v = p[0]

        # is v is unvisited, vertex with unknown exit is found
        if v == '?':
            # assign path to all values from index 1 on, ie removing the ?
            path = p[1:]
            # break out of for loop - otherwise ? will be added into the 'visited' set
            break
        # if vertex not visited yet
        if v not in visited:
            # add vertex to visited
            visited.add(v)

            # for each neighbor direction(n,s,w,e) in current_path dict
            # ie each item in nested dictionary in current_path dict
            for neighbor in current_path[v]:
                # node is current_path[vertex][neighbor] where vertex is integer key and neighbor is direction string
                node = current_path[v][neighbor]
                # make a pass by value copy of p to avoid mutating original p
                new_path = p.copy()
                # add each neighbor node to new_path at 0'th index
                new_path.insert(0, node)
                # enqueue the new path
                q.enqueue(new_path)

    # keep track of directions player needs to move to get to room with unvisited exits here
    player_move_directions = []

    # while path still has length
    while len(path) > 1:
        # remove the last item from path and assign to current var
        # current is the last room visited
        current = path.pop(-1)

        # for every route in current_path dict at key current, ie last room visited id
        for route in current_path[current]:
            # if the current_path[last room visited id][string direction(n,s,w,e)] is the same as the last item
            # in the path
            if current_path[current][route] == path[-1]:
                # tell player to move that direction
                player_move_directions.append(route)

    # run all moves in player directions
    for move in player_move_directions:
        player.travel(move)

    # return directions to be used in traversalPath
    return player_move_directions
    
def reverse_direction(direction):
    if direction is 'n':
        switch_direction = 's'
    elif direction is 's':
        switch_direction = 'n'
    elif direction is 'e':
        switch_direction = 'w'
    elif direction is 'w':
        switch_direction = 'e'

    return switch_direction
