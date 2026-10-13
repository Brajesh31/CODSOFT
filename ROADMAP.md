# Roadmap

These are possible improvements based on the current repository history. They are proposals, not release commitments.

## Repository clarity

- Decide whether the exercises should be restored to main, moved to separate repositories, or kept as history-only examples.
- If code is restored, make README commands match the actual files and document a supported Python version.
- Add a lightweight validation workflow only after runnable source is present.

## If the exercises are restored

- Replace unrestricted eval in the calculator with a parser that accepts only arithmetic operations.
- Use secrets for password generation when passwords are intended for actual security use; document the permitted character policy.
- Add input validation, keyboard behavior, and accessibility improvements to the Tkinter interfaces.
- Give the contact book explicit import/export handling and data-retention guidance; keep personal exports outside version control.
- Add repeatable checks for the underlying game and utility logic, separate from GUI code.

## Project maintenance

- Add examples and screenshots using synthetic inputs.
- Document dependency and platform requirements if third-party packages or platform-specific features are introduced.
- Publish releases only after defining a maintenance and support process.

Discuss a proposal in an issue before making a broad change. See [Contributing](CONTRIBUTING.md).
