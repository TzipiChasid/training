### find Command
The main function of the find command is to traverse down the file hierarchy, match the files that meet the conditions, and perform the corresponding operations. Under Linux systems, find command provides a lot of search conditions. The function is very powerful and the corresponding learning is also much more difficult.

# Command Format
`find option [expression]`

### find Command
To find files by file type, use the -type option.

### xargs Command
We can use pipe to redirect stdout (standard output) of one command to stdin (standard input) of another command. However, some commands can only receive data in the form of command-line parameters and cannot receive data streams through stdin. In this case, data cannot be redirected to these commands through pipes.

In such cases, xargs can play its role. The xargs command can receive input from standard input and convert that to a specific parameter list.

# Command Format
`command | xargs [Options] command`