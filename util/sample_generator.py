# Sample Python code that can be used to generate rooms in
# a zig-zag pattern.
#
# You can modify generate_rooms() to create your own
# procedural generation algorithm and use print_rooms()
# to see the world.

from django.contrib.auth.models import User
from adventure.models import Player, Room


Room.objects.all().delete()

from random import seed
from random import randint

seed(1)


class Room:
    def __init__(self, id, name, description, x, y):
        self.id = id
        self.name = name
        self.description = description
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
        self.x = x
        self.y = y

    def __repr__(self):
        if self.e_to is not None:
            return f"({self.x}, {self.y}) -> ({self.e_to.x}, {self.e_to.y})"
        return f"({self.x}, {self.y})"

    def connect_rooms(self, connecting_room, direction):
        '''
        Connect two rooms in the given n/s/e/w direction
        '''
        reverse_dirs = {"n": "s", "s": "n", "e": "w", "w": "e"}
        reverse_dir = reverse_dirs[direction]
        setattr(self, f"{direction}_to", connecting_room)
        setattr(connecting_room, f"{reverse_dir}_to", self)

    def get_room_in_direction(self, direction):
        '''
        Connect two rooms in the given n/s/e/w direction
        '''
        return getattr(self, f"{direction}_to")


class World:
    def __init__(self):
        self.grid = None
        self.width = 0
        self.height = 0

    def generate_rooms(self, size_x, size_y, num_rooms):
        '''
        Fill up the grid, bottom to top, in a zig-zag pattern
        '''

        # Initialize the grid
        self.grid = [None] * size_y
        self.width = size_x
        self.height = size_y
        for i in range(len(self.grid)):
            self.grid[i] = [None] * size_x


        # OUR ROOM GENERATOR
        x = size_x // 2
        y = size_y // 2

        room_count = 1
        room = Room(room_count, "A Generic Room", "This is a generic room.", x, y)
        room.save()
        previous_room = room
        fall_back_room = room

        fail_counter = 0

        while room_count < num_rooms:
            dir = randint(1, 4)

            print(f'{x},{y}')

 
            if dir == 1 and room.n_to is None and y+1 < size_y:
                if self.grid[y+1][x] is None:
                    room_count += 1
                    room_direction = "n"
                    y += 1
                    room = Room(room_count, "A Generic Room", "This is a generic room.", x, y)
                    room.save()
                    self.grid[y][x] = room
                    previous_room.connect_rooms(room, room_direction)
                    previous_room = room
                    fail_counter = 0
            elif dir == 2 and room.e_to is None and x+1 < size_x:
                if self.grid[y][x+1] is None:
                    room_count += 1
                    room_direction = "e"
                    x += 1
                    room = Room(room_count, "A Generic Room", "This is a generic room.", x, y)
                    room.save()
                    self.grid[y][x] = room
                    previous_room.connect_rooms(room, room_direction)
                    previous_room = room
                    fail_counter = 0
            elif dir == 3 and room.s_to is None and 0 <= y-1:
                if self.grid[y-1][x] is None:
                    room_count += 1
                    room_direction = "s"
                    y -= 1
                    room = Room(room_count, "A Generic Room", "This is a generic room.", x, y)
                    room.save()
                    self.grid[y][x] = room
                    previous_room.connect_rooms(room, room_direction)
                    previous_room = room
                    fail_counter = 0
            elif dir == 4 and room.w_to is None and 0 <= x-1:
                if self.grid[y][x-1] is None:
                    room_count += 1
                    room_direction = "w"
                    x -= 1
                    room = Room(room_count, "A Generic Room", "This is a generic room.", x, y)
                    room.save()
                    self.grid[y][x] = room
                    previous_room.connect_rooms(room, room_direction)
                    previous_room = room
                    fail_counter = 0
            else:
                fail_counter += 1
                if fail_counter > 10:
                    previous_room = fall_back_room
                    x = previous_room.x
                    y = previous_room.y

        # # Start from lower-left corner (0,0)
        # x = -1 # (this will become 0 on the first step)
        # y = 0
        # room_count = 0

        # # Start generating rooms to the east
        # direction = 1  # 1: east, -1: west


        # # While there are rooms to be created...
        # previous_room = None
        # while room_count < num_rooms:

        #     # Calculate the direction of the room to be created
        #     if direction > 0 and x < size_x - 1:
        #         room_direction = "e"
        #         x += 1
        #     elif direction < 0 and x > 0:
        #         room_direction = "w"
        #         x -= 1
        #     else:
        #         # If we hit a wall, turn north and reverse direction
        #         room_direction = "n"
        #         y += 1
        #         direction *= -1

        #     # Create a room in the given direction
        #     room = Room(room_count, "A Generic Room", "This is a generic room.", x, y)
        #     # Note that in Django, you'll need to save the room after you create it

        #     # Save the room in the World grid
        #     self.grid[y][x] = room

        #     # Connect the new room to the previous room
        #     if previous_room is not None:
        #         previous_room.connect_rooms(room, room_direction)

        #     # Update iteration variables
        #     previous_room = room
        #     room_count += 1

    # def print_rooms(self):
    #     '''
    #     Print the rooms in room_grid in ascii characters.
    #     '''

    #     # Add top border
    #     str = "# " * ((3 + self.width * 5) // 2) + "\n"

    #     # The console prints top to bottom but our array is arranged
    #     # bottom to top.
    #     #
    #     # We reverse it so it draws in the right direction.
    #     reverse_grid = list(self.grid)  # make a copy of the list
    #     reverse_grid.reverse()
    #     for row in reverse_grid:
    #         # PRINT NORTH CONNECTION ROW
    #         str += "#"
    #         for room in row:
    #             if room is not None and room.n_to is not None:
    #                 str += "  |  "
    #             else:
    #                 str += "     "
    #         str += "#\n"
    #         # PRINT ROOM ROW
    #         str += "#"
    #         for room in row:
    #             if room is not None and room.w_to is not None:
    #                 str += "-"
    #             else:
    #                 str += " "
    #             if room is not None:
    #                 str += f"{room.id}".zfill(3)
    #             else:
    #                 str += "   "
    #             if room is not None and room.e_to is not None:
    #                 str += "-"
    #             else:
    #                 str += " "
    #         str += "#\n"
    #         # PRINT SOUTH CONNECTION ROW
    #         str += "#"
    #         for room in row:
    #             if room is not None and room.s_to is not None:
    #                 str += "  |  "
    #             else:
    #                 str += "     "
    #         str += "#\n"

    #     # Add bottom border
    #     str += "# " * ((3 + self.width * 5) // 2) + "\n"

    #     # Print string
    #     print(str)


w = World()
num_rooms = 100
width = 20 #size_x
height = 20 #size_y
w.generate_rooms(width, height, num_rooms)
# w.print_rooms()


print(
    f"\n\nWorld\n  height: {height}\n  width: {width},\n  num_rooms: {num_rooms}\n")


players=Player.objects.all()
for p in players:
  p.currentRoom=fall_back_room.id
  p.save()