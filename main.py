import os
import tkinter as tk
from PIL import Image, ImageTk

bg_color = "#282a36"
fg_color = "#f1fa8c"
fg_color1 = "#50fa7b"
fg_color2= "#ffb86c"

btn_bg_color1 = "#328a35"
btn_ac_bg_color1 = "#6bb56d"

btn_bg_color = "#e85b1e"
btn_ac_bg_color = "#ed9c79"

def destroy_all_widgets(frame):
    for widget in frame.winfo_children():
        widget.destroy()

def load_frame1():
    #destroy_all_widgets(frame2)    
   
    frame1.tkraise()  # Bring frame1 to the front
    frame1.grid_propagate(False)  # Prevent frame1 from resizing to fit its contents

    # Get the directory where the current script is located
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Construct the path to the logo file
    logo_path = os.path.join(script_dir, "logo.png")

    # Load the logo image using Pillow
    logo = Image.open(logo_path).convert("RGBA")  # Replace with your image file path and Ensure RGBA format
    logo = logo.resize((125, 125))  # Resize the image if needed

    # Convert the image to a format Tkinter can use
    logo_tk = ImageTk.PhotoImage(logo)

    # Create a label to display the image
    label = tk.Label(frame1, image=logo_tk, bg=bg_color)
    label.grid(row=0, column=0, pady=10) # Add some padding for better placement

    # Keep a reference to the image to prevent garbage collection
    label.image = logo_tk

    tk.Label(
        frame1,
        text="QUESTION REVISION APPLICATION",
        bg=bg_color,
        fg="#ffffff",
        font=("Verdana", 30)
    ).grid(row=0, column=1, padx=10, pady=10)
    

def load_frame2():
    #destroy_all_widgets(frame2)    
   
    frame2.tkraise() 
    frame2.grid_propagate(False) 

    
    tk.Label(
        frame2,
        text="TOTAL QUESTIONS",
        bg=bg_color,
        fg=fg_color2,
        font=("Verdana", 20)
    ).grid(row=0, column=0, padx=(25, 10), pady=10)

    # Circle properties
    radius = 60
    center_x = 200
    center_y = 200
    # Create a Canvas widget that fits exactly around the circle
    canvas = tk.Canvas(frame2, width=2 * radius, height=2 * radius, bg=bg_color, bd=0, highlightthickness=0)
    canvas.grid(row=0, column=1)

    # Draw the circle centered at (radius, radius) with the given radius
    canvas.create_oval(0, 0, 2 * radius, 2 * radius, outline=bg_color, fill=btn_bg_color1, width=2)
    # Add text to the center of the circle
    canvas.create_text(radius, radius, text="50", font=("Verdana", 20), fill="#ffffff")

    tk.Label(
        frame2,
        text="EASY QUESTIONS",
        bg=bg_color,
        fg=fg_color2,
        font=("Verdana", 20)
    ).grid(row=0, column=2, padx=(100,10), pady=10)

    # Circle properties
    radius = 60
    center_x = 200
    center_y = 200
    # Create a Canvas widget that fits exactly around the circle
    canvas = tk.Canvas(frame2, width=2 * radius, height=2 * radius, bg=bg_color, bd=0, highlightthickness=0)
    canvas.grid(row=0, column=3)
    
    # Draw the circle centered at (radius, radius) with the given radius
    canvas.create_oval(0, 0, 2 * radius, 2 * radius, outline=bg_color, fill=btn_bg_color1, width=2)
    # Add text to the center of the circle
    canvas.create_text(radius, radius, text="10", font=("Verdana", 20), fill="#ffffff")

    tk.Label(
        frame2,
        text="MEDIUM QUESTIONS",
        bg=bg_color,
        fg=fg_color2,
        font=("Verdana", 20)
    ).grid(row=1, column=0, padx=(50,10), pady=75)

    # Circle properties
    radius = 60
    center_x = 200
    center_y = 200
    # Create a Canvas widget that fits exactly around the circle
    canvas = tk.Canvas(frame2, width=2 * radius, height=2 * radius, bg=bg_color, bd=0, highlightthickness=0)
    canvas.grid(row=1, column=1)
    
    # Draw the circle centered at (radius, radius) with the given radius
    canvas.create_oval(0, 0, 2 * radius, 2 * radius, outline=bg_color, fill=btn_bg_color1, width=2)
    # Add text to the center of the circle
    canvas.create_text(radius, radius, text="20", font=("Verdana", 20), fill="#ffffff")

    tk.Label(
        frame2,
        text="HARD QUESTIONS",
        bg=bg_color,
        fg=fg_color2,
        font=("Verdana", 20)
    ).grid(row=1, column=2, padx=(100,10), pady=10)

    # Circle properties
    radius = 60
    center_x = 200
    center_y = 200
    # Create a Canvas widget that fits exactly around the circle
    canvas = tk.Canvas(frame2, width=2 * radius, height=2 * radius, bg=bg_color, bd=0, highlightthickness=0)
    canvas.grid(row=1, column=3)
    
    # Draw the circle centered at (radius, radius) with the given radius
    canvas.create_oval(0, 0, 2 * radius, 2 * radius, outline=bg_color, fill=btn_bg_color1, width=2)
    # Add text to the center of the circle
    canvas.create_text(radius, radius, text="9", font=("Verdana", 20), fill="#ffffff")

