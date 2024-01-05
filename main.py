from queue import Queue

from task_generator import generate_tasksest, Task
import numpy as np


#
# tasks_with_3 = generate_tasksest(100, 0.3)
# tasks_with_5 = generate_tasksest(100, 0.5)
# tasks_with_7 = generate_tasksest(100, 0.7)


def assign_frequency(tasks):
    frequencies = [0.4, 0.6, 0.8, 1, 1.1]
    computation_times = np.zeros((len(tasks), len(frequencies)))
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


def branch_and_bound(tasks, cores):
    tasks.sort(key=lambda x: x.deadline)

    def calculate_bound(schedule):
        total_utility = 0
        for task in schedule:
            total_utility += task.utility
        return total_utility

    def is_feasible(schedule):
        current_time = 0
        for task in schedule:
            current_time += task.computation_time / task.frequency
            if current_time > task.deadline:
                return False
        return True

    def branch(schedule, remaining_tasks):
        if not remaining_tasks:
            return schedule, calculate_bound(schedule)

        task = remaining_tasks[0]

        # Branch without including the current task
        result1 = branch(schedule, remaining_tasks[1:])

        # Branch by including the current task
        new_schedule = schedule + [task]
        result2 = branch(new_schedule, remaining_tasks[1:])

        if is_feasible(new_schedule):
            return max(result1, result2, key=lambda x: x[1])

        return result1

    final_schedule, _ = branch([], tasks)

    return final_schedule


# def bound_and_branch_scheduler(tasks):
#     # Generate instances of the Task class with updated period_number
#     # tasks_instances = [Task(**task_data) for task_data in tasks]
#
#     # Assign frequencies to tasks
#     tasks_instances = assign_frequency(tasks)
#
#     # Initialize individual task queues for each core
#     cores = [Queue() for _ in range(8)]
#     current_time = 0
#     MAX_SIMULATION_STEPS = 10000  # You can adjust this value based on your needs
#
#     while current_time < MAX_SIMULATION_STEPS and (
#             any(not core.empty() for core in cores) or any(task.computation_time > 0 for task in tasks_instances)):
#         for core_index, core in enumerate(cores):
#             if not core.empty():
#                 current_task = core.get()
#                 # Check if task deadline is reached for hard tasks
#                 if current_time % current_task.deadline == 0 and current_task.criticality == "Hard":
#                     print(f"Deadline missed for {current_task.name} at time {current_time}")
#                 else:
#                     # Simulate task execution
#                     current_task.computation_time -= 1
#                     print(f"Task {current_task.name} is running on Core {core_index + 1} at time {current_time}")
#
#                     # Check if task is completed
#                     if current_task.computation_time == 0:
#                         print(f"Task {current_task.name} completed at time {current_time}")
#
#             # Enqueue eligible tasks based on period and deadline
#             eligible_tasks = [task for task in tasks_instances if current_time % task.period_number == 0]
#             eligible_tasks.sort(key=lambda task: task.utility, reverse=True)  # Sort by utility in descending order
#
#             for task in eligible_tasks:
#                 if task not in core.queue:
#                     core.put(task)
#                     break  # Assign only one task to each core in each iteration
#
#         current_time += 1
#
#     print("Simulation completed.")


def write_to_file(utility):
    file_name = f'utility_{utility}.txt'
    task_set = generate_tasksest(10, utility)
    tasks = assign_frequency(task_set)
    return branch_and_bound(tasks, cores=8)
    # with open(file_name, 'w') as file:
    #     for item in tasks:
    #         file.write(f"Task Name: {item.name} ")
    #         file.write(f"Computation Time: {item.computation_time} ")
    #         file.write(f"Deadline: {item.deadline} ")
    #         file.write(f"Criticality: {item.criticality} ")
    #         file.write(f"Utility: {item.utility} ")
    #         file.write(f"frequency: {item.frequency} ")
    #         file.write("\n")


print(write_to_file(0.7))
