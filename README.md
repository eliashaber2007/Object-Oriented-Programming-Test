# Git Mini Exercise

## Part 1: Setup & config

### Q1. Install Git
Git was already installed on my Mac (it comes with the Xcode Command Line Tools).

### Q2. Verify the version
`git --version` prints `git version 2.50.1 (Apple Git-155)`.

### Q3. Configure username and email
- `git config --global user.name "Elias Habr"`
- `git config --global user.email "your-email@example.com"`

## Part 2: Create Your First Repository

### Create a folder called my-first-repo
`mkdir my-first-repo`

### Navigate into that folder
`cd my-first-repo`

### Initialize a Git repository
`git init -b main` (`-b main` names the default branch `main`)

### Create a file called readme.txt
`touch readme.txt`

## Part 3: Your First Commit

### Q1. What command shows the current state of the repository?
`git status`

### Q2. What command stages readme.txt for commit?
`git add readme.txt`

### Q3. What command commits with the message "Add readme file"?
`git commit -m "Add readme file"`

### Q4. What command shows the commit history?
`git log`

## Part 4: Make Changes

### Q1. Edit readme.txt and add a new line of text
`echo "This is my first Git repository." >> readme.txt` (`>>` adds the line at the end of the file)

### Q2. What does git status show now?
It shows `readme.txt` as **modified** under "Changes not staged for commit". Git noticed the file changed since the last commit, but the change is not staged yet, so it will not be in the next commit until I run `git add`.

### Q3. Stage and commit the changes
- `git add readme.txt`
- `git commit -m "Add description line to readme"`

### Q4. How many commits do you have now?
2 commits: "Add readme file" and "Add description line to readme".

## Part 5: Exploration

### git diff
Shows the exact changes in my files that are not staged yet, line by line. Added lines start with `+` (green) and removed lines start with `-` (red). If nothing changed since the last commit, it shows nothing.

### git log --oneline
Shows the commit history in a short format: one commit per line, with a short commit ID and the commit message. It is easier to read than the full `git log`.

## Part 6: Working with Branches

### Q1. What command lists all branches?
`git branch`

### Q2. What command creates a new branch called feature-script?
`git branch feature-script`

### Q3. What command switches to the feature-script branch?
`git switch feature-script` (older equivalent: `git checkout feature-script`)

### Q4. What single command creates and switches to a new branch called dev?
`git switch -c dev` (older equivalent: `git checkout -b dev`)

### Q5. Switch back to the feature-script branch
`git switch feature-script`

### Q6. Verify you are on the correct branch
`git branch` puts a `*` next to the current branch, here `* feature-script`. `git status` also says "On branch feature-script".

## Part 7: Create a Bash Script on a Branch

### Q1. Make sure you are on the feature-script branch
`git branch` shows `* feature-script` (switch with `git switch feature-script` if not).

### Q2. Create a new file called install.sh
`touch install.sh`

### Q3. Content of install.sh

    #!/bin/bash
    echo "Starting installation..."
    sudo apt update
    sudo apt install -y curl
    echo "Installation complete!"

- `#!/bin/bash` is the shebang: it tells the system to run the file with Bash.
- `sudo apt update` updates the package lists.
- `sudo apt install -y curl` installs the package curl (`-y` answers yes automatically).

### Q4. Make the script executable
`chmod +x install.sh`

### Q5. Stage and commit the script
- `git add install.sh`
- `git commit -m "Add install script"`

### Q6. Check the commit history on this branch
`git log --oneline` shows 3 commits, with "Add install script" at the top.

## Part 8: Merge Branches

### Q1. Switch back to the main branch
`git switch main`

### Q2. Is install.sh present? Why or why not?
No, `ls` only shows `readme.txt`. `install.sh` was committed only on the `feature-script` branch, and `main` does not have that commit yet. Each branch has its own version of the files.

### Q3. What command merges feature-script into main?
`git merge feature-script`

### Q4. List the files again. What changed?
`install.sh` is now there. The merge brought the commit from `feature-script` into `main`.

