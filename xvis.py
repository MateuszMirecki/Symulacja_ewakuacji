import matplotlib.pyplot as plt
import re
import os

for i in range(1, 5):
    filename = f'statistics_{i}.txt'

    simulation_number = re.search(r"statistics_(\d+)\.txt", filename)
    if simulation_number:
        title = f"Statystyki z symulacji nr {simulation_number.group(1)}"
    else:
        title = "Statystyki z symulacji"

    steps = []
    agents_remaining = []
    moves_made = []
    exited_agents = []  

    last_remaining = None  # To calculate agents exiting in each step

    with open(filename, 'r') as f:
        for line in f:
            match_agents = re.match(r"Step (\d+): (\d+) agents remaining", line)
            if match_agents:
                step = int(match_agents.group(1))
                remaining = int(match_agents.group(2))
                steps.append(step)
                agents_remaining.append(remaining)
                
                if last_remaining is not None:
                    exited = last_remaining - remaining
                    exited_agents.append(max(0, exited))
                else:
                    exited_agents.append(0)  
                
                last_remaining = remaining
                continue

       
            match_moves = re.match(r"Step (\d+): (\d+) moves made", line)
            if match_moves:
                moves = int(match_moves.group(2))
                moves_made.append(moves)
                continue

    fig, ax1 = plt.subplots(figsize=(14, 8))

    ax1.plot(steps, agents_remaining, 'b-', label='Pozostałe agenty')
    ax1.set_xlabel('Numer iteracji')
    ax1.set_ylabel('Pozostałe agenty', color='b')
    ax1.tick_params(axis='y', labelcolor='b')

    ax2 = ax1.twinx()
    ax2.bar(steps, exited_agents, color='gray', alpha=0.6, label='Wydostane agenty w danej iteracji')
    ax2.set_ylabel('Liczba wydostanych agentów', color='gray')
    ax2.tick_params(axis='y', labelcolor='gray')

    ax3 = ax1.twinx()
    ax3.spines.right.set_position(("outward", 60))  # Offset the third axis
    ax3.plot(steps, moves_made, 'r--', label='Kroki wykonane w danej iteracji')
    ax3.set_ylabel('Kroki wykonane', color='r')
    ax3.tick_params(axis='y', labelcolor='r')

    lines_1, labels_1 = ax1.get_legend_handles_labels()
    lines_2, labels_2 = ax2.get_legend_handles_labels()
    lines_3, labels_3 = ax3.get_legend_handles_labels()
    ax1.legend(lines_1 + lines_2 + lines_3, labels_1 + labels_2 + labels_3, loc='upper right')

    plt.title(title)
    plt.grid(True)

    output_file = f"simulation_{simulation_number.group(1)}_results.png" if simulation_number else "output.png"
    plt.savefig(output_file)
    print(f"Plot saved as {output_file}")

    # plt.show()
