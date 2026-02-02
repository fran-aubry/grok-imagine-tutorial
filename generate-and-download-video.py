from xai_sdk import Client
from dotenv import load_dotenv
import utils

# Load the API key
load_dotenv() 

# Initialize the xAI client
client = Client()

# Sending a video generation request
prompt = """
A pixel art cat playing with a ball.
"""

response = client.video.generate(
    prompt=prompt,
    model="grok-imagine-video",
)

# Download the video
utils.download_video(response.url)
