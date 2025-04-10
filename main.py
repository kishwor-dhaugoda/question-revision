import os
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

import random


bg_color = "#282a36"
bg_color_txt_fld = "#626363"
fg_color = "#f1fa8c"
fg_color1 = "#13d443"
fg_color2= "#ffb86c"

btn_bg_color1 = "#328a35"
btn_ac_bg_color1 = "#6bb56d"

btn_bg_color = "#e85b1e"
btn_ac_bg_color = "#ed9c79"



def destroy_all_widgets(frame):
    for widget in frame.winfo_children():
        widget.destroy()

def set_hover_effects(button, hover_bg=btn_ac_bg_color, hover_fg="#000000", normal_bg=btn_bg_color, normal_fg="#ffffff"):
    button.bind("<Enter>", lambda e: button.config(bg=hover_bg, fg=hover_fg))
    button.bind("<Leave>", lambda e: button.config(bg=normal_bg, fg=normal_fg))

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
    logo = logo.resize((140, 140))  # Resize the image if needed

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

    set_hover_effects(add_button)

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

    set_hover_effects(list_button)

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

    set_hover_effects(revise_button)

def load_frame4():
    frame4.tkraise() 
    frame4.grid_propagate(False) 
    
    tk.Label(
        frame5,
        text="Question ID",
        bg="#5c5c5c",
        fg=fg_color2,
        font=("Verdana", 15)
    ).grid(row=0, column=0, padx=(25, 10), pady=10, sticky="w")

    tk.Entry(
        frame5,
        width=5,
        font=("Verdana", 15),
        bg=bg_color_txt_fld,
        fg=fg_color1,
        insertbackground=fg_color1
    ).grid(row=0, column=1, padx=10, ipadx=5, ipady=5, sticky="w")

    add_que_ser_btn = tk.Button(
        frame5,
        text="SEARCH",
        font=("Verdana", 12),
        bg=btn_bg_color,
        fg="white",
        cursor="hand2",
        activebackground=btn_ac_bg_color,
        activeforeground="black",
        command=lambda: print("hello")
    )
    add_que_ser_btn.grid(row=0, column=2, padx=10, sticky="w")
    set_hover_effects(add_que_ser_btn)

    tk.Label(
        frame6,
        text="Question ID",
        bg=bg_color,
        fg=fg_color2,
        font=("Verdana", 12)
    ).grid(row=0, column=0, padx=(25, 10), pady=15, sticky="w")

    tk.Entry(
        frame6,
        width=5,
        font=("Verdana", 12),
        bg=bg_color_txt_fld,
        fg=fg_color1,
        insertbackground=fg_color1
    ).grid(row=0, column=1, padx=10, pady= 5, ipadx=5, ipady=5, sticky="w")

    tk.Label(
        frame6,
        text="Category",
        bg=bg_color,
        fg=fg_color2,
        font=("Verdana", 12)
    ).grid(row=0, column=2, padx=(25, 10), pady=15, sticky="w")

    # Function to display the selected option
    def show_drop_selection():
        print(f"Selected: {dropdown.get()}")

    # Create a list of options
    options = ["DSA", "PYTHON", "JAVASCRIPT"]

    # Create a Tkinter variable to hold the selected value
    dropdown = tk.StringVar()
    dropdown.set(options[0])  # Set default value to the first option

    # Create the OptionMenu widget
    option_menu = tk.OptionMenu(frame6, dropdown, *options)
    option_menu.config(bg=bg_color_txt_fld, fg=fg_color2, font=("Verdana", 12), width=15, bd=0, highlightthickness=0)
    option_menu.grid(row=0, column=3, padx=10, pady= 5, ipadx=5, ipady=5, sticky="w")

    tk.Label(
        scrollable_frame,
        text="Question",
        bg=bg_color,
        fg=fg_color2,
        font=("Verdana", 12)
    ).grid(row=2, column=0, padx=(25, 10), pady=5, sticky="w")

    tk.Text(
        scrollable_frame,
        width=110,
        height=10,
        font=("Verdana", 12),
        bg=bg_color_txt_fld,
        fg=fg_color1,
        insertbackground=fg_color1
    ).grid(row=3, column=0, columnspan=25, padx=(25, 10), pady=5, ipadx=5, ipady=5, sticky="w")

    
    tk.Label(
        frame7,
        text="Difficulty",
        bg=bg_color,
        fg=fg_color2,        
        font=("Verdana", 12)
    ).grid(row=0, column=0, padx=(25, 10), pady=5, sticky="w")
    
    # Variable to store the selected option
    selected_option = tk.StringVar(value="Easy")  # Initially, no option is selected

    # Function to display the selected option
    def show_selection():
        print(f"Selected: {selected_option.get()}")

    # Create radio buttons with 3 options
    tk.Radiobutton(
        frame7,
        bg= bg_color,
        fg= fg_color2,
        selectcolor= bg_color,
        font=("Verdana", 12),
        text="Easy", 
        variable=selected_option, 
        value="Easy", 
        command=show_selection
    ).grid(row=0, column=1, padx=(25, 10), pady=5, sticky="w")

    tk.Radiobutton(
        frame7, 
        bg= bg_color,
        fg= fg_color2,
        selectcolor= bg_color,
        font=("Verdana", 12),
        text="Medium", 
        variable=selected_option, 
        value="Medium", 
        command=show_selection
    ).grid(row=0, column=2, padx=(25, 10), pady=5, sticky="w")
    
    tk.Radiobutton(
        frame7, 
        bg= bg_color,
        fg= fg_color2,
        selectcolor= bg_color,
        font=("Verdana", 12),
        text="Hard", 
        variable=selected_option, 
        value="Hard", 
        command=show_selection
    ).grid(row=0, column=3, padx=(25, 10), pady=5, sticky="w")

    tk.Label(
        scrollable_frame,
        text="Solution",
        bg=bg_color,
        fg=fg_color2,
        font=("Verdana", 12)
    ).grid(row=5, column=0, padx=(25, 10), pady=5, sticky="w")

    solution_text = tk.Text(
        scrollable_frame,
        width=110,
        height=10,
        font=("Verdana", 12),
        bg=bg_color_txt_fld,
        fg=fg_color1,
        insertbackground=fg_color1
    )
    solution_text.grid(row=6, column=0, columnspan=4, padx=(25, 10), pady=5, ipadx=5, ipady=5, sticky="w")

    add_ques_save_btn = tk.Button(
        frame8,
        text="SAVE CHANGES",
        font=("Verdana", 12),
        bg=btn_bg_color,
        fg="white",
        cursor="hand2",
        activebackground=btn_ac_bg_color,
        activeforeground="black",
        command=lambda: print("hello")
    )
    add_ques_save_btn.grid(row=0, column=0, padx=(25, 10), pady=15, sticky="w")
    set_hover_effects(add_ques_save_btn)

    add_ques_gtadmin_btn = tk.Button(
        frame8,
        text="GOTO ADMIN",
        font=("Verdana", 12),
        bg=btn_bg_color,
        fg="white",
        cursor="hand2",
        activebackground=btn_ac_bg_color,
        activeforeground="black",
        command=lambda: print("hello")
    )
    add_ques_gtadmin_btn.grid(row=0, column=1, padx=(25, 10), pady=15 , sticky="w")
    set_hover_effects(add_ques_gtadmin_btn)

