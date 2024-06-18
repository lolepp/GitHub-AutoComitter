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
    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {e}\n{e.stderr}")

# def git_commit(message):
#     run_git_command(["git", "commit", "-m", message])

# def git_push(branch):
#     run_git_command(["git", "push", "origin", branch])

def printer(filename):
    random_letter = random.choice(string.ascii_letters)  # ascii_letters is lowercase and uppercase
    # Open the file in append mode and add the random letter
    with open(filename, 'a') as file:
        file.write(random_letter + '\n')

# Adds random letter to text file
def main():
    filename = 'text.txt' # filename here
    printer(filename)

# Executes git commands
def main2():
    for i in range(1): # change number of times to commit here
        msg = f"git commit -m \"{i + 2}. commit\""  # commit message here
        branch = "main"  # branch name here
        command("git add .")
        command(msg)
        command("git push origin main")

if __name__ == "__main__":
    main()
    main2()