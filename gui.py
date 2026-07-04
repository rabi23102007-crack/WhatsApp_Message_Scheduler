import customtkinter as ctk
from scheduler import send_whatsapp_message
from tkinter import messagebox
from tkcalendar import DateEntry


class WhatsAppSchedulerGUI:

    def __init__(self):

        # Theme
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        # Main Window
        self.app = ctk.CTk()
        self.app.title("WhatsApp Message Scheduler")
        self.app.geometry("1000x650")

        # Heading
        self.heading = ctk.CTkLabel(
            self.app,
            text="📱 WhatsApp Message Scheduler",
            font=("Arial", 28, "bold")
        )
        self.heading.pack(pady=30)

        # Phone Number Label
        self.phone_label = ctk.CTkLabel(
            self.app,
            text="📱 Phone Number",
            font=("Arial", 16)
        )
        self.phone_label.pack(pady=(20, 5))

        # Phone Number Entry
        self.phone_entry = ctk.CTkEntry(
            self.app,
            width=350,
            height=40,
            placeholder_text="+91XXXXXXXXXX"
        )
        self.phone_entry.pack(pady=10)
        # Message Label
        self.message_label = ctk.CTkLabel(
            self.app,
            text="💬 Message",
            font=("Arial", 16)
        )
        self.message_label.pack(pady=(20, 5))

        # Message Textbox
        self.message_box = ctk.CTkTextbox(
            self.app,
            width=500,
            height=150
       )
        self.message_box.pack(pady=10)
        # Date Label
        self.date_label = ctk.CTkLabel(
            self.app,
            text="📅 Date",
            font=("Arial", 16)
        )
        self.date_label.pack(pady=(20, 5))

        # Date Entry
        self.date_entry = DateEntry(
            self.app,
            width=18,
            date_pattern="dd/mm/yyyy",
            font=("Arial",14)
        )
        self.date_entry.pack()

        # Time Label
        self.time_label = ctk.CTkLabel(
            self.app,
            text="⏰ Time",
            font=("Arial", 16)
        )
        self.time_label.pack(pady=(20, 5))

        # Time Frame
        self.time_frame = ctk.CTkFrame(self.app, fg_color="transparent")
        self.time_frame.pack()
        #Hour Combobox
        self.hour_combo = ctk.CTkComboBox(
            self.time_frame,
            values=[f"{i:02d}" for i in range(24)],
            width=80
    
        )
        self.hour_combo.set("00")
        self.hour_combo.pack(side="left", padx=5)

        #colon label
        self.colon_label = ctk.CTkLabel(
            self.time_frame,
            text=":",
            font= ("Arial", 18, "bold")
        )
        self.colon_label.pack(side="left")

        #Minute combobox
        self.minute_combo = ctk.CTkComboBox(
            self.time_frame,
            values=[f"{i:02d}" for i in range(60)],
            width=80
        )
        self.minute_combo.set("00")
        self.minute_combo.pack(side="left", padx=5)

        # Schedule Button
        self.schedule_button = ctk.CTkButton(
            self.app,
            text="📤 Schedule Message",
            command=self.schedule_message
        )
        self.schedule_button.pack(pady=25)
    def schedule_message(self):
        phone = self.phone_entry.get().strip()
        message = self.message_box.get("1.0", "end").strip()
        date = self.date_entry.get()
        hour =int(self.hour_combo.get())
        minute = int(self.minute_combo.get())
        time = f"{hour:02d}:{minute:02d}"

    # Validation
        
    #phone number validation
        if not phone.startswith("+91"):
            messagebox.showerror(
                "Invalid Number",
                "Phone number must start with +91."
            )
            return
        
        if len(phone) !=13:
            messagebox.showerror(
                "Invalid Number",
                "Phone number must contain 10 digits after +91."

            )
            return
        
        if not phone [3:].isdigit():
            messagebox.showerror(
                "Invalid Number",
                "Phone number should contain only digits after +91."
            )
            return
        if  not message :
           messagebox.showerror("Error", "Please enter message.")
           return

        if date == "":
           messagebox.showerror("Error", "Please enter date.")
           return

        

        print("Phone :", phone)
        print("Message :", message)
        print("Date :", date)
        print("Time :", time)

    # Time ko Hour aur Minute me convert karo
        
    # WhatsApp Message Send
        send_whatsapp_message(phone, message, hour, minute)

    # Success Popup
        messagebox.showinfo("Success", "Message Scheduled Successfully!")

    
    

    def run(self):
        self.app.mainloop()