# YourCyberTutor - Email Automation
# PyCharm 2021.2.2 (Community Edition)
# Python 3.9.7
import win32com.client
import PySimpleGUI as sg
from datetime import datetime

date = datetime.now().strftime("%m/%d/%Y")

# Function to craft and send the emil
def send_email(value):
    path = str(value)
    print(path)
    outlook = win32com.client.Dispatch('outlook.application')
    mail = outlook.CreateItem(0)
    mail.To = "knowledge@yourcybertutor.com"
    mail.Subject = 'My Daily Email - ' + date
    mail.Body = "Hello Team, Please see the attached for today's Daily Report" \
                "\nExample for a line 2 " \
                "\n\nThank you, " \
                "\nYourCyberTutor"
    mail.Attachments.Add(path)
    mail.Send()
    sg.popup("Sent Email!")

# Creates a gui using PySimpleGui
layout = [[sg.Text("Please select a file to attach")],
          [sg.Text("Attachment", size=(8,1)), sg.Input(do_not_clear=False), sg.FileBrowse()],
          [sg.Button("Send Email"), sg.Quit()]]

window = sg.Window("Sending Email with Attchments", layout)
while True:
    event, value = window.read()
    if event in ('Quit', sg.WIN_CLOSED):
        break
    elif event == ("Send Email"):
        send_email(value[0])

    else:
        window.close
