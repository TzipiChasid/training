### mkdir
sudo apt-get update
sudo apt-get install tree

mkdir -vp shiyanlou/{lib/,bin/,doc/{info,product}}
tree shiyanlou/
![tree](assets/tree.png)


# To create multiple directories recursively, you can use the following command:

`mkdir -p [name directory]/test`

# To create a directory with privileges 777, use the following command:

`mkdir -m 777 [name directory]`

# To create a directory and display a success message, use the following command:

`mkdir -vp [name directory]/test`


### rm 
This command is to delete one or more files or directories in a directory. It can also delete a directory and all files and subdirectories under it. For the link file, only the link is deleted, leaving the original file unchanged.
"rm" is short for remove.

Command Format:
`rm [options] file-or-directory`

answer:
1. D is a variable that receives routing, create a folder whose routing is D
Then move all the files into the folder

# Delete the file. The system will first ask whether to delete. You can use the following command:

`rm <name file>`

#  Forcibly deleting files. The system does not prompt confirmation. You can use the following command:

`rm -f <name file>`

#  Delete all the .<file extension> files with the specified suffix. Before deleting them, you can use the following command:

`rm *.<file extension> --OR-- rm -i *.<file extension>`

### mv
The mv command's function is to move files or change file names. It is a commonly used command on Linux systems and is often used to back up files or directories.
When the second parameter is an existing directory name, there can be multiple source files or directory parameters. The mv command moves the source files specified by each parameter to the target directory.
"mv" is an abbreviation of move


Command Format:
`mv [options] source-file-or-directory target-file-or-directory`


# Changing a file name by the command:
`mv <file1 name> <file2 name>`

### cp
The cp command is used to copy files or directories and is one of the most commonly used commands on Linux systems.

"cp" is an abbreviation for copy.

Command Format:
`cp [options] source-file directory`


Specify the target directory.

`-t --target-directory`

Ask before overwriting (Make the -n option invalid).
`-i --interactive`

Do not overwrite existing files (Disable -i option).
`-n --no-clobber`

Create symbolic links to source files instead of copying files.
`-s --symbolic-link`

Forcibly copy files or directories, regardless of whether the destination files or directories already exist.
`-f --force`

When using this parameter, the file copy operation only performs when the source file's modification time is more (later) than the destination file or the corresponding destination file does not exist.
`-u --update`
### cat
The function of the cat command is to output a file or standard input combination to standard output. 

"cat" is an abbreviation for concatenate.

command format:
`cat [option] [file]`

Equivalent to -vET
`-A --show-all`

Number of non-empty output lines.
`-b --number-nonblank`

Equivalent to -vE.
`-e`

Display $ at the end of each line.

`-E --show-ends`

Display line numbers, starting from 1.
`-n --number`

If there are two or more consecutive blank lines, replace them with a single blank line.
`-s --squeeze-blank`

Is equivalent to -vT.
`-t`

Display tab characters as ^I.
`-T --show-tabs`

(Be ignored).
`-u`

Use ^ and M-references, except LFD and TAB.
`-v --show-nonprinting`

answer:
1. this command show all the files in EOF

### nl
The nl command is used in the Linux system to calculate the number of lines in a file.

"nl" is an abbreviation for number of lines.

Command Format
`nl [option] file`

There are two main ways to specify the line numbers with -b
`-b`

Indicates that the line number is listed irrespective of whether a line is blank (similar to cat -n).
`-b a`

If there is an empty line, do not list the line number in the empty line (default).
`-b t`

There are three main ways to list line numbers with -n.
`-n`

The line number is displayed at the far left of the screen.
`-n ln`

The line number is displayed on the far right of its own field without adding '0's to the left.
`-n rn`

The line number is displayed on the far right of its own field, left padded with '0's.
`-n rz`

The number of digits occupied by the row number field.
`-w`
