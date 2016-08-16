class Amity(object):
    """Super class for amity"""

    def __init__(self):
        super(Amity, self).__init__()
        self.rooms = {
            'O': [],
            'L': []
        }

    def create_room(self, args):
        """Allows user to enter a list of room names specifying
                whether office or living spaces"""

        room_type = None

        #Assign a group of rooms to a room type
        if room_type == None:
            room_type = raw_input(
                "Enter room type: \n O: Office space \n L: Living space: \n")
            room_type = room_type.upper()
            while room_type != "O" and room_type != "L":
                room_type = raw_input(
                    "Try again. Enter Room Type:\n O: Office space \n L: Living space: \n")
                
        #Adds room to the rooms dict
        for room in args["<room_name>"]:
            if room_type == "O":
                self.rooms['O'].append(room)
            elif room_type == "L":
                self.rooms['L'].append(room)

        print self.rooms

    def save_state(self):
        pass

    def load_state(self):
        pass