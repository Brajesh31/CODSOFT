# Deployment

## Current deployment status

This repository contains no runnable application in the current main tree and has no application deployment configuration. The only current GitHub Actions workflow updates the README timestamp; it does not build, package, or publish the historical Tkinter programs.

The historical exercises are desktop GUI programs. They were not web services and did not include a deployment pipeline, server, installer, or release artifact.

## Running recovered scripts

A recovered script runs locally on a desktop with Python and Tkinter available. See [Installation](installation.md) for the Git history commands. Run only reviewed source, particularly because the historical calculator evaluates entered Python expressions.

No app deployment is configured. Do not describe the repository as hosted software or assume that the README automation publishes application code.

## Future packaging

If executable source returns to main, first choose a supported Python version and operating systems, document Tcl/Tk requirements, and verify each script on supported platforms. A future installer or packaged release should include only the selected program files, a license, and clear security/data handling notes. Add automated packaging only after the source layout and release target are defined.

## README automation

.github/workflows/update-readme.yml can be dispatched manually to create or edit README.md. It is repository housekeeping, not a publishing workflow.
