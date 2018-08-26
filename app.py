from flask import Flask, request, abort

from linebot import (
	LineBotApi, WebhookHandler
)
from linebot.exceptions import (
	InvalidSignatureError
)
from linebot.models import *
import requests
import datetime
import sys
from flaskext.mysql import MySQL

mysql = MySQL()
app = Flask(__name__)
app.config['MYSQL_DATABASE_HOST'] = '140.115.157.76'
app.config['MYSQL_DATABASE_USER'] = 'ericdai'
app.config['MYSQL_DATABASE_PASSWORD'] = 'beetles51105'
app.config['MYSQL_DATABASE_DB'] = 'ericdai_linebot'
mysql.init_app(app)
line_bot_api = LineBotApi('PnFjlMMJ6ZDNJwcZEHXU3pQkJ1bSG6BpdquxePzS72pJDlKY8lupjtE7mJ5xjXVYOEpWSs6HSA6fVYxd7HufAOPDQoN0xUD/JjZ4+m3gW97gvSo9aEV6lkHvJbeglnqAoYxR1BQnudUbD9QciErOvgdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('135b550e5b916e4b0c36c75bdaf16aec')

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

@handler.add(MessageEvent, message=ImageMessage)
def handle_message(event):
    profile = line_bot_api.get_profile(event.source.user_id)
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text='圖片'))

if __name__ == "__main__":
    app.run(debug=True)
