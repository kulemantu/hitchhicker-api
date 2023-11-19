"""
garbage_collector.py
--------------------

This module provides functionality for managing storage space in a directory by
garbage collecting older files. It is designed to keep the total size of files in
a specified directory below a defined threshold by removing the oldest files first.

Example Usage:
--------------
from file_utils import garbage_collector
garbage_collector(100, '/path/to/metrics') # Adjust the path and size limit as needed
"""

import os
import logging
from pathlib import Path

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def garbage_collector(max_storage_mb, directory):
   """
    Garbage collects files in the specified directory to maintain a maximum storage size.

    This function calculates the total size of files in the given directory. If the total
    size exceeds the specified maximum storage size, it deletes the oldest files first
    until the total size is within the limit.

    Parameters:
    max_storage_mb (int): Maximum storage size in megabytes.
    directory (str): Path to the directory containing the files.

    Side Effects:
    - Deletes files from the filesystem.
    - Logs actions and errors to the console.

    Returns:
    None

    Raises:
    Exception: Describes any exceptions that are caught during the execution of the function.
    """

    # Convert MB to bytes for size comparison
    max_storage_bytes = max_storage_mb * 1024 * 1024

    # Check if the directory exists
    if not os.path.exists(directory):
        logging.error(f"Directory does not exist: {directory}")
        return

    try:
        # Get all files in the directory with their paths and sizes
        files = [(file, os.path.getsize(file), os.path.getmtime(file)) for file in Path(directory).glob('*')]
        
        # Sort files by modification time (newest first)
        files.sort(key=lambda x: x[2], reverse=True)

        total_size = 0
        for file, size, _ in files:
            total_size += size

            # If the total size exceeds the maximum storage limit, delete the file
            if total_size > max_storage_bytes:
                os.remove(file)
                logging.info(f"Deleted: {file}")

    except Exception as e:
        logging.error(f"An error occurred: {e}")
