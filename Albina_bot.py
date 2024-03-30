import aiogram as ag
import asyncio
import logging
from aiogram import Bot,Dispatcher,types,F
from aiogram.filters import Command
from aiogram.types import ReplyKeyboardMarkup
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State,StatesGroup
from aiogram.filters import StateFilter
from aiogram.utils.keyboard import InlineKeyboardBuilder
token=("6409599873:AAEQXLsReZYKFXjJIeMYFeKmEh9fwKMTySk")
bot=Bot(token=token)
dp=Dispatcher()
logging.basicConfig(level=logging.INFO)

class States(StatesGroup):
    calc=State()
    pol=State()
    vozrast=State()
    rost=State()
    ves=State()
    obraz_zhizny=State()
    cel=State()
    nabor_pohudenie=State()
    k_p=State()
    max_v=State()
    voda=State()
    puls=State()

@dp.message(Command("start"))
async def start(message:types.Message):
    btnlist=[[types.KeyboardButton(text="Калькулятор"),types.KeyboardButton(text="Упражнения")]]
    keyboard=ReplyKeyboardMarkup(keyboard=btnlist,resize_keyboard=True)
    await message.answer(text="Добро пожаловать", reply_markup=keyboard)

def get_kb():
    kb = [
            [types.InlineKeyboardButton(text="Грудь", callback_data="grud")],
            [types.InlineKeyboardButton(text="Спина", callback_data="spina")],
            [types.InlineKeyboardButton(text="Пресс", callback_data="press")],
            [types.InlineKeyboardButton(text="Ноги", callback_data="nogi")],
            [types.InlineKeyboardButton(text="Ягодицы", callback_data="popa")],
            [types.InlineKeyboardButton(text="Руки", callback_data="ruki")]
         ]
    builder=types.InlineKeyboardMarkup(inline_keyboard=kb)
    return builder

@dp.message(StateFilter(None),F.text)
async def msg(message:types.Message, state:FSMContext):
    if message.text.lower()=="привет":
        await message.answer(text="Привет!")
    if message.text=="Как дела?":
        await message.answer(text="Ужасно, замучили капризные клиенты!")
    if message.text=="Я хочу сегодня высокоинтенсивную тренировку":
        await message.answer(text="Сделай лицо попроще селедка,сегодня будет растяжка")
    if message.text=="У меня нет настроения сегодня тренироваться":
        await message.answer(text="НЕ грусти, нето сиськи не будут расти")
    if message.text=="Я не понимаю этого упражнения":
        await message.answer(text="Это мои чтоли проблемы?")
    if message.text=="У меня не получается":
        await message.answer(text="Нечего ,не получилось с первого раза,получится со второго.Не получится сегодня,значит получится завтра")
    if message.text=="Я устал":
        await message.answer(text="Втяни живот и выпрями спину! Чего трясешься как сосиска!")
    if message.text=="Что будем сегодня делать":
        await message.answer(text="То что я скажу")
    if message.text=="Я хочу накачать руки" or message.text == "Я хочу накачать грудь" or message.text == "Я хочу накачать спину" or message.text == "Я хочу накачать плечи" or message.text == "Я хочу накачать ноги":
        await message.answer(text="Нет,ты не знаешь чего хочешь,я лучше знаю что тебе надо")
    if message.text == "Я хочу накачать ягодицы":
        await message.answer(text="Ну тогда для начала подними свою тощую жопу с дивана!")
    if message.text == "Я хочу убрать живот":
        await message.answer(text="Ну тогда для начала подними свою жирную жопу с дивана!")
    if message.text=="Калькулятор":
        btnlist = [
                    [types.KeyboardButton(text="Калькулятор КБЖУ"),types.KeyboardButton(text="Рабочий вес"),],
                    [types.KeyboardButton(text="Пульс"),types.KeyboardButton(text="Расчет потребляемой воды")],
                    [types.KeyboardButton(text="Выйти")]
                  ]
        keyboard = ReplyKeyboardMarkup(keyboard=btnlist, resize_keyboard=True)
        await message.answer(text="Выберите калькулятор",reply_markup=keyboard)
        await state.set_state(States.calc)
    if message.text=="Упражнения":
        await message.answer(text="Что будем качать сегодня?😉", reply_markup=get_kb())

