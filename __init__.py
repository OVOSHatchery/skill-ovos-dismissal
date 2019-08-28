
from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill, intent_handler


class NevermindSkill(MycroftSkill):

    def __init__(self):
        super(NevermindSkill, self).__init__(name='NevermindSkill')

    @intent_handler(IntentBuilder('dismiss.mycroft').require('Nevermind'))
    def handle_dismiss_intent(self, message):
        self.log.info("User dismissed Mycroft.")
        if self.settings.get('verbal_feedback', False):
            self.speak_dialog('dismissed')


def create_skill():
    return NevermindSkill()
