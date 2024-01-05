import random

from numpy import lcm


class Task:
    def __init__(self, name, computation_time, deadline, criticality, utility, period_num):
        self.name = name
        self.computation_time = computation_time
        self.deadline = deadline
        self.criticality = criticality
        self.utility = utility
        self.period_number = period_num
        self.frequency = None


def generate_tasksest(task_number, utilization):
    tasks = []
    sumU = utilization
    for i in range(1, task_number):
        task_index = f"Task_{i}"
        criticalities = random.choice(["soft", "hard"])

        nextSumU = sumU * random.random() ** (1.0 / (task_number - i))
        utilizations = sumU - nextSumU
        sumU = nextSumU
        computation_time = random.randint(10, 50)
        deadline = random.randint(50, 100)
        period_size = random.randint(5, 7)
        task_data = Task(task_index, computation_time, deadline, criticalities, utilizations, period_size)
        tasks.append(task_data)

    return tasks


def write_to_file(utility):
    file_name = f'utility_{utility}.txt'
    task_set = generate_tasksest(100, utility)
    with open(file_name, 'w') as file:
        for item in task_set:
            file.write(str(item) + '\n')

# write_to_file(0.3)
# write_to_file(0.5)
# write_to_file(0.7)
