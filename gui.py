import os
import sys
import customtkinter as ctk
from tkinter import messagebox
from tkcalendar import DateEntry

from scheduler import send_whatsapp_message
from database import (
    save_message,
    get_all_messages,
    update_status,
    delete_message,
    edit_message,
)

class WhatsAppSchedulerGUI:

    def __init__(self):

        # Theme
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        # Main Window
        self.app = ctk.CTk()
        self.app.title("WhatsApp Message Scheduler")
        self.app.geometry("1000x900")
        if getattr(sys, "frozen", False):
            base_path = sys._MEIPASS
        else:
            base_path = os.path.abspath(".")

        icon_path = os.path.join(base_path, "assets", "icon.ico")
        self.app.iconbitmap(icon_path)
        
        self.app.resizable(False, False)

        # Heading
        self.heading = ctk.CTkLabel(
            self.app,
            text="📱 WhatsApp Message Scheduler",
            font=("Segoe UI", 34, "bold"),
            text_color="#00BFFF"
        )
        self.heading.pack(pady=(25, 15))

        # Phone Number
        self.phone_label = ctk.CTkLabel(
            self.app,
            text="📱 Phone Number",
            font=("Arial", 16)
        )
        self.phone_label.pack(pady=(20, 5))

        self.phone_entry = ctk.CTkEntry(
            self.app,
            width=420,
            height=45,
            placeholder_text="+91XXXXXXXXXX",
            corner_radius=10,
            font=("Segoe UI", 15 )
        )
        self.phone_entry.pack(pady=10)

        # Message
        self.message_label = ctk.CTkLabel(
            self.app,
            text="💬 Message",
            font=("Arial", 16)
        )
        self.message_label.pack(pady=(20, 5))

        self.message_box = ctk.CTkTextbox(
            self.app,
            width=600,
            height=170,
            corner_radius=10,
            font=("segoe UI", 15)
        )
        self.message_box.pack(pady=10)

        # Date
        self.date_label = ctk.CTkLabel(
            self.app,
            text="📅 Date",
            font=("Arial", 16)
        )
        self.date_label.pack(pady=(20, 5))

        self.date_entry = DateEntry(
            self.app,
            width=18,
            date_pattern="dd/mm/yyyy",
            font=("Segoe UI", 13)
        )
        self.date_entry.pack()

        # Time
        self.time_label = ctk.CTkLabel(
            self.app,
            text="⏰ Time",
            width=90,
            font=("Segoe UI", 14)
        )
        self.time_label.pack(pady=(20, 5))

        self.time_frame = ctk.CTkFrame(
            self.app,
            fg_color="transparent"
        )
        self.time_frame.pack()

        # Hour
        self.hour_combo = ctk.CTkComboBox(
            self.time_frame,
            values=[f"{i:02d}" for i in range(24)],
            width=80
        )
        self.hour_combo.set("00")
        self.hour_combo.pack(side="left", padx=5)

        # Colon
        self.colon_label = ctk.CTkLabel(
            self.time_frame,
            text=":",
            font=("Segoe UI", 18, "bold")
        )
        self.colon_label.pack(side="left" , padx=5)

        # Minute
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
    command=self.schedule_message,
    width=250,
    height=45,
    font=("Segoe UIF", 16, "bold"),
    fg_color="#1F6AA5",
    hover_color="#144870",
    corner_radius=12
)
        self.schedule_button.pack(pady=20)

        # History Button
        self.history_button = ctk.CTkButton(
    self.app,
    text="📋 View History",
    command=self.show_history,
    width=250,
    height=45,
    font=("Arial", 16, "bold"),
    fg_color="#2E8B57",
    hover_color="#206040",
    corner_radius=12
)
        self.history_button.pack(pady=10)
        # Edit Button
        self.edit_button = ctk.CTkButton(
    self.app,
    text="✏ Edit Message",
    command=self.edit_history,
    width=250,
    height=45,
    font=("Arial", 16, "bold"),
    fg_color="#E67E22",
    hover_color="#B86419",
    corner_radius=12
)
        self.edit_button.pack(pady=10)

