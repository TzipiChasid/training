### df Command
The function of the df command in Linux is to check the disk space usage of the file system. You can use this command to find out how much space on your hard disk is occupied and how much space is left free (unused).

"df" is an acronym for disk free.

# Command Format
`df [option] file`

### du Command
The du command in Linux also looks at the space used, but unlike the df command, the du command is used to view the space used by files and directories on a disk.

"du" is an acronym for disk usage.

# Command Format
`du [option] file`

### time Command
The time command is often used to measure the running time of a command, including the actual time, the processing time spent in user mode, and the processing time spent in kernel mode.

Actual time: The time from the submission of the command on the command line to the end of its run.

User mode usage time: The user CPU time spent to complete the command execution, that is, the sum of the execution time slices of the command in the user mode.

Kernel state usage time: The system CPU time spent executing the command, that is, the sum of the execution time slices of the command in the core state.

# Command Format
`time command`