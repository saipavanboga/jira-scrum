# ---------------------------------------------------
# Employee Performance Analysis System
# ---------------------------------------------------

employees = [

    (1001, "Alice Johnson", "Sales", 15000, 4.2),

    (1002, "Bob Smith", "Sales", 12000, 3.8),

    (1003, "Carol Davis", "Marketing", 8000, 4.5),

    (1004, "David Brown", "Sales", 18000, 4.0),

    (1005, "Eva Wilson", "Marketing", 9500, 3.2),

    (1006, "Frank Miller", "IT", 11000, 3.9),

    (1007, "Grace Lee", "Sales", 13500, 2.1),

    (1008, "Henry Taylor", "IT", 10500, 4.1),

    (1009, "Ivy Chen", "Marketing", 7800, 3.7),

    (1010, "Jack Davis", "IT", 12500, 3.5)

]

# ---------------------------------------------------
# 1. Top 3 Performers by Department
# ---------------------------------------------------

departments = {}

for emp in employees:

    emp_id, name, dept, sales, rating = emp

    if dept not in departments:
        departments[dept] = []

    departments[dept].append(emp)

print("Top 3 Performers by Department:\n")

for dept, emp_list in departments.items():

    # Sort by sales descending
    sorted_employees = sorted(
        emp_list,
        key=lambda x: x[3],
        reverse=True
    )

    print(f"{dept} Department:")

    top_3 = sorted_employees[:3]

    for i, emp in enumerate(top_3, start=1):

        print(f"{i}. {emp[1]}: ${emp[3]}")

    print()


# ---------------------------------------------------
# 2. Average Rating for Each Department
# ---------------------------------------------------

print("Department Average Ratings:\n")

for dept, emp_list in departments.items():

    avg_rating = sum(emp[4] for emp in emp_list) / len(emp_list)

    print(f"{dept}: {avg_rating:.2f}")

print()


# ---------------------------------------------------
# 3. Employees Needing Improvement
# ---------------------------------------------------

print("Employees Needing Improvement:\n")

for emp in employees:

    emp_id, name, dept, sales, rating = emp

    if rating < 3.0:

        print(f"{name} ({dept}): Rating {rating}")

print()


# ---------------------------------------------------
# 4. Performance Ranking
# ---------------------------------------------------

performance_list = []

for emp in employees:

    emp_id, name, dept, sales, rating = emp

    performance_score = sales * rating

    performance_list.append((name, performance_score))

# Sort descending
performance_list.sort(key=lambda x: x[1], reverse=True)

print("Performance Ranking:\n")

for i, emp in enumerate(performance_list, start=1):

    print(f"{i}. {emp[0]}: {emp[1]}")

print()


# ---------------------------------------------------
# 5. Department-wise Performance Summary
# ---------------------------------------------------

print("Department Performance Summary:\n")

for dept, emp_list in departments.items():

    total_employees = len(emp_list)

    avg_sales = sum(emp[3] for emp in emp_list) / total_employees

    avg_rating = sum(emp[4] for emp in emp_list) / total_employees

    print(
        f"{dept}: {total_employees} employees, "
        f"Avg Sales: ${avg_sales:.2f}, "
        f"Avg Rating: {avg_rating:.2f}"
    )