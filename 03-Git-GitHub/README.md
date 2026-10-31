# 03. Git and GitHub
Concepts: repository, working tree, staging area, commit, branch, merge, remote, pull request, issues and tags.

## Safe starter lab
    mkdir git-practice && cd git-practice
    git init
    printf '# Git Practice\n' > README.md
    git status
    git add README.md
    git commit -m "Add starter README"
    git log --oneline

Exercises: create a feature branch, merge it, explain fetch vs pull, and open a practice pull request.

Never commit API keys, passwords, private keys or access tokens.