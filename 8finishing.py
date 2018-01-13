import sys
import time
import threading
import random
import telepot
from telepot.loop import MessageLoop
from telepot.namedtuple import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, ForceReply
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton
from telepot.namedtuple import InlineQueryResultArticle, InlineQueryResultPhoto, InputTextMessageContent
import lampu,terminal
import gpiostatus
from time import strftime
import locale

"""
Deskripsi spesifikasi versi tahap 8 finishing (8finishing.py):
- Inline Keyboard muncul otomatis saat pengguna menambahkan akun bot (klik start/restart bot)
- Otorisasi ID user untuk pengguna dan deteksi ID user tidak dikenal
"""


message_with_inline_keyboard = None

#Deklarasi variabel global dari library lampu.py dan terminal.py
global pin_lampu, pin_terminal
pin_lampu    = lampu.pin_lampu
pin_terminal = terminal.pin_terminal

#Set waktu lokal ke Bahasa Indonesia (id_ID.utf-8) untuk format waktu strftime
locale.setlocale(locale.LC_ALL, 'id_ID.utf8')

#Inisialisasi catat_waktu
catat_waktu = ['catat_waktu1', 'catat_waktu2', 'catat_waktu3', 'catat_waktu4', 'catat_waktu5']

#Pengenalan kepemilikan ID user
id_user = {223107165: 'Ayah', 239526959: 'Mamah', 148554570: 'Isal', 212030160: 'Ede', 460358488: 'Calon Mantu'}

#Inisialisasi oleh (siapa 'pengguna' untuk 'perangkat ke-'). Versi dinamis dari catat_waktu
oleh = []
for i in range(1,6):
    oleh.append('pengguna%s' %i)

