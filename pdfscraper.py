#######################################################
#######################################################
############# ###################### ##################
############   ####################   #################
############# ###################### ##################
#######################################################
#######################   #############################
######################## ##############################
#######################################################
############ ######################## #################
############## #################### ###################
#################                ######################
#######################################################
#######################################################
#######################################################
#######################################################

from tkinter import *
import PyPDF2
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfile


root = Tk()



#Header

header = Frame(root, width=600, height=300, bg="white")
header.grid(columnspan=3, rowspan=2, row=0)

#Logo
logo = Image.open('xxxxxxxx/xxxxxxx/xxxxxxxx/xxxxx')
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo)
logo_label.image = logo
logo_label.grid(column=1, row=0)

#Instructions
instructions = tk.Label(root, text="Select a PDF file on your computer to extract its text.")
instructions.grid(columnspan=3, column=1, row=2)

def open_file():
    browse_text.set("loading...")
    file = askopenfile(parent=root, mode='rb', title="Choose a file.", filetype=[("Pdf file", "*.pdf")])
    if file:
        read_pdf = PyPDF2.PdfReader(file)
        page = read_pdf.pages[0]
        page_content = page.extract_text()
        print(page_content)
        
        #text box
        text_box =tk.Text(root, height=10, width=75, padx=15, pady=10)
        text_box.insert(1.0, page_content)
        text_box.tag_configure("center", justify="center")
        text_box.tag_add("center", 1.0, "end")
        text_box.grid(column=1, row=1)
        
        browse_text.set("Browse")

#browse button
browse_text = tk.StringVar()
browse_button = tk.Button(root, textvariable=browse_text, command=lambda:open_file(), bg="black", fg="white")
browse_text.set("Browse")
browse_button.grid(column=1, row=3)









root.mainloop()
