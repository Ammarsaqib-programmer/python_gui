import tkinter as tk
from tkinter import ttk, messagebox, PhotoImage
from instaloader import Instaloader, Profile
import threading
import webbrowser
from urllib.request import urlopen
from io import BytesIO
from PIL import Image, ImageTk
import os

class InstagramViewerPro:
    def __init__(self, root):
        self.root = root
        self.root.title("Instagram Profile Viewer Pro")
        self.root.geometry('800x600')
        self.root.minsize(700, 550)
        self.root.configure(bg='#f5f5f5')
        
        self.L = Instaloader()
        self.profile_data = None
        self.profile_image = None
        
        try:
            self.L.load_session_from_file("YOUR_USERNAME")  # Replace with your Instagram username
        except Exception as e:
            print(f"Couldn't load session: {e}")
        
        self.setup_ui()
    
    def setup_ui(self):
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Header
        header_frame = ttk.Frame(main_frame)
        header_frame.pack(fill=tk.X, pady=(0, 20))
        
        ttk.Label(header_frame, text="Instagram Profile Viewer", 
                font=('Helvetica', 16, 'bold')).pack(side=tk.LEFT)
        
        search_frame = ttk.LabelFrame(main_frame, text="Search Profile", padding=10)
        search_frame.pack(fill=tk.X, pady=(0, 20))
        
        self.username_entry = ttk.Entry(search_frame, width=40)
        self.username_entry.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=(0, 10))
        
        search_btn = ttk.Button(search_frame, text="Search", command=self.start_search)
        search_btn.pack(side=tk.RIGHT)
        
        display_frame = ttk.Frame(main_frame)
        display_frame.pack(fill=tk.BOTH, expand=True)
        
        self.left_panel = ttk.Frame(display_frame, width=200, relief=tk.RIDGE)
        self.left_panel.pack(side=tk.LEFT, fill=tk.Y, padx=(0, 10))
        self.left_panel.pack_propagate(False)
        
        self.profile_image_label = ttk.Label(self.left_panel)
        self.profile_image_label.pack(pady=20)
        
        view_image_btn = ttk.Button(
            self.left_panel, 
            text="View Full Image", 
            command=self.show_profile_pic,
            state=tk.DISABLED
        )
        view_image_btn.pack(pady=10)
        self.view_image_btn = view_image_btn
        
        self.right_panel = ttk.Frame(display_frame)
        self.right_panel.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        
        self.notebook = ttk.Notebook(self.right_panel)
        self.notebook.pack(fill=tk.BOTH, expand=True)
        
        # Profile Info tab
        self.info_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.info_tab, text="Profile Info")
        
        self.details_text = tk.Text(
            self.info_tab, 
            wrap=tk.WORD, 
            font=('Segoe UI', 10), 
            padx=10, 
            pady=10,
            state=tk.DISABLED
        )
        self.details_text.pack(fill=tk.BOTH, expand=True)
        
        # Stats tab
        self.stats_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.stats_tab, text="Statistics")
        
        self.stats_canvas = tk.Canvas(self.stats_tab)
        self.scrollbar = ttk.Scrollbar(self.stats_tab, orient="vertical", command=self.stats_canvas.yview)
        self.scrollable_frame = ttk.Frame(self.stats_canvas)
        
        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.stats_canvas.configure(
                scrollregion=self.stats_canvas.bbox("all")
            )
        )
        
        self.stats_canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.stats_canvas.configure(yscrollcommand=self.scrollbar.set)
        
        self.stats_canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")
        
        # Status bar
        self.status_var = tk.StringVar()
        self.status_bar = ttk.Label(
            self.root, 
            textvariable=self.status_var,
            relief=tk.SUNKEN,
            anchor=tk.W
        )
        self.status_bar.pack(fill=tk.X)
    
    def start_search(self):
        username = self.username_entry.get().strip()
        if not username:
            messagebox.showwarning("Warning", "Please enter a username")
            return
        
        self.status_var.set(f"Fetching data for @{username}...")
        self.root.config(cursor="watch")
        
        self.clear_display()
        
        # Run in a separate thread
        threading.Thread(
            target=self.fetch_profile_data,
            args=(username,),
            daemon=True
        ).start()
    
    def fetch_profile_data(self, username):
        try:
            profile = Profile.from_username(self.L.context, username)
            
            self.profile_data = {
                'username': profile.username,
                'userid': profile.userid,
                'followers': profile.followers,
                'following': profile.followees,
                'full_name': profile.full_name,
                'posts': profile.mediacount,
                'is_private': profile.is_private,
                'is_verified': profile.is_verified,
                'is_business': profile.is_business_account,
                'external_url': profile.external_url,
                'bio': profile.biography,
                'profile_pic_url': profile.profile_pic_url
            }
            
            # Try to download profile picture
            self.download_profile_pic()
            
            # Update UI
            self.root.after(0, self.display_profile_data)
            
        except Exception as e:
            self.root.after(0, self.show_error, str(e))
        finally:
            self.root.after(0, self.reset_ui)
    
    def download_profile_pic(self):
        if not self.profile_data or not self.profile_data['profile_pic_url']:
            return
            
        try:
            with urlopen(self.profile_data['profile_pic_url']) as response:
                image_data = response.read()
            
            image = Image.open(BytesIO(image_data))
            image.thumbnail((180, 180))
            self.profile_image = ImageTk.PhotoImage(image)
        except Exception as e:
            print(f"Error downloading profile picture: {e}")
            self.profile_image = None
    
    def display_profile_data(self):
        if not self.profile_data:
            return
        
        data = self.profile_data
        
        # Display profile picture
        if self.profile_image:
            self.profile_image_label.config(image=self.profile_image)
            self.view_image_btn.config(state=tk.NORMAL)
        else:
            self.profile_image_label.config(image='')
            self.view_image_btn.config(state=tk.DISABLED)
        
        # Display profile info
        self.details_text.config(state=tk.NORMAL)
        self.details_text.delete(1.0, tk.END)
        
        info_text = f"""
        {'✓ Verified' if data['is_verified'] else ''} {'🔒 Private' if data['is_private'] else ''} {'💼 Business' if data['is_business'] else ''}
        
        📌 {data['full_name']}
        👤 @{data['username']}
        🔗 {data['external_url'] or 'No link'}
        
        📝 Bio:
        {data['bio']}
        
        """
        self.details_text.insert(tk.END, info_text.strip())
        self.details_text.config(state=tk.DISABLED)
        
        # Display stats
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()
        
        stats = [
            ("📸 Posts", data['posts']),
            ("👥 Followers", data['followers']),
            ("🫂 Following", data['following']),
            ("🆔 User ID", data['userid'])
        ]
        
        for i, (label, value) in enumerate(stats):
            ttk.Label(
                self.scrollable_frame,
                text=f"{label}:",
                font=('Segoe UI', 10, 'bold')
            ).grid(row=i, column=0, sticky=tk.W, padx=5, pady=2)
            
            ttk.Label(
                self.scrollable_frame,
                text=f"{value:,}" if isinstance(value, int) else value,
                font=('Segoe UI', 10)
            ).grid(row=i, column=1, sticky=tk.W, padx=5, pady=2)
        
        self.status_var.set(f"Successfully loaded @{data['username']}'s profile")
    
    def show_profile_pic(self):
        if self.profile_data and self.profile_data['profile_pic_url']:
            webbrowser.open(self.profile_data['profile_pic_url'])
    
    def clear_display(self):
        self.profile_image_label.config(image='')
        self.view_image_btn.config(state=tk.DISABLED)
        self.details_text.config(state=tk.NORMAL)
        self.details_text.delete(1.0, tk.END)
        self.details_text.config(state=tk.DISABLED)
        
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()
    
    def show_error(self, error_msg):
        messagebox.showerror("Error", f"Failed to fetch profile:\n{error_msg}")
        self.status_var.set("Error fetching profile data")
    
    def reset_ui(self):
        self.root.config(cursor="")
        if not self.profile_data:
            self.status_var.set("Ready")

if __name__ == "__main__":
    root = tk.Tk()
    app = InstagramViewerPro(root)
    root.mainloop()
