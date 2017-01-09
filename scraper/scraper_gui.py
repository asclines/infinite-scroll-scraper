import tkinter as tk
from tkinter import filedialog

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
                    font = FONT).grid(row = 0, column = 1)

urlButton = tk.Button(window,
                      text = "Check URL",
                      highlightbackground = COLOR).grid(row = 0, column = 2)


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
scrapeButton = tk.Button(window,
                         text = "Scrape",
                         highlightbackground = COLOR,
                         font = FONT).grid(row = 3, column = 1)


#Run the program
window.mainloop()