import math
import os
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk

import validators as vd

import Question as ques
import Themes as the

the.load_themes()
ques.load_questions()

theme = the.get_theme()

bg_color = theme['bg_color']
bg_color_txt_fld = theme['bg_color_txt_fld']
fg_color = theme['fg_color']
fg_color1 = theme['fg_color1']
fg_color2 = theme['fg_color2']
btn_bg_color1 = theme['btn_bg_color1'] 
btn_ac_bg_color1 = theme['btn_ac_bg_color1']
btn_bg_color = theme['btn_bg_color'] 
btn_ac_bg_color = theme['btn_ac_bg_color']
even_row_table_bg = theme['even_row_table_bg']  
even_row_table_fg = theme['even_row_table_fg']  
odd_row_table_bg = theme['odd_row_table_bg'] 

def destroy_all_widgets(frame):
    if frame:
        # Recursively destroy all widgets including all subchildren and containers
        def destroy_recursively(widget):
            for child in widget.winfo_children():
                # print(f"Destroying child widget: {child}")
                destroy_recursively(child)
                child.destroy()

        destroy_recursively(frame)

def destroy_all_widgets_exclude(frame):
    if frame:
        # Function to recursively destroy widgets, excluding Frame, Canvas, and Scrollbar
        def destroy_recursively(widget):
            # Skip destroying Frame, Canvas, and Scrollbar widgets, but destroy their children
            if isinstance(widget, (tk.Frame, tk.Canvas, tk.Scrollbar)):
                # If it's a Frame, Canvas, or Scrollbar, only destroy its children, not the widget itself
                for child in widget.winfo_children():
                    # print(f"Destroying child of {widget}: {child}")  # Debug print
                    destroy_recursively(child)  # Recursively destroy child widgets
                return  # Skip destroying the Frame, Canvas, or Scrollbar itself

            # Destroy the widget itself and its children
            # print(f"Destroying widget: {widget}")  # Debug print
            for child in widget.winfo_children():
                # print(f"Destroying child widget: {child}")  # Debug print
                destroy_recursively(child)  # Recursively destroy child widgets
            # print(widget)
            widget.destroy()  # Finally, destroy the current widget

        # Start the recursion from the given frame
        destroy_recursively(frame)

def set_hover_effects(button, hover_bg=btn_ac_bg_color, hover_fg="#000000", normal_bg=btn_bg_color, normal_fg="#ffffff"):
    button.bind("<Enter>", lambda e: button.config(bg=hover_bg, fg=hover_fg))
    button.bind("<Leave>", lambda e: button.config(bg=normal_bg, fg=normal_fg))


def load_frame1():
    
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


def load_frame3(frame):

    destroy_all_widgets_exclude(frame)    
   
    frame2.tkraise() 
    frame2.grid_propagate(False) 

    frame3.tkraise()
    frame3.grid_propagate(False)

    
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
    canvas.create_text(radius, radius, text=len(ques.get_questions()), font=("Verdana", 20), fill="#ffffff")

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
    canvas.create_text(radius, radius, text=ques.search_by_one_difficulty_count("Easy"), font=("Verdana", 20), fill="#ffffff")

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
    canvas.create_text(radius, radius, text=ques.search_by_one_difficulty_count("Medium"), font=("Verdana", 20), fill="#ffffff")

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
    canvas.create_text(radius, radius, text=ques.search_by_one_difficulty_count("Hard"), font=("Verdana", 20), fill="#ffffff")



    
    add_button = tk.Button(
        frame3,
        text="ADD QUESTION",
        font=("Verdana", 15),
        bg=btn_bg_color,
        fg="white",
        cursor="hand2",
        activebackground=btn_ac_bg_color,
        activeforeground="black",
        command=lambda: load_frame4(frame3)
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
        command=lambda: load_frame9(frame3)
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
        command=lambda: load_frame12(frame3)
    )
    revise_button.grid(row=0, column=2, padx=60, pady=10)

    set_hover_effects(revise_button)

