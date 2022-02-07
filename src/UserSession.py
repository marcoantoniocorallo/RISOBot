import json

class UserSession:
    def __init__(self, chatid : int, userid : int, username : str, name : str, plan : str = None) -> None:
        self.chatid = chatid
        self.userid = userid
        self.username = username
        self.name = name
        self.plan = plan
        self.day = None
        self.meal = None
        self.alt = None

    def reset(self):
        self.day = None
        self.meal = None
        self.alt = None

    def toJSON(self):
        return json.dumps(self,
            default = lambda o : 
            { k:o.__dict__[k] for k in o.__dict__ if k not in 
            ['day','meal','alt'] }, 
            sort_keys=False)

    def __str__(self) -> str:
        return self.toJSON()