def load_frame9():
    frame9.tkraise() 
    frame9.grid_propagate(False) 
    
    tk.Label(
        scrollable_frame1,
        text="Questions List",
        bg=bg_color,
        fg=fg_color2,
        font=("Verdana", 15)
    ).grid(row=0, column=0, padx=(25, 10), pady=10, sticky="w")





    # Define style
    style = ttk.Style()
    style.theme_use("default")

    # Base Treeview style
    style.configure("Custom.Treeview",
                    background=bg_color_txt_fld,           # Default background
                    foreground=fg_color1,             # Text color
                    rowheight=100,
                    fieldbackground=bg_color_txt_fld,      # Background for empty space
                    font=("Verdana", 10))

    # Alternate row colors
    style.map("Custom.Treeview", 
            background=[("selected", "#b57e43")],  # Selected row
            foreground=[("selected", "white")])   # Selected row text color

    # Hover effect (active row highlight) — optional workaround
    style.layout("Custom.Treeview", style.layout("Treeview"))

    # Style for headings
    style.configure("Custom.Treeview.Heading", 
                    background=bg_color_txt_fld, 
                    foreground=fg_color2, 
                    font=("Verdana", 12, "bold"),
                    padding=(10, 5))

    # 🔕 Disable hover effects on headings
    style.map("Custom.Treeview.Heading", background=[], foreground=[], relief=[], font=[])

    # Create Treeview
    tree = ttk.Treeview(scrollable_frame1, columns=("id", "question", "category", "difficulty"), show="headings", style="Custom.Treeview")

    # Define columns
    tree.heading("id", text="ID", anchor="w")
    tree.heading("question", text="Question", anchor="w")
    tree.heading("category", text="Category", anchor="w")
    tree.heading("difficulty", text="Difficulty", anchor="w")

    tree.column("id", width=50, anchor="center")
    tree.column("question", width=900, anchor="w")
    tree.column("category", width=120, anchor="center")
    tree.column("difficulty", width=120, anchor="center")

    # Insert sample data with alternating background manually
    categories = ['Math', 'Science', 'History', 'Geography', 'Literature']
    difficulties = ['easy', 'medium', 'hard']
    questions = [
        "What is the capital of France?",
        "Who developed\n\t the theory of \nrelativity?Who developed\n\t the theory of \nrelativity?Who developed\n\t the theory of \nrelativity?",
        "In what year did World War II end?",
        "Who wrote 'Pride and Prejudice'?",
        "What is the square root of 144?",
        "What is the chemical symbol for water?",
        "Who painted the Mona Lisa?",
        "What is the longest river in the world?",
        "Which planet is known as the Red Planet?",
        "What is the atomic number of oxygen?",
        "Who invented the telephone?",
        "What is the tallest mountain in the world?",
        "Who was the first President of the United States?",
        "What is the capital of Japan?",
        "Who discovered penicillin?"
    ]

    # Random data generation
    data = [
        (i+1, random.choice(questions), random.choice(categories), random.choice(difficulties))
        for i in range(15)
    ]
    # Tag configuration for alternate rows
    tree.tag_configure('evenrow', background="#f7dec3", foreground="#000000") 
    tree.tag_configure('oddrow', background="#444444")   

    for index, row in enumerate(data):
        tag = 'evenrow' if index % 2 == 0 else 'oddrow'
        tree.insert("", "end", values=row, tags=(tag,))

    tree.grid(row=1, column=0, padx=(25, 10), pady=10, sticky="w")

    li_ques_pag_btn = tk.Button(
        frame10,
        text="1",
        font=("Verdana", 10),
        bg=btn_bg_color,
        fg="white",
        cursor="hand2",
        activebackground=btn_ac_bg_color,
        activeforeground="black",
        command=lambda: print("hello")
    )
    li_ques_pag_btn.grid(row=0, column=0, padx=(25, 10), pady=15 , ipadx=3, ipady=3 , sticky="w")
    set_hover_effects(li_ques_pag_btn)


    li_ques_pag_btn4 = tk.Button(
        frame10,
        text="2",
        font=("Verdana", 10),
        bg=btn_bg_color,
        fg="white",
        cursor="hand2",
        activebackground=btn_ac_bg_color,
        activeforeground="black",
        command=lambda: print("hello")
    )
    li_ques_pag_btn4.grid(row=0, column=1, padx=(25, 10), pady=15 ,ipadx=3, ipady=3 , sticky="w")
    set_hover_effects(li_ques_pag_btn4)


    li_ques_pag_btn1 = tk.Button(
        frame10,
        text="3",
        font=("Verdana", 10),
        bg=btn_bg_color,
        fg="white",
        cursor="hand2",
        activebackground=btn_ac_bg_color,
        activeforeground="black",
        command=lambda: print("hello")
    )
    li_ques_pag_btn1.grid(row=0, column=2, padx=(25, 10), pady=15, ipadx=3, ipady=3 , sticky="w")
    set_hover_effects(li_ques_pag_btn1)

    li_ques_pag_btn2= tk.Button(
        frame10,
        text="4",
        font=("Verdana", 10),
        bg=btn_bg_color,
        fg="white",
        cursor="hand2",
        activebackground=btn_ac_bg_color,
        activeforeground="black",
        command=lambda: print("hello")
    )
    li_ques_pag_btn2.grid(row=0, column=3, padx=(25, 10), pady=15, ipadx=3, ipady=3 , sticky="w")
    set_hover_effects(li_ques_pag_btn2)




    li_ques_view= tk.Button(
        frame11,
        text="View Question",
        font=("Verdana", 12),
        bg=btn_bg_color,
        fg="white",
        cursor="hand2",
        activebackground=btn_ac_bg_color,
        activeforeground="black",
        command=lambda: print("hello")
    )
    li_ques_view.grid(row=0, column=1, padx=(25, 10), pady=15, ipadx=3, ipady=3 , sticky="w")
    set_hover_effects(li_ques_view)

    li_ques_delete= tk.Button(
        frame11,
        text="Delete Question(s)",
        font=("Verdana", 12),
        bg=btn_bg_color,
        fg="white",
        cursor="hand2",
        activebackground=btn_ac_bg_color,
        activeforeground="black",
        command=lambda: print("hello")
    )
    li_ques_delete.grid(row=0, column=2, padx=(25, 10), pady=15, ipadx=3, ipady=3 , sticky="w")
    set_hover_effects(li_ques_delete)


    li_ques_update= tk.Button(
        frame11,
        text="Update Question",
        font=("Verdana", 12),
        bg=btn_bg_color,
        fg="white",
        cursor="hand2",
        activebackground=btn_ac_bg_color,
        activeforeground="black",
        command=lambda: print("hello")
    )
    li_ques_update.grid(row=0, column=3, padx=(25, 10), pady=15, ipadx=3, ipady=3 , sticky="w")
    set_hover_effects(li_ques_update)

