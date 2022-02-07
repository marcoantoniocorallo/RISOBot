import logging
import telebot as t

from Utils import *
from MyConstants import *
from MyMaps import days, meals
from UserSession import UserSession

# Msg handler fun
def listener(msgs):

    for m in msgs:
        chatid = m.chat.id
        userid = m.from_user.id
        username = m.from_user.username
        name = m.from_user.full_name
        if m.content_type=='text':
            text = m.text.lower().replace('ì','i').replace('/','')
        elif m.content_type=='document':
            text = IN_PATH+str(userid)+".pdf"
        logger.info(str(username)+" - "+str(name)+" - "+str(m.content_type)+": \""+str(text)+"\"")

        # Save new user
        if userid not in users:
            users[userid] = UserSession(chatid,userid,username,name)
            store(users)

        # handle text messages
        if m.content_type=='text':
            
            if text in START:
                bot.send_message(chatid,WELCOME_MESSAGE)
            elif users[userid].plan is not None:
                handle_text(text,chatid,userid)
            else:
                bot.send_message(chatid,
                    'Per utilizzare il bot devi prima inviare un piano alimentare.\n')

        # handle diets received
        elif m.content_type=='document':
            handle_docs(m.document,userid)

def handle_docs(doc,user):
    file_path = bot.get_file(doc.file_id).file_path
    file = bot.download_file(file_path)
    users[user].plan = IN_PATH+str(users[user].userid)+".pdf"
    with open(users[user].plan,'wb') as f:
        f.write(file)
    
    # check plan correctness
    if checkCorrectness(users[user].plan):
        store(users)
        bot.send_message(users[user].chatid,"La dieta è stata salvata ed è ora consultabile.")
        logger.info('Salvato correttamente file: '+users[user].plan)
    else:
        logger.warning('Formattazione non supportata: '+users[user].plan)
        bot.send_message(users[user].chatid,ERROR_FILE_MSG)
        bot.send_message(AUTHORID,
            'È stato inviato un file con formattazione non supportata da '+str(users[user].username))
        users[user].plan = None

def handle_text(text,chatid,userid):

    # Set day for the query
    if text in days:
        users[userid].day = days[text]
        if users[userid].meal is None:
            bot.send_message(chatid,"Che pasto?")
        else:
            bot.send_message(chatid,lookupForMeal(users[userid]))
            users[userid].reset()

    # Set meal for the query
    elif text in meals:
        users[userid].meal = meals[text]
        if users[userid].day is None:
            bot.send_message(chatid,"Che giorno?")
        else:
            bot.send_message(chatid,lookupForMeal(users[userid]))
            users[userid].reset()

    # Query for the alternatives
    elif text in ALTERNATIVE:
        users[userid].alt = True
        bot.send_message(chatid,"Che cibo vuoi sostituire?")

    # Set food for the query for the alternatives
    elif users[userid].alt:
        s = lookupForAlternatives(users[userid],text)
        bot.send_message(chatid, s if s is not None else text+" non è stato trovato.")
        users[userid].reset()

    else:
        bot.send_message(chatid,"Comando non riconosciuto.")

########################################################################################################

# Load data from DB
users = load()

# Config log
logging.basicConfig(format='[%(levelname)s - %(name)s - %(asctime)s]: %(message)s', 
                    level=logging.INFO, datefmt='%Y/%m/%d %H:%M:%S',
                    filename=LOG_PATH, filemode='a')
logger = logging.getLogger(PROJECT_NAME)
logging.getLogger("pdfminer").setLevel(logging.ERROR) # increment log level for imported modules

bot = t.TeleBot(TOKEN) # TOKEN
bot.set_update_listener(listener)
bot.polling()