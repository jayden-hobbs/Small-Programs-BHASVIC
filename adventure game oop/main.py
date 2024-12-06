from room import Room

kitchen = Room("kitchen")
kitchen.set_description("A dank and dirty room buzzing with flies")
kitchen.describe()


dining_hall = Room("dining hall")
dining_hall.set_description("A large room with ornate golden decorations on each wall")
dining_hall.describe()

ballroom = Room("ballroom")
ballroom.set_description("A vast room with a shiny wooden floor; huge candlesticks guard the entrance")
ballroom.describe()

kitchen.link_room(dining_hall, "south")
dining_hall.link_room(kitchen, "north")
ballroom.link_room(dining_hall, "east")
dining_hall.link_room(ballroom, "west")

current_room = kitchen

while True:
    print("\n")
    current_room.get_details()
    command = input("> ")
    current_room = current_room.move(command)