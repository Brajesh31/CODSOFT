# Contributing

Thanks for helping improve this repository. The current main branch is documentation-only apart from repository automation; the five historical Tkinter exercises are available in earlier Git commits. Please read this guide and the [Code of Conduct](CODE_OF_CONDUCT.md) before contributing.

## Before starting

- Check existing issues and pull requests to avoid duplicate work.
- For larger changes, first describe the goal and proposed scope in an issue.
- Do not commit contact lists, exported CSV files, passwords, credentials, or other personal data.
- Check licenses before adding dependencies, images, fonts, or copied code.

## Development setup

There is no Python source file or package manifest in the current checkout. To inspect a historical file, use the commands in [Installation](docs/installation.md). If you restore or add a Tkinter exercise, use an environment with Python and Tcl/Tk available.

For a recovered or restored Python script, review it before execution. The historical calculator evaluates user-entered Python expressions, and the historical password generator uses random rather than a cryptographic generator; see [Security](SECURITY.md).

## Contribution expectations

- Keep each exercise independent unless a shared application is intentionally introduced.
- Prefer clear input validation, accessible control labels, and explicit error handling.
- Do not use eval on untrusted input. Use a restricted arithmetic parser for calculator expressions.
- Use Python's secrets module for password generation intended to protect accounts or other real secrets.
- Keep private contact data and exported files outside the repository.
- Update README and the relevant docs if files, commands, dependencies, or behavior change.
- Do not commit virtual environments, bytecode caches, local IDE state, or generated exports.

## Pull request process

1. Branch from main using a descriptive name.
2. Make the smallest coherent change that addresses an issue or clearly improves the project.
3. Review the full diff, including filenames containing spaces, and confirm no private data is present.
4. Run relevant checks for changed Python files. If you restore a historical GUI, at minimum verify syntax and manually exercise it in a desktop session; record any checks you could not run.
5. Open a pull request against main with the reason for the change, a summary, verification results, and screenshots for visible UI changes. Use synthetic contact data.
6. Call out any change to data storage, CSV format, or security behavior.

There is no formal release process or response-time commitment. Maintainers may request revisions before merging.

## Commit messages

Use concise messages that describe the change, such as docs: explain historical exercise recovery or fix: replace unsafe expression evaluation.

## Security reports

Do not file suspected vulnerabilities publicly. Follow [SECURITY.md](SECURITY.md) to report them privately.
