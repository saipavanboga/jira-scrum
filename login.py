# Log Data
log_data = [
    ("2023-10-26 10:00:00", "INFO", "User logged in"),
    ("2023-10-26 10:01:00", "ERROR", "Database connection failed"),
    ("2023-10-26 10:01:30", "INFO", "Data processed successfully"),
    ("2023-10-26 10:02:00", "WARN", "Low disk space"),
    ("2023-10-26 10:03:00", "ERROR", "Database connection failed"),
    ("2023-10-26 10:04:00", "INFO", "User logged out"),
    ("2023-10-26 10:05:00", "ERROR", "Null pointer exception"),
    ("2023-10-26 10:05:30", "DEBUG", "Debugging user session"),
]

# 1. Filter Error Logs
error_logs = [log for log in log_data if log[1] == "ERROR"]

print("ERROR LOGS:")
for log in error_logs:
    print(log)

# 2. Count Specific Errors
db_error_count = sum(
    1 for log in error_logs if log[2] == "Database connection failed"
)

print("\nDatabase connection failed count:", db_error_count)

# 3. Find First Warning
first_warn = next((log for log in log_data if log[1] == "WARN"), None)

if first_warn:
    print("\nFirst WARN Log:")
    print("Timestamp:", first_warn[0])
    print("Message:", first_warn[2])
else:
    print("\nNo WARN log found")

# 4. Sort Logs by Timestamp
sorted_logs = sorted(log_data, key=lambda x: x[0])

print("\nSORTED LOGS:")
for log in sorted_logs:
    print(log)

# 5. Check for Critical Issues

# all() -> check all messages length < 100
all_short = all(len(log[2]) < 100 for log in log_data)

# any() -> check any CRITICAL level exists
has_critical = any(log[1] == "CRITICAL" for log in log_data)

print("\nAre all log messages shorter than 100 characters?", all_short)
print("Is there any CRITICAL log?", has_critical)

# 6. Append New Log
new_log = ("2023-10-26 10:06:00", "INFO", "System check complete")

log_data.append(new_log)

print("\nUPDATED LOG DATA:")
for log in log_data:
    print(log)