# Installation

## Current checkout

The current main branch has no Python program to launch and no requirements file or package manifest. Clone the repository to read its documentation:

~~~sh
git clone https://github.com/Brajesh31/CODSOFT.git
cd CODSOFT
~~~

There is no .env configuration needed. The root .env.example is intentionally a comment-only template.

## Inspect an earlier exercise

The five scripts remain in Git history. From the cloned repository, print one to the terminal:

~~~sh
git show ebdab4e:"TASK 1/TO_DO_LIST.py"
git show 6a2cad5:"TASK 2/CALCULATOR.py"
git show 95197aa:"TASK 3/PASSWORD GENERATOR.py"
git show f621cab:"TASK 4/Rock Paper Scissors Game.py"
git show 9a74ca2:"TASK 5 /Contact Book.py"
~~~

The path for the contact book contains a space after TASK 5. Keep the path quoted. Review the source before running it; the calculator evaluates user-provided Python text and the password generator is not designed for security-sensitive passwords.

To save a historical file from PowerShell, use a quoted path and redirect the output, for example:

~~~powershell
git show 6a2cad5:"TASK 2/CALCULATOR.py" | Set-Content -Encoding utf8 "TASK 2/CALCULATOR.py"
~~~

Check the resulting file before execution. To avoid changing the current checkout, use a separate Git worktree or copy the file to a temporary directory.

## Requirements for recovered programs

The historical scripts use Python standard-library modules, including tkinter, random, string, and csv. They do not pin a Python version. A desktop Python installation with Tcl/Tk support is needed for the GUI; availability depends on the operating system and Python distribution. No third-party Python package installation was required by those historical source files.

For security-sensitive password generation, do not use the historical implementation. Python's secrets module is designed for that purpose; see [Security](../SECURITY.md).
