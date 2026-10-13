# Architecture and Repository History

## Current main branch

At the baseline commit 3b00c41, the current main tree contained the README timestamp automation workflow but no application source, package metadata, or README content. That commit removed five Python scripts that had been added in earlier commits. This handbook documents the repository's history and current state; it does not restore the removed programs.

The only workflow present is .github/workflows/update-readme.yml. It can be dispatched manually to update or create a README timestamp. It is not an application build, test, or deployment pipeline.

## Historical program structure

The earlier files were separate Python/Tkinter desktop scripts rather than one integrated application:

| Historical script | Main implementation |
| --- | --- |
| TASK 1/TO_DO_LIST.py | Tkinter window with an entry field, listbox, and add/edit/delete/clear buttons. |
| TASK 2/CALCULATOR.py | Tkinter entry and button grid; arithmetic result produced with eval. |
| TASK 3/PASSWORD GENERATOR.py | Tkinter length input and generated-password field; used random. |
| TASK 4/Rock Paper Scissors Game.py | Tkinter choice buttons and computer selection with random. |
| TASK 5 /Contact Book.py | Tkinter tree view and dialogs; records in a Python list; CSV export. |

Each script created its own Tk root and event loop. There was no shared application shell, package, API, network service, database, or persistence layer.

## Data flow and persistence in historical snapshots

- The to-do list stored items in a listbox widget only. Closing the program discarded them.
- The contact book stored Contact objects in a process-local list. Its export action wrote name, phone, email, and address columns to a user-selected CSV file. No import or reload path was present.
- The calculator, password generator, and game had no persistent data.
- None of the programs used a server or called a remote API.

## Recovery and future structure

The current checkout is not executable as an application. To inspect or recover a historical file, use the commit references and git show commands in [Installation](installation.md). If the project is restored, decide whether the exercises remain independent scripts or become a structured package before introducing shared modules or tooling.

Security limitations of the historical calculator, generator, and contact export are described in [Security](../SECURITY.md).
