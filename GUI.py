from tkinter import *
import os
import numpy as np


def test():
    if(username_entry.get() != "" and password_entry.get() != "" and url_entry.get() != "" and shoe_size.get() != ""):
        command = 'py .\main.py --purchase --username %s --password %s --url %s --shoe-size %s' % (
            username_entry.get(), password_entry.get(), url_entry.get(), shoe_size.get())

        #  Determines if bot features where disabled.
        if(login_time_int.get() != 1):
            command += ' --login-time %sh%sm' % (
                login_time_hours.get(), login_time_minutes.get())
        if(release_time_int.get() != 1):
            command += ' --release-time %sh' % (release_time.get())

        if(retries_int.get() != 1):
            command += ' --num-retries %s' % (retries.get())

        if(page_load_int.get() != 1):
            command += ' --page-load-timeout %s' % (page_load_timeout.get())

        if(headless_int.get() != 0):
            command += ' --headless'

        if(no_quit_int.get() != 0):
            command += ' --dont-quit'
        print(command)
        os.system(command)


def logTimeStatus():
    #  Removes widget if disable checkbox is checked
    if(login_time_int.get() == 1):
        login_time_label.grid_remove()
        login_time_hours_dropdown.grid_remove()
        login_time_minutes_dropdown.grid_remove()
    else:
        login_time_label.grid()
        login_time_hours_dropdown.grid()
        login_time_minutes_dropdown.grid()


def releaseTimeStatus():
    if(release_time_int.get() == 1):
        release_time_label.grid_remove()
        release_time_dropdown.grid_remove()
    else:
        release_time_label.grid()
        release_time_dropdown.grid()


def retriesStatus():
    if(retries_int.get() == 1):
        retries_label.grid_remove()
        retries_dropdown.grid_remove()
    else:
        retries_label.grid()
        retries_dropdown.grid()


def pageLoadTimeoutStatus():
    if(page_load_int.get() == 1):
        page_load_timeout_label.grid_remove()
        page_load_timeout_dropdown.grid_remove()
    else:
        page_load_timeout_label.grid()
        page_load_timeout_dropdown.grid()


app = Tk()

# Login Information Label
login_information_label = Label(
    app, text="Login Information", font=('bold', 16))
login_information_label.grid(row=0, column=0, sticky=W, pady=10)

# Username
username_text = StringVar()
username_label = Label(app, text="username *", font=('bold', 10))
username_label.grid(row=1, column=0, sticky=W, padx=25)
username_entry = Entry(app, textvariable=username_text)
username_entry.grid(row=2, column=0, sticky=W, padx=25)

# Password
password_text = StringVar()
password_label = Label(app, text="password *", font=('bold', 10))
password_label.grid(row=1, column=1, sticky=W, padx=25)
password_entry = Entry(app, textvariable=password_text)
password_entry.grid(row=2, column=1, sticky=W, padx=25)

# Shoe Information Label
shoe_information_label = Label(app, text="Shoe Information", font=('bold', 16))
shoe_information_label.grid(row=3, column=0, sticky=W, pady=10)

# Url
url_text = StringVar()
url_label = Label(app, text="url *", font=('bold', 10))
url_label.grid(row=4, column=0, sticky=W, padx=25)
url_entry = Entry(app, textvariable=url_text)
url_entry.grid(row=5, column=0, sticky=W, padx=25)

# Show size
shoe_size_text = StringVar()
shoe_size_label = Label(app, text="shoe size (Men)*", font=('bold', 10))
shoe_size_label.grid(row=4, column=1, sticky=W, padx=25)
OptionList = [8, 8.5, 9, 9.5, 10, 10.5, 11, 11.5, 12, 13, 14, 15]
shoe_size = StringVar()
shoe_size.set(OptionList[0])
shoe_size_dropdown = OptionMenu(app, shoe_size, *OptionList)
shoe_size_dropdown.config(width=15, font=('Helvetica', 10))
shoe_size_dropdown.grid(row=5, column=1, sticky=W, padx=25)

# Bot Settings Label
bot_settings_label = Label(
    app, text="Bot Settings", font=('bold', 16))
bot_settings_label.grid(row=6, column=0, sticky=W, )

# Disable lable
bot_settings_label = Label(
    app, text="Check box to disable feature", font=('Helvetica', 8))
bot_settings_label.grid(row=7, column=0, sticky=W, padx=25)

# Login Time Status
login_time_int = IntVar()
login_time_int_checkbox = Checkbutton(
    app, text="Login Time", variable=login_time_int, command=logTimeStatus)
login_time_int_checkbox.grid(row=8, column=0, sticky=W, padx=25)

