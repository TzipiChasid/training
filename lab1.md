### cd Command
The cd command is the most basic command statement in Linux. Other command statements are to be operated on using the cd command. The cd command is an abbreviation of "change directory", which switches the current directory to another one you specified.

# Command Format
cd [Directory ]


# List the details of all the files and directories in the /home folder. You can use the following command:

`ls -a -l /home , ls -al /home`

# create a test file

`cd /home`
`sudo touch labex.txt`

# List the contents of all the file directories starting with "d" in the current directory. You can use the following command:

`sudo ls -l d*`

# List the size of all the file directories in the /home directory in an easy-to-understand format. You can use the following command:

`ls -alh /home -<name file>`

# task 1

1. `ls -d  s*/home -<name file>`

2. `ls -alh d* /home -<name file>`

# The cd command is the most basic command statement in Linux. Other command statements are to be operated on using the cd command. The cd command is an abbreviation of "change directory", which switches the current directory to another one you specified

`cd [Directory ]`

### pwd Command
Use the pwd command in Linux to see the full path of the "current working directory". You will have a current working directory every time you operate in the terminal. If you are uncertain about the current path, pwd is the best way to determine the exact location of the current directory within the file system.

The pwd command is an acronym for Print Working Directory.

# Command Format
`pwd [OPTION]`
#  To display the path of the current directory, use the following command:

`pwd`

# To display the physical path of the current directory, use the following command:

`pwd -P`

# To display the connection path of the current directory, use the following command:

`pwd -L`






