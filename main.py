from gui import WhatsAppSchedulerGUI
from database import create_database

# Create Database
create_database()

# Start GUI
app = WhatsAppSchedulerGUI()
app.run()