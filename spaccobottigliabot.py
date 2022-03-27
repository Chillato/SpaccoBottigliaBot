from pyrogram import *
from pyrogram.types import *
import os, json, random

if not os.path.exists("botmain_session"):
    os.mkdir("botmain_session")

api_id = 1 # api hash
api_hash = "api_id"
spaccobottiglietoken = "tokendelbot"

spaccobottiglie = Client("botmain_session/botmain", api_id, api_hash, bot_token=spaccobottiglietoken)

if os.path.exists("users.json"):
    with open("users.json", "r+") as f:
        Users = json.load(f)
else:
    Users = []
    with open("users.json", "w+") as f:
        json.dump(Users, f)


def save():
    global Users
    with open("users.json", "w+") as f:
        json.dump(Users, f)

statsperms = [] # tuo id per il comando /stats

helpmsg = """
<b>⁉️Comandi e funzionalità⁉️</b>

● /help - Apre questo menù
● /vergine - Dice se sei vergine
● /insulta - Insulta un utente (via reply)
● /covid - Controlla se sei infettato da covid19
● /eroe - Ti dice che eroe sei
● /bello - Ti dice quanto sei bello (maschi)
● /bella - Ti dice quanto sei bella (femmine)
● /bowling - Gioca a bowling
● /gay - Ti dice se sei gay (maschi)
● /lesbica - Ti dice se sei lesbica (femmine)
● /neuroni - Ti dice quanti neuoroni ti sono rimasti
● /bestemmie - Ti dice quante volte bestemmi ogni giorno
● /lungo - Ti dice quanti cm lo hai lungo (maschi)
● /larga - Ti dice quanti cm la hai larga (femmine)
● /morte - Ti dice tra quanto tempo morirai
● /dado - Lancia un dado
● /moneta - Lancia una moneta
● /qi - Ti dice il tuo quozziente intellettivo
● /soldi - Ti dice se sei ricco o povero
● /tiktok - Ti dice se sei famoso
● /drogato - Ti dice se sei drogato
● /animale - Ti dice che animale sei
● /lavoro - Ti dice che lavoro farai da grande
● /sesso - Fai sesso (Reply)
● /nomignolo - Ti dice il tuo nomignolo
● /youtube - Ti dice se sei un bravo youtuber

● Messaggi di entrata random impostati dallo staff

» Sempre in aggiornamento        
"""
@spaccobottiglie.on_message(filters.private & filters.command("start"))
async def start(client, message):
    try:
        canale = "" # metti la @ del canale senza @
        await client.get_chat_member(canale, message.chat.id)
        msgstart = f"👋Ciao, {message.from_user.mention}, benvenuto in <b>🍾SpaccoBottiglia</b>\n\n<i>😂Aggiungimi ad un gruppo come admin per farvi divertire!</i>"
        btnstart = InlineKeyboardMarkup([
            [InlineKeyboardButton("➕AGGIUNGIMI AD UN GRUPPO➕", url="http://telegram.me/UsernameDelBot?startgroup=start")],
            [InlineKeyboardButton("📝COMANDI📝", "cmd")],
            [InlineKeyboardButton("🆘SUPPORTO🆘", url="t.me/ChillatoDev"), InlineKeyboardButton("🌐CANALE🌐", url="t.me/canale")], # canale che preferisci
            [InlineKeyboardButton("❤️DONAZIONI❤️", "donazioni")]
        ])
        await client.send_message(message.chat.id, msgstart, reply_markup=btnstart)
    except:
        msgverify = "❌ Non puoi usare SpaccoBottiglia perchè non sei iscritto!"
        btnverify = InlineKeyboardMarkup([
            [InlineKeyboardButton("📂 Canale 📂 ", url="https://t.me/ChillatoDevProject")],
            [InlineKeyboardButton("✅ Fatto ✅", "fatto")]
        ])
        await client.send_message(message.chat.id, msgverify, reply_markup=btnverify)

@spaccobottiglie.on_message(filters.command("help"))
async def help(client, message):
    await client.send_message(message.chat.id, helpmsg)

@spaccobottiglie.on_message(filters.command("vergine"))
async def vergine(client, message):
    vergine = random.choice([f"‼️Occhio, {message.from_user.mention} non è vergine quindi state attenti!💦🥵👉👌", f"Buone notizie, {message.from_user.mention} è vergine, quindi state tranquilli!😉👍"])
    await client.send_message(message.chat.id, vergine)