def load_frame4(frame, update_id=None):
    
    destroy_all_widgets_exclude(frame)

    frame4.tkraise() 
    frame4.grid_propagate(False) 

    canvas.yview_moveto(0)


    ser_or_update = False
    
    qid_ser = tk.Label(
        frame5,
        text="Question ID",
        bg="#5c5c5c",
        fg=fg_color2,
        font=("Verdana", 15)
    )
    qid_ser.grid(row=0, column=0, padx=(25, 10), pady=10, sticky="w")

    question_ser = tk.Entry(
        frame5,
        width=5,
        font=("Verdana", 15),
        bg=bg_color_txt_fld,
        fg=fg_color1,
        insertbackground=fg_color1
    )
    question_ser.grid(row=0, column=1, padx=10, ipadx=5, ipady=5, sticky="w")

    tk.Label(
        frame6,
        text="Question ID",
        bg=bg_color,
        fg=fg_color2,
        font=("Verdana", 12)
    ).grid(row=0, column=0, padx=(25, 10), pady=15, sticky="w")

    # Create a custom style
    style = ttk.Style()
    style.theme_use('default')  # Use 'default' or other known themes

    # Define a style for readonly entry
    style.configure("CustomReadonly.TEntry",
                    foreground="green",
                    fieldbackground="red",  # This is what sets the background
                    background="gray")
    
    style.map("CustomReadonly.TEntry",
          fieldbackground=[("readonly", bg_color_txt_fld)],
          foreground=[("readonly", fg_color1)])

    qid = ttk.Entry(
        frame6,
        width=5,
        font=("Verdana", 12),
        style="CustomReadonly.TEntry"
        
    )
    qid.grid(row=0, column=1, padx=10, pady= 5, ipadx=5, ipady=5, sticky="w")


    def get_next_id(data):

        if not data:
            return 1 

        # Get the latest key (assuming the keys are in a sorted order)
        latest_key = max(data.keys(), key=lambda k: int(k))  # max by the integer value of the keys
        
        # Convert the latest key to an integer and add 1
        next_id = int(latest_key) + 1
        
        return next_id
    
    qid.insert(0, get_next_id(ques.get_questions()))    
    qid.config(state="readonly")
    

    tk.Label(
        frame6,
        text="Category",
        bg=bg_color,
        fg=fg_color2,
        font=("Verdana", 12)
    ).grid(row=0, column=2, padx=(25, 10), pady=15, sticky="w")

    # Create a list of options
    options = ques.get_categories()
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

    question_in = tk.Text(
        scrollable_frame,
        width=110,
        height=10,
        font=("Verdana", 12),
        bg=bg_color_txt_fld,
        fg=fg_color1,
        insertbackground=fg_color1
    )
    question_in.grid(row=3, column=0, columnspan=25, padx=(25, 10), pady=5, ipadx=5, ipady=5, sticky="w")

    
    tk.Label(
        frame7,
        text="Difficulty",
        bg=bg_color,
        fg=fg_color2,        
        font=("Verdana", 12)
    ).grid(row=0, column=0, padx=(25, 10), pady=5, sticky="w")
    
    # Variable to store the selected option
    selected_option = tk.StringVar(value="Easy")  # Initially, easy is selected

    
    # Create radio buttons with 3 options
    tk.Radiobutton(
        frame7,
        bg= bg_color,
        fg= fg_color2,
        selectcolor= bg_color,
        font=("Verdana", 12),
        text="Easy", 
        variable=selected_option, 
        value="Easy"
    ).grid(row=0, column=1, padx=(25, 10), pady=5, sticky="w")

    tk.Radiobutton(
        frame7, 
        bg= bg_color,
        fg= fg_color2,
        selectcolor= bg_color,
        font=("Verdana", 12),
        text="Medium", 
        variable=selected_option, 
        value="Medium"
    ).grid(row=0, column=2, padx=(25, 10), pady=5, sticky="w")
    
    tk.Radiobutton(
        frame7, 
        bg= bg_color,
        fg= fg_color2,
        selectcolor= bg_color,
        font=("Verdana", 12),
        text="Hard", 
        variable=selected_option, 
        value="Hard"
    ).grid(row=0, column=3, padx=(25, 10), pady=5, sticky="w")

    tk.Label(
        scrollable_frame,
        text="Solution",
        bg=bg_color,
        fg=fg_color2,
        font=("Verdana", 12)
    ).grid(row=5, column=0, padx=(25, 10), pady=5, sticky="w")

    solution_in = tk.Text(
        scrollable_frame,
        width=110,
        height=10,
        font=("Verdana", 12),
        bg=bg_color_txt_fld,
        fg=fg_color1,
        insertbackground=fg_color1
    )
    solution_in.grid(row=6, column=0, columnspan=4, padx=(25, 10), pady=5, ipadx=5, ipady=5, sticky="w")

    add_ques_save_btn = tk.Button(
        frame8,
        text="SAVE CHANGES",
        font=("Verdana", 12),
        bg=btn_bg_color,
        fg="white",
        cursor="hand2",
        activebackground=btn_ac_bg_color,
        activeforeground="black",
        command=lambda: add_question()
    )
    add_ques_save_btn.grid(row=0, column=0, padx=(25, 10), pady=15, sticky="w")
    set_hover_effects(add_ques_save_btn)

    def add_question():
        nonlocal ser_or_update

        if vd.is_text_empty(question_in.get("1.0", "end-1c")):
            messagebox.showerror("QUESTION REVISION APP", "Question can't be empty.")
            return
        elif vd.is_text_empty(solution_in.get("1.0", "end-1c")):
            messagebox.showerror("QUESTION REVISION APP", "Solution can't be empty.")
            return
        else:
            try:
                if ser_or_update:
                    ques.add_question(qid.get(), question_in.get("1.0", "end-1c"), solution_in.get("1.0", "end-1c"), dropdown.get(), selected_option.get(), ques.get_questions()[qid.get()]["revised"])
                else:
                    ques.add_question(qid.get(), question_in.get("1.0", "end-1c"), solution_in.get("1.0", "end-1c"), dropdown.get(), selected_option.get(), 0)
                
                ser_or_update = False
                messagebox.showinfo("QUESTION REVISION APP", "Question saved successfully.")

            except Exception as ex:
                print(ex)
                messagebox.showerror("QUESTION REVISION APP", "Question save failed.")
        
        
        qid.config(state="normal")
        qid.delete(0, tk.END)
        qid.insert(0, get_next_id(ques.get_questions()))    
        qid.config(state="readonly")



        question_in.delete(1.0, tk.END)
        solution_in.delete(1.0, tk.END)
        selected_option.set("Easy")
        dropdown.set(options[0])

        question_ser.delete(0, tk.END)

        canvas.yview_moveto(0)
        qid.focus_set() 
     

    add_ques_gtadmin_btn = tk.Button(
        frame8,
        text="GOTO ADMIN",
        font=("Verdana", 12),
        bg=btn_bg_color,
        fg="white",
        cursor="hand2",
        activebackground=btn_ac_bg_color,
        activeforeground="black",
        command=lambda: load_frame3(frame4)
    )
    add_ques_gtadmin_btn.grid(row=0, column=1, padx=(25, 10), pady=15 , sticky="w")
    set_hover_effects(add_ques_gtadmin_btn)


    def search_ques():
        nonlocal ser_or_update

        if vd.is_text_empty(question_ser.get()):  
            messagebox.showerror("QUESTION REVISION APP", "Question ID can't be empty.")
            return
        elif vd.is_not_digit(question_ser.get()):  
            messagebox.showerror("QUESTION REVISION APP", "Question ID can only be number.")
            return
        else:    
            try:
                question = ques.search_question(question_ser.get())
                
            except Exception as ex:
                messagebox.showerror("QUESTION REVISION APP", "Question with given ID not found.")
                question_ser.delete(0, tk.END)
                qid.delete(0, tk.END)
                qid.config(state="normal")
                qid.delete(0, tk.END)
                qid.insert(0, get_next_id(ques.get_questions()))
                qid.config(state="readonly")
                question_in.delete(1.0, tk.END)
                solution_in.delete(1.0, tk.END)
                selected_option.set("Easy")
                dropdown.set(options[0])            
                return           
       
        
        qid.config(state="normal")
        qid.delete(0, tk.END)
        qid.insert(0, question_ser.get())
        qid.config(state="readonly")
        
        ser_or_update = True

        question_in.delete(1.0, tk.END)
        question_in.insert(1.0, question["question"])

        solution_in.delete(1.0, tk.END)
        solution_in.insert(1.0, question["solution"])

        selected_option.set("Easy")
        selected_option.set(question["difficulty"])

        dropdown.set(question["category"])
        
        canvas.yview_moveto(0)
        qid.focus_set() 
    
