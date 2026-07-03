import pywhatkit


def send_whatsapp_message(phone, message, hour, minute):
    pywhatkit.sendwhatmsg(
        phone,
        message,
        hour,
        minute,
        wait_time=30,
        tab_close=False,
        
    )