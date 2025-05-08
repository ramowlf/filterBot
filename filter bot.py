import json
import shlex
from telethon import TelegramClient, events
from telethon import TelegramClient, events, Button
from random import choice

yarrak = api id gir
amcikk = "api hash gir"
ohh = "token gir"
amcik = "ramazann"

ramos = f"{amcik}.json"

def azginlar(dosya):
    try:
        with open(dosya, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {"filters": {}}

def gavatlar(data, dosya):
    with open(dosya, "w") as file:
        json.dump(data, file, indent=4)

ramowlf = TelegramClient(amcik, yarrak, amcikk).start(bot_token=ohh)

@ramowlf.on(events.NewMessage(pattern="/start"))
async def sikkirigi(ramazan):
    sigma = Button.url("🇹🇷 Kanalımız", "https://t.me/TurkUserBotKanali")
    Telegram_ramowlf = Button.url("💬 Beni Gruba Ekle", "https://t.me/filterbotcukbot?startgroup=true")
    Instagram_ramowlf = Button.url("👨‍💻 Bot Sahibi", "https://t.me/ramowlf")
    ramowlf = Button.url("🩵 Geliştirici", "https://t.me/ramowlf")

    await ramazan.respond(
        "❤️‍🔥 Merhaba canım ben filter botuyum komutlarm aşağıda\n\n/filter - yeni bir filter ekler\n/stop - eklediğiniz filteri siler\n/hepsinisil - bütün filtreleri siler\n/filters - eklediğiniz filtreleri gösterir",
        buttons=[
            [Instagram_ramowlf, ramowlf], 
            [Telegram_ramowlf, sigma],
        ]
    )
    
@ramowlf.on(events.NewMessage(pattern=r"^/filter (.+)"))
async def amgot(event):
    try:
        ramowlf = event.message.text.split(" ", 1)[1]
        mihriban = shlex.split(ramowlf)

        if len(mihriban) < 2:
            await event.reply("🥰 örnek kullanım: /filter sa as ")
            return

        keltos = mihriban[0].strip().lower()
        ramazan = mihriban[1]

        dindin = azginlar(ramos)
        ınstagram_ramowlf = str(event.chat_id)

        if ınstagram_ramowlf not in dindin["filters"]:
            dindin["filters"][ınstagram_ramowlf] = {}

        if keltos in dindin["filters"][ınstagram_ramowlf]:
            dindin["filters"][ınstagram_ramowlf][keltos].append(ramazan)
        else:
            dindin["filters"][ınstagram_ramowlf][keltos] = [ramazan]

        gavatlar(dindin, ramos)
        await event.reply(f"🩵 `{keltos}` filteri eklendi kiral")
    except Exception:
        pass

@ramowlf.on(events.NewMessage(incoming=True))
async def sikisenler(event):
    try:
        if not event.message.message:
            return

        data = azginlar(ramos)
        chat_id = str(event.chat_id)
        mesaj = event.message.message.strip().lower()

        if chat_id in data["filters"]:
            for kelime, cevaplar in data["filters"][chat_id].items():
                if mesaj == kelime:
                    await event.reply(choice(cevaplar))
                    break
    except Exception:
        pass

@ramowlf.on(events.NewMessage(pattern=r"^/filters$"))
async def amcik_yenir(event):
    data = azginlar(ramos)
    chat_id = str(event.chat_id)

    if chat_id in data["filters"] and data["filters"][chat_id]:
        cevap = "**📂 Aktif Filtreler:**\n"
        for kelime in data["filters"][chat_id]:
            cevap += f"• `{kelime}`\n"
        await event.reply(cevap)
    else:
        await event.reply("Şuanda filter yok aynı PKK'lıların ülke kurma hayali gibi yok")

@ramowlf.on(events.NewMessage(pattern=r"^/hepsinisil$"))
async def gotunu_yerim(event):
    data = azginlar(ramos)
    chat_id = str(event.chat_id)

    if chat_id in data["filters"]:
        del data["filters"][chat_id]
        gavatlar(data, ramos)
        await event.reply("🙂 Hepsi temizlendi")
    else:
        await event.reply("💥 Silecek bir filter yok")

@ramowlf.on(events.NewMessage(pattern=r"^/stop (.+)"))
async def stop_filter(event):
    try:
        kelime = event.message.text.split(" ", 1)[1].strip().lower()
        data = azginlar(ramos)
        chat_id = str(event.chat_id)

        if chat_id in data["filters"] and kelime in data["filters"][chat_id]:
            del data["filters"][chat_id][kelime]
            gavatlar(data, ramos)
            await event.reply(f"🫣 `{kelime}` filter silindi.")
        else:
            await event.reply(f"😼 `{kelime}` Diye bir filter yok")
    except Exception:
        pass

ramowlf.run_until_disconnected()