def load_frame12():
    frame12.tkraise() 
    frame12.grid_propagate(False) 
    
    tk.Label(
        frame12,
        text="Question Generator",
        bg=bg_color,
        fg=fg_color2,
        font=("Verdana", 15)
    ).grid(row=0, column=0, padx=(25, 10), pady=10, sticky="w")

    tk.Label(
        frame14,
        text="No. of Questions",
        bg=bg_color,
        fg=fg_color2,
        font=("Verdana", 15)
    ).grid(row=0, column=0, padx=(25, 10), pady=10, sticky="w")

    tk.Entry(
        frame14,
        width=5,
        font=("Verdana", 12),
        bg=bg_color_txt_fld,
        fg=fg_color1,
        insertbackground=fg_color1
    ).grid(row=0, column=1, padx=10, pady= 5, ipadx=5, ipady=5, sticky="w")

    # Variable to store the selected option
    selected_option = tk.StringVar(value="Easy")  # Initially, no option is selected

    # Function to display the selected option
    def show_selection():
        print(f"Selected: {selected_option.get()}")

    tk.Label(
        frame13,
        text="Difficulty",
        bg=bg_color,
        fg=fg_color2,
        font=("Verdana", 15)
    ).grid(row=0, column=0, padx=(25, 10), pady=10, sticky="w")


     # Create radio buttons with 3 options
    tk.Radiobutton(
        frame13,
        bg= bg_color,
        fg= fg_color2,
        selectcolor= bg_color,
        font=("Verdana", 12),
        text="Easy", 
        variable=selected_option, 
        value="Easy", 
        command=show_selection
    ).grid(row=0, column=1, padx=(25, 10), pady=5, sticky="w")

    tk.Radiobutton(
        frame13, 
        bg= bg_color,
        fg= fg_color2,
        selectcolor= bg_color,
        font=("Verdana", 12),
        text="Medium", 
        variable=selected_option, 
        value="Medium", 
        command=show_selection
    ).grid(row=0, column=2, padx=(25, 10), pady=5, sticky="w")
    

    tk.Radiobutton(
        frame13, 
        bg= bg_color,
        fg= fg_color2,
        selectcolor= bg_color,
        font=("Verdana", 12),
        text="Hard", 
        variable=selected_option, 
        value="Hard", 
        command=show_selection
    ).grid(row=0, column=3, padx=(25, 10), pady=5, sticky="w")


    tk.Label(
        frame15,
        text="Revised",
        bg=bg_color,
        fg=fg_color2,
        font=("Verdana", 15)
    ).grid(row=0, column=0, padx=(25, 10), pady=10, sticky="w")

    # Variable to store the selected option
    selected_option_revi = tk.StringVar(value="Easy")  # Initially, no option is selected

    tk.Radiobutton(
        frame15, 
        bg= bg_color,
        fg= fg_color2,
        selectcolor= bg_color,
        font=("Verdana", 12),
        text="Less Than", 
        variable=selected_option_revi, 
        value="less_than", 
        command=lambda: print("select")
    ).grid(row=0, column=1, padx=(25, 10), pady=5, sticky="w")

    tk.Entry(
        frame15,
        width=3,
        font=("Verdana", 12),
        bg=bg_color_txt_fld,
        fg=fg_color1,
        insertbackground=fg_color1
    ).grid(row=0, column=2, padx=10, pady= 5, ipadx=5, ipady=5, sticky="w")


    tk.Radiobutton(
        frame15, 
        bg= bg_color,
        fg= fg_color2,
        selectcolor= bg_color,
        font=("Verdana", 12),
        text="Any", 
        command=lambda: print("select"),
        value="any", 
        variable=selected_option_revi
    ).grid(row=0, column=3, padx=(25, 10), pady=5, sticky="w")


    # List of options
    checkbox_texts = ["DSA", "PYTHON", "JAVASCRIPT", "GK", "APTITUDE"]
    checkbox_vars = []

    # Create a Checkbutton for each item
    for index in range(len(checkbox_texts)):
        var = tk.IntVar()  # Variable to store the checkbox state
        checkbox_vars.append(var)
        cb = tk.Checkbutton(
            frame16,
            text=checkbox_texts[index], 
            variable=var, 
            bg = bg_color, 
            fg= fg_color2, 
            selectcolor=bg_color,
            font=("Verdana", 12)
        )
        cb.grid(row=0, column=index, padx=(25, 10), pady=5, sticky="w")

    ques_gene_btn = tk.Button(
        frame12,
        text="GENERATE QUESTIONS",
        font=("Verdana", 12),
        bg=btn_bg_color,
        fg="white",
        cursor="hand2",
        activebackground=btn_ac_bg_color,
        activeforeground="black",
        command=lambda: print("hello")
    )
    ques_gene_btn.grid(row=6, column=0, padx=(25, 10), pady=15 , sticky="w")
    set_hover_effects(ques_gene_btn)



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
# frame3 is used for buttom buttons in admin frame
frame1 = tk.Frame(root, width=window_width, height=150, bg=bg_color)
frame2 = tk.Frame(root, width=window_width, height=window_height-150, bg=bg_color)
frame3 = tk.Frame(frame2, width=window_width, height=100, bg=bg_color)

