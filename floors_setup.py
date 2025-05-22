from floor import Floor

# def agent_setup_test(floor):
#     # górne pokoje lewa strona
#     floor.place_agents((40, 80), (30, 39), 75)  
#     # górne pokoje prawa strona
#     floor.place_agents((86, 123), (30, 39), 75) 
#     # dolne pokoje
#     floor.place_agents((40, 135), (13, 22), 200) 
#     # sala wykładowa
#     floor.place_agents((16, 32), (8, 21), 150) 


# def exit_setup_test(floor):
#     floor.place_exit(82, 39)
#     floor.place_exit(83, 39)
#     floor.place_exit(84, 39)
#     floor.place_exit(147, 26)
#     floor.place_exit(147, 25)
#     floor.place_exit(147, 24)
#     floor.place_exit(24, 36)
#     floor.place_exit(25, 36)
#     floor.place_exit(24, 36)
#     floor.place_exit(26, 36)


def agent_setup_low_everywhere(floor):
    floor.place_agents((40, 80), (30, 39), 20)  
    floor.place_agents((86, 123), (30, 39), 20)  
    floor.place_agents((40, 135), (13, 22), 30)  
    floor.place_agents((16, 32), (8, 21), 20)  

def exit_setup_all(floor):
    floor.place_exit(82, 39)
    floor.place_exit(83, 39)
    floor.place_exit(147, 25)
    floor.place_exit(147, 26)
    floor.place_exit(24, 36)
    floor.place_exit(25, 36)


def agent_setup_low_big_room(floor):
    floor.place_agents((40, 80), (30, 39), 70)  
    floor.place_agents((86, 123), (30, 39), 70)  
    floor.place_agents((40, 135), (13, 22), 10)  
    floor.place_agents((16, 32), (8, 21), 120)  

def exit_setup_no_middle(floor):
    floor.place_exit(147, 25)
    floor.place_exit(147, 26)
    floor.place_exit(24, 36)
    floor.place_exit(25, 36)

def agent_setup_low_small_rooms(floor):
    floor.place_agents((40, 80), (30, 39), 20)  
    floor.place_agents((86, 123), (30, 39), 20) 
    floor.place_agents((40, 135), (13, 22), 150) 
    floor.place_agents((16, 32), (8, 21), 40) 


def agent_setup_no_low(floor):
    floor.place_agents((40, 80), (30, 39), 75)  
    floor.place_agents((86, 123), (30, 39), 175) 
    floor.place_agents((40, 135), (13, 22), 200) 
    floor.place_agents((16, 32), (8, 21), 150) 




class FirstFloor(Floor):
    def __init__(self, model, agent_unique_id):
        super().__init__(model, agent_unique_id, 1)

    def set_agents(self):
        # agent_setup_no_low(self)
        # agent_setup_low_big_room(self)
        agent_setup_low_everywhere(self)
        # agent_setup_low_small_rooms(self)

    def set_exits(self):
        exit_setup_all(self)
        # exit_setup_no_middle(self)


    def set_walls(self):
        self.set_stairs_first_floor()
        self.set_walls_first_floor()


class SecondFloor(Floor):

    def __init__(self, model, agent_unique_id):
        super().__init__(model, agent_unique_id, 2)

    def set_agents(self):
        # agent_setup_no_low(self)
        # agent_setup_low_big_room(self)
        agent_setup_low_everywhere(self)
        # agent_setup_low_small_rooms(self)

    def set_exits(self):
        exit_setup_all(self)
        # exit_setup_no_middle(self)

    def set_walls(self):
        self.set_stairs_second_floor()
        self.set_walls_second_floor()
