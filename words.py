'''Тут слова на которые реагирует бот, что 
обращение было к нему. Его имя и команда могут быть сказаны
в любой последовательности и даже в перемешку и тд...,
главное без продолжительной паузы'''

TRIGGERS = {'альбина','альбинка'}



'''Тренировочная модель для матрицы ИИ'''
data_set = {

'какая погода': 'weather wait a minute',
'какая погода на улице': 'weather боишься замерзнуть?',
'что там на улице': 'weather сейчас гляну...',
'сколько градусов': 'weather можешь выглянуть в окно, но сейчас проверю',
'запусти браузер': 'browser запускаю браузер',
'открой браузер': 'browser интернет активирован',
'интернет открой': 'browser открываю браузер',
'посмотреть фильм': 'browser сейчас открою браузер',
'играть': 'game лишь бы баловаться',
'хочу поиграть в игру': 'game а нам лишьбы баловаться',
'запусти игру': 'game запускаю игру, а нам лишь бы баловаться',
'выключи компьютер': 'offpc отключаю компьютер',
'отключись': 'offBot отключаюсь',
'как у тебя дела':'passive работаю в фоне, не переживай',
'что делаешь':'passive жду очередной команды, хоть мог бы и сам на кнопку нажать',
'привет':'passive и тебе привет',
'расскажи анекдот':'passive Вчера помыла окна, теперь у меня рассвет на два часа раньше...',
'работаешь':'passive как видишь',
'ты тут':'passive вроде да',
'ты будешь меня тренировать':'passive нет, у меня есть клиенты которые платят больше, понял крестьянский сын',
'мне грустно':'passive не грусти, а то сиськи не будут расти',
'я устал':'passive заткнись селёдка и продолжай работать',
'доктор рекомендовал пропить витамины':'passive у этого твоего доктора образование вообще есть',
'я не помню':'passive это всё твои плохие привычки',
'что нужно чтобы работать тренером':'passive научится стоя на одном пальце, жанглировать ушами',
'почему ты грубишь мне':'passive потому что ты мало платишь крестьянский сын',
'сколько надо учиться на тренера':'passive надо постоянно учится и работать тридцать лет в одном клубе, пока не помрешь от старости',
'я нечего не понял':'passive это мои чтоли проблемы',
'запусти телеграм бота':'start_bot запускаю',
'отличный денёк чтобы по ворчать':'passive ха ха это ты так шутишь чтоли',
'не до смеха':'passive хуйню мне всякую несёшь',
}