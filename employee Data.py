# Employee Data
employee_data = [

    (101, "Alice Smith", "Engineering", 90000, 5),

    (102, "Bob Johnson", "Marketing", 75000, 3),

    (103, "Charlie Brown", "Engineering", 120000, 8),

    (104, "Diana Prince", "HR", 65000, 2),

    (105, "Edward King", "Marketing", 80000, 5),

    (106, "Frank Castle", "Engineering", 95000, 0)

]

# ---------------------------------------------------
# 1. Sort by Salary (Descending)
# ---------------------------------------------------

salary_sorted = sorted(employee_data, key=lambda x: x[3], reverse=True)

print("Employees Sorted by Salary:")
for emp in salary_sorted:
    print(emp)


# ---------------------------------------------------
# 2. Sort by Years of Service (Descending)
#    then Name (Ascending)
# ---------------------------------------------------

service_sorted = sorted(
    employee_data,
    key=lambda x: (-x[4], x[1])
)

print("\nEmployees Sorted by Service and Name:")
for emp in service_sorted:
    print(emp)


# ---------------------------------------------------
# 3. Calculate Statistics
# ---------------------------------------------------

# Total Salary
total_salary = sum(emp[3] for emp in employee_data)

# Minimum Salary
min_salary = min(emp[3] for emp in employee_data)

# Maximum Salary
max_salary = max(emp[3] for emp in employee_data)

# Average Years of Service
avg_service = sum(emp[4] for emp in employee_data) / len(employee_data)

print("\nTotal Salary Expenditure:", total_salary)
print("Minimum Salary:", min_salary)
print("Maximum Salary:", max_salary)
print("Average Years of Service:", avg_service)


# ---------------------------------------------------
# 4. Identify High Earners
# ---------------------------------------------------

high_earners = [emp[1] for emp in employee_data if emp[3] > 90000]

print("\nEmployees earning more than 90000:")
print(high_earners)


# ---------------------------------------------------
# 5. Remove Employee with ID = 104
# ---------------------------------------------------

for i, emp in enumerate(employee_data):

    if emp[0] == 104:
        del employee_data[i]
        break

print("\nEmployee Data after Removing ID 104:")
for emp in employee_data:
    print(emp)


# ---------------------------------------------------
# 6. Data Validation Checks
# ---------------------------------------------------

# Check if all employees have at least 1 year service
all_service = all(emp[4] >= 1 for emp in employee_data)

# Check if any Engineering employee earns less than 70000
low_engineering_salary = any(
    emp[2] == "Engineering" and emp[3] < 70000
    for emp in employee_data
)

print("\nDo all employees have at least 1 year of service?")
print(all_service)

print("\nIs any Engineering employee earning less than 70000?")
print(low_engineering_salary)