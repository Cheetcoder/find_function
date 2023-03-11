In this implementation, we define a `findFiles()` function that uses the built-in Node.js modules `fs` and `path` to recursively search for files in a directory and its subdirectories. The `fileName` argument is used to match filenames, and the `fileType` argument is used to filter by file type.

In the `main()` function, we parse command-line arguments using `process.argv` and call `findFiles()`, and print the results.

To find files in a directory and its subdirectories, run the script with the directory you want to search in as the first argument, and the name of the file you're looking for as the second argument. For example, to find all files with the name `example.txt` in the directory `/path/to/directory`, use:

bashCopy code

`node find_files.js /path/to/directory example.txt`

To filter the search results by file type, pass the file type as the third argument. For example, to find all regular files with the extension `.txt` in the directory `/path/to/directory`, use:

bashCopy code

`node find_files.js /path/to/directory "" txt`

This implementation provides a pure JavaScript solution for finding files in a directory and its subdirectories with various filtering options, without using any external libraries.
