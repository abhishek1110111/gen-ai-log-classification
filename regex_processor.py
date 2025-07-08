import re
def classification_with_regex(log_message):
    ''' Classify the given log message using regex patterns.'''
    regex_patterns = {
        r"User User \d+ logged (in|out).": "User Action",
        r"Backup (started|ended) at .*": "System Notification",
        r"Backup completed successfully.": "System Notification",
        r"System updated to version .*": "System Notification",
        r"File .* uploaded successfully by user .*": "System Notification",
        r"Disk cleanup completed successfully.": "System Notification",
        r"System reboot initiated by user .*": "System Notification",
        r"Account with ID .* created by .*": "User Action"
    }
    for pattern, label in regex_patterns.items():
        if re.search(pattern, log_message):
            return label
    return None

if __name__ == "__main__":
    print(classification_with_regex("Backup completed successfully."))
    print(classification_with_regex("Account with ID 1234 created by User1."))
    print(classification_with_regex("Hey Bro, chill ya!"))


