import segno
import tkinter as tk 
from PIL import Image, ImageTk 

print("Welcome to the QR code generator.")

data = input("What would you like to be in your QR code? ")
if data == "":
    print("Please insert a valid input")
else:
    qr_color = int(input("If you want the QR code colors to be black and white type 1, and if you want them to be blue and white type 2: "))

    # generate the QR code
    qrcode = segno.make_qr(data)
    qrcode.version

    # save the QR code with the selected colors
    if qr_color == 1:
        qrcode.save('QRcode.png', dark='black', light='white')
        print("QR code is generated and saved as 'QRcode.png' with black and white colors.")
    elif qr_color == 2:
        qrcode.save('QRcode.png', dark='blue', light='white')
        print("QR code is generated and saved as 'QRcode.png' with blue and white colors.")
    else:
        print("Please choose 1 or 2 for the color option.")

# display the QR code in a GUI
root = tk.Tk()
root.title("QR code")
root.geometry("320x320")
photo = Image.open("QRcode.png")
resized_image = photo.resize((300,300), Image.Resampling.LANCZOS)
converted_image = ImageTk.PhotoImage(resized_image)
label = tk.Label(root,
                image = converted_image,
                compound="bottom",
                text="here is your QR code!!",
                font=('Verdana', 16),
                fg='white',
                bg='black'
                )
label.pack()
root.mainloop()


    


    