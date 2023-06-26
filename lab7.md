### cut Command
The cut command is a gadget that splits the text into columns, and it can specify the delimiter that separates the columns in its output.

If a row of data contains more than one field (multiple columns) and you now want to extract one or more of them, for this you have the cut command.

# Command Format
`cut [option] file-name`

### paste Command
The function of the paste command is exactly the opposite of cut. It adds one or more text columns to a file. It reads multiple files and then combines the fields in the files into a single text stream that is input to the standard output.

# Command Format

`paste [option] file-name`

### tr Command
The tr command is often used to change characters. We can think of it as a character-based "search and replace" operation. The word change is the process of converting characters from one letter to another. tr replaces, reduces (squeezes), and/or deletes characters from standard input and writes the result to standard output.

tr can read only from stdin (standard input) and cannot accept input via command-line arguments.

"tr" is the abbreviation for translate.

Command Format
`tr [options] SET1 SET2`