@spaccobottiglie.on_message(filters.group & filters.command("insulta"))
async def insulta(client, message):
    if message.reply_to_message:
        insulti = random.choice([f"{message.reply_to_message.from_user.mention}, il cesso rimorchia piu di te", f"{message.reply_to_message.from_user.mention}, fai cosi schifo che sei ancora vergine", f"{message.reply_to_message.from_user.mention}, se ti uccidi la vita migliora", "sei come kill cammina a prendere la pensione"])
        await client.send_message(message.chat.id, insulti)
    else:
        await client.send_message(message.chat.id, "per utilizzare questo comando devi rispondere al messaggio del utente")

@spaccobottiglie.on_message(filters.command("covid"))
async def covid(client, message):
    covvidi = random.choice([f"{message.from_user.mention} purtroppo è appena morto⚰️ per covid, R.I.P.👼", f"{message.from_user.mention} è risultato positivo al 1° test di covid19, prendete le precauzioni e stategli lontano!🩸", f"‼️Attenzione, {message.from_user.mention} otrebbe essere affetto da covid19, quindi proteggetevi e stategli distante.😷"])
    await client.send_message(message.chat.id, covvidi)

@spaccobottiglie.on_message(filters.command("eroe"))
async def eroe(client, message):
    eroi = random.choice([f"{message.from_user.mention} si è trasformato nel supereroe <b>Wolverine.🌌</b>", f"{message.from_user.mention} si è trasformato nel supereroe <b>Mister Fantastic.🌌</b>", f"{message.from_user.mention} si è trasformato nel supereroe <b>Occhio Di Falco.🌌</b>", f"{message.from_user.mention} si è trasformato nel supereroe <b>Punisher.🌌</b>", f"{message.from_user.mention} si è trasformato nel supereroe <b>Jean Grey.🌌</b>"])
    await client.send_message(message.chat.id, eroi)

@spaccobottiglie.on_message(filters.command("bello"))
async def bello(client, message):
    bell = random.choice([f"{message.from_user.mention} è 😓bruttissimo.", f"{message.from_user.mention} è 🤪bello."])
    await client.send_message(message.chat.id, bell)

@spaccobottiglie.on_message(filters.command("bella"))
async def bella(client, message):
    cess = random.choice([f"{message.from_user.mention} è troppo figa e bella🥰.", f"{message.from_user.mention} purtroppo è una cessa a pedali🤮."])
    await client.send_message(message.chat.id, cess)

@spaccobottiglie.on_message(filters.command("bowling"))
async def bowling(client, message):
    await client.send_dice(message.chat.id, "🎳")

@spaccobottiglie.on_message(filters.command("gay"))
async def gay(client, message):
    percentuale = random.randint(0, 100)
    await client.send_message(message.chat.id, f"{message.from_user.mention} è gay al <b>{percentuale}%</b>.🥵")

@spaccobottiglie.on_message(filters.command("lesbica"))
async def lesbica(client, message):
    percentuale = random.randint(0, 100)
    await client.send_message(message.chat.id, f"{message.from_user.mention}  è lesbica al {percentuale}%.🥵")

@spaccobottiglie.on_message(filters.command("neuroni"))
async def neuroni(client, message):
    neuroni = random.randint(0, 1000)
    await client.send_message(message.chat.id, f"A {message.from_user.mention} sono rimasti <b>{neuroni}</b> neuroni.🧬")

@spaccobottiglie.on_message(filters.command("bestemmie"))
async def bestemmie(client, message):
    totbestemmie = random.randint(0, 100000)
    await client.send_message(message.chat.id, f"{message.from_user.mention} bestemmia <b>{totbestemmie}</b> volte al giorno.")

@spaccobottiglie.on_message(filters.command("lungo"))
async def lungo(client, message):
    lunghezza = random.randint(0, 90)
    await client.send_message(message.chat.id, f"🙅‍♂️{message.from_user.mention} ha il cazzo lungo <b>{lunghezza}cm</b>.🤫")

@spaccobottiglie.on_message(filters.command("larga"))
async def larga(client, message):
    larghezza = random.randint(0, 90)
    await client.send_message(message.chat.id, f"🙅‍♀️{message.from_user.mention} ha la vagina larga <b>{larghezza}</b>.🤫")

