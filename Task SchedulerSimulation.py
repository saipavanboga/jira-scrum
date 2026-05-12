# ---------------------------------------------------
# Task Scheduler Simulation
# ---------------------------------------------------

# (task_id, description, priority, dependencies)

tasks_definitions = [

    ("T1", "Compile Code", 1, []),

    ("T2", "Run Unit Tests", 2, ["T1"]),

    ("T3", "Generate Report", 3, ["T2"]),

    ("T4", "Deploy Artifacts", 2, ["T1"]),

    ("T5", "Urgent Patch", 0, [])

]

# ---------------------------------------------------
# 1. Initialize Task Queue
# ---------------------------------------------------

task_queue = list(tasks_definitions)

print("Initial Task Queue:")
for task in task_queue:
    print(task)


# ---------------------------------------------------
# 2. Sort by Priority
# ---------------------------------------------------

task_queue.sort(key=lambda x: x[2])

print("\nTask Queue Sorted by Priority:")
for task in task_queue:
    print(task)


# ---------------------------------------------------
# 3. Process Tasks
# ---------------------------------------------------

completed_tasks = []

print("\nProcessing Tasks...\n")

while task_queue:

    # Get first task from queue
    current_task = task_queue.pop(0)

    task_id, description, priority, dependencies = current_task

    # Check dependencies
    if all(dep in completed_tasks for dep in dependencies):

        print(f"Processing {task_id} : {description}")

        completed_tasks.append(task_id)

    else:
        print(f"Skipping {task_id} - Dependencies not completed")

print("\nCompleted Tasks:")
print(completed_tasks)


# ---------------------------------------------------
# 4. Add High-Priority Task
# ---------------------------------------------------

new_task = ("T6", "Emergency DB Backup", 0, [])

task_queue.insert(0, new_task)

print("\nQueue after inserting new high-priority task:")
for task in task_queue:
    print(task)


# ---------------------------------------------------
# 5. Reverse Order Processing
# ---------------------------------------------------

reverse_queue = list(tasks_definitions)

# Sort ascending
reverse_queue.sort(key=lambda x: x[2])

# Reverse list
reverse_queue.reverse()

print("\nReverse Order Processing:")

while reverse_queue:

    task = reverse_queue.pop()

    print("Processing:", task[0], "-", task[1])


# ---------------------------------------------------
# 6. Analyze Priorities
# ---------------------------------------------------

priorities = [task[2] for task in tasks_definitions]

min_priority = min(priorities)

max_priority = max(priorities)

sum_priority = sum(priorities)

print("\nMinimum Priority:", min_priority)

print("Maximum Priority:", max_priority)

print("Sum of Priorities:", sum_priority)


# ---------------------------------------------------
# 7. Remove Dependency from T4
# ---------------------------------------------------

updated_tasks = []

for task in tasks_definitions:

    if task[0] == "T4":

        # Create new tuple without dependency
        updated_task = ("T4", "Deploy Artifacts", 2, [])

        updated_tasks.append(updated_task)

    else:
        updated_tasks.append(task)

print("\nUpdated Tasks after removing dependency from T4:")

for task in updated_tasks:
    print(task)