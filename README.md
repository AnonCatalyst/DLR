### DLR (Dead Link Remover)

The DLR (Dead Link Remover) is a Python script designed to efficiently manage and validate a list of URLs contained in a text file. This tool automates the process of checking each link's status, ensuring that only live URLs (those responding with an HTTP status code of 200) are retained while dead links are removed.

### Features:

- **User-Friendly Input Management**: Prompts the user for an input file name, defaulting to `input_links.txt`. If the specified file does not exist, it will continue to request a valid filename until one is provided.
- **Batch Processing**: Links are processed in manageable batches, allowing for efficient network usage and reducing the risk of overwhelming servers.
- **Real-Time Status Checking**: Each URL is checked for its HTTP status, and the script reports whether each link is alive or dead as it processes them.
- **Automatic Dead Link Removal**: Dead links are automatically filtered out and not included in the output file.
- **Output Generation**: The script generates an output file (`alive_links.txt`) containing only the live URLs, making it easy to access and organize your valid links.

### Usage Instructions:

1. Ensure the `requests` library is installed (`pip install requests`).
2. Prepare a text file containing your list of URLs (one URL per line).
3. Run the DLR script and follow the prompts to validate your links.
4. Review the output file for the list of live URLs.

DLR is perfect for anyone looking to maintain a clean and functional list of links, enhancing organization and accessibility. Whether you're managing a personal project, a website, or simply curating resources, DLR provides a straightforward solution for link management.
