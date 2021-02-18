# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 19:01:53 2021

@author: TalhaSoftware
"""

import requests
from bs4 import BeautifulSoup
import time
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

options = Options()
options.headless = True
browser = webdriver.Firefox(options=options)


def telegram_bot_sendtext(bot_message):
    
    bot_token = ''
    bot_chatID = ''
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)

    return response.json()


def altin(update: Update, context: CallbackContext) -> None:
    
    browser.get("https://www.doviz.com")

    source = browser.page_source
    
    soup = BeautifulSoup(source,"lxml")
    
    dolar = soup.find_all("span",{"class":"value"})
    
    for i in range(0,len(dolar)):
        print(dolar[i].text)
    telegram_bot_sendtext(dolar[0].text)

def dolar(update: Update, context: CallbackContext) -> None:
    browser.get("https://www.doviz.com")

    source = browser.page_source
    
    soup = BeautifulSoup(source,"lxml")
    
    dolar = soup.find_all("span",{"class":"value"})
    
    for i in range(0,len(dolar)):
        print(dolar[i].text)
    telegram_bot_sendtext(dolar[1].text)

def euro(update: Update, context: CallbackContext) -> None:
    browser.get("https://www.doviz.com")

    source = browser.page_source
    
    soup = BeautifulSoup(source,"lxml")
    
    dolar = soup.find_all("span",{"class":"value"})
    
    for i in range(0,len(dolar)):
        print(dolar[i].text)
    telegram_bot_sendtext(dolar[2].text)

def sterlin(update: Update, context: CallbackContext) -> None:
    browser.get("https://www.doviz.com")

    source = browser.page_source
    
    soup = BeautifulSoup(source,"lxml")
    
    dolar = soup.find_all("span",{"class":"value"})
    
    for i in range(0,len(dolar)):
        print(dolar[i].text)
    telegram_bot_sendtext(dolar[3].text)
    
def echo(update: Update, context: CallbackContext) -> None:
    """Echo the user message."""
    #update.message.reply_text(update.message.text)
    pass
    
def main():
    """Start the bot."""
    
    updater = Updater("", use_context=True)

    dispatcher = updater.dispatcher

    
    
    dispatcher.add_handler(CommandHandler("dolar", dolar))
    dispatcher.add_handler(CommandHandler("altın", altin))
    dispatcher.add_handler(CommandHandler("euro", euro))
    dispatcher.add_handler(CommandHandler("sterlin", sterlin))

    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    # Start the Bot
    updater.start_polling()

    updater.idle()

main()
