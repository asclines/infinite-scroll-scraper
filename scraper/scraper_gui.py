import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from scraper import *
import os
import utils.urls as URLS

#Colors, fonts etc...
COLOR = "#EAECEE"
FONT = "Arial 14"

#Create the main window
window = tk.Tk()
window.geometry("550x125")
window.title("Infinite Scroll Scraper")
window.configure(background = COLOR)

#----------URL label and entry----------#
urlLabel = tk.Label(window,
                    text = "URL to be scraped:",
                    font = FONT,
                    bg = COLOR).grid(row = 0, column = 0)

urlEntry = tk.Entry(window,
                    highlightbackground = COLOR,
                    font = FONT)
urlEntry.grid(row = 0, column = 1)

#checkURL(url) checks the users url validity if check button is pressed.
# def checkURL(url):
#     urlBool = URLS.is_url_valid(url)
#     if urlBool:
#         tkMessageBox.showinfo("","Valid URL").pack()
#     else:
#         tkMessageBox.showerror("ERROR", "Invalid URL").pack()
#     return None

urlButton = tk.Button(window,
                      text = "Check URL",
                      highlightbackground = COLOR,
                      command = lambda: url = urlEntry.get()).grid(row = 0, column = 2)

#----------pages label and entry----------#
pagesLabel = tk.Label(window,
                      text = "Number of times to page down: ",
                      font = FONT,
                      bg = COLOR).grid(row = 1, column = 0)

pagesEntry = tk.Entry(window,
                      highlightbackground = COLOR,
                      font = FONT)
pagesEntry.grid(row = 1, column = 1)

#-----------saveLocation label and entry and button to access directory-------

saveLocationLabel = tk.Label(window,
                             text = "Save location:",
                             font = FONT,
                             bg = COLOR).grid(row = 2, column = 0)

#Seperate initialization of object and inserting it to maintain variable type
saveLocationEntry = tk.Entry(window,
                             highlightbackground = COLOR,
                             font = FONT)
saveLocationEntry.grid(row = 2, column = 1)

#function for saveLocationButton; pulls up folder directory
def findDirectory():
    file_path = filedialog.askdirectory()
    saveLocationEntry.delete(0, tk.END)
    saveLocationEntry.insert(0, str(file_path))
    return None

saveLocationButton = tk.Button(window,
                               text = 'Folder',
                               highlightbackground = COLOR,
                               command = lambda: findDirectory()).grid(row = 2, column = 2)

#----------Final button to execute program----------#
# Determine if all user data is valid before executing
def check(url,pages,folder):
    urlBool = URLS.is_url_valid(url)
    pagesBool = pages.isdigit()
    folderBool = os.path.isdir(folder)
    if urlBool and pagesBool and folderBool:
        return True
    else:
        return False

# scrapeCall(url,pages,folder) creates an object from Data class with all
# necessary data and passest to scraper(args)
class Data:
    def __init__(self,url,pages,folder):
        self.url = url
        self.pages = pages
        self.folder = folder

def scrapeCall(url,pages,folder):
    pages = int(pages)
    data = Data(url,pages,folder)
    return data

#Function that passes proper object to scraper with valid inputs
def execute():
    url = urlEntry.get()
    pages = pagesEntry.get()
    folder = saveLocationEntry.get()
    if check(url,pages,folder):
        scrapeCall(url,pages,folder)
    else:
        print("ERROR")

scrapeButton = tk.Button(window,
                         text = "Scrape",
                         highlightbackground = COLOR,
                         font = FONT,
                         command = lambda: execute()).grid(row = 3, column = 1)

#Run the program
window.mainloop()
