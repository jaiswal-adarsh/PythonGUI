import customtkinter as ckt
import tkinter as tk

ckt.set_appearance_mode("dark")
ckt.set_default_color_theme("dark-blue")

root=ckt.CTk()
root.geometry("500x350")
root.title("Login")

def login():
    print("login Page")

frame=ckt.CTkFrame(master=root,width=300,height=500)
frame.pack(pady=20,padx=60,fill="both",expand=True)

label=ckt.CTkLabel(master=frame,text="Login Page")
label.pack(pady=12,padx=10)

entry1=ckt.CTkEntry(master=frame, placeholder_text="Username")
entry1.pack(pady=12,padx=10)
entry2=ckt.CTkEntry(master=frame, placeholder_text="Password")
entry2.pack(pady=12,padx=10)

button=ckt.CTkButton(master=frame,text="Login")
button.pack(pady=12,padx=10)

checkbox=ckt.CTkCheckBox(master=frame,text="Remember Me")
checkbox.pack(pady=12,padx=10)







root.mainloop()