### Q5. Check the commit history. What do you observe?
`git log --oneline` on `main` now shows 3 commits, including "Add install script". Git did a **fast-forward** merge: `main` had no new commits of its own, so Git simply moved `main` forward to the latest commit, without creating an extra merge commit.

### Q6. What command deletes the feature-script branch after merging?
`git branch -d feature-script`

## Part 9: Push to GitHub

### Q1 and Q2. Create a repository on GitHub without a README
Instead of a new repository, I used my course repository `Object-Oriented-Programming-Test`, shared with my teacher. I pushed the project to its own branch, `my-first-repo`, so it stays separate from `main`. A brand new repository should be created without a README: otherwise GitHub has a commit my local repo does not have, and the first push gets rejected.

### Q3. What command links the local repo to GitHub?
`git remote add origin https://github.com/eliashaber2007/Object-Oriented-Programming-Test.git`

### Q4. What command pushes the commits to GitHub?
`git push -u origin main:my-first-repo` (sends my local `main` to a branch called `my-first-repo` on GitHub, and `-u` remembers the link)

### Q5. Refresh the GitHub page. What do you see?
On the `my-first-repo` branch, GitHub shows my files (`readme.txt` and `install.sh`) and my commit history, the same as on my computer.

## Part 10: Delete and Clone

### Q1. Navigate out of the project folder
`cd ..`

### Q2. What command deletes the local repository folder?
`rm -rf my-first-repo` (`-r` deletes the folder and everything inside it, `-f` does it without asking)

### Q3. What command clones the repository from GitHub?
`git clone -b my-first-repo https://github.com/eliashaber2007/Object-Oriented-Programming-Test.git my-first-repo` (`-b my-first-repo` picks the branch where I pushed the project, and the last word names the folder)

### Q4. Navigate into the cloned folder and verify the files are there
- `cd my-first-repo`
- `ls` shows `install.sh` and `readme.txt`, and `git log --oneline` shows the full history. Everything came back from GitHub.

## Part 10: Delete and Clone

### Q1. Navigate out of the project folder
`cd ..`

### Q2. What command deletes the local repository folder?
`rm -rf my-first-repo` (`-r` deletes the folder and everything inside it, `-f` does it without asking)

### Q3. What command clones the repository from GitHub?
`git clone -b my-first-repo https://github.com/eliashaber2007/Object-Oriented-Programming-Test.git my-first-repo` (`-b my-first-repo` picks the branch where I pushed the project, and the last word names the folder)

### Q4. Navigate into the cloned folder and verify the files are there
- `cd my-first-repo`
- `ls` shows `install.sh` and `readme.txt`, and `git log --oneline` shows the full history. Everything came back from GitHub.

## Part 11: Full Workflow Practice

Since my GitHub repository is shared with my teacher, I used branches of `Object-Oriented-Programming-Test` instead of creating and deleting separate repositories.

1. Delete the local folder: `cd ~` then `rm -rf my-first-repo` (I first saved a copy of `install.sh` to reuse in step 8)
2. Delete the repository on GitHub: `git push origin --delete my-first-repo` (deletes the `my-first-repo` branch on GitHub)
3. Create the folder: `mkdir bash-installer` then `cd bash-installer`
4. Initialize Git: `git init -b main`
5. Create a `README.md` on main explaining the project
6. Commit it: `git add README.md` then `git commit -m "Add README"`
7. Create the branch: `git switch -c feature-install`
8. Bring the previous script: `cp ~/Desktop/install.sh .` then `chmod +x install.sh`
9. Commit it: `git add install.sh` then `git commit -m "Add install script"`
10. Back to main: `git switch main`
11. Merge: `git merge feature-install`
12. Delete the branch: `git branch -d feature-install`
13. New place on GitHub: a new branch `bash-installer` in the shared repository
14. Push: `git remote add origin https://github.com/eliashaber2007/Object-Oriented-Programming-Test.git` then `git push -u origin main:bash-installer`