@dp.callback_query(F.data=="grud")
async def grud(callback: types.CallbackQuery):
    kb = [
            [types.InlineKeyboardButton(text="Жим штанги лежа горизонтально", callback_data="g_ex_1")],
            [types.InlineKeyboardButton(text="Жим штанги в наклоне", callback_data="g_ex_2")],
            [types.InlineKeyboardButton(text="Жим гантелей лежа", callback_data="g_ex_3")],
            [types.InlineKeyboardButton(text="Разведение рук с гантелями", callback_data="g_ex_4")],
            [types.InlineKeyboardButton(text="Сведение рук на нижнем блоке кроссовера", callback_data="g_ex_5")],
            [types.InlineKeyboardButton(text="Сведение рук в тренажере бабочка", callback_data="g_ex_6")],
            [types.InlineKeyboardButton(text="Отжимания на брусьях", callback_data="g_ex_7")],
            [types.InlineKeyboardButton(text="Хаммер", callback_data="g_ex_8")],
            [types.InlineKeyboardButton(text="Жим гантелей", callback_data="g_ex_9")],
            [types.InlineKeyboardButton(text="Жим штанги сидя перед собой в тренажере Смита", callback_data="g_ex_10")],
            [types.InlineKeyboardButton(text="Назад ⬅️", callback_data="back2ex")]
         ]
    builder=types.InlineKeyboardMarkup(inline_keyboard=kb)
    await callback.message.edit_text("Упражнения на грудь", reply_markup=builder)
    await callback.answer()

@dp.callback_query(F.data=="spina")
async def spina(callback: types.CallbackQuery):
    kb = [
            [types.InlineKeyboardButton(text="Подтягивание", callback_data="s_ex_1")],
            [types.InlineKeyboardButton(text="Австрийское подтягивание", callback_data="s_ex_2")],
            [types.InlineKeyboardButton(text="Тяга горизонтального блока", callback_data="s_ex_3")],
            [types.InlineKeyboardButton(text="Гравитрон", callback_data="s_ex_4")],
            [types.InlineKeyboardButton(text="Тяга к подбородку", callback_data="s_ex_5")],
            [types.InlineKeyboardButton(text="Тяга гантелей одной рукой на скамье", callback_data="s_ex_6")],
            [types.InlineKeyboardButton(text="Тяга Т-грифа с упором на скамью", callback_data="s_ex_7")],
            [types.InlineKeyboardButton(text="Гиперэкстензия", callback_data="s_ex_8")],
            [types.InlineKeyboardButton(text="Тяга штанги в наклоне", callback_data="s_ex_9")],
            [types.InlineKeyboardButton(text="Становая тяга", callback_data="s_ex_10")],
            [types.InlineKeyboardButton(text="Обратные махи гантелями лежа", callback_data="s_ex_11")],
            [types.InlineKeyboardButton(text="Назад ⬅️", callback_data="back2ex")]
         ]
    builder=types.InlineKeyboardMarkup(inline_keyboard=kb)
    await callback.message.edit_text("Упражнения на спину", reply_markup=builder)  
    await callback.answer()  

@dp.callback_query(F.data=="nogi")
async def nogi(callback: types.CallbackQuery):
    kb = [
            [types.InlineKeyboardButton(text="Приседание со штангой на спине", callback_data="n_ex_1")],
            [types.InlineKeyboardButton(text="Приседание со штангой на груди", callback_data="n_ex_2")],
            [types.InlineKeyboardButton(text="Выпады", callback_data="n_ex_3")],
            [types.InlineKeyboardButton(text="Жим ногами в тренажере", callback_data="n_ex_4")],
            [types.InlineKeyboardButton(text="Болгарский присед", callback_data="n_ex_5")],
            [types.InlineKeyboardButton(text="Сведение / разведение в тренажере", callback_data="n_ex_6")],
            [types.InlineKeyboardButton(text="Подъем на носки стоя", callback_data="n_ex_7")],
            [types.InlineKeyboardButton(text="Сгибание ног", callback_data="n_ex_8")],
            [types.InlineKeyboardButton(text="Разгибание ног", callback_data="n_ex_9")],
            [types.InlineKeyboardButton(text="Назад ⬅️", callback_data="back2ex")]
         ]
    builder=types.InlineKeyboardMarkup(inline_keyboard=kb)
    await callback.message.edit_text("Упражнения на ноги", reply_markup=builder)  
    await callback.answer()      

