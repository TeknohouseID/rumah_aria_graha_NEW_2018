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
Deskripsi spesifikasi versi tahap 2 (2utama_tahap.py):
- Status Lengkap sudah diberikan aksi
- Aksi Status Lengkap berupa pengiriman chat seperti biasa, namun akan hilang dalam 15 detik
- Aksi ini diperlukan agar tidak ada chat yang menumpuk sehingga tetap 'neat'
- Awalnya dicoba aksi alert, namun error karena kepanjangan.
- Kemudian aksi editMessageText, update teks pesan on the fly. Namun, dirasa kompleks dan ada error yang sulit diidentifikasi
- Tombol menu tetap standby dan kembali ke posisi semula saat semua pesan Status Lengkap hilang
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
        bot.answerCallbackQuery(query_id, text='Status kondisi perangkat listrik saat ini:\n\n'
        '1. Kos Lampu Luar MATI\n'
        '2. Kos Lampu Dalam Cewek MENYALA\n'
        '3. Kos Lampu Dalam Cowok MATI\n'
        '4. Dispenser Cewek MENYALA\n'
        '5. Dispenser Cowok MATI', show_alert=True)
    elif data == 'status_lengkap':
        kll   = bot.sendMessage(from_id, '1. Kos Lampu Luar\n DIMATIKAN pada Minggu 31 Desember 2017 05:37:00 WIB oleh Ayah')
        kldce = bot.sendMessage(from_id, '2. Kos Lampu Dalam Cewek\n DINYALAKAN pada Minggu 31 Desember 2017 18:10:18 WIB oleh Emah')
        kldco = bot.sendMessage(from_id, '3. Kos Lampu Dalam Cowok\n DIMATIKAN pada Minggu 31 Desember 2017 05:27:33 WIB oleh Isal')
        dice  = bot.sendMessage(from_id, '4. Dispenser Cewek\n DINYALAKAN pada Minggu 31 Desember 2017 17:00:10 WIB oleh Ede')
        dico  = bot.sendMessage(from_id, '5. Dispenser Cowok\n DIMATIKAN pada Minggu 31 Desember 2017 08:27:00 WIB oleh Emah')

        kll_identifier   = telepot.message_identifier(kll)
        kldce_identifier = telepot.message_identifier(kldce)
        kldco_identifier = telepot.message_identifier(kldco)
        dice_identifier  = telepot.message_identifier(dice)
        dico_identifier  = telepot.message_identifier(dico)

        time.sleep(15)

        bot.deleteMessage(kll_identifier)
        bot.deleteMessage(kldce_identifier)
        bot.deleteMessage(kldco_identifier)
        bot.deleteMessage(dice_identifier)
        bot.deleteMessage(dico_identifier)


TOKEN = '186043755:AAGeHYtpo7l31MlzwBmGO_ZewDahotofOas'

bot = telepot.Bot(TOKEN)

MessageLoop(bot, {'chat': on_chat_message,
                  'callback_query': on_callback_query}).run_as_thread()

print('Listening ...')

# Keep the program running.
while 1:
    time.sleep(10)
