# Troubleshooting

## There is no program to launch

That is expected on the current main branch: the five historical Python files were removed by commit 3b00c41. Use the Git history commands in [Installation](installation.md) to inspect or recover a script.

## Tkinter cannot create a window

The old programs require a desktop Python environment with Tcl/Tk support. A minimal or headless environment may not include Tk or a display server. Check that tkinter imports in the same Python installation used to run the script, and run GUI programs in a desktop session.

## Git cannot find a historical file

Confirm that the repository history is complete and that the path is quoted. The contact book path includes an embedded space: TASK 5 /Contact Book.py. Use the exact commit hash and path from [Installation](installation.md).

## The historical calculator displays Error

The old calculator catches all exceptions and replaces the entry with Error. Check that the typed expression ends in a valid value and uses supported arithmetic syntax. Do not use eval to process untrusted input; fix the implementation with a restricted parser before restoring it.

## The password generator output is not suitable for real credentials

The historical source used Python random. That generator is not intended for cryptographic security. Use the secrets module for security-sensitive random values and do not reuse an output from the old script as a real account password.

## Contacts disappear after closing

The historical contact list was held in memory. Exporting to CSV was manual, and the old program did not load exported CSV files on startup. Treat any exported file as sensitive personal data.

## A workflow changes README

The repository has a manually dispatched README timestamp workflow. Its edits are housekeeping; it does not run Python applications or publish releases.
