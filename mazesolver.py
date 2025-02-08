def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def get_neighbors(pos, maze, visited):
    rows, cols = len(maze), len(maze[0])
    neighbors = [(pos[0] + dx, pos[1] + dy) for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]]
    return [n for n in neighbors if 0 <= n[0] < rows and 0 <= n[1] < cols and maze[n[0]][n[1]] == 0 and n not in visited]

def bidirectional_maze_solver(maze, start, end):
    start_queue, end_queue = [start], [end]
    start_visited, end_visited = {start: None}, {end: None}
    
    while start_queue and end_queue:
        start_current = start_queue[0]
        end_current = end_queue[0]
        
        if start_current == end_current:
            return reconstruct_path(start_visited, end_visited, start_current)
        
        start_queue.pop(0)
        for neighbor in get_neighbors(start_current, maze, start_visited):
            start_visited[neighbor] = start_current
            start_queue.append(neighbor)
            if neighbor in end_visited:
                return reconstruct_path(start_visited, end_visited, neighbor)
        
        end_queue.pop(0)
        for neighbor in get_neighbors(end_current, maze, end_visited):
            end_visited[neighbor] = end_current
            end_queue.append(neighbor)
            if neighbor in start_visited:
                return reconstruct_path(start_visited, end_visited, neighbor)
    
    return brute_force_solver(maze, start, end)  

def reconstruct_path(start_visited, end_visited, meeting_point):
    path = []
    current = meeting_point
    while current is not None:
        path.append(current)
        current = start_visited[current]
    path.reverse()
    current = end_visited[meeting_point]
    while current is not None:
        path.append(current)
        current = end_visited[current]
    return path

def brute_force_solver(maze, start, end):
    queue = [(start, [start])]
    visited = {start}
    while queue:
        current, path = queue[0]
        queue.pop(0)
        if current == end:
            return path
        for neighbor in get_neighbors(current, maze, visited):
            queue.append((neighbor, path + [neighbor]))
            visited.add(neighbor)
    return None

maze = [
    [0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 0],
    [1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1],
    [1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1],
    [1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 0, 1],
    [0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0]
]

start = (0, 0)
end = (10, 19)
solution = bidirectional_maze_solver(maze, start, end)
print("Çözüm Yolu:" if solution else "Çözüm bulunamadı", solution)