frame1.grid(row=0, column=0, sticky="nsew")
frame2.grid(row=1, column=0, sticky="nsew")
frame3.grid(row=3, column=0, columnspan=20, sticky="w", pady=(50,0))



# 👀frame4 is for question add update
# 👀frame5 is for search bar
# 👀frame6 is for question id
# 👀frame7 is for difficulty radios
# 👀frame8 for the question add update buttons


# --- FRAME4 with Canvas and Scrollbar Setup ---
frame4 = tk.Frame(root, width=window_width, height=window_height-150, bg=bg_color)
frame4.grid(row=1, column=0, sticky="nsew")

# root.grid_rowconfigure(1, weight=1)
# Tells row 1 of the root window to expand vertically when the window is resized.

# root.grid_columnconfigure(0, weight=1)
# Tells column 0 of the root window to expand horizontally.
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)


def bind_mousewheel_to_widget(widget, canvas):
    def _on_mousewheel(event):
        canvas.yview_scroll(int(-1*(event.delta / 50)), "units")

    widget.bind("<Enter>", lambda e: widget.bind_all("<MouseWheel>", _on_mousewheel))
    widget.bind("<Leave>", lambda e: widget.unbind_all("<MouseWheel>"))




# Create Canvas and Scrollbar
canvas = tk.Canvas(frame4, bg=bg_color, highlightthickness=0)
scrollbar = ttk.Scrollbar(frame4, orient="vertical", command=canvas.yview)
scrollable_frame = tk.Frame(canvas, bg=bg_color)

