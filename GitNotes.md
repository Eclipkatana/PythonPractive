# Git Notes

## Introduction

This document provides basic notes and commands for using Git efficiently.

### Git Commands

#### `git clone`

To clone a repository:
```bash
git clone <repository_link>
```

#### `git checkout`

To switch between branches or create a new branch:
```bash
git checkout -b <branch_name>   # Create and switch to a new branch
git checkout <branch_name>      # Switch to an existing branch
```

#### `git status`

To check the status of your repository:
```bash
git status
```

#### `git add`

To add changes to the staging area before committing:
```bash
git add .
```

#### `git commit`

To commit changes to the repository:
```bash
git commit -m "commit_message"
```

#### `git push`

To push changes to a remote repository:
```bash
git push <remote_name> <branch_name>
```

#### `git commit --amend`

To amend the last commit:
```bash
git commit --amend
```
After this, need to force push. add -f after 
#### `git pull`

To pull changes from a remote repository:
```bash
git pull <remote_name> <branch_name>
```
Example: 
```bash
git pull origin master
```
#### `git rebase`. Check google: Git rebase vs git merge

To rebase changes from one branch onto another:
```bash
git rebase <base_branch>
```
Exp: 

```bash
git rebase master
```

#### `git remote`

To manage remote repositories:
```bash
git remote -v                   # List all remotes
git remote rm <remote_name>    # Remove a remote
git remote add <remote_name> <repository_link>  # Add a new remote
```

#### `git branch`

To manage branches:
```bash
git branch                     # List all branches
git branch -D <branch_name>    # Delete a local branch
```

#### Restore a Branch

To restore a branch:
```bash
git checkout -b <branch_name> <commit_hash>
```
<commit_hash> is branch code

#### `git cherry-pick`

To pick a commit from one branch and apply it to another:
```bash
git cherry-pick <commit_hash>
```

These are basic Git commands and concepts to get started with version control.
