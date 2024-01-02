import random

def generate_tasksest(task_number, utilization):
    tasks = []
    sumU = utilization
    for i in range(1, task_number):
        task_index = f"Task_{i}"
        criticalities = random.choice(["soft", "hard"])

        nextSumU = sumU * random.random() ** (1.0 / (task_number - i))
        utilizations = sumU - nextSumU
        sumU = nextSumU
        computation_time = random.randint(1,50)
        deadline = random.randint(1,50)
        task_data = {"Taskname": task_index, "Computation Time (ms)": computation_time, "Deadline (ms)": deadline, "Criticality": criticalities, "Utilization": utilizations}
        tasks.append(task_data)

    return tasks


def write_to_file(utility):
    file_name = f'utility_{utility}'
    task_set = generate_tasksest(100, utility)
    with open (file_name,'w') as file:
        for item in task_set:
            file.write(str(item) + '\n')

write_to_file(0.3)
write_to_file(0.5)
write_to_file(0.7)

