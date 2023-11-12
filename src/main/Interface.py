import tkinter as tk

class BubblePopup:
    def __init__(self, master, text, duration=3000):
        self.master = master
        self.text = text
        self.duration = duration

        self.popup = tk.Toplevel(master)
        self.popup.wm_overrideredirect(True)  # Remove window decorations
        self.popup.wm_geometry("+{}+{}".format(master.winfo_x() + 50, master.winfo_y() + 50))

        self.text_widget = tk.Text(self.popup, wrap='word', width=30, height=5, font=("Helvetica", 12))
        self.text_widget.insert('1.0', text)
        self.text_widget.pack(side='left', fill='both', expand=True)

        scrollbar = tk.Scrollbar(self.popup, command=self.text_widget.yview)
        scrollbar.pack(side='right', fill='y')

        self.text_widget.config(yscrollcommand=scrollbar.set)
        
        self.popup.after(duration, self.close_popup)

    def close_popup(self):
        self.popup.destroy()

class ScreenOverlay:
    def __init__(self, root):
        self.root = root
        self.root.attributes('-alpha', 0.5)  # Set transparency level
        self.root.attributes('-topmost', True)  # Make the window stay on top

        # Create a label with some text
        self.label = tk.Label(root, text="This is a screen overlay", font=("Helvetica", 16))
        self.label.pack(pady=20)

        # Create a button to show the bubble popup
        self.show_popup_button = tk.Button(root, text="Show Popup", command=self.show_bubble_popup)
        self.show_popup_button.pack(pady=10)

    def show_bubble_popup(self):
        # Example of a large amount of text
        long_text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. " * 50

        duration = 10000  # Duration in milliseconds

        bubble_popup = BubblePopup(self.root, long_text, duration)

if __name__ == "__main__":
    root = tk.Tk()

    # Set window size and position
    width = 400
    height = 200
    x = (root.winfo_screenwidth() - width) // 2
    y = (root.winfo_screenheight() - height) // 2

    root.geometry(f'{width}x{height}+{x}+{y}')

    overlay = ScreenOverlay(root)
    root.mainloop()