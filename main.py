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
def submain():
    filename = 'text.txt' # filename here
    printer(filename)

# Executes git commands
def main():
    output = command(["git", "rev-list", "--count", "HEAD"])
    output = int(output) if output is not None else 0
    for i in range(10): # change number of times to commit here
        submain()
        msg = f"git commit -m \"{i + output}. commit\""  # commit message here
        branch = "main"  # branch name here
        command("git add .")
        command(msg)
    command("git push origin " + branch)

if __name__ == "__main__":
    main()