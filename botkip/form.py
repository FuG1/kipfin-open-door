from aiogram.fsm.context import FSMContext
from aiogram.types import Message
import ex1
import keyboards
from ex1.statesform import StepsForm


async def get_fio(message: Message, state: FSMContext):
    await state.update_data({"fio": message.text})
    await message.answer("Понравился ли вам День открытых дверей?")
    await state.set_state(ex1.statesform.StepsForm.GET_OPI)

async def get_opi(message: Message, state: FSMContext):
    await state.update_data({"opi": message.text})
    await message.answer(f'Что больше всего вам понравилось в этом мероприятии?')
    await state.set_state(ex1.statesform.StepsForm.GET_BEST)


async def get_best(message: Message, state: FSMContext):
    await state.update_data({"best": message.text})
    await message.answer(f'Что вам не понравилось в проведении Дня открытых Дверей?')
    await state.set_state(ex1.statesform.StepsForm.GET_NONRAV)


async def get_nonnrav(message: Message, state: FSMContext):
    await state.update_data({"nonrav": message.text})
    await message.answer(f'Что по вашему мнению нужно поменять в проведении Дня открытых дверей?')
    await state.set_state(ex1.statesform.StepsForm.GET_END)

async def get_end(message: Message, state: FSMContext, bot):
    context_data = await state.get_data()
    fio = context_data.get('fio')
    opi = context_data.get('opi')
    best = context_data.get('best')
    nonrav = context_data.get('nonrav')
    data_user = f'Вот ваши ответы\r\n' \
                f'1){fio}\n' \
                f'2){opi}\n' \
                f'3){best}\n' \
                f'4){nonrav}\n' \
                f'5){message.text}'
    await message.answer(data_user)
    await bot.send_message(chat_id=511800914, text=f"Новая форма:\n{data_user}")
    await state.clear()
    await message.answer('Если вы где-то допустили ошибку, то вы можете пройти его еще раз!', reply_markup=keyboards.reset_kb)
