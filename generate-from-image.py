from xai_sdk import Client
from dotenv import load_dotenv
import utils

# Load the API key
load_dotenv() 

# Initialize the xAI client
client = Client()

# Sending a video generation request
prompt = """
A FPV drone shot of the people riding the horses on the beach.
"""

response = client.video.generate(
    prompt=prompt,
    model="grok-imagine-video",
    image_url="https://raw.githubusercontent.com/fran-aubry/grok-imagine-tutorial/main/horses.jpeg",
)

# Download the video
print(response.url)
utils.download_video(response.url)
