import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox

# 🔖 Categories and their file extensions
FILE_CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".pptx", ".xlsx"],
    "Audio": [".mp3", ".wav", ".m4a"],
    "Videos": [".mp4", ".mkv", ".mov", ".avi"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Scripts": [".py", ".js", ".html", ".css", ".java", ".cpp"],
    "Others": []
}

def get_category(file_extension):
    """
    Determines the category for a file based on its extension.
    """
    for category, extensions in FILE_CATEGORIES.items():
        if file_extension.lower() in extensions:
            return category
    return "Others"

def organize_folder(folder_path):
    """
    Organizes files in the selected folder into subfolders based on category.
    """
    if not os.path.exists(folder_path):
        messagebox.showerror("Error", "❌ Folder path does not exist.")
        return

    file_count = 0

    # Loop through all files in the folder
    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)

        # Skip if it's already a folder
        if os.path.isdir(file_path):
            continue

        _, file_extension = os.path.splitext(file_name)
        category = get_category(file_extension)

        # Create category folder if needed
        category_folder = os.path.join(folder_path, category)
        os.makedirs(category_folder, exist_ok=True)

        # Move the file
        new_file_path = os.path.join(category_folder, file_name)
        shutil.move(file_path, new_file_path)
        file_count += 1

    messagebox.showinfo("Success", f"🎉 Organized {file_count} files!")

def browse_folder():
    """
    Opens file dialog to choose a folder and triggers organization.
    """
    folder_path = filedialog.askdirectory()
    if folder_path:
        organize_folder(folder_path)

# 🖥️ GUI Layout
root = tk.Tk()
root.title("🗂️ File Organizer Bot")
root.geometry("400x200")
root.config(bg="#f4f4f4")

# Title
title_label = tk.Label(root, text="🧠 Organize Your Files by Type", font=("Helvetica", 14, "bold"), bg="#f4f4f4")
title_label.pack(pady=20)

# Button to choose folder
browse_button = tk.Button(
    root,
    text="📁 Choose Folder to Organize",
    command=browse_folder,
    font=("Helvetica", 12),
    bg="#4CAF50",
    fg="white",
    padx=10,
    pady=5
)
browse_button.pack(pady=10)

# Start the GUI loop
root.mainloop()
