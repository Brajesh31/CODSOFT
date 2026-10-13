# Development Guide

## Repository status

The current main branch is documentation-only except for a README timestamp workflow. The five Python programs documented here exist in earlier Git commits but are not files in the current checkout. Avoid writing setup instructions that imply they are currently runnable.

Use [Installation](installation.md) to inspect or recover one historical script. If source is restored, update this guide, README, and the roadmap to match the files that actually exist.

## Historical source map

- The to-do list is a standalone Tkinter window with in-memory listbox items.
- The calculator is a standalone Tkinter keypad and expression entry.
- The password generator uses random choices from letters, digits, and a small punctuation set.
- Rock-paper-scissors uses a random computer choice and determines a winner.
- The contact book uses a local Python list, a Tkinter tree view, and CSV export.

There is no shared package, requirements file, test suite, database schema, or service layer in the current tree.

## Safe development practices

- Never execute the historical calculator with untrusted input; its eval call can run arbitrary code.
- Do not rely on the historical random-based generator for real account passwords.
- Use synthetic names and contact values when testing the contact book.
- Treat contact CSV exports as sensitive personal data and keep them outside version control.
- Avoid committing Python bytecode, virtual environments, local editor files, or generated exports.
- Update documentation and changelog when restoring code, changing behavior, adding dependencies, or changing data handling.

## Suggested local checks after restoring code

For a restored Python file, first inspect the diff and run an appropriate syntax check using the installed Python interpreter. GUI behavior requires a desktop session with Tk support. These are suggested contributor checks; no test or lint workflow currently exists in the repository.

## Pull requests

Follow [Contributing](../CONTRIBUTING.md). Describe what source was restored or changed, how it was reviewed, the commands and checks actually run, and any security or data-format implications.
