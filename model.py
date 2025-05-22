from mesa import Model
from mesa.space import SingleGrid
from mesa.time import RandomActivation
from floors_setup import FirstFloor, SecondFloor


class CrowdSimulatorModel(Model):

    def __init__(self, grid_width: int, grid_height: int) -> None:
        super().__init__()
        self.grid = SingleGrid(grid_width, grid_height, False)
        self.grid2 = SingleGrid(grid_width, grid_height, False)

        self.schedule = RandomActivation(self)

        self.unique_id = [i for i in range(10000)]
        self.first_floor = FirstFloor(self, self.unique_id)
        self.second_floor = SecondFloor(self, self.unique_id)

        self.step_count = 0
        self.total_agents = 0  


        with open('statistics.txt', 'w') as stats_file:
            stats_file.write("Simulation Statistics\n")
            stats_file.write("=====================\n")


    def step(self) -> None:
        if self.step_count == 0:
            self.total_agents = len(self.schedule.agents)  

        self.step_count += 1  

        self.moves_this_step = 0

        self.schedule.step()

        remaining_agents = len(self.schedule.agents)
        with open('statistics.txt', 'a') as stats_file:
            stats_file.write(f"Step {self.step_count}: {remaining_agents} agents remaining\n")
            stats_file.write(f"Step {self.step_count}: {self.moves_this_step} moves made\n")

        if remaining_agents == 0:
            self.running = False
            with open('statistics.txt', 'a') as stats_file:
                stats_file.write("\nSimulation Complete\n")
                stats_file.write(f"Total Steps: {self.step_count}\n")
                stats_file.write(f"Initial Agents: {self.total_agents}\n")
                stats_file.write(f"Agents Exited: {self.total_agents}\n")