@dp.callback_query(F.data=="popa")
async def popa(callback: types.CallbackQuery):
    kb = [
            [types.InlineKeyboardButton(text="Подъем таза с опорой на лавку", callback_data="pp_ex_1")],
            [types.InlineKeyboardButton(text="Ягодичный мост с весом", callback_data="pp_ex_2")],
            [types.InlineKeyboardButton(text="Тяга в кроссовере между ног", callback_data="pp_ex_3")],
            [types.InlineKeyboardButton(text="Русские махи гирей", callback_data="pp_ex_4")],
            [types.InlineKeyboardButton(text="Обратная гиперэкстензия", callback_data="pp_ex_5")],
            [types.InlineKeyboardButton(text="Отведение бедра назад в кроссовере", callback_data="pp_ex_6")],
            [types.InlineKeyboardButton(text="Приседания со штангой", callback_data="pp_ex_7")],
            [types.InlineKeyboardButton(text="Становая тяга", callback_data="pp_ex_8")],
            [types.InlineKeyboardButton(text="Выпады", callback_data="pp_ex_9")],
            [types.InlineKeyboardButton(text="Жим ногами в тренажёре", callback_data="pp_ex_10")],
            [types.InlineKeyboardButton(text="Назад ⬅️", callback_data="back2ex")]
        ]
    builder=types.InlineKeyboardMarkup(inline_keyboard=kb)
    await callback.message.edit_text("Упражнения на ягодицы", reply_markup=builder)  
    await callback.answer()

@dp.callback_query(F.data=="ruki")
async def ruki(callback: types.CallbackQuery):
    kb = [
            [types.InlineKeyboardButton(text="Плечи", callback_data="shoulders")],
            [types.InlineKeyboardButton(text="Бицепс", callback_data="biceps")],
            [types.InlineKeyboardButton(text="Трицепс", callback_data="triceps")],
            [types.InlineKeyboardButton(text="Назад ⬅️", callback_data="back2ex")]
         ]
    builder=types.InlineKeyboardMarkup(inline_keyboard=kb)
    await callback.message.edit_text("Выберите категорию", reply_markup=builder)  
    await callback.answer()

@dp.callback_query(F.data=="biceps")
async def press(callback: types.CallbackQuery):
    kb = [
            [types.InlineKeyboardButton(text="Подъем w образной штанги", callback_data="b_ex_1")],
            [types.InlineKeyboardButton(text="Подьем гантелей сидя на мнаклонной скамье", callback_data="b_ex_2")],
            [types.InlineKeyboardButton(text="Молот", callback_data="b_ex_3")],
            [types.InlineKeyboardButton(text="Подъем гантелей на бицепс стоя", callback_data="b_ex_4")],
            [types.InlineKeyboardButton(text="Работа в бицепс машине", callback_data="b_ex_5")],
            [types.InlineKeyboardButton(text="Сгибание в кроссовере", callback_data="b_ex_6")],
            [types.InlineKeyboardButton(text="Подтягивание обратным хватом", callback_data="b_ex_7")],
            [types.InlineKeyboardButton(text="Штанга хватом сверху", callback_data="b_ex_8")],
            [types.InlineKeyboardButton(text="Изолированные сгибания", callback_data="b_ex_9")],
            [types.InlineKeyboardButton(text="Назад ⬅️", callback_data="ruki")]
         ]
    builder=types.InlineKeyboardMarkup(inline_keyboard=kb)
    await callback.message.edit_text("Упражнения на бицепс", reply_markup=builder)  
    await callback.answer()


