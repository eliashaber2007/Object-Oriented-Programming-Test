# Git Mini Exercise

## Part 1: Setup & config
1. Git was already installed on my Mac.
2. `git --version` gives `git version 2.50.1 (Apple Git-155)`
3. `git config --global user.name "Elias Habr"` and `git config --global user.email "your-email@example.com"`

## Part 2: Create Your First Repository
- `mkdir my-first-repo`
- `cd my-first-repo`
- `git init -b main`
- `touch readme.txt`

## Part 3: Your First Commit
1. `git status`
2. `git add readme.txt`
3. `git commit -m "Add readme file"`
4. `git log`

## Part 4: Make Changes
1. `echo "This is my first Git repository." >> readme.txt`
2. readme.txt shows as modified but not staged, so it won't be in the next commit until I add it.
3. `git add readme.txt` then `git commit -m "Add description line to readme"`
4. 2 commits

## Part 5: Exploration
- `git diff` shows the changes I made that are not staged yet (+ for added lines, - for removed ones).
- `git log --oneline` shows the commit history, one line per commit.

## Part 6: Working with Branches
1. `git branch`
2. `git branch feature-script`
3. `git switch feature-script`
4. `git switch -c dev`
5. `git switch feature-script`
6. `git branch` (the current branch has a * next to it)

## Part 7: Create a Bash Script on a Branch
1. `git branch` shows I'm on feature-script
2. `touch install.sh`
3. Script below
4. `chmod +x install.sh`
5. `git add install.sh` then `git commit -m "Add install script"`
6. `git log --oneline` shows the new commit at the top

Content of install.sh:

    #!/bin/bash
    echo "Starting installation..."
    sudo apt update
    sudo apt install -y curl
    echo "Installation complete!"

## Part 8: Merge Branches
1. `git switch main`
2. No, because install.sh was only committed on feature-script, not on main.
3. `git merge feature-script`
4. install.sh is now there.
5. The install script commit is now in main's history. It was a fast-forward merge, so no extra merge commit.
6. `git branch -d feature-script`

## Part 9: Push to GitHub
I used my course repo (shared with my teacher) instead of a new one, and pushed the project to a branch called my-first-repo. A new repo should be created without a README, otherwise the first push gets rejected.

3. `git remote add origin https://github.com/eliashaber2007/Object-Oriented-Programming-Test.git`
4. `git push -u origin main:my-first-repo`
5. The files and commits show up on GitHub on the my-first-repo branch.

## Part 10: Delete and Clone
1. `cd ..`
2. `rm -rf my-first-repo`
3. `git clone -b my-first-repo https://github.com/eliashaber2007/Object-Oriented-Programming-Test.git my-first-repo`
4. `cd my-first-repo` and `ls`, the files are back.

## Part 11: Full Workflow Practice
Same steps again, with a branch called bash-installer instead of a new repo.

    cd ~
    rm -rf my-first-repo
    git push origin --delete my-first-repo
    mkdir bash-installer
    cd bash-installer
    git init -b main
    # wrote README.md explaining the project
    git add README.md
    git commit -m "Add README"
    git switch -c feature-install
    cp ~/Desktop/install.sh .
    chmod +x install.sh
    git add install.sh
    git commit -m "Add install script"
    git switch main
    git merge feature-install
    git branch -d feature-install
    git remote add origin https://github.com/eliashaber2007/Object-Oriented-Programming-Test.git
    git push -u origin main:bash-installer

## Reflection Questions
1. It keeps the history of the project, so I can go back if something breaks and work with others without overwriting their work.
2. Staging picks which changes go in the next commit, committing saves them in the history.
3. After each small change that works.
4. `git init` creates a new repo, `git clone` copies an existing one from GitHub.
5. So you and others can understand what changed and why.
6. To work on something without touching main.
7. When adding a new feature or trying something that could break main.
