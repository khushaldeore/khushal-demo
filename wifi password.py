import subprocess
import re

def get_wifi_profiles():
    """Get the list of Wi-Fi profiles stored on the system."""
    profiles = subprocess.check_output("netsh wlan show profiles", shell=True, text=True)
    profile_names = re.findall(r"Profile\s*:\s*(.*)", profiles)
    return profile_names

def get_wifi_password(profile_name):
    """Retrieve the Wi-Fi password for a given profile name."""
    try:
        result = subprocess.check_output(f"netsh wlan show profile \"{profile_name}\" key=clear", shell=True, text=True)
        password_match = re.search(r"Key Content\s*:\s*(.*)", result)
        if password_match:
            return password_match.group(1)
        else:
            return "No password found or not saved."
    except subprocess.CalledProcessError:
        return "Failed to retrieve password."

def main():
    profiles = get_wifi_profiles()
    if not profiles:
        print("No Wi-Fi profiles found.")
        return

    for profile in profiles:
        print(f"Profile Name: {profile}")
        password = get_wifi_password(profile)
        print(f"Password: {password}\n")

if __name__ == "__main__":
    main()
