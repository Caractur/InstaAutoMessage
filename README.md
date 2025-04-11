## Instagram Auto Messenger using Selenium

This Python script allows you to automatically send a message to a specific Instagram user using the Selenium library.

## 📦 Features

- Logs into Instagram using your credentials
- Navigates to the recipient's profile
- Sends a direct message
- Automatically handles "Save Login Info" and "Turn on Notifications" prompts

## ⚙️ Requirements

- Python 3.6+
- Google Chrome
- ChromeDriver (automatically managed via `webdriver-manager`)

## 🧠 Libraries Used

- `selenium`
- `webdriver_manager`
- `time`

## 🔧 Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/instagram-auto-message.git
   cd instagram-auto-message

2. Install dependencies:
   pip install selenium webdriver-manager

## 🚀 Usage

Edit the last line of the script and provide your credentials and message details:

SendMessage("your_instagram_username", "your_instagram_password", "recipient_username", "Your message here")

Then run the script:

python script.py

⚠️ Disclaimer: Use at your own risk. Instagram may block or restrict your account for using automation. This tool is for educational purposes only.

## 📌 Notes

Make sure you are using the latest version of Chrome.
The script may break if Instagram updates its UI. In that case, XPath selectors may need to be updated.

## 📝 License

This project is licensed under the MIT License.







