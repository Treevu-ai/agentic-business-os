import telebot
from telebot import types
import os
import html

# Tu token proporcionado
TOKEN = '8770043938:AAHnBzfuKV6TTzHlI6vfJCFus2ZTOxE7Cu0'
bot = telebot.TeleBot(TOKEN)

# Diccionario para almacenar temporalmente los datos de los usuarios
user_data = {}

def log_lead(chat_id, data):
    """Guarda los leads en un archivo local para seguimiento posterior (Nurturing)"""
    import json
    try:
        leads = {}
        if os.path.exists('leads_log.json'):
            with open('leads_log.json', 'r', encoding='utf-8') as f:
                leads = json.load(f)
        
        leads[str(chat_id)] = {
            **data,
            "last_active": str(message_date())
        }
        
        with open('leads_log.json', 'w', encoding='utf-8') as f:
            json.dump(leads, f, indent=2, ensure_ascii=False)
    except Exception as e:
        print(f"Error en log_lead: {e}")

def message_date():
    from datetime import datetime
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    chat_id = message.chat.id
    user_data[chat_id] = {}
    
    # Crear Teclado Inline
    markup = types.InlineKeyboardMarkup(row_width=1)
    btn_workshop = types.InlineKeyboardButton("🎓 Taller IA (S/ 387 / $97 USD)", callback_data="flow_workshop")
    btn_triage = types.InlineKeyboardButton("🔍 Diagnóstico Gratis (45 min)", callback_data="flow_triage")
    markup.add(btn_workshop, btn_triage)
    
    welcome_text = (
        "🖥️ <b>SINAPSIS_OS // Business Automation</b>\n\n"
        "Bienvenido al Centro de Control. Soy tu asistente de configuración.\n\n"
        "¿Cómo deseas proceder hoy?"
    )
    
    # Si viene con parámetro workshop por URL
    if 'workshop' in message.text.lower():
        start_workshop_flow(chat_id)
    else:
        bot.send_message(chat_id, welcome_text, parse_mode="HTML", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data.startswith('flow_'))
def handle_flow_choice(call):
    chat_id = call.message.chat.id
    if call.data == "flow_workshop":
        start_workshop_flow(chat_id)
    elif call.data == "flow_triage":
        start_triage_flow(chat_id)

def start_workshop_flow(chat_id):
    user_data[chat_id]['flow'] = 'workshop'
    log_lead(chat_id, {"flow": "workshop", "status": "started", "date": message_date()})
    
    welcome_workshop = (
        "🚀 <b>SINAPSIS_OS // Workshop Registration</b>\n\n"
        "Excelente decisión. Vamos a rediseñar tu negocio con Agentes de IA.\n\n"
        "⚠️ <b>AVISO:</b> Solo <b>20 cupos</b> por edición para garantizar soporte real.\n\n"
        "<b>¿Podrías indicarme tu nombre completo?</b>"
    )
    msg = bot.send_message(chat_id, welcome_workshop, parse_mode="HTML")
    bot.register_next_step_handler(msg, process_workshop_name)

def start_triage_flow(chat_id):
    user_data[chat_id]['flow'] = 'triage'
    welcome_triage = (
        "🔍 <b>SINAPSIS_OS // Diagnóstico</b>\n\n"
        "Vamos a evaluar el ROI de automatizar tu operación.\n\n"
        "<b>¿Cuál es tu nombre, cargo y web de tu empresa?</b>"
    )
    msg = bot.send_message(chat_id, welcome_triage, parse_mode="HTML")
    bot.register_next_step_handler(msg, process_context_step)

# --- FLUJO DE WORKSHOP ---

def process_workshop_name(message):
    chat_id = message.chat.id
    user_data[chat_id]['nombre'] = html.escape(message.text)
    
    msg = bot.send_message(chat_id, f"<b>Gracias, {user_data[chat_id]['nombre']}.</b>\n\n¿A qué <b>email</b> enviamos el material y el link de Zoom?", parse_mode="HTML")
    bot.register_next_step_handler(msg, process_workshop_email)

def process_workshop_email(message):
    chat_id = message.chat.id
    user_data[chat_id]['email'] = html.escape(message.text)
    
    markup = types.InlineKeyboardMarkup()
    btn_paid = types.InlineKeyboardButton("✅ YA REALICÉ EL PAGO", callback_data="workshop_paid")
    markup.add(btn_paid)
    
    instrucciones = (
        "💳 <b>INSTRUCCIONES DE PAGO - S/ 387.00 / $97.00 USD</b>\n\n"
        "Reserva tu lugar (Solo quedan 20 vacantes):\n\n"
        "🔸 <b>Yape / Plin:</b> +51 902 126 765 (Ricardo Cuba)\n"
        "🔸 <b>BCP:</b> 570-099912325-0-93\n"
        "🔸 <b>PayPal:</b> contact@gettreevu.com\n\n"
        "📌 <b>PASO FINAL:</b> Una vez pagado, pulsa el botón de abajo y adjunta tu comprobante."
    )
    bot.send_message(chat_id, instrucciones, parse_mode="HTML", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == "workshop_paid")
