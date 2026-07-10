"""
Dashboard Page - Quick information cards
CustomTkinter 6.x Compatible
"""

import customtkinter as ctk
from ..config.theme import THEME_CONFIG


class DashboardPage(ctk.CTkScrollableFrame):
    """Dashboard page with quick info cards - CustomTkinter 6.x"""
    
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.grid_columnconfigure(0, weight=1)
        
        self._create_title()
        self._create_cards_grid()
    
    def _create_title(self):
        """Create page title using CTkLabel"""
        title = ctk.CTkLabel(
            self,
            text="Dashboard",
            font=ctk.CTkFont(family="Arial", size=24, weight="bold"),
            text_color=THEME_CONFIG["text_primary"],
            anchor="w"
        )
        title.grid(row=0, column=0, sticky="w", pady=(0, 20), padx=10)
    
    def _create_cards_grid(self):
        """Create grid of info cards using CTkFrame"""
        # Card data
        cards_data = [
            ("Dispositivo Conectado", "Nenhum", "📱"),
            ("Android", "--", "🤖"),
            ("SDK", "--", "📦"),
            ("Fabricante", "--", "🏭"),
            ("Modelo", "--", "📱"),
            ("CPU", "--", "⚙"),
            ("RAM", "--", "💾"),
            ("Armazenamento", "--", "💿"),
            ("Estado do ADB", "Desconectado", "🔌"),
            ("Scrcpy", "Inativo", "🖥"),
            ("Tempo Conectado", "--", "⏱"),
        ]
        
        # Create cards in grid (3 columns)
        row = 1
        col = 0
        
        for title_text, value, icon in cards_data:
            card = ctk.CTkFrame(
                self,
                fg_color=THEME_CONFIG["bg_card"],
                corner_radius=8
            )
            card.grid(row=row, column=col, padx=10, pady=10, sticky="ew")
            
            # Card title
            title_label = ctk.CTkLabel(
                card,
                text=f"{icon} {title_text}",
                font=ctk.CTkFont(family="Arial", size=12, weight="bold"),
                text_color=THEME_CONFIG["text_secondary"],
                anchor="w"
            )
            title_label.pack(padx=15, pady=(15, 5))
            
            # Card value
            value_label = ctk.CTkLabel(
                card,
                text=value,
                font=ctk.CTkFont(family="Arial", size=16, weight="bold"),
                text_color=THEME_CONFIG["text_primary"],
                anchor="w"
            )
            value_label.pack(padx=15, pady=(0, 15))
            
            col += 1
            if col >= 3:
                col = 0
                row += 1
        
        # Configure grid weights
        for i in range(3):
            self.grid_columnconfigure(i, weight=1)
