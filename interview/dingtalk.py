#coding=utf-8
from dingtalkchatbot.chatbot import DingtalkChatbot

from django.conf import settings

def send(message, at_mobiles=[]):
    # Reference the DingTalk group message notification WebHook address configured in settings:
    webhook = settings.DINGTALK_WEB_HOOK

    # Initialize robot xiaoding, # Method 1: Standard initialization method
    xiaoding = DingtalkChatbot(webhook)

    # Method 2: Used when "signature" option is checked (v1.5 and above new feature)
    # xiaoding = DingtalkChatbot(webhook, secret=secret)

    # Text message @all
    xiaoding.send_text(msg=('Interview Notification: %s' % message), at_mobiles = at_mobiles )


