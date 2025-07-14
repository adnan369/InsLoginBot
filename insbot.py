
import tkinter as tk
from tkinter import messagebox
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import threading
import time

def login_instagram(username, password, status_label):
    service = Service('chromedriver')
    options = webdriver.ChromeOptions()
    options.add_argument('--start-maximized')

    driver = webdriver.Chrome(service=service, options=options)

    try:
        status_label.config(text="🔄 Opening Instagram...", fg="#555")
        driver.get('https://www.instagram.com/accounts/login/')
        time.sleep(5)

        driver.find_element(By.NAME, "username").send_keys(username)
        driver.find_element(By.NAME, "password").send_keys(password)
        driver.find_element(By.XPATH, "//button[@type='submit']").click()

        status_label.config(text="🔐 Logging in...", fg="#555")
        time.sleep(8)
        status_label.config(text="✅ Login successful (if credentials are correct)", fg="green")

    except Exception as e:
        status_label.config(text=f"❌ Error: {e}", fg="red")
    finally:
        time.sleep(5)
        driver.quit()
        status_label.config(text="🧹 Browser closed.", fg="#555")

def start_login_thread(username_entry, password_entry, status_label):
    username = username_entry.get()
    password = password_entry.get()

    if not username or not password:
        messagebox.showwarning("Input Error", "Please enter both username and password!")
        return

    thread = threading.Thread(target=login_instagram, args=(username, password, status_label))
    thread.start()

# --- GUI Setup like Instagram ---
root = tk.Tk()
root.title("Instagram")
root.geometry("320x400")
root.config(bg="white")

# Instagram logo-style heading
tk.Label(root, text="Instagram", font=("Helvetica", 24, "bold"), bg="white", fg="#000").pack(pady=30)

# Username field
username_entry = tk.Entry(root, width=30, font=("Helvetica", 10), bd=1, relief="solid")
username_entry.insert(0, "Username")
username_entry.pack(pady=8)

# Password field
password_entry = tk.Entry(root, width=30, font=("Helvetica", 10), bd=1, relief="solid", show="*")
password_entry.insert(0, "")
password_entry.pack(pady=8)

# Login button styled like Instagram
tk.Button(root, text="Log In", command=lambda: start_login_thread(username_entry, password_entry, status_label),
          font=("Helvetica", 10, "bold"), bg="#3897f0", fg="white", width=28, pady=5).pack(pady=12)

# Status label below
status_label = tk.Label(root, text="", bg="white", fg="#555", font=("Helvetica", 9))
status_label.pack(pady=10)

# Footer
tk.Label(root, text="© Meta • Instagram", font=("Helvetica", 8), bg="white", fg="#999").pack(side="bottom", pady=20)

root.mainloop()
op()
