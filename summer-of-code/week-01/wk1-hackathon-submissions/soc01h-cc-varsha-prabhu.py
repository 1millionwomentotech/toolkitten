visited = list()


def check_around(x, y, rows, columns, land):
    global visited
    my_size = 1

    # Upper left corner
    if x > 0 and y > 0 and not visited[x-1][y-1] and land[x-1][y-1] == 1:
        visited[x-1][y-1] = True
        my_size += check_around(x - 1,  y - 1,  rows, columns, land)

    # Upper same column
    if x > 0 and not visited[x-1][y] and land[x-1][y] == 1:
        visited[x - 1][y] = True
        my_size += check_around(x - 1,  y, rows, columns, land)

    # Upper right corner
    if x > 0 and y < (columns-1) and not visited[x-1][y+1] and land[x-1][
        y+1] == 1:
        visited[x - 1][y + 1] = True
        my_size += check_around(x - 1,  y + 1,  rows, columns, land)

    # Same level left column
    if y > 0 and not visited[x][y-1] and land[x][y-1] == 1:
        visited[x][y - 1] = True
        my_size += check_around(x, y - 1,  rows, columns, land)

    # Same level right column
    if y < (columns-1) and not visited[x][y+1] and land[x][y+1] == 1:
        visited[x][y + 1] = True
        my_size += check_around(x, y + 1,  rows, columns, land)

    # Down left column
    if x < (rows-1) and y > 0 and not visited[x+1][y-1] and land[x+1][y-1] \
            == 1:
        visited[x + 1][y - 1] = True
        my_size += check_around(x + 1,  y - 1,  rows, columns, land)

    # Down same column
    if x < (rows-1) and not visited[x+1][y] and land[x+1][y] == 1:
        visited[x + 1][y] = True
        my_size += check_around(x + 1,  y, rows, columns, land)

    # Down right column
    if x < (rows-1) and y < (columns-1) and not visited[x+1][y+1] and land[
        x+1][y+1] == 1:
        visited[x + 1][y + 1] = True
        my_size += check_around(x + 1,  y + 1,  rows, columns, land)
    return my_size


def count_continents(land):
    global visited
    rows = len(land)
    if rows == 0:
        return 0
    columns = len(land[0])
    visited = [[False for j in range(0, columns)] for i in range(0, rows)]
    continent_sizes = list()
    for i in range(0, rows):
        for j in range(0, columns):
            if not visited[i][j] and land[i][j] == 1:
                visited[i][j] = True
                size = check_around(i, j, rows, columns, land)
                continent_sizes.append(size)
    return len(continent_sizes), continent_sizes


if __name__ == '__main__':
    land = [
        [0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0],
        [1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1],
        [0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0],
        [0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0],
        [1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0],
        [0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0]]
    print(count_continents(land))
