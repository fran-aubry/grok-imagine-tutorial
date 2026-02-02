import requests
from pathlib import Path
from urllib.parse import urlparse

def download_video(url: str, output_dir: str = "."):
    """
    Download a video and save it using the filename from the URL.

    :param url: Video URL
    :param output_dir: Directory to save the file (default: current dir)
    """
    # Extract filename from URL
    filename = Path(urlparse(url).path).name
    if not filename:
        raise ValueError("Could not determine filename from URL")

    output_path = Path(output_dir) / filename

    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(output_path, "wb") as f:
            for chunk in r.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)

    print(f"✅ Video saved to {output_path.resolve()}")
