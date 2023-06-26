### which Command
The which command is used to search for the executable file's location in the path specified by the PATH variable. Usually, we use it to determine whether the selected software is already installed.

# Command Format
which executable-file-name

### whereis Command
The whereis command is mainly used to locate the executable file, source code file, and help file in the file system. The whereis command also has the ability to search for source code, specifying an alternate search path to search for unusual items.

The whereis command looks up very quickly because it isn't just looking around randomly on disk, but in a database (/var/lib/mlocate/). This database is automatically created by the Linux system, contains information on all local files, and is updated once every day by automatically executing the updatedb command. Precisely since this database is updated once a day, the search results of whereis command may sometimes be inaccurate, such as the files added just now may not be found.

# Command Format
whereis [options] file