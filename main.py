from task_generator import generate_tasksest
import numpy as np

frequencies = [0.4,0.6,0.8,1,1.1]

tasks_with_3 = generate_tasksest(100, 0.3)
tasks_with_5 = generate_tasksest(100, 0.5)
tasks_with_7 = generate_tasksest(100, 0.7)



def assign_frequency(tasks):
    computation_times = np.zeros((len(tasks) , len(frequencies)))
    test = []

    for i, task in enumerate(tasks):
        for j, frequency in enumerate(frequencies):
            computation_times[i][j] = task.computation_time / frequency

    
    for task in tasks:
        frequencies_for_task = []
        for frequency in frequencies:
            if computation_times[tasks.index(task)][frequencies.index(frequency)] <= task.deadline:
                frequencies_for_task.append(frequency)
        if len(frequencies_for_task) > 0:
            task.frequency = min(frequencies_for_task)
    
    return tasks


def write_to_file(utility):
    file_name = f'utility_{utility}.txt'
    task_set = generate_tasksest(100, utility)
    tasks = assign_frequency(task_set)
    with open (file_name,'w') as file:
        for item in tasks:
            file.write(f"Task Name: {item.name} ")
            file.write(f"Computation Time: {item.computation_time} ")
            file.write(f"Deadline: {item.deadline} ")
            file.write(f"Criticality: {item.criticality} ")
            file.write(f"Utility: {item.utility} ")
            file.write(f"frequency: {item.frequency} ")
            file.write("\n") 

write_to_file(0.3)
        
    





# {"Taskname": task_index, "Computation Time (ms)": computation_time, "Deadline (ms)": deadline, "Criticality": criticalities, "Utilization": utilizations}