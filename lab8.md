### sort Command
When dealing with text files, you can't avoid sorting. That's because sorting can play a big role in text-processing tasks. The sort command helps us sort text files and stdin. Usually, it combines other commands to generate the desired output.

# Command Format
`sort [option] file-name`

### uniq Command
The uniq command is often used in conjunction with the sort command. uniq accepts an ordered list of data from standard input or a single file name parameter, and by default removes any duplicate rows from the data list.

uniq can only be used for sorted data input, so uniq uses either piped or sorted files as input and is always used in conjunction with the sort command in this way.

"uniq" is an abbreviation for unique.

# Command Format
`uniq [option] [file-name]`

### join Command
The join command is similar to paste which adds columns to the file, but it uses a unique approach. A join operation is usually associated with a relational database in which data from multiple tables sharing common key fields is combined to obtain the desired result. This join command does the same thing and it combines data from multiple shared key domain-based files.

In layman's terms, it is used to connect the two lines with the same field in the two files, that is, to splice the corresponding lines into one line according to a common column in the two files.

# Command Format
`join [option] file1 file2`