def load_frame3():
    
    frame3 = tk.Frame(frame2, width=window_width, height=100, bg=bg_color)
    frame3.grid(row=3, column=0, columnspan=20, sticky="w", pady=(50,0))
        
    add_button = tk.Button(
        frame3,
        text="ADD QUESTION",
        font=("Verdana", 15),
        bg=btn_bg_color,
        fg="white",
        cursor="hand2",
        activebackground=btn_ac_bg_color,
        activeforeground="black",
        command=lambda: load_frame2()
    )
    add_button.grid(row=0, column=0, padx=60, pady=10)

    add_button.bind("<Enter>", lambda e, b=add_button: change_button_color(b, btn_ac_bg_color, "#000000"))
    add_button.bind("<Leave>", lambda e, b=add_button: change_button_color(b, btn_bg_color, "#ffffff"))


    list_button = tk.Button(
        frame3,
        text="LIST QUESTIONS",
        font=("Verdana", 15),
        bg=btn_bg_color,
        fg="white",
        cursor="hand2",
        activebackground=btn_ac_bg_color,
        activeforeground="black",
        command=lambda: load_frame2()
    )
    list_button.grid(row=0, column=1, padx=60, pady=10)

    list_button.bind("<Enter>", lambda e, b=list_button: change_button_color(b, btn_ac_bg_color, "#000000"))
    list_button.bind("<Leave>", lambda e, b=list_button: change_button_color(b, btn_bg_color, "#ffffff"))


    def change_button_color(button, bg_color, fg_color):
        button.config(bg=bg_color, fg=fg_color)

    revise_button = tk.Button(
        frame3,
        text="REVISE QUESTIONS",
        font=("Verdana", 15),
        bg=btn_bg_color,
        fg="white",
        cursor="hand2",
        activebackground=btn_ac_bg_color,
        activeforeground="black",
        command=lambda: load_frame2()
    )
    revise_button.grid(row=0, column=2, padx=60, pady=10)

    # Hover effect for revise_button
    revise_button.bind("<Enter>", lambda e, b=revise_button: change_button_color(b, btn_ac_bg_color, "#000000"))
    revise_button.bind("<Leave>", lambda e, b=revise_button: change_button_color(b, btn_bg_color, "#ffffff"))


# Set up the main window
root = tk.Tk()
root.title("Question Revision Application")

# Get the screen width and height
window_width = root.winfo_screenwidth()
window_height = root.winfo_screenheight()

# Subtract 10px from each side (20px total)
window_width -= 100
window_height -= 150

# Set the window to the new size
root.geometry(f"{window_width}x{window_height}+20+50")  # Add 10px offset to top-left corner

root.resizable(False, False)

# frame1 is Header Frame
# frame2 is Admin Frame
frame1 = tk.Frame(root, width=window_width, height=150, bg=bg_color)
frame2 = tk.Frame(root, width=window_width, height=window_height-150, bg=bg_color)

# Grid both frames, but only the one on top will be visible at a time
frame1.grid(row=0, column=0, sticky="nsew")
frame2.grid(row=1, column=0, sticky="nsew")


# Initially, show frame1
load_frame1()
load_frame2()
load_frame3()

root.mainloop()