def handle_payment_click(call):
    chat_id = call.message.chat.id
    msg = bot.send_message(chat_id, "🎯 ¡Perfecto! Por favor, <b>envía la captura de pantalla o PDF</b> del comprobante ahora.")
    bot.register_next_step_handler(msg, process_workshop_payment)

def process_workshop_payment(message):
    chat_id = message.chat.id
    if message.content_type in ['photo', 'document']:
        confirmacion_text = (
            "🎉 <b>¡BIENVENIDO, " + user_data[chat_id].get('nombre', 'Estratega') + "!</b>\n\n"
            "Tu cupo está <b>oficialmente reservado</b>.\n\n"
            "📅 <b>Fecha:</b> 15 de Abril | 09:00 AM (PE)\n"
            "🔗 <b>Zoom:</b> <a href='https://zoom.us/j/1234567890'>Link de la Sala</a>\n\n"
            "📥 <b>ACTIVOS METODOLÓGICOS (3):</b>\n"
            "Descarga estos archivos ahora mismo para empezar el workshop con ventaja:"
        )
        bot.send_message(chat_id, confirmacion_text, parse_mode="HTML")
        log_lead(chat_id, {**user_data[chat_id], "status": "paid", "date": message_date()})
        
        try:
            # Enviar los 3 activos
            assets_dir = os.path.join('backend', 'assets')
            files = [
                ('Agentic_Canvas_Sinapsis.txt.md', "🧬 Agentic Canvas - Guía de Mapeo"),
                ('Claude_System_Prompt.txt', "🧠 Claude System Prompt Maestro"),
                ('sinapsis_os_metodologias_taller.html', "📜 Guía Metodológica Sinapsis")
            ]
            
            for fname, caption in files:
                with open(os.path.join(assets_dir, fname), 'rb') as doc:
                    bot.send_document(chat_id, doc, caption=caption)
                
        except Exception as e:
            print(f"Error enviando activos: {e}")
            bot.send_message(chat_id, "⚠️ Error al enviar archivos. Contacta a @rcuba para soporte directo.")
    else:
        msg = bot.send_message(chat_id, "⚠️ Por favor, adjunta una foto o archivo para validar el pago.")
        bot.register_next_step_handler(msg, process_workshop_payment)

# --- FLUJO DE TRIAGE ---

def process_context_step(message):
    chat_id = message.chat.id
    user_data[chat_id]['contexto'] = html.escape(message.text)
    msg = bot.send_message(chat_id, "<b>2. Entendido.</b>\n\n¿Cuál es el proceso manual que <b>más dinero/tiempo</b> le quita a tu equipo hoy?", parse_mode="HTML")
    bot.register_next_step_handler(msg, process_pain_step)

def process_pain_step(message):
    chat_id = message.chat.id
    user_data[chat_id]['dolor'] = html.escape(message.text)
    msg = bot.send_message(chat_id, "<b>3. Último paso.</b>\n\n¿A qué <b>email</b> enviamos tu Blueprint de Automatización?", parse_mode="HTML")
    bot.register_next_step_handler(msg, process_email_step)

def process_email_step(message):
    chat_id = message.chat.id
    user_data[chat_id]['email'] = html.escape(message.text)
    data = user_data[chat_id]
    
    resumen = (
        "✅ <b>DIAGNÓSTICO REGISTRADO</b>\n\n"
        f"📧 Enviado a: {data['email']}\n\n"
        "⚡ <b>FAST-TRACK:</b> Mientras analizamos tu caso, puedes agendar una sesión 1-a-1 aquí:\n"
        "👉 <a href='https://calendar.app.google/uStyE1Mys3Qcievz5'>Google Calendar Sinapsis</a>"
    )
    bot.send_message(chat_id, resumen, parse_mode="HTML", disable_web_page_preview=True)
    log_lead(chat_id, {**data, "status": "completed", "date": message_date()})

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, "Por favor, usa el comando /start para iniciar el proceso de registro.")

if __name__ == '__main__':
    print("Iniciando Bot Inline Sinapsis OS...")
    bot.infinity_polling()