def on_chat_message(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print('Tipe konten: ', content_type, 'Tipe chat: ', chat_type, 'ID chat (user): ', chat_id)

    if content_type != 'text':
        return

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

    if from_id in id_user:
        if data == 'kos_lampu_luar':
            if gpiostatus.status_kos_lampu_luar() == 'mati':
                lampu.lampu_on(pin_lampu[0])
                status1_on = 'Kos Lampu Luar DINYALAKAN'
                bot.answerCallbackQuery(query_id, text=status1_on, show_alert=True)
                catat_waktu[0] = strftime('%A, %d %B %Y, pukul %X (%Z)')
                oleh[0] = id_user[from_id]
            elif gpiostatus.status_kos_lampu_luar() == 'menyala':
                lampu.lampu_off(pin_lampu[0])
                status1_off = 'Kos Lampu Luar DIMATIKAN'
                bot.answerCallbackQuery(query_id, text=status1_off, show_alert=True)
                catat_waktu[0] = strftime('%A, %d %B %Y, pukul %X (%Z)')
                oleh[0] = id_user[from_id]
        elif data == 'kos_lampu_dalam_cewek':
            if gpiostatus.status_kos_lampu_dalam_cewek() == 'mati':
                lampu.lampu_on(pin_lampu[1])
                status2_on = 'Kos Lampu Dalam Cewek DINYALAKAN'
                bot.answerCallbackQuery(query_id, text=status2_on, show_alert=True)
                catat_waktu[1] = strftime('%A, %d %B %Y, pukul %X (%Z)')
                oleh[1] = id_user[from_id]
            elif gpiostatus.status_kos_lampu_dalam_cewek() == 'menyala':
                lampu.lampu_off(pin_lampu[1])
                status2_off = 'Kos Lampu Dalam Cewek DIMATIKAN'
                bot.answerCallbackQuery(query_id, text=status2_off, show_alert=True)
                catat_waktu[1] = strftime('%A, %d %B %Y, pukul %X (%Z)')
                oleh[1] = id_user[from_id]
        elif data == 'kos_lampu_dalam_cowok':
            if gpiostatus.status_kos_lampu_dalam_cowok() == 'mati':
                lampu.lampu_on(pin_lampu[2])
                status3_on = 'Kos Lampu Dalam Cowok DINYALAKAN'
                bot.answerCallbackQuery(query_id, text=status3_on, show_alert=True)
                catat_waktu[2] = strftime('%A, %d %B %Y, pukul %X (%Z)')
                oleh[2] = id_user[from_id]
            elif gpiostatus.status_kos_lampu_dalam_cowok() == 'menyala':
                lampu.lampu_off(pin_lampu[2])
                status3_off = 'Kos Lampu Dalam Cowok DIMATIKAN'
                bot.answerCallbackQuery(query_id, text=status3_off, show_alert=True)
                catat_waktu[2] = strftime('%A, %d %B %Y, pukul %X (%Z)')
                oleh[2] = id_user[from_id]
        elif data == 'dispenser_cewek':
            if gpiostatus.status_dispenser_cewek() == 'mati':
                terminal.terminal_on(pin_terminal[0])
                status4_on = 'Dispenser Cewek DINYALAKAN'
                bot.answerCallbackQuery(query_id, text=status4_on, show_alert=True)
                catat_waktu[3] = strftime('%A, %d %B %Y, pukul %X (%Z)')
                oleh[3] = id_user[from_id]
            elif gpiostatus.status_dispenser_cewek() == 'menyala':
                terminal.terminal_off(pin_terminal[0])
                status4_off = 'Dispenser Cewek DIMATIKAN'
                bot.answerCallbackQuery(query_id, text=status4_off, show_alert=True)
                catat_waktu[3] = strftime('%A, %d %B %Y, pukul %X (%Z)')
                oleh[3] = id_user[from_id]
        elif data == 'dispenser_cowok':
            if gpiostatus.status_dispenser_cowok() == 'mati':
                terminal.terminal_on(pin_terminal[1])
                status5_on = 'Dispenser Cowok DINYALAKAN'
                bot.answerCallbackQuery(query_id, text=status5_on, show_alert=True)
                catat_waktu[4] = strftime('%A, %d %B %Y, pukul %X (%Z)')
                oleh[4] = id_user[from_id]
            elif gpiostatus.status_dispenser_cowok() == 'menyala':
                terminal.terminal_off(pin_terminal[1])
                status5_off = 'Dispenser Cowok DIMATIKAN'
                bot.answerCallbackQuery(query_id, text=status5_off, show_alert=True)
                catat_waktu[4] = strftime('%A, %d %B %Y, pukul %X (%Z)')
                oleh[4] = id_user[from_id]
        elif data == 'status':
            bot.answerCallbackQuery(query_id, text='Status kondisi perangkat listrik saat ini:\n\n'
            '1. Kos Lampu Luar ' + gpiostatus.status_kos_lampu_luar().upper() + '\n'
            '2. Kos Lampu Dalam Cewek ' + gpiostatus.status_kos_lampu_dalam_cewek().upper() + '\n'
            '3. Kos Lampu Dalam Cowok ' + gpiostatus.status_kos_lampu_dalam_cowok().upper() + '\n'
            '4. Dispenser Cewek ' + gpiostatus.status_dispenser_cewek().upper() + '\n'
            '5. Dispenser Cowok ' + gpiostatus.status_dispenser_cowok().upper(), show_alert=True)
        elif data == 'status_lengkap':
            kll   = bot.sendMessage(from_id, '1. Kos Lampu Luar ' + gpiostatus.status_kos_lampu_luar().upper() + 
            '\npada ' + catat_waktu[0] + '\noleh '+ oleh[0])
            kldce = bot.sendMessage(from_id, '2. Kos Lampu Dalam Cewek ' + gpiostatus.status_kos_lampu_dalam_cewek().upper() + 
            '\npada ' + catat_waktu[1] + '\noleh ' + oleh[1])
            kldco = bot.sendMessage(from_id, '3. Kos Lampu Dalam Cowok ' + gpiostatus.status_kos_lampu_dalam_cowok().upper() + 
            '\npada ' + catat_waktu[2] + '\noleh ' + oleh[2])
            dice  = bot.sendMessage(from_id, '4. Dispenser Cewek ' + gpiostatus.status_dispenser_cewek().upper() + 
            '\npada ' + catat_waktu[3] + '\noleh ' + oleh[3])
            dico  = bot.sendMessage(from_id, '5. Dispenser Cowok ' + gpiostatus.status_dispenser_cowok().upper() + 
            '\npada ' + catat_waktu[4] + '\noleh ' + oleh[4])
    
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
            
    elif from_id not in id_user:
        bot.sendMessage(from_id, 'Maaf, Anda tidak memilik akses!')
        bot.sendMessage(148554570, 'Admin Isal, ID user tidak dikenal terdeteksi: ' + str(from_id))


TOKEN = '186043755:AAGeHYtpo7l31MlzwBmGO_ZewDahotofOas'

bot = telepot.Bot(TOKEN)

MessageLoop(bot, {'chat': on_chat_message,
                  'callback_query': on_callback_query}).run_as_thread()

print('Listening ...')

# Keep the program running.
while 1:
    time.sleep(10)
