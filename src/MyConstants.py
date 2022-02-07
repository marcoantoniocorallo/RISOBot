# path and keywords (constants!)
inPath = "../files/in/"
logPath = "../files/out/risobot.log"
DBPath = "../files/DB.json"
kwAlternatives = "Alternative alimentari"
kwPlan = "LUNEDÌ"
token = ""  # @AdrianosDietsConsultingBot
projectName = "RISOBot"
authorid = -1 # My userid
authorUsername = '@mac96'
welcomeMessage = (
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
errorFileMsg = (
    'Il file inviato non rispetta la formattazione prevista.'
    'Puoi contattare '+authorUsername+' per chiedere una revisione delle regole di formattazione.'
    )

# commands
start = ["start","info","help"]
alternative = ["alternative","alt","alternativa"]
