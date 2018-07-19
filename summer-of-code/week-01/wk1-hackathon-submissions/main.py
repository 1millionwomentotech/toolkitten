import continent_counter


def main():
    coordinates = (5, 5)
    list_of_close_tiles = continent_counter.add_default_coordinates(coordinates)
    list_of_tiles = continent_counter.generate_random_world()
    sorted_list_of_tiles = continent_counter.sort_list_of_tiles_by_x_y(list_of_tiles)
    list_of_close_tiles = continent_counter.count_area(sorted_list_of_tiles, coordinates, list_of_close_tiles)
    print(list_of_close_tiles)
    print("The area of your continent is: " + str(len(list_of_close_tiles)))


if __name__ == '__main__':
    main()
