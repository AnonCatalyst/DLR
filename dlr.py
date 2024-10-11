import requests
from time import sleep
import os

def is_link_alive(url):
    try:
        response = requests.head(url, allow_redirects=True, timeout=5)
        return response.status_code == 200  # Check for status code 200
    except requests.RequestException:
        return False

def get_input_file():
    while True:
        input_file = input("Enter the input file name (or press Enter to use 'input_links.txt'): ") or 'input_links.txt'
        if os.path.isfile(input_file):
            return input_file
        else:
            print(f"File '{input_file}' does not exist. Please enter a valid file name.")

def filter_links(input_file, output_file, batch_size=5):
    with open(input_file, 'r') as infile:
        links = infile.readlines()

    alive_links = []
    total_links = len(links)
    
    print(f"Total links to check: {total_links}\n")
    
    for i in range(0, total_links, batch_size):
        batch = links[i:i + batch_size]
        print(f"Checking batch {i // batch_size + 1}...")
        
        for link in batch:
            link = link.strip()
            if link:  # Check if link is not empty
                print(f"Testing: {link}...")
                if is_link_alive(link):
                    print(f"✔️ Alive: {link}")
                    alive_links.append(link)
                else:
                    print(f"❌ Dead: {link}")
        
        sleep(1)  # Sleep to avoid overwhelming the server

    with open(output_file, 'w') as outfile:
        for link in alive_links:
            outfile.write(link + '\n')

    print(f"\nAlive links written to {output_file} ({len(alive_links)} found).")

if __name__ == "__main__":
    input_file = get_input_file()
    output_file = 'alive_links.txt'  # Change this to your desired output file
    filter_links(input_file, output_file)
