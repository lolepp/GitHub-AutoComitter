import random
import string
import subprocess

def command(command):
    """
    Runs a git command using subprocess and prints the output.
    """
    try:
        result = subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        print(result.stdout)
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {e}\n{e.stderr}")

def printer(filename):
    random_letter = random.choice(string.ascii_letters)  # ascii_letters is lowercase and uppercase
    # Open the file in append mode and add the random letter
    with open(filename, 'a') as file:
        file.write(random_letter + '\n')

# Adds random letter to text file
def submain():
    filename = 'text.txt' # filename here
    printer(filename)

def commit_counter():
    output = command(["git", "rev-list", "--count", "HEAD"])
    return int(output) if output is not None else 0

# Executes git commands
def main():
    amount = 3 # Enter here how many committs you want 
    counter = commit_counter()
    for i in range(amount): # change number of times to commit here
        i += 1
        submain()
        msg = f"git commit -m \"{i + counter}. commit\""  # commit message here
        branch = "main"  # branch name here
        command("git add .")
        command(msg)
    command("git push origin " + branch)

if __name__ == "__main__":
    main()
    