# Release Time Status
release_time_int = IntVar()
release_time_int_checkbox = Checkbutton(
    app, text="Release Time", variable=release_time_int, command=releaseTimeStatus)
release_time_int_checkbox.grid(row=8, column=0, sticky=E, padx=25)

# Retrie Status
retries_int = IntVar()
retries_int_checkbox = Checkbutton(
    app, text="Retries", variable=retries_int, command=retriesStatus)
retries_int_checkbox.grid(row=8, column=1, sticky=W, padx=25)

# Page Load Status
page_load_int = IntVar()
page_load_int_checkbox = Checkbutton(
    app, text="Page Load", variable=page_load_int, command=pageLoadTimeoutStatus)
page_load_int_checkbox.grid(row=8, column=1, sticky=E, padx=25)

# Log in time
login_time_label = Label(
    app, text="Login Time (Military Time HH:MM)", font=('bold', 10))
login_time_label.grid(row=9, column=0, sticky=W, padx=25)
HoursList = np.arange(24)
login_time_hours = StringVar()
login_time_hours.set(HoursList[9])
login_time_hours_dropdown = OptionMenu(app, login_time_hours, *HoursList)
login_time_hours_dropdown.config(width=3, font=('Helvetica', 10))
login_time_hours_dropdown.grid(row=10, column=0, sticky=W, padx=25)

MinutesList = np.arange(60)
login_time_minutes = StringVar()
login_time_minutes.set(MinutesList[59])
login_time_minutes_dropdown = OptionMenu(
    app, login_time_minutes, *MinutesList)
login_time_minutes_dropdown.config(width=3, font=('Helvetica', 10))
login_time_minutes_dropdown.grid(row=10, column=0,  padx=25)

# Release Time
release_time_label = Label(
    app, text="Release Time (Military Time)", font=('bold', 10))
release_time_label.grid(row=9, column=1, sticky=W, padx=25)
HoursList = np.arange(24)
release_time = StringVar()
release_time.set(HoursList[10])
release_time_dropdown = OptionMenu(
    app, release_time, *HoursList)
release_time_dropdown.config(width=15, font=('Helvetica', 10))
release_time_dropdown.grid(row=10, column=1, sticky=W, padx=25)

# Web Driver
DriverList = ["firefox", "chrome"]
driver_label = Label(
    app, text="Web Driver", font=('bold', 10))
driver_label.grid(row=11, column=0, sticky=W, padx=25)
driver = StringVar()
driver.set(DriverList[0])
driver_dropdown = OptionMenu(app, driver, *DriverList)
driver_dropdown.config(width=15, font=('Helvetica', 10))
driver_dropdown.grid(row=12, column=0, sticky=W, padx=25)

# Retries
RetriesSecondsList = [1, 2, 3, 4, 5]
retries_label = Label(
    app, text="Number of Retries", font=('bold', 10))
retries_label.grid(row=11, column=1, sticky=W, padx=25)
retries = StringVar()
retries.set(RetriesSecondsList[0])
retries_dropdown = OptionMenu(app, retries, *RetriesSecondsList)
retries_dropdown.config(width=15, font=('Helvetica', 10))
retries_dropdown.grid(row=12, column=1, sticky=W, padx=25)

# Page Load Timeout
PageLoadTimeoutSecondsList = [1, 2, 3]
page_load_timeout_label = Label(
    app, text="Page Load Timeout", font=('bold', 10))
page_load_timeout_label.grid(row=13, column=0, sticky=W, padx=25)
page_load_timeout = StringVar()
page_load_timeout.set(PageLoadTimeoutSecondsList[0])
page_load_timeout_dropdown = OptionMenu(
    app, page_load_timeout, *PageLoadTimeoutSecondsList)
page_load_timeout_dropdown.config(width=15, font=('Helvetica', 10))
page_load_timeout_dropdown.grid(row=14, column=0, sticky=W, padx=25)

# Headless
headless_int = IntVar()
headless_checkbox = Checkbutton(app, text="Headless", variable=headless_int)
headless_checkbox.grid(row=15, sticky=W, padx=25)

# No Quit
no_quit_int = IntVar()
no_quit_checkbox = Checkbutton(
    app, text="Dont Quit After Purchase", variable=no_quit_int)
no_quit_checkbox.grid(row=16, sticky=W, padx=25)

# Start Script
btn = Button(app, text='Start', width=12, command=test)
btn.grid(row=17, column=0, sticky=W, padx=25)

app.title('Sneaker Bot')
app.rowconfigure(17, {'minsize': 30})
app.columnconfigure(17, {'minsize': 30})

# Start program
app.mainloop()
