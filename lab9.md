### comm Command
It is often helpful to compare the contents of text files. This is especially important for system administrators and software developers. A system administrator may, for example, need to compare existing configuration files with previous versions to diagnose a system error. Similarly, a programmer often needs to check the program's changes.

The comm command will compare two files already sorted line by line. The display consists of three columns: Column 1 depicts the lines found only in the first file, Column 2 depicts the lines found only in the second file and Column 3 depicts the lines common to both files.

Note that the comm command, like join and uniq commands, can only be used for data that has already been sorted.

# Command Format
`comm [option] file1 file2`

### diff Command
Like the comm command, the diff command is used to monitor the differences between files. However, diff is a more sophisticated tool that supports many output formats and can handle many text files at a time. Software developers often use the diff program to check for changes between source code versions of different programs. diff can recursively examine the source directory, often referred to as the source tree. A common use case for diff programs is to create a diff file or patch that will be used by other programs, such as the patch program (which we'll talk about later) to convert files from one version to another.

diff prints every line change on the command line, and diff is an integral part of version control tools such as svn, cvs, git, and so on.

"diff" is an abbreviation for differential.

# Command Format
`diff [option] file`

### patch Command
The patch command is used to apply the changes to a text file. It accepts output from the diff program and is usually used to convert older file versions to newer file versions. Let us consider a well-known example. The Linux kernel was developed by a large, loosely-organized team of contributors who submitted a fixed number of changes to the source package. This Linux kernel is made up of millions of lines of code, though each contributor makes very few changes each time. For a contributor, it makes no sense to send the entire kernel source tree to each developer for every modification. Instead, submit a diff file. A diff file contains the difference between the previous kernel version and the new version with contributor modifications. A recipient then uses the patch program to apply these changes to his own source tree.

Using the diff/patch combination provides two major advantages:

A diff file is very small, compared to the size of the entire source tree.
A diff file succinctly shows the changes, allowing reviewers of program patches to evaluate them quickly.
Of course, diff/patch works on any text file, not just on source files. It also applies to configuration files or any other type of text.

Prepare a diff file for the patch command. The GNU documentation recommends using the diff command like this:

diff -Naur old_file new_file > diff_file
Here old_file and new_file sections are not necessarily single files or directories that contain files. This -r option supports recursive directory trees.

# Command Format
`patch [options] patch-file`