# This button is added as last cause search_ques must be declared first its command
# And search_ques needs all the qid, question and so on to be initialized first

    add_que_ser_btn = tk.Button(
        frame5,
        text="SEARCH",
        font=("Verdana", 12),
        bg=btn_bg_color,
        fg="white",
        cursor="hand2",
        activebackground=btn_ac_bg_color,
        activeforeground="black",
        command=lambda: search_ques()
    )

    if update_id:
        question_ser.insert(0, update_id)
        search_ques()


    add_que_ser_btn.grid(row=0, column=2, padx=10, sticky="w")
    set_hover_effects(add_que_ser_btn)



def load_frame9(frame, curr=None):

    destroy_all_widgets_exclude(frame)

    frame9.tkraise() 
    frame9.grid_propagate(False) 
    
    canvas1.yview_moveto(0)

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
                    rowheight=150,
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
    tree = ttk.Treeview(
        scrollable_frame1,
        columns=("id", "question", "category", "difficulty"), 
        show="headings", 
        style="Custom.Treeview")

    # Define columns
    tree.heading("id", text="ID", anchor="w")
    tree.heading("question", text="Question", anchor="w")
    tree.heading("category", text="Category", anchor="w")
    tree.heading("difficulty", text="Difficulty", anchor="w")

    tree.column("id", width=50, anchor="center")
    tree.column("question", width=900, anchor="w")
    tree.column("category", width=120, anchor="center")
    tree.column("difficulty", width=120, anchor="center")

    #loading all the questions
    # data = ques.get_questions()
    # # Tag configuration for alternate rows
    # tree.tag_configure('evenrow', background="#f7dec3", foreground="#000000") 
    # tree.tag_configure('oddrow', background="#444444")   

    # for index, (key, item) in enumerate(data.items()):
    #     row = (key, item["question"], item["category"], item["difficulty"] )
    #     tag = 'evenrow' if index % 2 == 0 else 'oddrow'
    #     tree.insert("", "end", values=row, tags=(tag,))

    # tree.grid(row=1, column=0, padx=(25, 10), pady=10, sticky="w")

