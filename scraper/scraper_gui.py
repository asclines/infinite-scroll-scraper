import tkinter as tk

#Create the main window
window = tk.Tk()
window.geometry("500x125")
window.title("Infinite Image Scraper")

#URL label and entry
urlLabel = tk.Label(window,
                    text = "URL to be scraped:",
                    font = "Verdana 14").grid(row = 0, column = 0)

urlEntry = tk.Entry(window).grid(row = 0, column = 1)

#pages label and entry
pagesLabel = tk.Label(window,
                      text = "Number of pages to be scraped: ",
                      font = "Verdana 14").grid(row = 1, column = 0)
pagesEntry = tk.Entry(window).grid(row = 1, column = 1)

#saveLocation label and entry
saveLocationLabel = tk.Label(window,
                             text = "Save location:",
                             font = "Verdana 14").grid(row = 2, column = 0)
saveLocationEntry = tk.Entry(window).grid(row = 2, column = 1)

#Execute button
scrapeButton = tk.Button(window,text = "SCRAPE").grid(row = 3, column = 1)
#Run the program
window.mainloop()
