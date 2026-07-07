import pywhatkit


def send_whatsapp_message(phone, message, hour, minute):
    try:
        pywhatkit.sendwhatmsg(
            phone,
            message,
            hour,
            minute,
            wait_time=30,
            tab_close=False
        )
        return True

    except Exception as e:
        print("Error:", e)
        return False