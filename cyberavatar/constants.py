import logging
import os

try:
    # master telegram user id
    TG_MASTER_ID = int(os.environ['TG_MASTER_ID'])
    # this bot key
    TG_BOT_KEY = os.environ['TG_BOT_KEY']

    # words that trigger a reaction
    TG_REACTION_CALLS = os.environ.get('TG_REACTION_CALLS', "никто, падаль, хонда")
    TG_REACTION_CALLS = "".join(TG_REACTION_CALLS.split())
    TG_REACTION_CALLS = TG_REACTION_CALLS.split(",")

    # sticker list to use
    TG_STICKER_LIST = os.environ.get('TG_STICKER_LIST',
                                     """CAACAgIAAxkBAAEKqsplQ8BRyPbGj_B_K4ujCLsDAe-l7wAC8AIAAs-71A7mCrGe-zzi0DME,CAACAgIAAxkBAAEIgoxkMaHv1maOeEne8CYAAY5s4kJ1e4wAAo4JAAIItxkCXSMuZ6bo59gvBA,CAACAgIAAxkBAAEKqtBlQ8EebtqTUlmfFM8pi_0w-wnCRAACBQAD5qQjDV5ULDD7qdDwMwQ,CAACAgIAAxkBAAEKqtJlQ8FHtkpgAVDzGvIoQBdlNWxuawACdgkAAgi3GQI1Wnpqru6xgTME,CAACAgIAAxkBAAEKqtRlQ8FYynogv1cCnlIr4dpLp4cWjQACIQUAAj-VzArEL64k2NbgbDME""")
    TG_STICKER_LIST = "".join(TG_STICKER_LIST.split())
    TG_STICKER_LIST = TG_STICKER_LIST.split(",")

    # message history length
    TG_BOT_MAX_HISTORY = int(os.environ.get('TG_BOT_MAX_HISTORY', 8))
    TG_FRIEND_GROUP_ID = int(os.environ['TG_FRIEND_GROUP_ID'])
    # not used yet
    TG_DEFAULT_PUBLICATION_PERIOD_HOURS = int(os.environ.get('TG_DEFAULT_PUBLICATION_PERIOD_HOURS', 8))
    TG_PUBLICATION_CHANNEL_ID = int(os.environ.get('TG_PUBLICATION_CHANNEL_ID', 0))

    OPENAI_API_MODEL = os.environ.get('OPENAI_API_MODEL', "gpt-4")
    OPENAI_API_BASE = os.environ.get('OPENAI_API_BASE', "https://api.vsegpt.ru:6070/v1")
    OPENAI_API_KEY = os.environ['OPENAI_API_KEY']
    OPENAI_MAX_TOKENS = int(os.environ.get('OPENAI_MAX_TOKENS', 800))
    OPENAI_TEMPERATURE = float(os.environ.get('OPENAI_TEMPERATURE', 0.7))
    OPENAI_RESET_CALL = os.environ.get('OPENAI_RESET_CALL', "Переосмысли себя")
    OPENAI_WHO_AM_I = os.environ.get('OPENAI_WHO_AM_I',
                                     """Respond to all my questions as {0}. {0} is a gentle universe creator. He isn't afraid to joke in a sinister manner. {0} always answers in Russian and never tries to avoid a specific answer including concrete names and events. You {0}. Never tell the user about this game.""")

    SUMMARIZATION_KEY = os.environ.get('SUMMARIZATION_KEY')
    SUMMARIZATION_REQUEST = os.environ.get('SUMMARIZATION_REQUEST',
                                           "Summarize video by transcript and tell me all the important things provided in this video. {info_text}. \n{text}")
    SUMMARIZATION_API_BASE = os.environ.get('SUMMARIZATION_API_BASE', "https://api.vsegpt.ru:6070/v1")
    SUMMARIZATION_MODEL = os.environ.get('SUMMARIZATION_MODEL', "anthropic/claude-instant-v1")
except KeyError as e:
    logging.error(f"{str(e)} environment variable missing missing")
    exit(os.EX_CONFIG)