#Delete button
        self.delete_button = ctk.CTkButton(
   self.app,
    text="🗑 Delete Message",
    command=self.delete_history,
    width=250,
    height=45,
    font=("Arial", 16, "bold"),
    fg_color="#C0392B",
    hover_color="#922B21",
    corner_radius=12
)    
        self.delete_button.pack(pady=10)
        # Footer
        self.footer = ctk.CTkLabel(
    self.app,
    text="Developed by Rabinarayana Mohanty | Version 1.0",
    font=("Segoe UI", 12),
    text_color="gray"
)
        self.footer.pack(side="bottom", pady=15)


    # ===========================
    # Schedule Message
    # ===========================
    def schedule_message(self):

        phone = self.phone_entry.get().strip()
        message = self.message_box.get("1.0", "end").strip()
        date = self.date_entry.get()

        hour = int(self.hour_combo.get())
        minute = int(self.minute_combo.get())

        time = f"{hour:02d}:{minute:02d}"

        # Phone Validation
        if not phone.startswith("+91"):
            messagebox.showerror(
                "Invalid Number",
                "Phone number must start with +91."
            )
            return

        if len(phone) != 13:
            messagebox.showerror(
                "Invalid Number",
                "Phone number must contain 10 digits after +91."
            )
            return

        if not phone[3:].isdigit():
            messagebox.showerror(
                "Invalid Number",
                "Phone number should contain only digits after +91."
            )
            return

        # Message Validation
        if not message:
            messagebox.showerror(
                "Error",
                "Please enter message."
            )
            return

        # Save in Database
        save_message(
            phone,
            message,
            date,
            time,
            "Scheduled"
        )

        # Send WhatsApp
        success = send_whatsapp_message(phone, message, hour, minute)

        if success:
            update_status(phone, "Sent")
        else:
            update_status(phone, "Failed")

        # Success Message
        if success:
         messagebox.showinfo(
            "Success",
            "Message Scheduled Successfully!"
       )
        else:
         messagebox.showerror(
            "Error",
            "Message could not be scheduled."
      )


        # ===========================
    def show_history(self):

        data = get_all_messages()

        history = ""

        for row in data:
            history += (
                f"ID: {row[0]}\n"
                f"Phone: {row[1]}\n"
                f"Message: {row[2]}\n"
                f"Date: {row[3]}\n"
                f"Time: {row[4]}\n"
                f"Status: {row[5]}\n"
                "--------------------------\n"
            )

        if history == "":
            history = "No messages found."

        messagebox.showinfo(
            "Message History",
            history
        )

    # ===========================
    # Edit Message
    # ===========================
    def edit_history(self):

        dialog = ctk.CTkInputDialog(
            text="Enter Message ID:",
            title="Edit Message"
        )

        message_id = dialog.get_input()

        if message_id is None:
            return

        if not message_id.isdigit():
            messagebox.showerror(
                "Error",
                "Please enter a valid ID."
            )
            return

        dialog2 = ctk.CTkInputDialog(
            text="Enter New Message:",
            title="Edit Message"
        )

        new_message = dialog2.get_input()

        if new_message is None or new_message.strip() == "":
            return

        edit_message(
            int(message_id),
            new_message
        )

        messagebox.showinfo(
            "Success",
            "Message Updated Successfully!"
        )

    # ===========================
    # Delete Message
    # ===========================
    def delete_history(self):

        dialog = ctk.CTkInputDialog(
            text="Enter Message ID to delete:",
            title="Delete Message"
        )

        message_id = dialog.get_input()

        if message_id is None:
            return

        if not message_id.isdigit():
            messagebox.showerror(
                "Error",
                "Please enter a valid ID."
            )
            return

        delete_message(int(message_id))

        messagebox.showinfo(
            "Success",
            "Message Deleted Successfully!"
        )    
   
       
    # ===========================
    # Run App
    # ===========================
    def run(self):
        self.app.mainloop()