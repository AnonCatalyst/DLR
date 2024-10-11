### DLR (Dead Link Remover)

The DLR (Dead Link Remover) is a comprehensive Python script designed to manage and validate a list of URLs in a text file. This tool automates the process of removing duplicate links, checking the status of each remaining URL, and ensuring that only live links (those responding with an HTTP status code of 200) are retained.

### Features:

- **Duplicate Link Removal**: Automatically identifies and removes duplicate URLs from the input file before checking their status.
- **User-Friendly Input Management**: Prompts the user for an input file name, defaulting to `input_links.txt`. If the specified file does not exist, it continues to request a valid filename until one is provided.
- **Batch Processing**: Checks links in manageable batches, optimizing network usage and minimizing server load.
- **Real-Time Status Checking**: Validates each URL's status, providing immediate feedback on whether a link is alive or dead during processing.
- **Automatic Dead Link Removal**: Filters out dead links and retains only the live ones in the output file.
- **Output Generation**: Generates an output file (`alive_links.txt`) containing only the live URLs for easy access and organization.

### Usage Instructions:

1. Ensure the `requests` library is installed (`pip install requests --break-system-packages`).
2. Prepare a text file with your list of URLs (one URL per line), including duplicates.
3. Run the DLR script and follow the prompts to validate your links.
4. Review the output file for the list of live URLs.

DLR is ideal for anyone looking to maintain a clean, organized list of links, whether for personal projects, websites, or resource curation. It streamlines link management by combining duplicate removal with live link validation, providing a straightforward solution for effective link organization.