#paginated links

    total = len(ques.get_questions())

    per_page = 5

    tree.configure(height=per_page)

    last_link = math.ceil(total/per_page)

    if not curr:
        curr = 1

    st_index = (curr-1) * per_page
    if curr == (last_link):
        ed_index = total-1
    else:
        ed_index = st_index + (per_page - 1)
    
    data = ques.get_questions()

    # Convert data.items() to a list for slicing
    items = list(data.items())

    # Clear previous entries from the tree
    for item in tree.get_children():
        tree.delete(item)

    # Tag configuration for alternate rows
    tree.tag_configure('evenrow', background=even_row_table_bg, foreground=even_row_table_fg) 
    tree.tag_configure('oddrow', background=odd_row_table_bg)   

    for index, (key, item) in enumerate(items[st_index: ed_index+1]):
        row = (key, item["question"], item["category"], item["difficulty"] )
        tag = 'evenrow' if index % 2 == 0 else 'oddrow'
        tree.insert("", "end", values=row, tags=(tag,))

    tree.grid(row=1, column=0, padx=(25, 10), pady=10, sticky="w")

    # pagination type 1 without double dotts(..)
    # for link in range(1, last_link+1):
        
    #     li_ques_pag_btn = tk.Button(
    #         frame10,
    #         text=link,
    #         font=("Verdana", 10),
    #         bg=btn_bg_color,
    #         fg="white",
    #         cursor="hand2",
    #         activebackground=btn_ac_bg_color,
    #         activeforeground="black",
    #         command=lambda page=link: load_frame9(frame9, page)
    #     )

    #     if link == curr:
    #         li_ques_pag_btn.config(bg=btn_bg_color1, activebackground=btn_bg_color1, activeforeground="white")     
    #         li_ques_pag_btn.grid(row=1, column=link, padx=1, pady=1 , ipadx=3, ipady=3 , sticky="w")
    #         continue   

    #     li_ques_pag_btn.grid(row=1, column=link, padx=1, pady=1 , ipadx=3, ipady=3 , sticky="w")
    #     set_hover_effects(li_ques_pag_btn)

    before_curr = False
    after_curr = False
    button_col = 1  # Column index for placing buttons

    for link in range(1, last_link + 1):
        show_button = False

        # Decide which buttons to show
        if link == 1 or link == last_link:
            show_button = True
        elif abs(link - curr) <= 2:
            show_button = True
        elif link < curr - 2 and not before_curr:
            # Ellipsis before current
            ellipsis_label = tk.Label(
                frame10,
                text="..",
                font=("Verdana", 10),
                bg=btn_bg_color,
                fg="white"
            )
            ellipsis_label.grid(row=0, column=button_col, padx=2, pady=2, ipadx=6, ipady=6, sticky="w")
            button_col += 1

            before_curr = True
            continue
        elif link > curr + 2 and not after_curr:
            # Ellipsis after current
            ellipsis_label = tk.Label(
                frame10,
                text="..",
                font=("Verdana", 10),
                bg=btn_bg_color,
                fg="white"
            )
            ellipsis_label.grid(row=0, column=button_col, padx=2, pady=2, ipadx=6, ipady=6, sticky="w")
            button_col += 1
            after_curr = True
            continue

        if show_button:
            li_ques_pag_btn = tk.Button(
                frame10,
                text=link,
                font=("Verdana", 10),
                bg=btn_bg_color,
                fg="white",
                cursor="hand2",
                activebackground=btn_ac_bg_color,
                activeforeground="black",
                command=lambda page=link: load_frame9(frame9, page)
            )

            # Highlight the current page
            if link == curr:
                li_ques_pag_btn.config(bg=btn_bg_color1, activebackground=btn_bg_color1, activeforeground="white")
                li_ques_pag_btn.grid(row=0, column=button_col, padx=1, pady=1, ipadx=3, ipady=3, sticky="w")
                button_col += 1
                continue

            li_ques_pag_btn.grid(row=0, column=button_col, padx=1, pady=1, ipadx=3, ipady=3, sticky="w")
            set_hover_effects(li_ques_pag_btn)
            button_col += 1


    li_ques_view= tk.Button(
        frame11,
        text="VIEW QUESTION",
        font=("Verdana", 12),
        bg=btn_bg_color,
        fg="white",
        cursor="hand2",
        activebackground=btn_ac_bg_color,
        activeforeground="black",
        command=lambda: view_question_form()
    )

    def view_question_form():
        selected_items = tree.selection()
        to_view_id = []

        for item in selected_items:
            values = tree.item(item, 'values')
            if values:
                to_view_id.append(values[0])  
        
        if vd.is_list_empty(to_view_id):
            messagebox.showerror("Question Revision App", "Please, select the question(s) first to view.")
            return
        else:          
            load_frame17(frame9, to_view_id)


    li_ques_view.grid(row=0, column=1, padx=(25, 10), pady=15, ipadx=3, ipady=3 , sticky="w")
    set_hover_effects(li_ques_view)

    li_ques_delete= tk.Button(
        frame11,
        text="DELETE QUESTION(S)",
        font=("Verdana", 12),
        bg=btn_bg_color,
        fg="white",
        cursor="hand2",
        activebackground=btn_ac_bg_color,
        activeforeground="black",
        command=lambda: delete_selected_row()
    )
    li_ques_delete.grid(row=0, column=2, padx=(25, 10), pady=15, ipadx=3, ipady=3 , sticky="w")
    set_hover_effects(li_ques_delete)

    def delete_selected_row():
        selected_items = tree.selection()  # Get all selected item IDs
        ids_to_delete = []
        for item in selected_items:
            values = tree.item(item, 'values')
            if values:
                ids_to_delete.append(values[0])   # Safely remove key if it exists

        if vd.is_list_empty(ids_to_delete):
            messagebox.showerror("Question Revision App", "Please, select the question(s) first to delete.")
            return
        else:        
            try:
                ques.delete_selected_row(ids_to_delete)

                for row in tree.get_children():
                    tree.delete(row)

                data = ques.get_questions()

                for index, (key, item) in enumerate(data.items()):
                    row = (key, item["question"], item["category"], item["difficulty"] )
                    tag = 'evenrow' if index % 2 == 0 else 'oddrow'
                    tree.insert("", "end", values=row, tags=(tag,))
                
                tree.yview_moveto(0)
                canvas1.yview_moveto(0)

                messagebox.showinfo("Question Revision App", "Question(s) deleted successfully.")
            
            except Exception as ex:
                print(ex)
                messagebox.showerror("Question Revision App", "Question(s) deletion failed.")       


    li_ques_update= tk.Button(
        frame11,
        text="UPDATE QUESTION",
        font=("Verdana", 12),
        bg=btn_bg_color,
        fg="white",
        cursor="hand2",
        activebackground=btn_ac_bg_color,
        activeforeground="black",
        command=lambda: send_for_update()
    )
    li_ques_update.grid(row=0, column=3, padx=(25, 10), pady=15, ipadx=3, ipady=3 , sticky="w")
    set_hover_effects(li_ques_update)

    def send_for_update():
        selected_item_id = tree.focus()

        # If nothing is selected, tree.focus() returns an empty string
        if not selected_item_id:
            messagebox.showerror("Question Revision App", "Please, select the question first to update.")
            return            
        else:
            item = tree.item(selected_item_id)
            values = item['values']
            to_update_id = values[0]

            load_frame4(frame9, to_update_id)

    li_ques_admin_btn = tk.Button(
        frame11,
        text="GOTO ADMIN",
        font=("Verdana", 12),
        bg=btn_bg_color,
        fg="white",
        cursor="hand2",
        activebackground=btn_ac_bg_color,
        activeforeground="black",
        command=lambda: load_frame3(frame9)
    )
    li_ques_admin_btn.grid(row=0, column=4, padx=(25, 10), pady=15 , sticky="w")
    set_hover_effects(li_ques_admin_btn)

