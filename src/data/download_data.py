import os
import requests

# Define the URLs of the legal documents (replace with actual URLs)
DOCUMENT_URLS = {
    "guide_to_litigation_india.pdf": "https://www.cyrilshroff.com/wp-content/uploads/2020/09/Guide-to-Litigation-in-India.pdf",
    "legal_compliance_corporate_laws.pdf": "https://kb.icai.org/pdfs/PDFFile5b28c9ce64e524.54675199.pdf",
}

# Define the directory to save the documents
DATA_DIR = "data"

def download_file(url, filename):
    """Downloads a file from the given URL and saves it with the given filename."""
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()  # Raise an exception for bad status codes
        with open(filename, "wb") as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        print(f"Downloaded: {filename}")
    except requests.exceptions.RequestException as e:
        print(f"Error downloading {url}: {e}")

def main():
    """Downloads the legal documents."""
    # Create the data directory if it doesn't exist
    os.makedirs(DATA_DIR, exist_ok=True)

    for filename, url in DOCUMENT_URLS.items():
        filepath = os.path.join(DATA_DIR, filename)
        if not os.path.exists(filepath):  # Only download if the file doesn't exist
            download_file(url, filepath)
        else:
            print(f"File already exists: {filepath}")

if __name__ == "__main__":
    main()
