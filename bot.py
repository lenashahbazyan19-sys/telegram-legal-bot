from telebot import TeleBot

TOKEN = "8998813106:AAHE-QCs_vxKB1ODQ5uAJX6sHPqaXrYgsvw"
bot = TeleBot(token=TOKEN)


@bot.message_handler(commands=["start"])
def start_bot(message):
    try:
        bot.send_photo(message.chat.id, open("lawyer_office.jpg", "rb"))
    except FileNotFoundError:
        pass

    welcome_text = (
        "Բարի գալուստ իրավաբանական օգնության բոտ։\n\n"
        "Գրեք հետևյալ բառերը տեղեկություն ստանալու համար՝\n"
        "🔹 ծառայություններ\n"
        "🔹 գին\n"
        "🔹 կապ"
    )
    bot.send_message(message.chat.id, welcome_text)


@bot.message_handler()
def handle_messages(message):
    user_text = message.text.lower()

    if user_text == "ծառայություններ":
        services_text = (
            "⚖️ Իմ ծառայությունները՝\n"
            "1. Քաղաքացիական և ընտանեկան վեճեր\n"
            "2. Պայմանագրերի կազմում\n"
            "3. Դատական ներկայացուցչություն"
        )
        bot.send_message(message.chat.id, services_text)
    elif user_text == "գին":
        bot.send_message(
            message.chat.id, "💰 Առաջին խորհրդատվությունը ԱՆՎՃԱՐ է։"
        )
    elif user_text == "կապ":
        bot.send_message(message.chat.id, "📞 Կապի հեռախոսահամար՝ +374 XX XX XX")
    else:
        bot.send_message(
            message.chat.id,
            "Խնդրում եմ գրել այս բառերից մեկը՝ ծառայություններ, գին կամ կապ։",
        )


bot.polling()

