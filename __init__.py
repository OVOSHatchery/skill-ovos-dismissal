# TODO add verbal toggle for setting
# TODO consider adding a confirmation tone as an alternative


from ovos_utils.intents import IntentBuilder
from ovos_workshop.decorators import intent_handler
from ovos_workshop.skills import OVOSSkill


class DismissalSkill(OVOSSkill):

    @intent_handler(IntentBuilder('dismiss.mycroft').require('Nevermind'))
    def handle_dismiss_intent(self, message):
        if self.settings.get('verbal_feedback_enabled', True):
            self.speak_dialog('dismissed')
        self.log.info("User dismissed OVOS")

