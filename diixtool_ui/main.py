"""
DiixTool UI - Official Graphical Interface for DiixTool Framework

Theme: Dark Black
Architecture: MVC/MVP
CustomTkinter 6.x Compatible
"""

import customtkinter as ctk
from tkinter import messagebox
import sys
import os

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from ui.config.theme import THEME_CONFIG
from ui.pages.dashboard import DashboardPage


class DiixToolUI(ctk.CTk):
    """Main Application Window - CustomTkinter 6.x"""
    
    def __init__(self):
        super().__init__()
        
        # Configure main window
        self.title("DiixTool UI")
        self.geometry("1400x900")
        self.minsize(1200, 700)
        
        # Set dark theme using CustomTkinter 6.x API
        ctk.set_appearance_mode("Dark")
        ctk.set_default_color_theme("dark-blue")
        
        # Configure grid layout
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)
        
        # Initialize components
        self._create_menubar()
        self._create_sidebar()
        self._create_main_area()
        self._create_statusbar()
        
        # Load dashboard by default
        self._load_page("dashboard")
    
    def _create_menubar(self):
        """Create top menu bar using CTkFrame"""
        self.menubar = ctk.CTkFrame(
            self, 
            height=40, 
            fg_color=THEME_CONFIG["bg_panel"],
            corner_radius=0
        )
        self.menubar.grid(row=0, column=0, columnspan=2, sticky="ew")
        self.menubar.grid_propagate(False)
        
        # Menu items
        menus = ["Arquivo", "ADB", "Ferramentas", "Visualizar", "Ajuda"]
        
        for i, menu in enumerate(menus):
            btn = ctk.CTkButton(
                self.menubar, 
                text=menu,
                width=100,
                height=30,
                fg_color="transparent",
                hover_color=THEME_CONFIG["hover"],
                text_color=THEME_CONFIG["text_primary"],
                anchor="w",
                corner_radius=6,
                command=lambda m=menu: self._show_menu(m)
            )
            btn.grid(row=0, column=i, padx=5, pady=5)
    
    def _create_sidebar(self):
        """Create left sidebar using CTkScrollableFrame"""
        self.sidebar = ctk.CTkScrollableFrame(
            self, 
            width=220, 
            fg_color=THEME_CONFIG["bg_sidebar"],
            scrollbar_button_color=THEME_CONFIG["hover"],
            corner_radius=0
        )
        self.sidebar.grid(row=1, column=0, sticky="ns", pady=(0, 40))
        self.sidebar.grid_propagate(False)
        
        # Sidebar items with icons
        sidebar_items = [
            ("🏠 Dashboard", "dashboard"),
            ("📱 Dispositivos", "devices"),
            ("📦 Aplicativos", "apps"),
            ("📑 Package Info", "package_info"),
            ("🧩 Activities", "activities"),
            ("⚙ Services", "services"),
            ("📡 Receivers", "receivers"),
            ("🗂 Providers", "providers"),
            ("🔐 Permissions", "permissions"),
            ("📁 APK Explorer", "apk_explorer"),
            ("📂 File Explorer", "file_explorer"),
            ("🖼 XML Inspector", "xml_inspector"),
            ("📋 Logcat", "logcat"),
            ("🖥 Scrcpy", "scrcpy"),
            ("🤖 Automação", "automation"),
            ("📸 Screenshot", "screenshot"),
            ("🔌 Plugins", "plugins"),
            ("⚙ Configurações", "settings"),
        ]
        
        self.sidebar_buttons = {}
        
        for icon_text, page_id in sidebar_items:
            btn = ctk.CTkButton(
                self.sidebar,
                text=icon_text,
                width=200,
                height=38,
                fg_color="transparent",
                hover_color=THEME_CONFIG["hover"],
                text_color=THEME_CONFIG["text_primary"],
                anchor="w",
                corner_radius=8,
                command=lambda p=page_id: self._load_page(p)
            )
            btn.pack(padx=10, pady=2)
            self.sidebar_buttons[page_id] = btn
    
    def _create_main_area(self):
        """Create main content area"""
        self.main_frame = ctk.CTkFrame(
            self, 
            fg_color=THEME_CONFIG["bg_main"],
            corner_radius=0
        )
        self.main_frame.grid(row=1, column=1, sticky="nsew", padx=0, pady=(0, 40))
        self.main_frame.grid_columnconfigure(0, weight=1)
        self.main_frame.grid_rowconfigure(0, weight=1)
        
        self.current_page = None
    
    def _create_statusbar(self):
        """Create bottom status bar using CTkFrame"""
        self.statusbar = ctk.CTkFrame(
            self, 
            height=40, 
            fg_color=THEME_CONFIG["bg_panel"],
            corner_radius=0
        )
        self.statusbar.grid(row=2, column=0, columnspan=2, sticky="ew")
        self.statusbar.grid_propagate(False)
        
        # Status indicators
        status_labels = [
            ("Dispositivo:", "Nenhum"),
            ("ADB:", "Desconectado"),
            ("Scrcpy:", "Inativo"),
            ("CPU:", "--"),
            ("RAM:", "--"),
        ]
        
        for i, (label, value) in enumerate(status_labels):
            lbl_frame = ctk.CTkFrame(self.statusbar, fg_color="transparent")
            lbl_frame.grid(row=0, column=i, padx=15, pady=5)
            
            lbl_name = ctk.CTkLabel(
                lbl_frame,
                text=label,
                text_color=THEME_CONFIG["text_secondary"],
                font=ctk.CTkFont(family="Arial", size=11)
            )
            lbl_name.pack(side="left", padx=(0, 5))
            
            lbl_value = ctk.CTkLabel(
                lbl_frame,
                text=value,
                text_color=THEME_CONFIG["text_primary"],
                font=ctk.CTkFont(family="Arial", size=11, weight="bold")
            )
            lbl_value.pack(side="left")
        
        # Right side status
        right_status = ctk.CTkLabel(
            self.statusbar,
            text="Tema: Dark Black",
            text_color=THEME_CONFIG["text_secondary"],
            font=ctk.CTkFont(family="Arial", size=11)
        )
        right_status.grid(row=0, column=len(status_labels), sticky="e", padx=15)
    
    def _load_page(self, page_id):
        """Load a specific page"""
        # Clear current page
        if self.current_page:
            self.current_page.destroy()
        
        # Reset sidebar buttons
        for btn in self.sidebar_buttons.values():
            btn.configure(fg_color="transparent")
        
        # Highlight selected button
        if page_id in self.sidebar_buttons:
            self.sidebar_buttons[page_id].configure(fg_color=THEME_CONFIG["selection"])
        
        # Create new page container
        self.current_page = ctk.CTkScrollableFrame(
            self.main_frame,
            fg_color=THEME_CONFIG["bg_main"],
            scrollbar_button_color=THEME_CONFIG["hover"],
            corner_radius=0
        )
        self.current_page.grid(row=0, column=0, sticky="nsew", padx=20, pady=20)
        self.current_page.grid_columnconfigure(0, weight=1)
        self.current_page.grid_rowconfigure(0, weight=1)
        
        # Page titles mapping
        page_titles = {
            "dashboard": "Dashboard",
            "devices": "Dispositivos",
            "apps": "Aplicativos",
            "package_info": "Package Info",
            "activities": "Activities",
            "services": "Services",
            "receivers": "Receivers",
            "providers": "Providers",
            "permissions": "Permissions",
            "apk_explorer": "APK Explorer",
            "file_explorer": "File Explorer",
            "xml_inspector": "XML Inspector",
            "logcat": "Logcat",
            "scrcpy": "Scrcpy",
            "automation": "Automação",
            "screenshot": "Screenshot",
            "plugins": "Plugins",
            "settings": "Configurações",
        }
        
        title = page_titles.get(page_id, page_id)
        
        # Load specific page or placeholder
        if page_id == "dashboard":
            dashboard = DashboardPage(self.current_page, fg_color=THEME_CONFIG["bg_main"])
            dashboard.grid(row=0, column=0, sticky="nsew")
        else:
            title_label = ctk.CTkLabel(
                self.current_page,
                text=title,
                font=ctk.CTkFont(family="Arial", size=24, weight="bold"),
                text_color=THEME_CONFIG["text_primary"],
                anchor="w"
            )
            title_label.grid(row=0, column=0, sticky="w", pady=(0, 20))
            
            # Add placeholder content
            placeholder = ctk.CTkLabel(
                self.current_page,
                text=f"Conteúdo da página: {title}\n\nEsta página será implementada com componentes específicos.",
                font=ctk.CTkFont(family="Arial", size=14),
                text_color=THEME_CONFIG["text_secondary"],
                justify="center"
            )
            placeholder.grid(row=1, column=0, sticky="nsew", pady=40)
    
    def _show_menu(self, menu_name):
        """Show menu options"""
        # Placeholder for menu functionality
        print(f"Menu clicked: {menu_name}")


def main():
    """Main entry point"""
    app = DiixToolUI()
    app.mainloop()


if __name__ == "__main__":
    main()
