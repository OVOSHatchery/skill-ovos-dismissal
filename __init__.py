
from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill, intent_handler


class NevermindSkill(MycroftSkill):

    def __init__(self):
        super(NevermindSkill, self).__init__(name='NevermindSkill')

        self.feedback = (self.settings.get('verbal_feedback') is not False)

    @intent_handler(IntentBuilder('').require('Nevermind'))
    def handle_nevermind_intent(self, message):
        self.log.info("User dismissed Mycroft.")
        if self.feedback:
            self.speak_dialog('dismissed')


def create_skill():
    return NevermindSkill()
