
# Solve find-prompt.pdf in 45 Minutes

### Finding Files

To find files in a directory and its subdirectories, use the following command:



`find /path/to/directory -name "filename.txt"`

Replace `/path/to/directory` with the directory you want to search in, and `"filename.txt"` with the name of the file you're looking for. You can use wildcards (`*`) to match multiple files.


### Filtering by Type

To filter the search results by file type, use the `-type` option followed by a single letter code:

-   `f` for regular files
-   `d` for directories
-   `l` for symbolic links

For example, to find all regular files with the extension `.txt`, use:


`find /path/to/directory -type f -name "*.txt"`
