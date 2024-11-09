from client import setup_client
import requests
from io import BytesIO
from PIL import Image


def generate_image(prompt):
    client = setup_client("config.yml")

    try:
        response = client.images.generate(
            prompt = prompt,
            n = 1,
            size = "1024x1024",
        )
        image_url = response.data[0].url
        return image_url
    except Exception as e:
        print(f"Error generating image: {str(e)}")


def download_image(url):
    response = requests.get(url)
    response.raise_for_status()
    return Image.open(BytesIO(response.content))
