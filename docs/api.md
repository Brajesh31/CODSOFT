# User Interface Reference

## No current application API

The current main branch has no runnable GUI or HTTP endpoint. The historical scripts were standalone desktop programs with Tkinter controls. They did not expose REST, GraphQL, command-line service, or library APIs.

This document describes their historical controls for context only.

## Historical interfaces

### To-do list

The old to-do window accepted text and offered Add, Delete, Update, Clear All, and Close actions. Adding blank input showed a warning. Items were held in a Tkinter listbox and disappeared when the process ended. Editing an item used a dialog.

### Calculator

The old calculator had a text entry, digit buttons, arithmetic operators, AC, and equals. It attempted to evaluate the entire entry as a Python expression. This is unsafe for untrusted input and should be replaced before restoring the program; see [Security](../SECURITY.md).

### Password generator

The old generator accepted a positive integer length and displayed a generated string. Its alphabet included uppercase and lowercase letters, digits, and the punctuation characters @ # $ ^ & * _. It did not expose controls for requiring a category, excluding ambiguous characters, or copying the result. It used random, which is unsuitable for security-sensitive passwords.

### Rock-paper-scissors

The old game offered Rock, Paper, and Scissors buttons. Each choice selected a computer move and displayed the computer choice plus win/loss/tie result. It did not keep a score or persist history.

### Contact book

The old contact book supported adding, viewing, searching by name or phone, updating, deleting, and exporting visible records to CSV. Contact fields were name, phone, email, and address. There was no storage/reload feature in the historical source.

## Data and error behavior

Historical behavior is described from source and is not a supported API contract. The scripts had no stable schemas, serialization formats beyond the contact CSV header, or compatibility guarantees.
