# CODSOFT Python Mini Projects

This repository records a set of beginner desktop exercises originally created for CODSOFT. The exercises found in earlier Git commits were a Tkinter to-do list, calculator, password generator, rock-paper-scissors game, and contact book.

> **Current checkout status:** The current main branch does not contain those Python source files. The latest source-history commit removed the five scripts and the original one-line README. The scripts remain available in Git history; this documentation does not imply they are runnable from a fresh clone.

The repository's README timestamp workflow is manual-only. It does not build or deploy an application.

## Historical exercises

| Exercise | Earlier source commit | Earlier behavior |
| --- | --- | --- |
| To-do list | ebdab4e | Tkinter task list with add, edit, delete, clear, and close actions. Items existed only in memory. |
| Calculator | 6a2cad5 | Tkinter interface for basic arithmetic; the historical implementation used Python eval on entry text. |
| Password generator | 95197aa | Tkinter form that generated a requested length from letters, digits, and a small punctuation set using random. |
| Rock-paper-scissors | f621cab | Tkinter player-versus-computer game using random choices. |
| Contact book | 9a74ca2 | Tkinter contact list with search, edit, delete, and CSV export; contacts were held in memory. |

## Recovering a historical script

Clone the repository, then view an earlier committed file directly. For example:

~~~sh
git show ebdab4e:"TASK 1/TO_DO_LIST.py"
git show 6a2cad5:"TASK 2/CALCULATOR.py"
git show 95197aa:"TASK 3/PASSWORD GENERATOR.py"
git show f621cab:"TASK 4/Rock Paper Scissors Game.py"
git show 9a74ca2:"TASK 5 /Contact Book.py"
~~~

To restore a script into a working tree, redirect the selected git show output to a path with the same name, or check out the earlier commit in a separate worktree. Review the source before running it. In particular, the old calculator evaluates typed Python input and the old password generator uses the non-cryptographic random module. See [Security](SECURITY.md).

The historical exercises use Python's standard library and Tkinter; they do not have a package manifest or pinned Python version. A working Python installation with Tcl/Tk support is required to run a recovered GUI. This current main branch contains no script entry point to launch.

## Documentation

- [Architecture and repository history](docs/architecture.md)
- [Installation and recovering historical code](docs/installation.md)
- [Development guide](docs/development.md)
- [Deployment](docs/deployment.md)
- [Historical GUI interfaces](docs/api.md)
- [Data and persistence](docs/database.md)
- [Troubleshooting](docs/troubleshooting.md)
- [FAQ](docs/faq.md)
- [Contributing](CONTRIBUTING.md)
- [Support](SUPPORT.md)
- [Security policy](SECURITY.md)
- [Roadmap](ROADMAP.md)
- [Changelog](CHANGELOG.md)

## License and attribution

Original CODSOFT exercise code and project documentation authored by Brajesh Kumar are licensed under MIT; see [LICENSE](LICENSE). Python, Tkinter, and any future third-party packages remain under their respective terms. CODSOFT is referenced as project context; no endorsement or affiliation is implied.

Last updated: 2026-10-25 05:44 UTC
