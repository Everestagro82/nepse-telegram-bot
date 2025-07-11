import telebot
import datetime

API_TOKEN = '7411519242:AAHuNngltinKsD8ENzkLn0rtGen6Uj_ndjk'
bot = telebot.TeleBot(API_TOKEN)

chat_id = None  # Replace with your chat ID manually if needed

@bot.message_handler(commands=['start'])
def send_welcome(message):
    global chat_id
    chat_id = message.chat.id
    bot.reply_to(message, "नमस्ते! Dnepse Alerts Bot सुरु भयो। तपाईंलाई दैनिक रिपोर्ट, स्विङ अलर्ट र IPO जानकारी प्राप्त हुनेछ।")

def send_daily_report():
    now = datetime.datetime.now()
    report_message = f"📊 {now.strftime('%Y-%m-%d')} NEPSE Daily Report:

" +                      "- 🟢 Swing Alerts: SICL, HDL
" +                      "- 🟡 IPO Status: Him Star (Applied), Bikash Hydro (Applied)
" +                      "- 📈 NEPSE Summary: Market closed today.

" +                      "#NEPSE #SwingTrading #IPO #Finance #Nepal"
    if chat_id:
        bot.send_message(chat_id, report_message)

if __name__ == '__main__':
    print("Bot is running...")
    bot.infinity_polling()