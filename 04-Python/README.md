# 04. Python 🐍
Topics: variables, types, conditions, loops, functions, collections, exceptions, modules, virtual environments, files, JSON, APIs, logging and tests.

## Starter exercise
    from pathlib import Path
    lab = Path("devops-lab")
    lab.mkdir(exist_ok=True)
    (lab / "hello.txt").write_text("Hello from Aarya DevOps!\n", encoding="utf-8")
    print((lab / "hello.txt").read_text(encoding="utf-8"))

Exercises: list files in a practice folder, read JSON, handle a missing file and write timestamped logs. Use virtual environments and never hard-code secrets.