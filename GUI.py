import tkinter as tk
from tkinter import ttk
import os
import threading
import time
import simulation_callout
from people_generation import *
from data_dict import *
import training
import training_data

class App:
    def __init__(self, master):
        print("Initalizing...")

        self.master = master
        master.title("Adaptive Sociopolitical Environment Simulator ")
        master.geometry("800x600")  # Set the window size to 800x600 pixels

        self.main_frame = ttk.Frame(master)
        self.second_frame = ttk.Frame(master)
        
        master.columnconfigure(0, weight=1)
        master.rowconfigure(0, weight=1)

        self.main_frame.grid(row=0, column=0, sticky="nsew")
        self.second_frame.grid(row=0, column=0, sticky="nsew")

        self.setup_main_frame()
        self.setup_second_frame()
        self.show_frame(self.main_frame)

    def setup_main_frame(self):
        # Navigation Buttons with Equal Heights
        main_frame = self.main_frame
        # Configure grid weights (responsiveness)
        main_frame.columnconfigure(0, weight=1)
        main_frame.rowconfigure(1, weight=3)
        for i in range(6):  # Ensure all rows can expand if necessary
            main_frame.rowconfigure(i, weight=1)

        # Middle Section (Dictionary Display with Treeview)
        self.tree_main = ttk.Treeview(main_frame, columns=("Title", "Value"))
        self.tree_main.heading("#0", text="ID", anchor=tk.W)
        self.tree_main.heading("Title", text="Title")
        self.tree_main.heading("Value", text="Value")
        self.tree_main.column("#0", width=0, stretch=tk.NO)
        self.tree_main.column("Title", anchor=tk.W, width=200)
        self.tree_main.column("Value", anchor=tk.W, width=200)
        self.tree_main.grid(row=0, column=1, rowspan=3, sticky="nsew")
        self.tree_main.bind("<<TreeviewSelect>>", self.on_select)

        ttk.Button(main_frame, text="Policy", command=lambda: self.show_section_ff("policy", self.tree_main)).grid(row=0, column=0, sticky="nsew")
        ttk.Button(main_frame, text="Popularity", command=lambda: self.show_section_ff("popularity", self.tree_main)).grid(row=1, column=0, sticky="nsew")
        ttk.Button(main_frame, text="Indicator", command=lambda: self.show_section_ff("indicator", self.tree_main)).grid(row=2, column=0, sticky="nsew")

        # Generate People Data (Half height of the left section)
        ttk.Label(main_frame, text="Generate People Data").grid(row=3, column=0, sticky="ew")
        self.input_number = ttk.Entry(main_frame)
        self.input_number.grid(row=4, column=0, sticky="ew")
        ttk.Button(main_frame, text="Confirm", command=lambda: self.generate_people_data(r"final_year_project\people")).grid(row=5, column=0, sticky="sew")

        self.progress_bar = ttk.Progressbar(main_frame, orient="horizontal", length=200, mode="determinate")
        self.progress_bar.grid(row=6, column=0, sticky="ew", columnspan=2)
        self.progress_bar.grid_remove()  # Initially hide the progress bar

        # Add a placeholder for the "Done" message
        self.done_label = ttk.Label(main_frame, text="Done")
        self.done_label.grid(row=6, column=0, sticky="ew", columnspan=2)
        self.done_label.grid_remove()  # Initially hide the Done label

        # Selected Target Display
        ttk.Label(main_frame, text="Selected Target:").grid(row=3, column=1, sticky="w")
        self.selected_target = ttk.Label(main_frame, text="")
        self.selected_target.grid(row=3, column=2, sticky="ew")

        # Target Options and Confirm
        ttk.Label(main_frame, text="Target:").grid(row=4, column=1, sticky="w")
        self.min_max = ttk.Combobox(main_frame, values=["Min", "Max"], width=5)
        self.min_max.grid(row=4, column=2, columnspan=2, sticky="ew")
        ttk.Button(main_frame, text="Confirm", command=self.confirm_selection).grid(row=5, column=1, columnspan=3, sticky="sew")

    def setup_second_frame(self):
        second_frame = self.second_frame
        second_frame.columnconfigure(0, weight=1)
        second_frame.columnconfigure(1, weight=3)
        for i in range(3):
            second_frame.rowconfigure(i, weight=1)
        
        # Middle Section (Dictionary Display with Treeview)
        self.tree = ttk.Treeview(second_frame, columns=("Title", "Value"))
        self.tree.heading("#0", text="ID", anchor=tk.W)  # Hide or remove if not needed
        self.tree.heading("Title", text="Title")
        self.tree.heading("Value", text="Value")
        self.tree.column("#0", width=0, stretch=tk.NO)  # Hide or remove if not needed
        self.tree.column("Title", anchor=tk.W, width=200)
        self.tree.column("Value", anchor=tk.W, width=200)
        self.tree.grid(row=0, column=1, rowspan=3, sticky="nsew")
        self.tree.bind("<<TreeviewSelect>>", self.on_select)
        
        ttk.Button(second_frame, text="Back", command=lambda: self.show_frame(self.main_frame)).grid(row=3, column=1, sticky="ew")

        ttk.Button(second_frame, text="Policy", command=lambda: self.show_section_sf("policy", self.tree)).grid(row=0, column=0, sticky="nsew")
        ttk.Button(second_frame, text="Popularity", command=lambda: self.show_section_sf("popularity", self.tree)).grid(row=1, column=0, sticky="nsew")
        ttk.Button(second_frame, text="Indicator", command=lambda: self.show_section_sf("indicator", self.tree)).grid(row=2, column=0, sticky="nsew")

    def show_section_ff(self, section, tree):
        tree.delete(*tree.get_children())  # Clear the treeview
        sections = {
            "policy" : policy_dict,
            "popularity": popularity_dict,
            "indicator": indicator_dict
        }

        for key, value in sections[section].items():
            tree.insert("", tk.END, values=(key.capitalize(), value))

    def show_section_sf(self, section, tree):
        tree.delete(*tree.get_children())  # Clear the treeview
        sections = {
            "policy" : finished_policy_dict,
            "popularity": finished_popularity_dict,
            "indicator": finished_indicator_dict
        }

        for key, value in sections[section].items():
            tree.insert("", tk.END, values=(key.capitalize(), value))
    
    def generate_people_data(self,people_data_path):
        # Hide Done label and show the progress bar
        self.done_label.grid_remove()
        self.progress_bar.grid()
        self.progress_bar['value'] = 0  # Reset progress bar to 0
        self.master.update()  # Update the GUI

        self.delete_files_in_folder(people_data_path)

        # Start the generation process in a new thread
        num_people = int(self.input_number.get()) if self.input_number.get().isdigit() else 10

        # Start the generation process in a new thread
        generation_thread = threading.Thread(target=self.run_generation, args=(num_people,))
        generation_thread.start()

        # Start another thread to update the progress bar
        progress_thread = threading.Thread(target=self.update_progress_thread, args=(num_people, people_data_path))
        progress_thread.start()

    def run_generation(self, num_people):
        generation(num_people)  

    def update_progress_thread(self, num_people,people_data_path):
        initial_count = len(os.listdir(people_data_path))
        total_steps = num_people
        expected_files = initial_count + total_steps
        
        while len(os.listdir(people_data_path)) < expected_files:
            #time.sleep(0.5)  # Check every half second
            current_files = len(os.listdir(people_data_path))
            progress = ((current_files - initial_count) / total_steps) * 100
            self.progress_bar['value'] = progress  # Update the progress bar
            self.master.update_idletasks()  # Update the GUI thread with progress bar changes

        self.progress_bar['value'] = 100  # Ensure the progress bar shows complete
        self.progress_bar.grid_remove()  # Hide progress bar after completion
        self.done_label.grid()  # Show the "Done" label


    def confirm_selection(self):
        global finished_policy_dict,finished_popularity_dict,finished_indicator_dict
        # Confirm the selected option
        print(f"Confirmed: {self.min_max.get()} for target {self.selected_target.cget('text')}")

        training_data.traning_data_generation()
        
        finished_policy_dict,finished_popularity_dict,finished_indicator_dict = training.training(self.min_max.get(),self.selected_target.cget('text'))

        self.show_frame(self.second_frame)
    
    def on_select(self, event):
        # Determine the event's origin (which treeview)
        origin = event.widget  # This will give us the treeview that triggered the event
        
        selected_item = origin.item(origin.selection())
        value = selected_item['values'][0] if selected_item['values'] else ""

        if origin == self.tree_main:
            self.selected_target.configure(text=value)

    def show_frame(self, frame):
        frame.tkraise()

    def delete_files_in_folder(self,folder_path):
        # List all files in the directory
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.remove(file_path)  # Remove the file

            except Exception as e:
                print(f"Failed to delete {file_path}. Reason: {e}")

root = tk.Tk()
app = App(root)
root.mainloop()