# Configure the canvas to work with the scrollbar
scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(
        scrollregion=canvas.bbox("all")
    )
)

canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

# Layout the canvas and scrollbar
canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")


frame5 = tk.Frame(scrollable_frame, width=window_width, height=100, bg="#5c5c5c", bd=2, relief="solid")
frame5.grid(row=0, column=0, sticky="w", padx=25, pady=(25,15))

frame6 = tk.Frame(scrollable_frame, width=window_width, height=100, bg=bg_color)
frame6.grid(row=1, column=0, sticky="w")

frame7 = tk.Frame(scrollable_frame, width=window_width, height=100, bg=bg_color)
frame7.grid(row=4, column=0, sticky="w")

frame8 = tk.Frame(scrollable_frame, width=window_width, height=100, bg=bg_color)
frame8.grid(row=8, column=0, sticky="w")

def _on_mousewheel(event):
    canvas.yview_scroll(int(-1*(event.delta/120)), "units")


# Bind mousewheel scrolling
# canvas.bind_all("<MouseWheel>", _on_mousewheel)

bind_mousewheel_to_widget(scrollable_frame, canvas)



# 👀frame9 is for list questions

frame9 = tk.Frame(root, width=window_width, height=window_height-150, bg=bg_color)
frame9.grid(row=1, column=0, sticky="nsew")


