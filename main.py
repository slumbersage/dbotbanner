import requests
import base64

# Replace discord token with yours
DISCORD_BOT_TOKEN = "your token here"

# Define URLs for profile picture and banner
PROFILE_IMAGE_URL = "link here"
BANNER_IMAGE_URL = "link here"

# Download profile and banner images
profile_image_response = requests.get(PROFILE_IMAGE_URL)
banner_image_response = requests.get(BANNER_IMAGE_URL)

# Check if images were downloaded successfully
if profile_image_response.status_code == 200 and banner_image_response.status_code == 200:
    # Encode images to base64
    profile_image_base64 = base64.b64encode(profile_image_response.content).decode('utf-8')
    banner_image_base64 = base64.b64encode(banner_image_response.content).decode('utf-8')

    # Prepare JSON payload with base64-encoded images
    payload = {
        "avatar": f"data:image/gif;base64,{profile_image_base64}",
        "banner": f"data:image/gif;base64,{banner_image_base64}"
    }

    # Prepare headers with bot token
    headers = {
        'Authorization': f'Bot {DISCORD_BOT_TOKEN}',
        'Content-Type': 'application/json'
    }

    # Send HTTP PATCH request to update profile picture and banner
    response = requests.patch('https://discord.com/api/v10/users/@me', headers=headers, json=payload)

    # Check if the response indicates success
    if response.status_code == 200:
        print('Profile picture and banner changed successfully!')
    else:
        print('Failed to change profile picture and banner:', response.text)
else:
    print('Failed to download profile picture or banner')
