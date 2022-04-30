from cgitb import text
from re import T
from sys import flags
import tkinter as tk
from tkinter import RAISED, Button, Canvas, Image, Label, PhotoImage, Tk, Toplevel, YView, ttk
from tkinter import font,colorchooser,filedialog,messagebox
import os,shutil
from turtle import back, delay, title, width
from numpy import var
from PIL import ImageTk,Image
from pip import main


main_application=tk.Tk()
main_application.title('LAXMAN FILE ORGANIZER')
main_application.resizable(width=False,height=False)


# background wallpaper
image1=Image.open("bg.jpg")
bground=ImageTk.PhotoImage(image1)
w = bground.width()
h = bground.height()
main_application.geometry('%dx%d+0+0' % (w,h))
backg=Label(main_application,image=bground)
backg.place(x=0,y=0)

# Create a label
browse_label=tk.Label(
    main_application,
    text='Choose a folder to organize',font='Arial 15 bold italic underline',
    foreground='Green',
    bg='#2db2d6',
    highlightbackground="#5497b8",
    highlightthickness=2,
    bd=3
    )
browse_label.pack(pady= 8)
####### create browse button########

def on_enter(e):
    browse_button['background'] = '#6fcfd6'
def on_leave(e):
    browse_button['background'] = '#77a9bf'

browse_button=tk.Button(
    main_application,text='BROWSE',
    font=('Calibri 15 bold'),
    width=20,height=3,
    background='#77a9bf',
    activebackground='#0a73a1',
    activeforeground='blue',
    relief=RAISED,
    wraplength='2c',
    highlightbackground="#5497b8",
    highlightthickness=20,
    bd=5
)

browse_button.bind("<Enter>", on_enter)
browse_button.bind("<Leave>", on_leave)

browse_button.pack(pady=30)


def browse_func():
    feedback =filedialog.askdirectory(initialdir=os.getcwd(),title='Select Folder')
    print(feedback)
    dict_extension={
    'Audio_extension':('.mp3','.m4a','.wav','.flac','.aac','.wav','.wma'),
    'Video_extension':('.mp4','.mov','.wmv','.avi','.avchd','.flv','.f4v','.swf','.mkv','.webm','mpeg-2'),
    'Document_extension':('.doc','.docx','.pdf','.txt','.pptx','.htm','.odt','.xls','.xlsx','.ods','.ppt','.webp'),
    'Coding_extension':('.py','.js','.css','.html','.cpp','.c','.java'),
    'Image_extension':('.jpg','.png','.jpeg','.RAW','.gif','.tiff','.psd','.eps','.ai','.ind'),
    'Compressed_extension':('.zip','.rar'),
    'WindowsApp_extension':('.exe','.msi')
    }

    def file_finder(folder_path,file_extension):
        files=[]
        for file in os.listdir(folder_path):
            for extension in file_extension:
                if file.endswith(extension):
                    files.append(file)
        return files

    if feedback:
        for extension_type,extension_tuple in dict_extension.items():
            folder_name=extension_type.split('_')[0]+'Files'
            folder_path=os.path.join(feedback,folder_name)
            if os.path.exists(folder_path):
                mbox=messagebox.askyesno(
                    'ASKING',
                    f'{folder_name} Folder already exists!\nDo you want to move the file to \nexisting {folder_name} folder?'
                    )
                if mbox is True:
                    for items in file_finder(feedback,extension_tuple):
                        item_path=os.path.join(feedback,items)
                        item_new_path=os.path.join(folder_path,items)
                        shutil.move(item_path,item_new_path)
                    
                elif mbox is False:
                    mbox2=messagebox.askyesno(
                    'ASKING',
                    'Do you Want to Create a New Folder?'
                    )
                    flag=True
                    while flag:
                        if mbox2 is True:
                            flag=True
                            while flag:
                                pop=Toplevel(main_application)
                                pop.geometry("400x250")
                                pop.configure(background="#73568f")

                                f_var=tk.StringVar()
                                f_entry=tk.Entry(
                                    pop,
                                    width=25,
                                    foreground="#9e4ca6",
                                    font='Arial 15 bold',
                                    textvariable=f_var)
                                f_entry.pack()
                                f_entry.focus()

                                def action():
                                    given_f=f_var.get()
                                    new_p=os.path.join(folder_path,given_f)
                                    if os.path.exists(new_p):
                                        top=Toplevel(main_application)
                                        top.geometry("200x200")
                                        top_label=tk.Label(top,text=f'{given_f} folder also already exists!')
                                        top_label.pack()
                                        top.after(2000,top.destroy)
                                    else:
                                        os.makedirs(new_p, exist_ok=True)
                                        tk.Label(
                                            pop,
                                            text=f"{new_p} folder created succesfully!",
                                            font='Arial 10 bold',
                                            background='#2a62bd',
                                            fg="White"
                                            )
                                        for items in file_finder(feedback,extension_tuple):
                                            item_path2=os.path.join(feedback,items)
                                            item_new_path2=os.path.join(new_p,items)
                                            shutil.move(item_path2,item_new_path2)
                                        print(new_p)
                                        pop.after(1500,pop.destroy)
                                submit_button=ttk.Button(
                                    pop,
                                    text='Submit',
                                    command=action
                                    )
                                submit_button.pack()
                                
                                return False
                        elif mbox2 is False:
                            return False
                        return False
            else:
                os.makedirs(folder_path)
                # created=Toplevel(main_application)
                # created.geometry("200x150")
                Label(main_application,text=f"{folder_name} Folder created successfully!",pady=10,font='Arial 7 bold',bg="red").pack()
                # main_application.wm_attributes(("-transparentcolor", 'grey'))
                print(f"{folder_name} Folder created successfully!")
            for items in file_finder(feedback,extension_tuple):
                item_path=os.path.join(feedback,items)
                item_new_path=os.path.join(folder_path,items)
                shutil.move(item_path,item_new_path)
                print(item_new_path)
    else:
        return

browse_button.configure(command=browse_func)


# main_application.config(menu=main_menu)
main_application.mainloop()