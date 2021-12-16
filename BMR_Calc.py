import tkinter as tk

root = tk.Tk()
root.title('Basal Metabolic Rate')

canvas1 = tk.Canvas(root, width = 400, height = 400)
canvas1.pack()

# Age text box
label1 = tk.Label(root, text="Age (years)")
label1.config(font =('helvetica', 10))
canvas1.create_window(200, 20, window=label1)

entry1 = tk.Entry(root)
canvas1.create_window(200, 40, width=120, window=entry1)

# Height text feet box
label2 = tk.Label(root, text="Height (ft/inch)")
label2.config(font =('helvetica', 10))
canvas1.create_window(200, 70, window=label2)

entry2 = tk.Entry(root)
canvas1.create_window(165, 90, width=50, window=entry2)

# Height text inches box
entry3 = tk.Entry(root)
canvas1.create_window(236, 90, width=50, window=entry3)

# Weight text box
label4 = tk.Label(root, text="Weight (pounds)")
label4.config(font =('helvetica', 10))
canvas1.create_window(200, 120, window=label4)

entry4 = tk.Entry(root)
canvas1.create_window(200, 140, width=120, window=entry4)

# Gender radio buttons
var = tk.IntVar()
radio1 = tk.Radiobutton(root, text = "Male", variable = var, value = 1)
canvas1.create_window(160, 170, window = radio1)

radio2 = tk.Radiobutton(root, text = "Female", variable = var, value = 2)
canvas1.create_window(230, 170, window = radio2)

# Definition text box
label5 = tk.Label(root, text="This calculator estimates the minimum amount \n of calories that your body needs to perform necessary \n functions, also known as basal metabolic rate (BMR).")
label5.config(font =('helvetica', 10))
canvas1.create_window(200, 350, window=label5)


# gathers entry results, converts to float and calculates
#  BMI based on gender and anteres values
def BMR():
    
    x1 = entry1.get()
    x2 = entry2.get()
    x3 = entry3.get()
    x4 = entry4.get()

    age = float(x1)
    height_inches = (float(x2) * 12) + float(x3)
    weight_lbs  = float(x4)

    height_meters = height_inches * 0.0254
    weight_kilos = weight_lbs * 0.45359237

    # male button vale is 1
    if var.get() == 1:
        BMR = round(10 * (weight_kilos) + (6.25 * (height_meters) * 100) - 5 * (age) + 5)

    # female button vale is 2
    elif var.get() == 2:
        BMR =  round(10 * (weight_kilos) + (6.25 * (height_meters) * 100) - 5 * (age) - 161)

    # no gender choice outputs a BMR of 0
    else:
        BMR = 0

    label4 = tk.Label(root, text= 'Your BMR is:',font=('helvetica', 10))
    canvas1.create_window(200, 240, window=label4)

    label5 = tk.Label(root, text= BMR ,font=('helvetica', 10, 'bold'))
    canvas1.create_window(200, 260, window=label5)

# calculate button which runs BMR()
button1 = tk.Button(root, text='Calculate', command=BMR)
canvas1.create_window(200, 210, window=button1)

root.mainloop()


