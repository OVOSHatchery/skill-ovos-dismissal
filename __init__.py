#TODO add verbal toggle for setting
#TODO consider adding a confirmation tone as an alternative


from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill, intent_handler


class DismissalSkill(MycroftSkill):

    def __init__(self):
        super(DismissalSkill, self).__init__(name='DismissalSkill')

    @intent_handler(IntentBuilder('dismiss.mycroft').require('Nevermind'))
    def handle_dismiss_intent(self, message):
        if self.settings.get('verbal_feedback_enabled'):
            self.speak_dialog('dismissed')
        self.log.info("User dismissed Mycroft.")

def create_skill():
    return DismissalSkill()
