import json
import asyncio
from pyppeteer import launch
from datetime import datetime, timedelta
import aiofiles
import random
import requests
import os

# Lấy Telegram Bot Token và Chat ID từ biến môi trường
TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
TELEGRAM_CHAT_ID = os.getenv('TELEGRAM_CHAT_ID')

def format_to_iso(date):
    return date.strftime('%Y-%m-%d %H:%M:%S')

async def delay_time(ms):
    await asyncio.sleep(ms / 1000)

# Trình duyệt toàn cục
browser = None

# Thông báo Telegram
message = 'serv00&ct8 script tự động đang chạy\n'

async def login(username, password, panel):
    global browser

    page = None  # Đảm bảo page được định nghĩa trong mọi tình huống
    serviceName = 'ct8' nếu 'ct8' trong panel khác thì 'serv00'
    try:
        if not browser:
            browser = await launch(headless=True, args=['--no-sandbox', '--disable-setuid-sandbox'])

        page = await browser.newPage()
        url = f'https://{panel}/login/?next=/'
        await page.goto(url)

        username_input = await page.querySelector('#id_username')
        if username_input:
            await page.evaluate('''(input) => input.value = ""''', username_input)

        await page.type('#id_username', username)
        await page.type('#id_password', password)

        login_button = await page.querySelector('#submit')
        if login_button:
            await login_button.click()
        else:
            raise Exception('Không thể tìm thấy nút đăng nhập')

        await page.waitForNavigation()

        is_logged_in = await page.evaluate('''() => {
            const logoutButton = document.querySelector('a[href="/logout/"]');
            return logoutButton !== null;
        }''')

        return is_logged_in

    except Exception as e:
        print(f'Lỗi khi đăng nhập tài khoản {serviceName} {username}: {e}')
        return False

    finally:
        if page:
            await page.close()

async def main():
    global message
    message = 'serv00&ct8 script tự động đang chạy\n'

    try:
        async with aiofiles.open('accounts.json', mode='r', encoding='utf-8') as f:
            accounts_json = await f.read()
        accounts = json.loads(accounts_json)
    except Exception as e:
        print(f'Lỗi khi đọc file accounts.json: {e}')
        return

    for account in accounts:
        username = account['username']
        password = account['password']
        panel = account['panel']

        serviceName = 'ct8' nếu 'ct8' trong panel khác thì 'serv00'
        is_logged_in = await login(username, password, panel)

        if is_logged_in:
            now_utc = format_to_iso(datetime.utcnow())
            now_beijing = format_to_iso(datetime.utcnow() + timedelta(hours=8))
            success_message = f'Tài khoản {serviceName} {username} đã đăng nhập thành công vào giờ Bắc Kinh {now_beijing} (giờ UTC {now_utc})!'
            message += success_message + '\n'
            print(success_message)
        else:
            message += f'Tài khoản {serviceName} {username} đăng nhập thất bại, vui lòng kiểm tra lại tài khoản và mật khẩu {serviceName}.\n'
            print(f'Tài khoản {serviceName} {username} đăng nhập thất bại, vui lòng kiểm tra lại tài khoản và mật khẩu {serviceName}.')

        delay = random.randint(1000, 8000)
        await delay_time(delay)
        
    message += f'Tất cả các tài khoản {serviceName} đã hoàn thành đăng nhập!'
    await send_telegram_message(message)
    print(f'Tất cả các tài khoản {serviceName} đã hoàn thành đăng nhập!')

async def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        'chat_id': TELEGRAM_CHAT_ID,
        'text': message,
        'reply_markup': {
            'inline_keyboard': [
                [
                    {
                        'text': 'Phản hồi vấn đề❓',
                        'url': 'https://t.me/yxjsjl'
                    }
                ]
            ]
        }
    }
    headers = {
        'Content-Type': 'application/json'
    }
    try:
        response = requests.post(url, json=payload, headers=headers)
        if response.status_code != 200:
            print(f"Gửi tin nhắn đến Telegram thất bại: {response.text}")
    except Exception as e:
        print(f"Lỗi khi gửi tin nhắn đến Telegram: {e}")

if __name__ == '__main__':
    asyncio.run(main())
