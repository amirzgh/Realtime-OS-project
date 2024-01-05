import heapq


class Task:
    def init(self, name, computation_time, deadline, criticality, utility, frequency):
        self.name = name
        self.computation_time = computation_time
        self.deadline = deadline
        self.criticality = criticality
        self.utility = utility
        self.frequency = frequency


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


if name == "main":
    # Example tasks
    tasks = [
        Task("Task_1", 29, 78, "soft", 0.0004714570741565227, 0.4),
        # ... (add other tasks here)
    ]

    # Number of cores
    cores = 8

    # Run the branch and bound algorithm
    result_schedule = branch_and_bound(tasks, cores)

    # Display the final schedule
    for task in result_schedule:
        print(f"Task: {task.name}, Deadline: {task.deadline}, Utility: {task.utility}")
