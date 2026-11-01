# Phase 2 — Scripting (Weeks 5–8)

**Outcome:** write small, reliable automation scripts and explain how they handle input, errors and files.

## Week 5 — Python foundations
1. Install/use Python 3 and verify with `python --version` or `python3 --version`.
2. Learn variables, naming, comments, strings, integers, floats and booleans.
3. Practise operators, comparisons, type conversion and formatted strings.
4. Use `input()` for simple input; validate values instead of assuming they are correct.
5. Learn `if/elif/else`, `for`, `while`, `range`, `break` and `continue`.
6. Understand lists, tuples, dictionaries and sets; choose a structure based on how data is used.

**Practice set:** temperature converter, even/odd checker, multiplication table, word counter, simple menu, list statistics, dictionary-based contact sample, and a loop that reads sample lines.

## Week 6 — Functions, files and errors
1. Define functions, parameters, return values, scope and docstrings.
2. Split code into modules and use imports.
3. Read and write text files with `with open(...)`; understand encoding.
4. Read/write JSON using the standard `json` module.
5. Handle expected failures with `try/except/else/finally`; do not hide all errors with a broad empty handler.
6. Use `pathlib` for paths and `argparse` for command-line arguments.
7. Learn logging levels: DEBUG, INFO, WARNING, ERROR and CRITICAL.

**Lab:** read a sample log file, count total lines and occurrences of INFO/WARNING/ERROR, and print a summary. Do not alter the source log.

## Week 7 — Practical Python automation
1. Learn virtual environments with `python -m venv .venv`.
2. Understand dependency installation and a requirements file.
3. Learn HTTP request concepts, status codes, JSON responses and timeouts.
4. Use a documented public test API only where its terms allow; never put API tokens in code.
5. Learn basic unit tests with `unittest` or `pytest`.
6. Learn code formatting, readable naming and small functions.
7. Write 5 more small programs, bringing the practice total to at least 10.

## Week 8 — Bash and scheduling
1. Understand shebang, executable permission, variables and quoting.
2. Practise positional arguments, `if`, `case`, loops and functions.
3. Understand exit codes, `$?`, standard streams, pipes and redirection.
4. Learn defensive script habits such as clear error messages and predictable paths.
5. Understand cron fields: minute, hour, day of month, month and day of week. Check the local system's scheduler documentation; Android app environments may not provide a normal cron service.
6. Test scheduling with a harmless script that writes a timestamp to a lab file.

## Mini project — Backup/report utility
Create a Python or Bash tool that:
- accepts a source folder and destination folder;
- validates that both paths are expected;
- supports a dry-run mode that lists planned actions;
- creates a dated backup or a read-only report;
- writes a log and returns a useful exit status;
- never deletes source data;
- documents restore/verification steps.

## Exit checklist
- [ ] 10+ small Python programs are saved and tested.
- [ ] Functions, loops, files, JSON and exceptions are used correctly.
- [ ] A harmless script has been scheduled in a personal lab, or the platform limitation is documented.
- [ ] The mini project has a README, sample input/output and tests.


## Where to learn this phase
See [Resources Directory](RESOURCES.md): Python → official Python Tutorial and standard library; Bash → GNU Bash manual; script quality → ShellCheck; small Python exercises → Exercism. Check platform compatibility before trying cron.