@spaccobottiglie.on_message(filters.command("morte"))
async def morte(client, message):
    anni = random.randint(0, 135)
    mesi = random.randint(0, 13)
    giorni = random.randint(1, 30)
    minuti = random.randint(0, 60)
    secondi = random.randint(0, 59)
    await client.send_message(message.chat.id, f"☠️{message.from_user.mention} morirà tra <b>{anni}</b> anni, <b>{mesi}</b> mesi, <b>{giorni}</b> giorni, <b>{minuti}</b> minuti e <b>{secondi}</b> secondi.⚰️")

@spaccobottiglie.on_message(filters.command("dado"))
async def dado(client, message):
    await client.send_dice(message.chat.id)

@spaccobottiglie.on_message(filters.command("moneta"))
async def moneta(client, message):
    moneta = random.choice(["💰è uscito <b>croce</b>", "💰è uscito <b>test</b>"])
    await client.send_message(message.chat.id, moneta)

@spaccobottiglie.on_message(filters.command("qi"))
async def qi(client, message):
    intelligenza = random.choice([f"{message.from_user.mention} ha il quoziente intellettivo di un 🐹<b>criceto</b>", f"{message.from_user.mention} ha il quoziente intelletivo di una <b>🐒scimmia</b>", f"Pazzesco, {message.from_user.mention} ha un quoziente intelletivo superiore alla media, forte!🧠"])
    await client.send_message(message.chat.id, intelligenza)

@spaccobottiglie.on_message(filters.command("soldi"))
async def soldi(client, message):
    richezza = random.choice([f"{message.from_user.mention} è <b>ricco💰</b>", f"{message.from_user.mention} è <b>povero📦</b>"])
    await client.send_message(message.chat.id, richezza)

@spaccobottiglie.on_message(filters.command("tiktok"))
async def tiktok(client, message):
    tiktokers = random.choice([f"Oh, {message.from_user.mention} la smetti di fare quei tuoi video di merda🔮", f"{message.from_user.mention} ha superato <b>100k</b> di followers, Gg per te, sei famoso🔮", f"{message.from_user.mention} ha superato <b>1k</b> di followers, scarso🔮", f"{message.from_user.mention} ha superato <b>10k</b> di followes, GG per te🔮"])
    await client.send_message(message.chat.id, tiktokers)

@spaccobottiglie.on_message(filters.command("drogato"))
async def drogato(client, message):
    percentuale = random.randint(0, 100)
    await client.send_message(message.chat.id, f"{message.from_user.mention} è drogato al <b>{percentuale}%</b> 🍁")

@spaccobottiglie.on_message(filters.private & filters.command("stats"))
async def stats(client, message):
    if message.from_user.id in statsperms:
        await client.send_message(message.chat.id, f"**📊 Statistiche del bot 📊\n🗣 Utenti che hanno avviato il bot:** `{Users.__len__()}`")
    else:
        await client.send_message(message.chat.id, "solo il developer può usare questo comando!")

@spaccobottiglie.on_message(filters.command("animale"))
async def animale(client, message):
    animali = random.choice([f"{message.from_user.mention} è un <b>🐷Maiale</b>", f"{message.from_user.mention} è un <b>🦅Aquila</b>", f"{message.from_user.mention} è un <b>🦉Gufo</b>"])
    await client.send_message(message.chat.id, animali)

@spaccobottiglie.on_message(filters.command("lavoro"))
async def lavoro(client, message):
    lavori = random.choice([f"{message.from_user.mention} da grande farà il <b>🐑Pastore</b>", f"{message.from_user.mention} da grande farà il <b>🌾Contadino</b>", f"{message.from_user.mention} da grande farà il <b>💊Dottore</b>"])
    await client.send_message(message.chat.id, lavori)

@spaccobottiglie.on_message(filters.command("sesso"))
async def sesso(client, message):
    if message.reply_to_message:
        sessismo = f"🥵{message.reply_to_message.from_user.mention} si sta facendo sbattere da {message.from_user.mention}, non metterla incinta!👉👌💦"
        await client.send_message(message.chat.id, sessismo)
    else:
        await client.send_message(message.chat.id, f"rispondi ad un messaggio!")

@spaccobottiglie.on_message(filters.command("nomignolo"))
async def nomignolo(client, message):
    nomignoli = random.choice([f"👨Il nomignolo di {message.from_user.mention} è A <b>SMANDRUPPATA</b>", f"👨Il nomignolo di {message.from_user.mention} è A <b>Celoduro</b>", f"👨Il nomignolo di {message.from_user.mention} è A <b>Boss(ol)i secondo Beppe Grillo</b>"])
    await client.send_message(message.chat.id, nomignoli)