def load_frame12(frame):

    destroy_all_widgets_exclude(frame)

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

    entry1 = tk.Entry(
        frame14,
        width=5,
        font=("Verdana", 12),
        bg=bg_color_txt_fld,
        fg=fg_color1,
        insertbackground=fg_color1
    )
    entry1.grid(row=0, column=1, padx=10, pady= 5, ipadx=5, ipady=5, sticky="w")
   
    tk.Label(
        frame13,
        text="Difficulty",
        bg=bg_color,
        fg=fg_color2,
        font=("Verdana", 15)
    ).grid(row=0, column=0, padx=(25, 10), pady=10, sticky="w")

    # List of options
    checkbox_texts = ["Easy", "Medium", "Hard"]
    checkbox_vars = []

    # Create a Checkbutton for each item
    for index in range(len(checkbox_texts)):
        var = tk.IntVar()  # Variable to store the checkbox state
        checkbox_vars.append(var)
        cb = tk.Checkbutton(
            frame13,
            text=checkbox_texts[index], 
            variable=var, 
            bg = bg_color, 
            fg= fg_color2, 
            selectcolor=bg_color,
            font=("Verdana", 12)
        )
        cb.grid(row=0, column=index+1, padx=(25, 10), pady=5, sticky="w")

    
    tk.Label(
        frame15,
        text="Revised",
        bg=bg_color,
        fg=fg_color2,
        font=("Verdana", 15)
    ).grid(row=0, column=0, padx=(25, 10), pady=10, sticky="w")

    # Variable to store the selected option
    global selected_option_revi 
    selected_option_revi= tk.StringVar(value="any")  # Initially, no option is selected

    tk.Radiobutton(        
        frame15, 
        bg= bg_color,
        fg= fg_color2,
        selectcolor= bg_color,
        font=("Verdana", 12),
        text="Any",
        value="any",         
        variable=selected_option_revi,
        command=lambda: update_entry_state()
    ).grid(row=0, column=1, padx=(25, 10), pady=5, sticky="w")

    tk.Radiobutton(
        frame15, 
        bg= bg_color,
        fg= fg_color2,
        selectcolor= bg_color,
        font=("Verdana", 12),
        text="Less Than",         
        value="less_than",
        variable=selected_option_revi,
        command= lambda: update_entry_state()
    ).grid(row=0, column=2, padx=(25, 10), pady=5, sticky="w")

    
    entry2 = tk.Entry(
        frame15,
        width=3,
        font=("Verdana", 12),
        bg=bg_color_txt_fld,
        fg=fg_color1,
        insertbackground=fg_color1
    )
    entry2.grid(row=0, column=3, padx=10, pady= 5, ipadx=5, ipady=5, sticky="w")
    entry2.config(state="disabled", disabledbackground=bg_color_txt_fld)
    
    def update_entry_state():
        if selected_option_revi.get() == "any":
            entry2.delete(0, tk.END)
            entry2.insert(0, "")
            entry2.config(state="disabled",disabledbackground=bg_color_txt_fld)
        else:
            entry2.config(state="normal",disabledbackground=bg_color_txt_fld)
    
    # List of options
    checkbox_texts1 = ques.get_categories()
    checkbox_vars1 = []
    # Create a Checkbutton for each item
    for index in range(len(checkbox_texts1)):
        var1 = tk.IntVar()  # Variable to store the checkbox state
        checkbox_vars1.append(var1)
        cb = tk.Checkbutton(
            frame16,
            text=checkbox_texts1[index], 
            variable=var1, 
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
        command=lambda: get_selected_questions()
    )
    ques_gene_btn.grid(row=6, column=0, padx=(25, 10), pady=15 , sticky="w")
    set_hover_effects(ques_gene_btn)

    def get_selected_questions():
        
        selected_difficulties = [checkbox_texts[i] for i in range(len(checkbox_texts)) if checkbox_vars[i].get() == 1]
       
        revised_times = selected_option_revi.get()
        if revised_times == "any":
            rev = -1
        else:
            if vd.is_text_empty(entry2.get()):
                messagebox.showerror("Question Revision App", "Please, enter revised less than.")
                return
            elif vd.is_not_digit(entry2.get()):
                messagebox.showerror("Question Revision App", "Please, revised less than must be digit.")
                return
            else:
                rev = int(entry2.get())
       
        selected_categories = [checkbox_texts1[i] for i in range(len(checkbox_texts1)) if checkbox_vars1[i].get() == 1]
        
        
        if vd.is_list_empty(entry1.get()):
            messagebox.showerror("Question Revision App", "Please, enter no of questions to be generated.")
            return
        elif vd.is_not_digit(entry1.get()):
            messagebox.showerror("Question Revision App", "Please, no of questions to be generated must be digit.")
            return
        elif vd.are_all_checkboxes_unselected(checkbox_vars):
            messagebox.showerror("Question Revision App", "Please, select at least one difficulty.")
            return
        elif vd.are_all_checkboxes_unselected(checkbox_vars1):
            messagebox.showerror("Question Revision App", "Please, select at least one category.")
            return
        else:
 
            selected_questions = ques.search_questions_by_categories(int(entry1.get()), selected_categories, selected_difficulties, rev)
            load_frame17(frame12, list(selected_questions.keys()))


    gen_back_btn = tk.Button(
        frame12,
        text="GOTO ADMIN",
        font=("Verdana", 12),
        bg=btn_bg_color,
        fg="white",
        cursor="hand2",
        activebackground=btn_ac_bg_color,
        activeforeground="black",
        command=lambda: load_frame3(frame12)
    )
    gen_back_btn.grid(row=6, column=0, padx=(300, 10), pady=15 , sticky="w")
    set_hover_effects(gen_back_btn)

