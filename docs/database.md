# Data and Persistence

## Current state

There is no database or persistence layer in the current checkout. The historical scripts did not connect to a database, server, or cloud service.

## Historical in-memory data

- To-do entries were kept in the GUI listbox.
- Contact book records were held in a process-local list of Contact objects with name, phone, email, and address values.
- Calculator state, generated password text, and game results existed only in their current GUI process.

When those processes closed, in-memory values were lost.

## Contact CSV export

The historical contact book could export current records to a user-selected CSV file with columns Name, Phone, Email, and Address. It did not provide an import or automatic reload operation. Exports may contain sensitive personal information:

- Use synthetic data when demonstrating or testing the program.
- Save exports in a private location with appropriate device access controls.
- Do not commit exports, send them in public issues, or include real contact details in screenshots.
- Delete local exports when no longer needed, following applicable retention expectations.

The root .gitignore ignores CSV files to reduce accidental commits. This does not replace secure storage or careful handling.

## If persistent storage is added

Document where records live, what fields are collected, who can access them, how exports/imports work, how data is deleted, and any migration path. Avoid collecting more personal data than the feature needs. No schema or database migration is currently supported.