@spaccobottiglie.on_message(filters.command("youtuber"))
async def youtuber(client, message):
    youtube = random.choice([f"{message.from_user.mention} sta facendo video in qualità, me piaceh🔴", f"{message.from_user.mention} la smetti di fare quei tuoi video di merda🔴", f"{message.from_user.mention} ha superato <b>10k</b> di iscritti, GG per te🔴"])


@spaccobottiglie.on_message(filters.new_chat_members)
async def benvenuto(client, message):
    for user in message.new_chat_members:
        if user.is_self:
            await client.send_message(message.chat.id, "👋Ciao, sono un bot divertente.\n‼️<b>IMPOSTAMI ADMIN</b> e richiedi un supporto con /supporto per attivarmi, perchè non sono ancora attivo", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("⁉️Come Impostarmi Admin", "admin"), InlineKeyboardButton("❕Comandi e Funzionalità", "cmdw")]]))
        else:
            try:
                await client.get_chat_member(message.chat.id)
            except:
                await client.send_message(message.chat.id, random.choice([f"Oddio è entrato {message.from_user.mention} salutatelo!", f"{message.from_user.mention} si unisce alla festa!"]))

@spaccobottiglie.on_callback_query()
async def bottoni(client, query):
    if query.data == "fatto":
        try:
            canale = "" # rimetti la @ del canale senza @
            await client.get_chat_member(canale, query.from_user.id)
            await query.message.delete()
            btnstart = InlineKeyboardMarkup([
            [InlineKeyboardButton("➕AGGIUNGIMI AD UN GRUPPO➕", url="http://telegram.me/UsernameDelBot?startgroup=start")],
            [InlineKeyboardButton("📝COMANDI📝", "cmd")],
            [InlineKeyboardButton("🆘SUPPORTO🆘", url="t.me/ChillatoDev"), InlineKeyboardButton("🌐CANALE🌐", url="t.ne/canale")],
            [InlineKeyboardButton("❤️DONAZIONI❤️", "donazioni")]
        ])
            await client.send_message(query.message.chat.id, f"👋Ciao, {query.from_user.mention}, benvenuto in <b>🍾SpaccoBottiglia</b>\n\n<i>😂Aggiungimi ad un gruppo come admin per farvi divertire!</i>", reply_markup=btnstart)
        except:
            await query.answer("iscrivi al canale per usarmi!", show_alert=True)
    elif query.data == "back":
        backbtn2 = InlineKeyboardMarkup([
            [InlineKeyboardButton("➕AGGIUNGIMI AD UN GRUPPO➕", url="http://telegram.me/UsernameDelBot?startgroup=start")],
            [InlineKeyboardButton("📝COMANDI📝", "cmd")],
            [InlineKeyboardButton("🆘SUPPORTO🆘", url="t.me/ChillatoDev"), InlineKeyboardButton("🌐CANALE🌐", url="t.ne/canale")],
            [InlineKeyboardButton("❤️DONAZIONI❤️", "donazioni")]
        ])
        await query.message.edit(f"👋Ciao, {query.from_user.mention}, benvenuto in <b>🍾SpaccoBottiglia</b>\n\n<i>😂Aggiungimi ad un gruppo come admin per farvi divertire!</i>", reply_markup=backbtn2)
    elif query.data == "admin":
        await query.message.edit("""
<b>⁉️Come impostarmi admin?</b>

è molto semplice, basta seguire questi passaggi
● Vai nel gruppo
● Premi sul nome del Gruppo
● Premi gestione gruppo o ✏️
● Premi su Amministratori
● Premi Aggiungi Amministratori
● Premi la lente di ingrandimento
● Cerca il nome o l'username del Bot
● Conferma

<i>Una volta impostato admin potrai richiedere un supporto mediante il comando</i> /supporto        
""", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("⬅️indietro", "welcome")]]))
    elif query.data == "cmdw":
        await query.message.edit(helpmsg, reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🔙INDIETRO🔙", "welcome")]]))
    elif query.data == "welcome":
        await query.message.edit("👋Ciao, sono un bot divertente.\n‼️<b>IMPOSTAMI ADMIN</b> e richiedi un supporto con /supporto per attivarmi, perchè non sono ancora attivo", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("⁉️Come Impostarmi Admin", "admin"), InlineKeyboardButton("❕Comandi e Funzionalità", "cmdw")]]))

    elif query.data == "cmd":
        await query.message.edit(helpmsg, reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🔙INDIETRO🔙", "back")]]))

spaccobottiglie.run()