@dp.callback_query(F.data=="triceps")
async def press(callback: types.CallbackQuery):
    kb = [
            [types.InlineKeyboardButton(text="Обратные отжимания на скамье", callback_data="t_ex1")],
            [types.InlineKeyboardButton(text="Брусья", callback_data="t_ex2")],
            [types.InlineKeyboardButton(text="Отжимания", callback_data="t_ex3")],
            [types.InlineKeyboardButton(text="Французкий жим", callback_data="t_ex4")],
            [types.InlineKeyboardButton(text="Жим гантели из-за головы", callback_data="t_ex5")],
            [types.InlineKeyboardButton(text="Разгибание на блоке с канатной ручкой", callback_data="t_ex6")],
            [types.InlineKeyboardButton(text="Разгибание на блоке обратным хватом", callback_data="t_ex7")],
            [types.InlineKeyboardButton(text="Разгибание на блоке из-за головы", callback_data="t_ex8")],
            [types.InlineKeyboardButton(text="Жим узким хватом", callback_data="t_ex9")],
            [types.InlineKeyboardButton(text="Назад ⬅️", callback_data="ruki")]
         ]
    builder=types.InlineKeyboardMarkup(inline_keyboard=kb)
    await callback.message.edit_text("Упражнения на трицепс", reply_markup=builder)  
    await callback.answer()


@dp.callback_query(F.data=="shoulders")
async def press(callback: types.CallbackQuery):
    kb = [
            [types.InlineKeyboardButton(text="Жим гантелей вверх стоя", callback_data="sh_ex1")],
            [types.InlineKeyboardButton(text="Жим штанги с груди стоя", callback_data="sh_ex2")],
            [types.InlineKeyboardButton(text="Разводы гантелей в стороны с разворотом", callback_data="sh_ex3")],
            [types.InlineKeyboardButton(text="Разводы гантелей в наклоне сидя", callback_data="sh_ex4")],
            [types.InlineKeyboardButton(text="Обратная бабочка", callback_data="sh_ex5")],
            [types.InlineKeyboardButton(text="Тяга к подбородку", callback_data="sh_ex6")],
            [types.InlineKeyboardButton(text="Бабочка назад", callback_data="sh_ex7")],
            [types.InlineKeyboardButton(text="Подьем блина с вращением", callback_data="sh_ex8")],
            [types.InlineKeyboardButton(text="Назад ⬅️", callback_data="ruki")]
         ]
    builder=types.InlineKeyboardMarkup(inline_keyboard=kb)
    await callback.message.edit_text("Упражнения на плечи", reply_markup=builder)  
    await callback.answer()

@dp.callback_query(F.data=="press")
async def press(callback: types.CallbackQuery):
    kb = [
            [types.InlineKeyboardButton(text="Скручивания", callback_data="p_ex_1")],
            [types.InlineKeyboardButton(text="Обратные скручивания", callback_data="p_ex_2")],
            [types.InlineKeyboardButton(text="Скручивания на наклонной скамье", callback_data="p_ex_3")],
            [types.InlineKeyboardButton(text="Косые скручивания к прямой ноге", callback_data="p_ex_4")],
            [types.InlineKeyboardButton(text="Подъем корпуса", callback_data="p_ex_5")],
            [types.InlineKeyboardButton(text="Твист с гантелей сидя", callback_data="p_ex_6")],
            [types.InlineKeyboardButton(text="Складка", callback_data="p_ex_7")],
            [types.InlineKeyboardButton(text="Складка 'нож'", callback_data="p_ex_8")],
            [types.InlineKeyboardButton(text="Ножницы", callback_data="p_ex_9")],
            [types.InlineKeyboardButton(text="Велосипед", callback_data="p_ex_10")],
            [types.InlineKeyboardButton(text="Планка / планка на вытянутых руках", callback_data="p_ex_11")],
            [types.InlineKeyboardButton(text="Назад ⬅️", callback_data="back2ex")]
         ]
    builder=types.InlineKeyboardMarkup(inline_keyboard=kb)
    await callback.message.edit_text("Упражнения на пресс", reply_markup=builder)  
    await callback.answer() 

@dp.callback_query(F.data=="back2ex")
async def back2ex(callback: types.CallbackQuery):
        await callback.message.edit_text("Что будем качать сегодня?😉", reply_markup=get_kb())
        await callback.answer() 


