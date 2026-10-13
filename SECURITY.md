# Security Policy

## Supported versions

No versioned application release or support schedule has been published. The latest main branch is the current documentation target. The historical exercise scripts are not present in the current checkout.

## Reporting a vulnerability

Report suspected vulnerabilities privately to the maintainer through [GitHub @brajesh31](https://github.com/brajesh31). If GitHub offers private vulnerability reporting or security advisories for this repository, use that channel. Otherwise use the account's available private contact method. Do not publish exploit details, contact data, passwords, or credentials in an issue or pull request.

Include the affected commit or file, steps to reproduce, expected and actual behavior, and potential impact. Use synthetic data. The maintainer will acknowledge and investigate the report when practical and coordinate a remediation and disclosure timeline.

## Security notes from historical source

The following observations apply to earlier commits, not to executable files in the current main tree:

- The old calculator passes its entry text to Python eval. Python documents that eval executes arbitrary code and that user-supplied input may cause security vulnerabilities. Do not use that implementation with untrusted input; replace it with a restricted arithmetic parser before restoring it.
- The old password generator uses Python's random module. The Python documentation explicitly says random is not for security or cryptographic use. Do not use that implementation to create real account passwords or other security-sensitive secrets; use the secrets module instead.
- The old contact book held records in process memory and exported them to a user-selected CSV path. Treat exports as personal data, store them securely, and do not commit or share them.
- The historical utilities do not implement authentication, encryption, a database, or network services.

References: [Python eval documentation](https://docs.python.org/3/library/functions.html#eval), [Python random documentation](https://docs.python.org/3/library/random.html), and [Python secrets documentation](https://docs.python.org/3/library/secrets.html).