# Create Canvas and Scrollbar
canvas1 = tk.Canvas(frame9, bg=bg_color, highlightthickness=0)
scrollbar1 = ttk.Scrollbar(frame9, orient="vertical", command=canvas1.yview)
scrollable_frame1 = tk.Frame(canvas1, bg=bg_color)

# Configure the canvas to work with the scrollbar
scrollable_frame1.bind(
    "<Configure>",
    lambda e: canvas1.configure(
        scrollregion=canvas1.bbox("all")
    )
)

canvas1.create_window((0, 0), window=scrollable_frame1, anchor="nw")
canvas1.configure(yscrollcommand=scrollbar1.set)

# Layout the canvas and scrollbar
canvas1.pack(side="left", fill="both", expand=True)
scrollbar1.pack(side="right", fill="y")


def _on_mousewheel1(event):
    canvas1.yview_scroll(int(-1*(event.delta/120)), "units")

# Bind mousewheel scrolling
# canvas1.bind_all("<MouseWheel>", _on_mousewheel1)

bind_mousewheel_to_widget(scrollable_frame1, canvas1)


# 👀frame10 is for list questions pagination

frame10 = tk.Frame(scrollable_frame1, width=window_width, height=100, bg=bg_color)
frame10.grid(row=2, column=0)

# 👀frame11 is for list questions buttons

frame11 = tk.Frame(scrollable_frame1, width=window_width, height=100, bg=bg_color)
frame11.grid(row=3, column=0)



# 👀frame12 is for question generator

frame12 = tk.Frame(root, width=window_width, height=window_height-150, bg=bg_color)
frame12.grid(row=1, column=0, sticky="nsew")


# 👀frame13 is for question generator radioboxes

frame13 = tk.Frame(frame12, width=window_width, height=100, bg=bg_color)
frame13.grid(row=3, column=0, sticky="w")

# 👀frame14 is for question qenerator no of questions

frame14 = tk.Frame(frame12, width=window_width, height=100, bg=bg_color)
frame14.grid(row=2, column=0, sticky="w")

# 👀frame15 is for question qenerator revised

frame15 = tk.Frame(frame12, width=window_width, height=100, bg=bg_color)
frame15.grid(row=4, column=0, sticky="w")

# 👀frame16 is for question qenerator categories

frame16 = tk.Frame(frame12, width=window_width, height=100, bg=bg_color)
frame16.grid(row=5, column=0, sticky="w")



load_frame1()

# load_frame2()
# load_frame3()

load_frame4()

# load_frame9()

# load_frame12()

root.mainloop()