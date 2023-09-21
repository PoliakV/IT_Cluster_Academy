import time
import re
import os
import sys
import logging

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from telegram import Update
from telegram import __version__ as TG_VER
from telegram.ext import (Application, CommandHandler,
                          ContextTypes, ConversationHandler, MessageHandler, filters)


API_TOKEN = "..." # ... - instead of dots please write Telegram Bot API

GREETING, KOD, CHECK_STATUS = range(3)

kods = []


async def greeting(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    await update.message.reply_text("Привіт! Вітаю, я Телеґрам-бот 👨‍💼 ЦНАПу м. Івано-Франківськ. Я допоможу перевірити статус виконання послуги")
    time.sleep(1)
    await update.message.reply_text("Надішліть перший код перевірки (8 цифр) без додаткових знаків або почніть спочатку, натиснувши /start")
    return KOD


async def kod(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    kods.append(update.message.text)
    await update.message.reply_text("Надішліть другий код перевірки (8 цифр) без додаткових знаків або почніть спочатку, натиснувши /start")
    return CHECK_STATUS


async def check_status(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    # for tests kod1, kod2 = "7619868", "5589679"
    def check_rezult(driver, kod1, kod2):
        input_kod_1 = driver.find_element(by="id", value="kod1")
        input_kod_1.send_keys(kod1)
        input_kod_2 = driver.find_element(by="id", value="kod11")
        input_kod_2.send_keys(kod2)
        time.sleep(2)
        send_btn = driver.find_element(by="id", value="skod")
        send_btn.click()
        time.sleep(2)
        rez = driver.find_element(by="id", value="kodcont")
        return rez

    await update.message.reply_text("Виконання запиту, будь ласка зачекайте\n🧑‍💻👩‍💻")
    kods.append(update.message.text)
    kod1, kod2 = kods[0], kods[1]
    chrome_options = Options()
    chrome_options.add_argument("--headless=new")
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://www.cnap.if.ua/stanp")
    time.sleep(2)

    rez = check_rezult(driver, kod1, kod2)
    print("спроба 1")
    if "Для отримання інформації щодо стану послуги Надішліть код" in rez.text:
        rez = check_rezult(driver, kod1, kod2)
        print("спроба 2")

    elif "Ви неправильно ввели код зворотнього зв'язку" in rez.text:
        driver.execute_script("scroll(0, 0);")
        driver.find_element(
            by="xpath", value="//*[contains(text(), 'Назад')]").click()
        time.sleep(2)
        rez = check_rezult(driver, kod1, kod2)
        print("спроба 3")
        if "Ви неправильно ввели код зворотнього зв'язку" or "Для отримання інформації щодо стану послуги" in rez.text:
            await update.message.reply_text("Введені коди перевірки не правильні, спробуйте ще раз, натиснувши /start")
            print("спроба 4")
        else:
            rezultat = re.sub(r"\nНАЗАД", "", rez.text, 0, re.MULTILINE)
            await update.message.reply_text(rezultat)

    else:
        rezultat = re.sub(r"\nНАЗАД", "", rez.text, 0, re.MULTILINE)
        print("спроба 1 спрацювала")
        await update.message.reply_text(rezultat)
    driver.quit()
    kods.clear()
    await update.message.reply_text("Щоб перевірити результат іншої послуги, натисніть /start")
    return GREETING


def main() -> None:
    # Run the bot.
    # Creating the Application and passing it the bot's token.
    application = Application.builder().token(API_TOKEN).build()
    # Adding a conversation handler with the states
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("start", greeting)],
        states={
            GREETING: [MessageHandler(filters.TEXT & ~filters.COMMAND, greeting)],
            KOD: [MessageHandler(filters.TEXT & ~filters.COMMAND, kod)],
            CHECK_STATUS: [MessageHandler(filters.TEXT & ~filters.COMMAND, check_status)],
        },
        fallbacks=[CommandHandler("start", greeting)],
    )

    application.add_handler(conv_handler)

    application.run_polling(allowed_updates=Update.ALL_TYPES)


# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)
# set higher logging level for httpx to avoid all GET and POST requests being logged
logging.getLogger("httpx").setLevel(logging.WARNING)
logger = logging.getLogger(__name__)

try:
    from telegram import __version_info__
except ImportError:
    __version_info__ = (0, 0, 0, 0, 0)  # type: ignore[assignment]

if __version_info__ < (20, 0, 0, "alpha", 1):
    raise RuntimeError(
        f"This example is not compatible with your current PTB version {TG_VER}. To view the "
        f"{TG_VER} version of this example, "
        f"visit https://docs.python-telegram-bot.org/en/v{TG_VER}/examples.html"
    )

if __name__ == "__main__":
    main()