@dp.message(StateFilter(States.calc),F.text)
async def clc(message:types.Message, state:FSMContext):
    if message.text == "Калькулятор КБЖУ":
        btnlist = [
                    [types.KeyboardButton(text="Набор массы")],
                    [types.KeyboardButton(text="Похудение")],
                    [types.KeyboardButton(text="Поддержание формы")]
                  ]
        keyboard = ReplyKeyboardMarkup(keyboard=btnlist, resize_keyboard=True)
        await message.answer(text="Укажите цель",reply_markup=keyboard)
        await state.set_state(States.nabor_pohudenie)
    if message.text=="Рабочий вес":
        await message.answer(text="Укажите количество повторений")
        await state.set_state(States.k_p)
    if message.text=="Расчет потребляемой воды":
        await message.answer(text="Укажите вес")
        await state.set_state(States.voda)
    if message.text=="Пульс":
        await message.answer(text="Укажите возраст")
        await state.set_state(States.puls)
    if message.text == "Выйти":
        btnlist = [
                    [types.KeyboardButton(text="Калькулятор"),
                     types.KeyboardButton(text="Упражнения")]
                  ]
        keyboard = ReplyKeyboardMarkup(keyboard=btnlist, resize_keyboard=True)
        await message.answer(text="Вы вышли в главное меню",reply_markup=keyboard)
        await state.clear()

@dp.message(StateFilter(States.voda),F.text)
async def voda(message:types.Message, state:FSMContext):
    await message.answer(text=f"Суточная норма употребления воды: {int(message.text)*30/1000} л.")
    await state.clear()

@dp.message(StateFilter(States.k_p),F.text)
async def k_p(message:types.Message, state:FSMContext):
    await state.update_data(k_p=message.text)
    await message.answer(text="Максимальный вес")
    await state.set_state(States.max_v)

@dp.message(StateFilter(States.max_v),F.text)
async def max_v(message:types.Message, state:FSMContext):
    btnlist = [
                [types.KeyboardButton(text="Калькулятор"),
                 types.KeyboardButton(text="Упражнения")]
              ]
    keyboard = ReplyKeyboardMarkup(keyboard=btnlist, resize_keyboard=True)
    data=await state.get_data()
    c_p=data["k_p"]
    await message.answer(text=f"Рабочий вес: {int((1.0278-(0.0278*int(c_p))*int(message.text)*-1))} кг.", reply_markup=keyboard)
    await state.clear()

@dp.message(StateFilter(States.nabor_pohudenie),F.text)
async def n_b(message:types.Message, state:FSMContext):
    btnlist = [
                [types.KeyboardButton(text="Мужской"),
                 types.KeyboardButton(text="Женский")]
              ]
    keyboard = ReplyKeyboardMarkup(keyboard=btnlist, resize_keyboard=True)
    await state.update_data(naborpohud=message.text)
    print(message.text)
    await message.answer(text="Выберите пол",reply_markup=keyboard)
    await state.set_state(States.pol)

@dp.message(StateFilter(States.pol),F.text)
async def pol(message:types.Message, state:FSMContext):
    await state.update_data(pol=message.text)
    await message.answer(text="Введите ваш возраст")
    await state.set_state(States.vozrast)

@dp.message(StateFilter(States.vozrast),F.text)
async def vozrast(message:types.Message, state:FSMContext):
    await state.update_data(vozrast=message.text)
    await message.answer(text="Введите ваш рост")
    await state.set_state(States.rost)

