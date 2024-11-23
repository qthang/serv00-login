## Automating Batch Account Retention for `serv00` and `ct8`: Auto Login to Panels Every 3 Days and Send Messages to Telegram

### Video Tutorial Here
[Free 10-Year VPS Serv00 + One-Click Deployment of Your Own Vless Node | Beginner's Guide | Automated Batch Account Retention](https://youtu.be/QnlzpvDl_mo)

Implemented using GitHub Actions and Python scripts.

🙏🙏🙏 Please give a **Star!! Star!! Star!!**

Join the discussion group: [https://t.me/yxjsjl](https://t.me/yxjsjl)

---

### Steps to Fork the Code to Your Repository and Run It

#### 1. Fork the Repository

1. **Access the Original Repository**:
   - Navigate to the GitHub page of the repository you want to fork.

2. **Fork the Repository**:
   - Click the "Fork" button in the top-right corner to copy the repository to your GitHub account.

---

#### 2. Set Up GitHub Secrets

1. **Create a Telegram Bot**:
   - Search for `@BotFather` in Telegram, create a new bot, and get the API token.
   - **Option 1**: Get your Chat ID by sending `/id@KinhRoBot` in the [YXJS Group](https://t.me/yxjsjl). The returned `ID` is your Chat ID.
   - **Option 2**: Send a message to your bot and visit `https://api.telegram.org/bot<your_bot_token>/getUpdates` to find the Chat ID.

2. **Configure GitHub Secrets**:
   - Open the repository you forked on GitHub.
   - Go to `Settings` → `Secrets` in the left menu.
   - Add the following secrets:
     - **`ACCOUNTS_JSON`**: JSON data containing account information, e.g.:
       ```json
       [
         {"username": "serv00_account", "password": "serv00_password", "panel": "panel6.serv00.com"},
         {"username": "ct8_account", "password": "ct8_password", "panel": "panel.ct8.pl"},
         {"username": "user2", "password": "password2", "panel": "panel6.serv00.com"}
       ]
       ```
     - **`TELEGRAM_BOT_TOKEN`**: Your Telegram Bot API token.
     - **`TELEGRAM_CHAT_ID`**: Your Telegram Chat ID.

---

#### 3. Start GitHub Actions

1. **Enable GitHub Actions**:
   - In the forked repository, go to the `Actions` tab.
   - If Actions are not enabled, click `Enable GitHub Actions`.

2. **Run the Workflow**:
   - The script will automatically run based on the scheduled tasks (e.g., every three days).
   - You can also manually trigger it from the `Actions` page.

---

### Summary of Secrets and How to Obtain Them

- **`TELEGRAM_BOT_TOKEN`**:
  - Example: `1234567890:ABCDEFghijklmnopQRSTuvwxyZ`
  - Obtain from `@BotFather` in Telegram after creating a bot.

- **`TELEGRAM_CHAT_ID`**:
  - Example: `1234567890`
  - Obtain by sending a message to your bot and visiting `https://api.telegram.org/bot<your_bot_token>/getUpdates`.

- **`ACCOUNTS_JSON`**:
  - Example:
    ```json
    [
      {"username": "serv00_account", "password": "serv00_password", "panel": "panel6.serv00.com"},
      {"username": "ct8_account", "password": "ct8_password", "panel": "panel.ct8.pl"}
    ]
    ```
  - Create a JSON file with account information and add it to your GitHub Secrets.

---

### Important Notes

- **Confidentiality**: Keep Secrets secure; do not expose them in public repositories or share them with unauthorized individuals.
- **Updates and Deletion**: Manage Secrets through the repository's `Secrets` page for modifications or removal.

Following these steps, you can successfully fork and run the code in your repository. If you need further assistance or have any questions, feel free to ask!

---

## 🌟🌟🌟 Star the Repo!!!
[![Stargazers over time](https://starchart.cc/yixiu001/serv00-login.svg?variant=adaptive)](https://starchart.cc/yixiu001/serv00-login)

[![Stargazers over time](https://starchart.cc/yixiu001/serv00-login.svg?variant=adaptive)](https://starchart.cc/yixiu001/serv00-login)
