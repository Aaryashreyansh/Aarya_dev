"""A safe, read-only starter system report. Uses Python standard library."""
import platform
import os
from pathlib import Path

def main():
    print("Aarya DevOps - System Report")
    print("OS:", platform.system(), platform.release())
    print("Python:", platform.python_version())
    print("Machine:", platform.machine())
    print("CPU count:", os.cpu_count())
    print("Current folder:", Path.cwd())

if __name__ == "__main__":
    main()
