# File: config.py
from dotenv import load_dotenv

# Load environment variables from .env file (optional)
load_dotenv()

# It's highly recommended to use environment variables for sensitive data like the bot token.
# Example: BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
# For this example, we'll keep it as a variable, but replace it with your actual token
# or load from environment variables in a real application.
BOT_TOKEN = "8033674488:AAGtJGJ29s88dCVGmWaebOxT6_32m9vPCzg" # Replace with your token or use os.getenv

if not BOT_TOKEN:
    raise ValueError("No BOT_TOKEN found. Set the TELEGRAM_BOT_TOKEN environment variable.")