def load_frame17(frame, to_view_id=None):
    curr_index = 0    
    question = None
    
    destroy_all_widgets_exclude(frame)

    frame17.tkraise() 
    frame17.grid_propagate(False) 
    frame20.grid_propagate(False)
    
    tk.Label(
        frame18,
        text="Question ID",
        bg=bg_color,
        fg=fg_color2,
        font=("Verdana", 15)
    ).grid(row=0, column=0, padx=(25, 10), pady=10, sticky="w")

    id_lbl = tk.Label(
        frame18,
        text="38",
        bg=bg_color,
        fg=fg_color1,
        font=("Verdana", 15)
    )
    id_lbl.grid(row=0, column=1, padx=(0, 10), pady=10, sticky="w")

    tk.Label(
        frame18,
        text="Difficulty",
        bg=bg_color,
        fg=fg_color2,
        font=("Verdana", 15)
    ).grid(row=0, column=2, padx=(100, 10), pady=10, sticky="w")

    diff_lbl = tk.Label(
        frame18,
        text="HARD",
        bg=bg_color,
        fg=fg_color1,
        font=("Verdana", 15)
    )
    diff_lbl.grid(row=0, column=3, padx=(0, 10), pady=10, sticky="w")

    tk.Label(
        frame18,
        text="Solved",
        bg=bg_color,
        fg=fg_color2,
        font=("Verdana", 15)
    ).grid(row=0, column=4, padx=(100, 10), pady=10, sticky="w")

    sol_lvl = tk.Label(
        frame18,
        text="5 times",
        bg=bg_color,
        fg=fg_color1,
        font=("Verdana", 15)
    )
    sol_lvl.grid(row=0, column=5, padx=(0, 10), pady=10, sticky="w")

    tk.Label(
        frame18,
        text="Question",
        bg=bg_color,
        fg=fg_color2,
        font=("Verdana", 15)
    ).grid(row=0, column=6, padx=(100, 10), pady=10, sticky="w")

    curr_index_lbl = tk.Label(
        frame18,
        text="0",
        bg=bg_color,
        fg=fg_color1,
        font=("Verdana", 15)
    )
    curr_index_lbl.grid(row=0, column=7, padx=(0, 10), pady=10, sticky="w")

    tk.Label(
        frame18,
        text="out of",
        bg=bg_color,
        fg=fg_color2,
        font=("Verdana", 15)
    ).grid(row=0, column=8, padx=(0, 10), pady=10, sticky="w")

    tot_selected_lbl = tk.Label(
        frame18,
        text="0",
        bg=bg_color,
        fg=fg_color1,
        font=("Verdana", 15)
    )
    tot_selected_lbl.grid(row=0, column=9, padx=(0, 10), pady=10, sticky="w")

    view_ques_btn = tk.Button(
        frame19,
        text="VIEW QUESTION",
        font=("Verdana", 12),
        bg=btn_bg_color,
        fg="white",
        cursor="hand2",
        activebackground=btn_ac_bg_color,
        activeforeground="black",
        command=lambda: show_question()
    )
    view_ques_btn.grid(row=0, column=0, padx=(25, 10), pady=15 , sticky="w")
    set_hover_effects(view_ques_btn)

    view_soln_btn = tk.Button(
        frame19,
        text="VIEW SOLUTION",
        font=("Verdana", 12),
        bg=btn_bg_color,
        fg="white",
        cursor="hand2",
        activebackground=btn_ac_bg_color,
        activeforeground="black",
        command=lambda: show_solution()
    )
    view_soln_btn.grid(row=0, column=1, padx=(25, 10), pady=15 , sticky="w")
    set_hover_effects(view_soln_btn)

    add_revised_btn = tk.Button(
        frame19,
        text="ADD REVISED",
        font=("Verdana", 12),
        bg=btn_bg_color,
        fg="white",
        cursor="hand2",
        activebackground=btn_ac_bg_color,
        activeforeground="black",
        command=lambda: add_revised()
    )
    add_revised_btn.grid(row=0, column=2, padx=(25, 10), pady=15 , sticky="w")
    set_hover_effects(add_revised_btn)

    def add_revised():
        new_revised = ques.add_revised(str(id_lbl.cget("text")))
        sol_lvl.config(text = new_revised)
        

    del_ques_btn = tk.Button(
        frame19,
        text="DELETE QUESTiON",
        font=("Verdana", 12),
        bg=btn_bg_color,
        fg="white",
        cursor="hand2",
        activebackground=btn_ac_bg_color,
        activeforeground="black",
        command=lambda: delete_question()
    )

    def delete_question():
        nonlocal curr_index
        nonlocal question
        try:
            ques.delete_one_row(str(id_lbl.cget("text")))
            messagebox.showinfo("Question Revision App", "Question deletion successful.")

            to_view_id.remove(str(id_lbl.cget("text")))
            
            if len(to_view_id) == 0 :
                load_frame9(frame12)
            else:
                curr_index = 0
                
                curr_index_lbl.config(text = curr_index + 1)
                tot_selected_lbl.config(text = len(to_view_id))

                question = ques.search_question(str(to_view_id[curr_index]))
                id_lbl.config(text = to_view_id[curr_index])
                diff_lbl.config(text = question["difficulty"])
                sol_lvl.config(text = question["revised"])

                ques_sol_txt.delete("1.0", tk.END)
                ques_sol_txt.insert("1.0", question["question"])

            
        except Exception as ex:
            print(ex)
            messagebox.showerror("Question Revision App", "Sorry, question deletion failed.")     


    del_ques_btn.grid(row=0, column=3, padx=(25, 10), pady=15 , sticky="w")
    set_hover_effects(del_ques_btn)

    view_ques_btn = tk.Button(
        frame19,
        text="GOTO ADMIN",
        font=("Verdana", 12),
        bg=btn_bg_color,
        fg="white",
        cursor="hand2",
        activebackground=btn_ac_bg_color,
        activeforeground="black",
        command=lambda: load_frame3(frame19)
    )
    view_ques_btn.grid(row=0, column=4, padx=(25, 10), pady=15 , sticky="w")
    set_hover_effects(view_ques_btn)

    ques_sol_txt = tk.Text(
        frame17,
        width=110,
        height=15,
        font=("Verdana", 12),
        bg=bg_color_txt_fld,
        fg=fg_color1,
        insertbackground=fg_color1
    )
    ques_sol_txt.grid(row=2, column=0, columnspan=25, padx=(25, 10), pady=5, ipadx=5, ipady=5, sticky="w")


    prev_ques_btn = tk.Button(
        frame20,
        text="PREVIOUS QUESTION",
        font=("Verdana", 12),
        bg=btn_bg_color,
        fg="white",
        cursor="hand2",
        activebackground=btn_ac_bg_color,
        activeforeground="black",
        command=lambda: show_previous()
    )
    prev_ques_btn.grid(row=0, column=0, padx=(25, 10), pady=15)
    set_hover_effects(prev_ques_btn)

    def show_previous():
        nonlocal curr_index
        nonlocal question

        if curr_index > 0:
            curr_index -= 1

            curr_index_lbl.config(text = curr_index + 1)
            tot_selected_lbl.config(text = len(to_view_id))

            question = ques.search_question(str(to_view_id[curr_index]))
            id_lbl.config(text = to_view_id[curr_index])
            diff_lbl.config(text = question["difficulty"])
            sol_lvl.config(text = question["revised"])

            ques_sol_txt.delete("1.0", tk.END)
            ques_sol_txt.insert("1.0", question["question"])
        else:
            messagebox.showwarning("Question Revision App", "No previous question to show.")

    
    next_ques_btn = tk.Button(
        frame20,
        text="NEXT QUESTION",
        font=("Verdana", 12),
        bg=btn_bg_color,
        fg="white",
        cursor="hand2",
        activebackground=btn_ac_bg_color,
        activeforeground="black",
        command=lambda: show_next()
    )
    next_ques_btn.grid(row=0, column=1, padx=(750, 10), pady=15)
    set_hover_effects(next_ques_btn)

    def show_next():
        nonlocal curr_index
        nonlocal question

        if curr_index < len(to_view_id)-1:
            curr_index += 1
            question = ques.search_question(str(to_view_id[curr_index]))

            curr_index_lbl.config(text = curr_index + 1)
            tot_selected_lbl.config(text = len(to_view_id))

            id_lbl.config(text = to_view_id[curr_index])
            diff_lbl.config(text = question["difficulty"])
            sol_lvl.config(text = question["revised"])

            ques_sol_txt.delete("1.0", tk.END)
            ques_sol_txt.insert("1.0", question["question"])
        else:
            messagebox.showwarning("Question Revision App", "No next question to show.")

        
    curr_index_lbl.config(text = curr_index + 1)
    tot_selected_lbl.config(text = len(to_view_id))

    question = ques.search_question(str(to_view_id[curr_index]))
    
    id_lbl.config(text = to_view_id[curr_index])
    diff_lbl.config(text = question["difficulty"])
    sol_lvl.config(text = question["revised"])

    ques_sol_txt.delete("1.0", tk.END)
    ques_sol_txt.insert("1.0", question["question"])
    

    def show_question():
        ques_sol_txt.delete("1.0", tk.END)
        ques_sol_txt.insert("1.0", question["question"])
    
    def show_solution():
        ques_sol_txt.delete("1.0", tk.END)
        ques_sol_txt.insert("1.0", question["solution"])



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


# 👀frame17 is for view question

frame17 = tk.Frame(root, width=window_width, height=window_height-150, bg=bg_color)
frame17.grid(row=1, column=0, sticky="nsew")

# 👀frame18 is for view question qid, difficulty and solved times

frame18 = tk.Frame(frame17, width=window_width, height=100, bg=bg_color)
frame18.grid(row=0, column=0, sticky="w")

# 👀frame19 is for question qenerator revised

frame19 = tk.Frame(frame17, width=window_width, height=100, bg=bg_color)
frame19.grid(row=1, column=0, sticky="w")

# 👀frame20 is for question qenerator revised

frame20 = tk.Frame(frame17, width=window_width, height=75, bg=bg_color)
frame20.grid(row=3, column=0, sticky="nsew")

load_frame1()
load_frame3(None)

root.mainloop()