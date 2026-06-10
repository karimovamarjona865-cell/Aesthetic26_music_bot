import telebot
import requests
import urllib.parse

API_TOKEN = '8840219376:AAEaykb23LW9P0yHpXn3ngDZ1g0nQx4fuFg'
bot = telebot.TeleBot(API_TOKEN)

# 30 talik limitli nazorat
LIMIT = 30

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Salom! Men tayyorman. Menga 30 tagacha qo'shiq ro'yxatini tashlang, men esa ularning eng toza to'liq variantlarini sizga yuboraman! 🎧")

@bot.message_handler(func=lambda message: True)
def handle_playlist(message):
    lines = [line.strip() for line in message.text.split('\n') if line.strip()]
    
    if len(lines) > LIMIT:
        bot.reply_to(message, f"⚠️ *Limit oshib ketdi!* Siz birdiga {len(lines)} ta qo'shiq yubordingiz. Iltimos, {LIMIT} tadan oshirmang.")
        return

    bot.reply_to(message, f"✅ Ro'yxat qabul qilindi ({len(lines)} ta). Qo'shiqlar to'liq variantda yuklanmoqda... ⏳")
    
    for song in lines:
        try:
            search_query = urllib.parse.quote(song)
            search_url = f"https://t.me/vkm_bot?start={search_query.replace(' ', '_')}"
            
            bot.send_message(
                message.chat.id, 
                f"🎵 *{song}*\n\n👉 [To'liq variantni yuklab olish]({search_url})", 
                parse_mode="Markdown"
            )
        except Exception as e:
            continue

print("To'liq variantli bot ishga tushdi...")
bot.polling()
