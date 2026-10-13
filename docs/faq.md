# FAQ

## What is in the current checkout?

The current main tree has no Python application source. It contains repository automation and this documentation. The five GUI exercises remain in earlier Git commits.

## Which programs were in the repository history?

A Tkinter to-do list, calculator, password generator, rock-paper-scissors game, and contact book. See [README](../README.md) for commit hashes and recovery examples.

## Can I run a program after cloning main?

Not directly. Retrieve a historical source file using the commands in [Installation](installation.md). Review it first; the historical calculator uses eval and the password generator uses random.

## Does this project use a database or API?

No. The old exercises were local GUI tools. Contact records and to-do entries were held in memory; the contact book could export a CSV file.

## What should I use for a real password?

Do not use the historical password generator for security-sensitive credentials. Use a maintained password manager or a cryptographically secure generator based on Python's secrets module.

## Is the calculator safe for arbitrary input?

No. The historical calculator evaluates Python expressions from its entry field. Python warns that eval with user-supplied input can cause security vulnerabilities. Do not use it with untrusted input.

## How can I contribute?

Read [CONTRIBUTING](../CONTRIBUTING.md). The current branch is documentation-only; discuss restoration or new source before creating a pull request.

## Where should I report a security issue?

Follow [SECURITY.md](../SECURITY.md) and use a private reporting channel. Do not publish credentials, contact data, or exploit details in an issue.
