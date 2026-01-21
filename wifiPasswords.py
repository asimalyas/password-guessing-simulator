import subprocess

# Get all Wi-Fi profiles
data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')

# Extract profile names
profiles = [i.split(":")[1].strip() for i in data if "All User Profile" in i]

# Print header
print("{:<30} {:<}".format("Wi-Fi Name", "Password"))
print("-" * 50)

# Loop through each profile and get password
for i in profiles:
    try:
        results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8').split('\n')
        # Extract the line containing the key
        results = [b.split(":")[1].strip() for b in results if "Key Content" in b]
        # Print Wi-Fi name and password
        print("{:<30} {:<}".format(i, results[0] if results else ""))
    except subprocess.CalledProcessError:
        print("{:<30} {:<}".format(i, "Error retrieving password"))
