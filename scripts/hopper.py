from collections import deque


def compute_available_spaces():
    try:
        grid_x, grid_y = list(map(int, input().split(" ")))
        matrix = [[0 for x in range(grid_x)] for y in range(grid_y)]
        start_x, start_y, end_x, end_y = list(map(int, input().split(" ")))
        no_of_obstacles = int(input())
        for _ in range(no_of_obstacles):
            obstacles_x1, obstacles_x2, obstacles_y1, obstacles_y2 = list(map(int, input().split(" ")))
            for x in range(obstacles_x1, obstacles_x2 + 1):
                for y in range(obstacles_y1, obstacles_y2 + 1):
                    if x == end_x and y == end_y:
                        return -1  # Assumption: End x,y should not be occupied
                    if x != start_x or y != start_y:
                        matrix[x][y] = 1
        return get_hopper_shortest_path(end_x, end_y, start_x, start_y, 0, 0, grid_x, grid_y, matrix)
    except Exception as e:
        print(e)
        return -1


def get_next_positions(speed_x, speed_y, current_x, current_y, grid_x, grid_y, matrix):
    neighbours = []
    for i in range(-1, 2):
        for j in range(-1, 2):
            new_x = speed_x + i + current_x
            new_y = speed_y + j + current_y
            if (0 <= new_x < grid_x) and (0 <= new_y < grid_y) and (matrix[new_x][new_y] == 0):
                neighbours.append((new_x, new_y, speed_x + i, speed_y + j))
    return neighbours


def get_hopper_shortest_path(end_x, end_y, start_x, start_y, speed_x, speed_y, grid_x, grid_y, matrix):
    queue = deque()
    queue.append((start_x, start_y, speed_x, speed_y))
    visited = set()
    moves = 0
    while queue:
        n = len(queue)
        for _ in range(n):
            a, b, current_speed_x, current_speed_y = queue.popleft()
            visited.add((a, b, current_speed_x, current_speed_y))
            if a == end_x and b == end_y:
                return moves
            neighbours = get_next_positions(current_speed_x, current_speed_y, a, b, grid_x, grid_y, matrix)
            for neighbour in neighbours:
                if neighbour not in visited:
                    queue.append(neighbour)
        moves += 1
    return -1


def main():
    no_of_test_cases = int(input())
    for _ in range(no_of_test_cases):
        no_of_hops = compute_available_spaces()
        if no_of_hops == -1:
            print("No solution.")
        else:
            print("Optimal solution takes {} hops.".format(no_of_hops))


if __name__ == "__main__":
    main()
