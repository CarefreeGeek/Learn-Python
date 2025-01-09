# # The syntax for opening a file in Python is given below -
# # file object = open(<file-name>, <access-mode>, <buffering>)   

# # File Handling Functions and Methods in Python

# ## Opening a File
# ```python
# def open_file(file_name, access_mode, buffering=0):
#     """
#     Opens a file in the specified mode.

#     Args:
#         file_name (str): The name of the file to open.
#         access_mode (str): The mode in which to open the file (e.g., 'r', 'w', 'a', 'r+', 'w+', 'a+').
#         buffering (int, optional): The buffering size. Defaults to 0.

#     Returns:
#         file: The opened file object.
#     """
#     return open(file_name, access_mode, buffering)
# ```

# ## Reading from a File
# ```python
# def read_file(file_object):
#     """
#     Reads the contents of a file.

#     Args:
#         file_object (file): The file object to read from.

#     Returns:
#         str: The contents of the file.
#     """
#     return file_object.read()

# def read_line(file_object):
#     """
#     Reads a line from a file.

#     Args:
#         file_object (file): The file object to read from.

#     Returns:
#         str: The line read from the file.
#     """
#     return file_object.readline()

# def read_lines(file_object):
#     """
#     Reads all lines from a file.

#     Args:
#         file_object (file): The file object to read from.

#     Returns:
#         list: A list of lines read from the file.
#     """
#     return file_object.readlines()
# ```

# ## Writing to a File
# ```python
# def write_to_file(file_object, content):
#     """
#     Writes content to a file.

#     Args:
#         file_object (file): The file object to write to.
#         content (str): The content to write.
#     """
#     file_object.write(content)

# def writelines_to_file(file_object, lines):
#     """
#     Writes multiple lines to a file.

#     Args:
#         file_object (file): The file object to write to.
#         lines (list): A list of lines to write.
#     """
#     file_object.writelines(lines)
# ```

# ## Closing a File
# ```python
# def close_file(file_object):
#     """
#     Closes a file.

#     Args:
#         file_object (file): The file object to close.
#     """
#     file_object.close()
# ```

# ## File Methods
# ```python
# def file_seek(file_object, offset, whence=0):
#     """
#     Moves the file pointer to the specified position.

#     Args:
#         file_object (file): The file object to move the pointer for.
#         offset (int): The offset from the specified position.
#         whence (int, optional): The position from which to move the pointer (0 - beginning, 1 - current, 2 - end). Defaults to 0.
#     """
#     file_object.seek(offset, whence)

# def file_tell(file_object):
#     """
#     Returns the current file position.

#     Args:
#         file_object (file): The file object to get the position for.

#     Returns:
#         int: The current file position.
#     """
#     return file_object.tell()

# def file_flush(file_object):
#     """
#     Flushes the file buffer.

#     Args:
#         file_object (file): The file object to flush.
#     """
#     file_object.flush()

# def file_truncate(file_object, size=None):
#     """
#     Truncates the file to the specified size.

#     Args:
#         file_object (file): The file object to truncate.
#         size (int, optional): The size to truncate the file to. Defaults to None.
#     """
#     file_object.truncate(size)

# def file_fileno(file_object):
#     """
#     Returns the file descriptor.

#     Args:
#         file_object (file): The file object to get the descriptor for.

#     Returns:
#         int: The file descriptor.
#     """
#     return file_object.fileno()

# def file_isatty(file_object):
#     """
#     Returns whether the file is a tty.

#     Args:
#         file_object (file): The file object to check.

#     Returns:
#         bool: Whether the file is a tty.
#     """
#     return file_object.isatty()

# def file_readable(file_object):
#     """
#     Returns whether the file is readable.

#     Args:
#         file_object (file): The file object to check.

#     Returns:
#         bool: Whether the file is readable.
#     """
#     return file_object.readable()

# def file_writable(file_object):
#     """
#     Returns whether the file is writable.

#     Args:
#         file_object (file): The file object to check.

#     Returns:
#         bool: Whether the file is writable.
#     """
#     return file_object.writable()

# def file_seekable(file_object):
#     """
#     Returns whether the file is seekable.

#     Args:
#         file_object (file): The file object to check.

#     Returns:
#         bool: Whether the file is seekable.
#     """
#     return file_object.seekable()

# def file_closed(file_object):
#     """
#     Returns whether the file is closed.

#     Args:
#         file_object (file): The file object to check.

#     Returns:
#         bool: Whether the file is closed.
#     """
#     return file_object.closed

# def file_mode(file_object):
#     """
#     Returns the file mode.

#     Args:
#         file_object (file): The file object to get the mode for.

#     Returns:
#         str: The file mode.
#     """
#     return file_object.mode

# def file_name(file_object):
#     """
#     Returns the file name.

#     Args:
#         file_object (file): The file object to get the name for.

#     Returns:
#         str: The file name.
#     """
#     return file_object.name

# def file_newlines(file_object):
#     """
#     Returns the file newlines.

#     Args:
#         file_object (file): The file object to get the newlines for.

#     Returns:
#         str: The file newlines.
#     """
#     return file_object.newlines
# ```

































