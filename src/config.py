SYSTEM_EMOJI = "⚙️"
AI_EMOJI = "🤖"

HELP_MSG = (
    f"{SYSTEM_EMOJI} !ai <запрос> - запрос к боту (gpt-3.5-turbo)"
    "\n\nПри использовании этой команды, gpt получает ваш запрос и ваше имя и"
    " фамилию (соответственно, разрешая отправлять эти данные компании OpenAI)."
    "\n\nЕсли использовать эту команду, ответив на сообщение другого пользователя,"
    " то gpt получает ваш запрос, ваше имя и фамилию, текст сообщения в ответе"
    " и имя и фамилию пользователя в ответе."
    "\n\nПриложив картинку к сообщению, бот будет использовать gpt-4-vision-preview,"
    " чтобы распознать её (только для избранных)."
)

MAX_IMAGE_WIDTH = 750

BAN_WORDS = ("hitler", "гитлер", "gitler", "ниггер", "негр", "vto.pe", "vtope",)
AI_BAN_WORDS = ("синий кит", "сова никогда не спит",)
CENSOR_WORDS = ("onion", "hitler", "vtope", "vto.pe", "vto pe",)

DB_PATH = "./db.db"
MOODS_PATH = "./moods.json"
