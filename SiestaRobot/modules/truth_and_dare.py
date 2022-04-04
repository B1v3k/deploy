import random

from telegram import Update
from telegram.ext import CallbackContext

import SiestaRobot.modules.truth_and_dare_string as truth_and_dare_string
from SiestaRobot import dispatcher
from SiestaRobot.modules.disable import DisableAbleCommandHandler


def truth(update: Update, context: CallbackContext):
    context.args
    update.effective_message.reply_text(random.choice(truth_and_dare_string.TRUTH))


def dare(update: Update, context: CallbackContext):
    context.args
    update.effective_message.reply_text(random.choice(truth_and_dare_string.DARE))
def sigma(update: Update, context: CallbackContext):
    update.effective_message.reply_video(random.choice(truth_and_dare_string.SIGMA))

def cosplay(update: Update, context: CallbackContext):
    update.effective_message.reply_photo(random.choice(truth_and_dare_string.COSPLAY))

def rather(update: Update, context: CallbackContext):
    context.args
    update.effective_message.reply_text(random.choice(truth_and_dare_string.RATHER))



TRUTH_HANDLER = DisableAbleCommandHandler("truth", truth, run_async=True)
DARE_HANDLER = DisableAbleCommandHandler("dare", dare, run_async=True)
SIGMA_HANDLER = DisableAbleCommandHandler("sigma", sigma, run_async=True)
COSPLAY_HANDLER = DisableAbleCommandHandler("cosplay", cosplay, run_async=True)
COSPLAY_HANDLER = DisableAbleCommandHandler("rather", rather, run_async=True)





dispatcher.add_handler(TRUTH_HANDLER)
dispatcher.add_handler(DARE_HANDLER)
dispatcher.add_handler(SIGMA_HANDLER)
dispatcher.add_handler(COSPLAY_HANDLER)
dispatcher.add_handler(RATHER_HANDLER)