@dp.message(StateFilter(States.puls),F.text)
async def puls(message:types.Message, state:FSMContext):
    btnlist = [
                [types.KeyboardButton(text="Калькулятор"),
                 types.KeyboardButton(text="Упражнения")]
              ]
    keyboard = ReplyKeyboardMarkup(keyboard=btnlist, resize_keyboard=True)
    max_puls=220-int(message.text)
    ozdorov=int(max_puls*0.57)
    fitnes=int(max_puls*0.63)
    aerob=int(max_puls*0.76)
    anaaerob=int(max_puls*0.95)
    await message.answer(text=f'''Оздоровительная - пульс до {ozdorov}
Эта пульсовая зона обычно соответствует пешей прогулке или неспешной езде на велосипеде по равнинной местности. 
Тренировки в этой зоне сердечного ритма полезны при восстановлении после более интенсивной тренировки.
                         
Фитнес зона - пульс от {ozdorov} до {fitnes}
Занятия в этой зоне не интенсивны и не очень эффективны для тренировки сердца и дыхательного аппарата. Зато соблюдение этого «коридора» уже помогает терять лишний вес. Обычно добиться такого пульса можно при ходьбе в быстром темпе.

Аэробная зона - пульс от {fitnes} до {aerob} 
Тренировки в этой зоне более интенсивны, во время них уже становится тяжелее дышать. Такие занятия подойдут новичкам, а нагрузку можно выдерживать в течение длительного времени, что часто принимают за эффективность для сжигания жира. Примеры такой тренировки — быстрая ходьба и легкий бег.

Анаэробная зона - пульс от {aerob} до {anaaerob}
Это тренировки высокой интенсивности, полезные для развития выносливости и потери веса у подготовленных спортсменов. Как правило, на таком пульсе проводят интервальные и круговые тренировки. Добиться таких значений пульса можно при спринте или быстрой езде на велосипеде. При этом лучше сделать ЭКГ и проконсультироваться с врачом-кардиологом перед тем, как приступать к занятиям в этой пульсовой зоне.

Максимальная зона - пульс от {anaaerob} до {max_puls}
Неподготовленным людям и тем, у кого нет разрешения от врача, тренироваться в этой зоне категорически не рекомендуется. Профессиональные спортсмены же проводят в этой пульсовой зоне соревнования и интервальные тренировки.
''',reply_markup=keyboard)
    await state.clear()
    
@dp.message(StateFilter(States.rost),F.text)
async def rost(message:types.Message, state:FSMContext):
    await state.update_data(rost=message.text)
    await message.answer(text="Введите ваш вес")
    await state.set_state(States.ves)

@dp.message(StateFilter(States.ves),F.text)
async def ves(message:types.Message, state:FSMContext):
    btnlist = [
                [types.KeyboardButton(text="Сидячая работа")],
                [types.KeyboardButton(text="Тренировки с низкой активностью")],
                [types.KeyboardButton(text="Тренировки с умеренной активностью")],
                [types.KeyboardButton(text="Высокий уровень нагрузки")],
                [types.KeyboardButton(text="Экстремальный уровень активности")]
              ]
    keyboard = ReplyKeyboardMarkup(keyboard=btnlist, resize_keyboard=True)
    await state.update_data(ves=message.text)
    await message.answer(text="Укажите образ жизни",reply_markup=keyboard)
    await state.set_state(States.obraz_zhizny)

@dp.message(StateFilter(States.obraz_zhizny),F.text)
async def obraz_zhizny(message:types.Message, state:FSMContext):
    slovar = {
                "Сидячая работа": 1.2,
                "Тренировки с низкой активностью": 1.375,
                "Тренировки с умеренной активностью": 1.55,
                "Высокий уровень нагрузки": 1.7,
                "Экстремальный уровень активности": 1.9
             }
    cel = {
            "Набор массы":1.15,
            "Похудение":0.85,
            "Поддержание формы":1
          }
    btnlist = [
                [types.KeyboardButton(text="Калькулятор"),
                types.KeyboardButton(text="Упражнения")]
              ]
    keyboard = ReplyKeyboardMarkup(keyboard=btnlist, resize_keyboard=True)
    user_data = await state.get_data()
    pol = user_data["pol"]
    vozrast = user_data["vozrast"]
    rost = user_data["rost"]
    ves = user_data["ves"]
    n_b=user_data["naborpohud"]
    obraz_zhizny=message.text
    if pol == "Мужской":
        result = 66.5 + (13.75 * int(ves)) + (5.003 * int(rost)) - (6.775 * int(vozrast))
        await message.answer(text=f"Базовая потребность в калориях - {int(result*slovar[message.text]*cel[n_b])}", reply_markup=keyboard)
    if pol == "Женский":
        result = 655.1 + (9.563 * int(ves)) + (1.85 * int(rost)) - (4.676 * int(vozrast))
        await message.answer(text=f"Базовая потребность в калориях - {int(result*slovar[message.text]*cel[n_b])}", reply_markup=keyboard)
    await state.clear()

async def main():
    await dp.start_polling(bot)

if __name__=="__main__":
    asyncio.run(main())