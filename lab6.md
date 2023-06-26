### Introduction
This lab will introduce the usage of wc and grep commands in Linux.

Great! Let me prepare the lab VM for you. While it's being set up, you can start reviewing the first step of this lab.

wc Command
The wc command is a statistical tool that is used to display the number of lines, words, and bytes contained in a file.

"wc" is an abbreviation for word count.

# Command Format
`wc [option] file`

### grep Command
grep is a very powerful command for finding matching text in a file, accepting regular expressions and wildcards, and using multiple grep command options to generate output in various formats.

grep works like this while searching for a string template in one or more files: If the template includes spaces, it must be referenced and all the strings after the template are treated as file names. The search results are sent to the standard output without affecting the original file content.

grep can be used for shell scripts because grep states the status of the search by returning one of the status values: 0 if the template search succeeded, 1 if the search was unsuccessful and 2 if the searched file did not exist. We can use these return values to perform some automated text processing.

# Command Format
`grep [options] pattern [file]`

### Regular Expressions and grep Commands
A regular expression is a symbolic representation that is used to identify text patterns. To some extent, they are similar to shell wildcards that match file and path names, but they are larger. Many command-line tools and most programming languages support regular expressions to help solve text manipulation problems.

Regular expression metacharacters consist of the following characters:

^ $ . [ ] { } - ? * + ( ) | \