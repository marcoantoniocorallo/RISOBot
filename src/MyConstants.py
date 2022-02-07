# path and keywords (constants!)
IN_PATH = "../files/in/"
LOG_PATH = "../files/out/risobot.log"
DB_PATH = "../files/DB.json"
KW_ALTERNATIVES = "Alternative alimentari"
KW_PLAN = "LUNEDÌ"
TOKEN = ""  # @AdrianosDietsConsultingBot
PROJECT_NAME = "ChefAdrianoBot"
AUTHORID = -1 # My userid
AUTHOR_USERNAME = '@mac96'
WELCOME_MESSAGE = (
    'Benvenuto, questo bot ti permetterà di inserire e consultare facilmente un piano alimentare.\n\n'
    'Puoi inserire un piano alimentare personalizzato inviandomi in qualsiasi momento il file PDF.\n\n'
    'Comandi: \n'
    '/lunedi per conoscere il menù di un pasto del lunedì;\n'
    '/martedi per conoscere il menù di un pasto del martedì;\n'
    '    : \n'
    '/colazione per conoscere il menù della colazione del giorno scelto;\n'
    '/mattina per conoscere il menù della merenda mattutina del giorno scelto;\n'
    '    : \n'
    '/alternative per conoscere le alternative di un piatto successivamente comunicato;\n\n'
    'Buon Appetito!'
    )
ERROR_FILE_MSG = (
    'Il file inviato non rispetta la formattazione prevista.'
    'Puoi contattare '+AUTHOR_USERNAME+' per chiedere una revisione delle regole di formattazione.'
    )

# commands
START = ["start","info","help"]
ALTERNATIVE = ["alternative","alt","alternativa"]
