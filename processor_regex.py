import re
def classify_with_regex(log_message):
    regex_pattern = {
        r"User User\d+ logged (out|in).": "User Action",
        r"Backup (started|ended) at .*": "System Notification",
        r"/Elevation of admin privileges detected for user \d+": "System Notification",
        r"System updated to version .*": "System Notification",
        r"File .* uploaded successfully by user .*": "System Notification",
        r"Disk cleanup completed successfully.": "System Notification",
        r"System reboot initiated by user .*": "System Notification",
        r"Account with ID .* created by .*": "User Action"
    }
    for pattern, label in regex_pattern.items():
        if re.search(pattern, log_message, re.IGNORECASE):
            return label
    return None

if __name__ == "__main__":
    print(classify_with_regex("user user123 logged in."))
    print(classify_with_regex("Backup started at 12:00."))
    print(classify_with_regex("hey Farnaz, this is a test"))