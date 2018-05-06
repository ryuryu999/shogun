from flask import Flask, request, abort

from linebot import (
 LineBotApi, WebhookHandler
)
from linebot.exceptions import (
 InvalidSignatureError
)
from linebot.models import (
 MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

# 自分のLINE botのデータを設定する。
line_bot_api = LineBotApi('H2BhCCb4wm8dyyosTi3bp6fDfBasBR6RFKA6O3X8Qs79wL/xyft/9MsBSQF0koROOnJk0iB0HPLJ+KPV/u/srhMhHzR9czxmmC/cnwAKLqEzIbakxZw1rEfvXDn3PhteF/hzMhm13U17rJBVTKiTZQdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('4a3b7434e9f34fae934518c3d4f7aa9e')

@app.route("/callback", methods=['POST'])
def callback():
 # get X-Line-Signature header value
 signature = request.headers['X-Line-Signature']

# get request body as text
 body = request.get_data(as_text=True)
 app.logger.info("Request body: " + body)

# handle webhook body
 try:
  handler.handle(body, signature)
 except InvalidSignatureError:
  abort(400)

 return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
 line_bot_api.reply_message(
  event.reply_token,
  TextSendMessage(text=event.message.text))

if __name__ == "__main__":
 app.run()