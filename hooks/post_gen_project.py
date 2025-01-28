import os
import subprocess

def main():
    # Initialize a Git repository
    subprocess.run(["git", "init"], check=True)
    print("Git repository initialized.")

    # Add files to the staging area
    subprocess.run(["git", "add", "."], check=True)
    print("Files added to the staging area.")

    # Create the initial commit
    subprocess.run(["git", "commit", "-m", "Initial commit"], check=True)
    print("Initial commit created.")

    # Set the main branch as 'main'
    subprocess.run(["git", "branch", "-M", "main"], check=True)
    print("Main branch set to 'main'.")

    # Ask the user for the remote repository URL
    repo_url = input("Enter the remote repository URL (leave empty if you don't want to add a remote now): ").strip()
    if repo_url:
        # Configure the remote repository
        subprocess.run(["git", "remote", "add", "origin", repo_url], check=True)
        print(f"Remote repository configured: {repo_url}")

        # Push the project to the remote repository
        subprocess.run(["git", "push", "-u", "origin", "main"], check=True)
        print("Code pushed to the remote repository.")

if __name__ == "__main__":
    main()
