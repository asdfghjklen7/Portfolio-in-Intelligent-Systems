import os
import piexif
import requests

# Direct image target
image_url = "https://www.maxfosterphotography.com/images/xl/Heirloom.jpg"
image_filename = "sample.jpg"

def download_sample_image():
    print(f"Downloading sample image from {image_url}...")
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    response = requests.get(image_url, headers=headers)
    response.raise_for_status()
    with open(image_filename, "wb") as f:
        f.write(response.content)

def analyze_exif():
    if not os.path.exists(image_filename):
        download_sample_image()

    print("\nEXIF Metadata Analysis:")
    try:
        exif_dict = piexif.load(image_filename)
        
        # Safely decode EXIF tags (returns "N/A" if tag is stripped by web compression)
        make_raw = exif_dict.get("0th", {}).get(piexif.ImageIFD.Make, b"N/A")
        model_raw = exif_dict.get("0th", {}).get(piexif.ImageIFD.Model, b"N/A")
        date_raw = exif_dict.get("Exif", {}).get(piexif.ExifIFD.DateTimeOriginal, b"N/A")

        make = make_raw.decode("utf-8").strip("\x00") if isinstance(make_raw, bytes) else make_raw
        model = model_raw.decode("utf-8").strip("\x00") if isinstance(model_raw, bytes) else model_raw
        date_time = date_raw.decode("utf-8").strip("\x00") if isinstance(date_raw, bytes) else date_raw

        print(f"Camera Make: {make}")
        print(f"Camera Model: {model}")
        print(f"Date/Time Original: {date_time}")

    except Exception as e:
        print(f"Error reading EXIF data: {e}")

if __name__ == "__main__":
    download_sample_image()
    analyze_exif()