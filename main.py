import random
import string
import subprocess

def command(command):
    """
    Runs any command using subprocess and prints the output.
    """
    try:
        result = subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        print(result.stdout)
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {e}\n{e.stderr}")

def printer(filename): # prints random letter to the given filename
    random_letter = random.choice(string.ascii_letters)  # ascii_letters is lowercase and uppercase
    # Open the file in append mode and add the random letter
    with open(filename, 'a') as file:
        file.write(random_letter + '\n')

def commit_counter(): # Gets the number of committs in this project
    output = command(["git", "rev-list", "--count", "HEAD"])
    return int(output) if output is not None else 0

def main(): # Executes git commands and the printer
    counter = commit_counter() # get the number of committs in this project
    amount = 66 # Enter here how many committs you want
    filename = 'text.txt' # filename here
    for i in range(amount): # change number of times to commit here
        branch = "main"  # branch name here
        i += 1
        msg = f"git commit -m \"{i + counter}. commit\""  # commit message here
        printer(filename) # printer adds random letter to file so there is something to add and commit
        command("git add .") # git add ., so every change is added
        command(msg) # commit with the msg
    command("git push origin " + branch) # git push at the end to shgrten run time

if __name__ == "__main__":
    main()
    