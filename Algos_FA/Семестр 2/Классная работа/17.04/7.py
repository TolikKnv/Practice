# from functools import cache

maze = ["S----", "##---", "---##", "----X"]


def labirint(road, row, col, visited=[], steps = []):
    if row < 0 or col < 0 or row >= len(road) or col >= len(road[0]):
        return []

    if road[row][col] == "#" or (row, col) in visited:
        return []
    if road[row][col] == "X":
        return steps
    visited.append([row, col])
    if len(visited)>1:
        if (visited[-1][0] - visited[-2][0] == 0) and (visited[-1][1] - visited[-2][1] == 1):
            steps.append('right')
        elif (visited[-1][0] - visited[-2][0] == 0) and (visited[-1][1] - visited[-2][1] == -1):
            steps.append('left')
        elif (visited[-1][0] - visited[-2][0] == 1) and (visited[-1][1] - visited[-2][1] == 0):
            steps.append('down')
        elif (visited[-1][0] - visited[-2][0] == -1) and (visited[-1][1] - visited[-2][1] == 0):
            steps.append('up')

    return (
        labirint(road, row - 1, col, visited) or
        labirint(road, row + 1, col, visited) or
        labirint(road, row, col - 1, visited) or
        labirint(road, row, col + 1, visited)
    )

print(labirint(maze, 0, 0))