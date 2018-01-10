import sys
import time
import threading
import random
import telepot
from telepot.loop import MessageLoop
from telepot.namedtuple import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, ForceReply
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton
from telepot.namedtuple import InlineQueryResultArticle, InlineQueryResultPhoto, InputTextMessageContent

"""
Deskripsi spesifikasi versi utama_tahap1.py:
- Pembentukan tombol menu (UI) menggunakan inline keyboard
- Menu terdiri dari:
      - Kos Lampu Luar
      - Kos Lampu Dalam Cewek
      - Kos Lampu Dalam Cowok
      - Dispenser Cewek
      - Dispenser Cowok
      - Status
      - Status Lengkap
- Semua menu sudah diberikan aksi berupa alert kecuali Status Lengkap
- Status Lengkap direncanakan akan menggunakan aksi update message on the fly pada tahap2
- Di sini update message sudah bisa dilakukan tapi semua tombol menu jadi hilang,
  diharapkan pada tahap2 bisa dimunculkan tomobl menu baru ketika diberikan aksi update message
- Data mati, nyala, dan status perangkat hanyalah data dummy (karena fokus pada pembentukan UI)
"""


message_with_inline_keyboard = None

def on_chat_message(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print('Tipe konten: ', content_type, 'Tipe chat: ', chat_type, 'ID chat (user): ', chat_id)

    if content_type != 'text':
        return

    command = msg['text'][-1:].lower()

    if command == 'i':
        markup = InlineKeyboardMarkup(inline_keyboard=[
                     [dict(text='Kos Lampu Luar', callback_data='kos_lampu_luar')],
                     [InlineKeyboardButton(text='Kos Lampu Dalam Cewek', callback_data='kos_lampu_dalam_cewek')],
                     [InlineKeyboardButton(text='Kos Lampu Dalam Cowok', callback_data='kos_lampu_dalam_cowok')],
                     [dict(text='Dispenser Cewek', callback_data='dispenser_cewek')],
                     [dict(text='Dispenser Cowok', callback_data='dispenser_cowok')],
                     [InlineKeyboardButton(text='Status', callback_data='status'), InlineKeyboardButton(text='Status Lengkap', callback_data='status_lengkap')],
                 ])

        global message_with_inline_keyboard
        message_with_inline_keyboard = bot.sendMessage(chat_id, 'Klik menu di bawah untuk mematikan atau menyalakan perangkat!', reply_markup=markup)

def on_callback_query(msg):
    query_id, from_id, data = telepot.glance(msg, flavor='callback_query')
    print('Callback query --> ', 'ID query: ', query_id, 'ID user: ', from_id, 'Callback data: ', data)

    if data == 'kos_lampu_luar':
        bot.answerCallbackQuery(query_id, text='Kos Lampu Luar DIMATIKAN', show_alert=True)
    elif data == 'kos_lampu_dalam_cewek':
        bot.answerCallbackQuery(query_id, text='Kos Lampu Dalam Cewek DINYALAKAN', show_alert=True)
    elif data == 'kos_lampu_dalam_cowok':
        bot.answerCallbackQuery(query_id, text='Kos Lampu Dalam Cowok DIMATIKAN', show_alert=True)
    elif data == 'dispenser_cewek':
        bot.answerCallbackQuery(query_id, text='Dispenser Cewek DINYALAKAN', show_alert=True)
    elif data == 'dispenser_cowok':
        bot.answerCallbackQuery(query_id, text='Dispenser Cowok DIMATIKAN', show_alert=True)
    elif data == 'status':
        global message_with_inline_keyboard

        if message_with_inline_keyboard:
            msg_idf = telepot.message_identifier(message_with_inline_keyboard)
            bot.editMessageText(msg_idf, 'Status kondisi perangkat listrik saat ini -->')
            
        else:
            bot.answerCallbackQuery(query_id, text='Status kondisi perangkat listrik saat ini:\n\n'
            '1. Kos Lampu Luar MATI\n'
            '2. Kos Lampu Dalam Cewek MENYALA\n'
            '3. Kos Lampu Dalam Cowok MATI\n'
            '4. Dispenser Cewek MENYALA\n'
            '5. Dispenser Cowok MATI', show_alert=True)



TOKEN = '186043755:AAGeHYtpo7l31MlzwBmGO_ZewDahotofOas'

bot = telepot.Bot(TOKEN)

MessageLoop(bot, {'chat': on_chat_message,
                  'callback_query': on_callback_query}).run_as_thread()

print('Listening ...')

# Keep the program running.
while 1:
    time.sleep(10)
