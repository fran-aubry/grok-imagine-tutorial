from xai_sdk import Client
from dotenv import load_dotenv
import utils

# Load the API key
load_dotenv() 

# Initialize the xAI client
client = Client()

# Sending a video generation request
prompt = """
Add fire to the balls.
"""

response = client.video.generate(
    prompt=prompt,
    model="grok-imagine-video",
    video_url="https://vidgen.x.ai/xai-vidgen-bucket/xai-video-2109c762-efcb-415b-ab3c-661b1df113cd.mp4",
)

# Download the video
utils.download_video(response.url)
