from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk

#------ GUI Code ------#

# image uploader function
def upload_image():
    fileTypes = [("Image files", "*.png;*.jpg;*.jpeg")]
    path = filedialog.askopenfilename(filetypes=fileTypes)
 
    # if file is selected
    if path:
        img = Image.open(path)
        img = img.resize((400, 300))
        pic = ImageTk.PhotoImage(img)
 
        # re-sizing the app window in order to fit picture
        # and button
        root.geometry("1024x768")
        img_label.config(image=pic)
        img_label.image = pic
 
    # if no file is selected, then we are displaying below message
    else:
        print("No file is Choosen !! Please choose a file.")

def convert_image_to_text():
    pass

def winCentre(window): 
    app_Width = 1440
    app_Height = 900 
    swidth = window.winfo_screenwidth() 
    screen_height = window.winfo_screenheight() 
    x = (swidth / 2) - (app_Width / 2)
    y = (screen_height / 2) - (app_Height / 2) 
    window.geometry(f'{app_Width}x{app_Height}+{int(x)}+{int(y)}')

# Main method
if __name__ == "__main__":
    root = Tk() 
    root.title('Image To Text using CRNN') 
    root.configure(bg='#F5F5F5')
    main_label = Label(root, text='Image to Text Converter', font=('Arial', 18,'bold'), bg='#F5F5F5')
    main_label.place(x=340,y=30)
    #text_label1 = Label(root, text='Image Preview:', font=('Helvetica', 14), bg='light gray')
    #text_label1.place(x=10,y=100)
    text_label2 = Label(root, text='Results:', font=('Helvetica', 14), bg='light gray')
    text_label2.place(x=10,y=450)

    # adding background image
    img = ImageTk.PhotoImage(file='images.jpeg')
    img_label = Label(root, image=img, bg='light gray')
    img_label.place(x= 340,y=100)
 
    # adding background color to our upload button
    # root.option_add("*Label*Background", "white")
    # root.option_add("*Button*Background", "lightgreen")
 
    # Create a Button to upload the image
    button_upload = Button(root, text='Upload Image', command=upload_image, font=('Helvetica', 14), bg='#ADD8E6', fg='black')
    button_upload.place(x=600,y=400)
    
    # Create a Button to convert the image to text
    button_convert = Button(root, text='Convert Image to Text', command=convert_image_to_text, font=('Helvetica', 14), bg='#ADD8E6', fg='black')
    button_convert.place(x=415,y=600)
    
    winCentre(root)
    root.mainloop()
