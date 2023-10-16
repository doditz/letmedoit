# install package gTTS to work with this plugin

import config
from utils.tts_utils import ttsUtil

try:
    from gtts import gTTS

    def pronunce_words(function_args):
        words = function_args.get("words") # required
        language = function_args.get("language") # required
        print("Loading speech feature ...")
        ttsUtil.play(words, language)
        return "Finished! Speech engine closed!"

    functionSignature = {
        "name": "pronunce_words",
        "description": "pronounce words or sentences",
        "parameters": {
            "type": "object",
            "properties": {
                "words": {
                    "type": "string",
                    "description": "Words to be pronounced",
                },
                "language": {
                    "type": "string",
                    "description": "Language of the words",
                    "enum": config.ttsLanguages,
                },
            },
            "required": ["words", "language"],
        },
    }

    config.chatGPTApiFunctionSignatures.append(functionSignature)
    config.chatGPTApiAvailableFunctions["pronunce_words"] = pronunce_words
except:
    print("You need to install package 'gTTS' to work with plugin 'pronunce words'! Run:\n> source venv/bin/activate\n> 'pip3 install gTTS'")