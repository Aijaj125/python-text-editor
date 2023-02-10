from tkinter import *
from tkinter import filedialog, messagebox
import os
file_path = ""
current_file_path = ""


class UiInterFace():
    def file_title(self):
        pass
        
        
        
    def open_file_dialog(self):
        global file_path
        
        if self.text.get("1.0", "end") == "":
            # self.text.delete("1.0", "end")
            file_path = filedialog.askopenfilename(defaultextension=".txt",
                                        filetypes=[("Text Files", "*.txt"),
                                                    ("All Files", "*.*")])
            with open(file_path, "r") as file:
                contents = file.read()
                self.text.insert("1.0", contents)
                
        elif self.text.get("1.0", "end") != "":
            msg = messagebox.askyesnocancel("Save File", "Do you want to save the changes to the file?")
            if msg == True:
                
                self.save_file_dialog()
            elif msg == False:
                self.text.delete("1.0", "end")
                file_path = filedialog.askopenfilename(defaultextension=".txt",
                                        filetypes=[("Text Files", "*.txt"),
                                                    ("All Files", "*.*")])
                with open(file_path, "r") as file:
                    contents = file.read()
                    self.text.insert("1.0", contents)
                
        
    
    def save_file_dialog(self):
        global current_file_path
        if current_file_path == "":
            return self.save_file_as()
        else:
            current_file_path = file_path
            with open(current_file_path, "w") as file:
                contents = self.text.get("1.0", "end")
                file.write(contents)
    
    def save_file_as(self):
        global current_file_path
        file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                                 filetypes=[("Text Files", "*.txt"),
                                                            ("All Files", "*.*")])
        current_file_path = file_path
        with open(current_file_path, "w") as file:
            contents = self.text.get("1.0", "end")
            file.write(contents)
                    
    def __init__(self):
        
        self.window = Tk()
        window_title = self.file_title()
        self.window.title(f"{window_title}")
        
        self.menu_bar = Menu(self.window)
        
        #file menu
        
        file_menu = Menu(self.menu_bar, tearoff=0)
        file_menu.add_command(label="New File",)
        file_menu.add_command(label="Open File", command=self.open_file_dialog)
        file_menu.add_command(label="Save File", command=self.save_file_dialog)
        file_menu.add_command(label="Save As" ,command=self.save_file_as)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.window.quit)
        
        #Edit menu
        
        edit_menu = Menu(self.menu_bar, tearoff=0)
        edit_menu.add_command(label="Undo")
        
        
        
        self.menu_bar.add_cascade(label="File", menu = file_menu)
        self.menu_bar.add_cascade(label="Edit", menu = edit_menu)
        self.window.config(menu = self.menu_bar)
        
        self.text= Text()
        self.text.pack(expand=True, fill=BOTH)

        self.window.mainloop()
   


        