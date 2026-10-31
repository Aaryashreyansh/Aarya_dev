# 05. Bash Scripting
Topics: variables, quoting, arguments, exit codes, conditions, loops, functions, pipes, redirection and scheduling concepts.

## Starter script
    #!/usr/bin/env bash
    set -euo pipefail
    echo "Aarya DevOps lab"
    printf 'Current directory: %s\n' "$PWD"

Exercises: accept an argument, check whether a sample file exists, count lines and add clear error messages.

Test scripts on sample files first. Be careful with wildcards, loops and deletion commands.