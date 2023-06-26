### more command

The more command, similar in function to cat, is used to display the contents of the entire file from top to bottom on the screen. The more command displays the content page by page, allowing users to read conveniently. The most basic commands are to press the space bar to display the next page and press the b button to return to the previous page. There is also a "search string" function. The more command reads the file from front to back, so the entire file gets loaded at startup.

# Command Format
more [option] file


### less Command

The less tool is also a tool for the pagination of files or other outputs. More specifically, less is an orthodox tool for viewing the content of files and is extremely powerful.

# Command Format
less [option] file


### The Difference between less, cat, and more:
cat command function: Used to display the contents of an entire file. They were used alone without page turning function. Therefore, it is often used with the command more. The cat command can also combine several files into one file.

more command function: Allows the screen to pause when an entire page is displayed. Press the space bar to continue to show the next screen, or press the q button to quit more and stop the display.

less command function: The less command is similar to the more command. It can also be used to browse more than one page of files. The difference is that the less command can use up and down keys to scroll through files and press the space bar to display files downward. When you want to end browsing, press q in the : prompt of the less command.

In fact, for the three commands, except for the function of merging files (with cat command), the rest of the functions are similar, but they are different regarding browsing habits and display methods.


### head Command
The head command is as easy to understand as its name is. It is mainly used to display the beginning of a file to the standard output. By default, the head command prints the first ten lines of the file.

# Command Format
head [option] file


### tail Command
The tail command is mainly used to display the contents of the specified file. Commonly used to view log files.

# Command Format
tail [option] file