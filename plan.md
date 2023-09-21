# File Tool

File Tool is a utility which provides a set of instruction which are parsed by another tool and then the operations on files are done.

## What it has?

File Tool provides instructions and we write these in a file, which is then passed to another file.

This file will have a similar structures as writing a dockerfile.

## Instructions

- NAME, It indicates the name of the file
- PATH, Indicates path of the file
- OPERATION, The operation to perform on file
- RENAME, If operation is MV then provide new name
- DESTINATION, Indicates destination
- START LINE, Starting line number
- END LINE, End line number

## The Tool

Tool should be written in bash so that many features of terminal can be used efficiently.
