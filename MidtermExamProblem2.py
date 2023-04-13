import tkinter as tk


class MidtermProblem2:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("600x400+10+10")
        self.root.title("Midterm Exam Problem 2")

        self.first_name_label = tk.Label(self.root, text="First Name:")
        self.first_name_label.grid(row=0, column=0, padx=100, pady=10)
        self.first_name_entry = tk.Entry(self.root)
        self.first_name_entry.grid(row=0, column=1, padx=100, pady=10)

        self.middle_name_label = tk.Label(self.root, text="Middle Name:")
        self.middle_name_label.grid(row=1, column=0, padx=100, pady=0)
        self.middle_name_entry = tk.Entry(self.root)
        self.middle_name_entry.grid(row=1, column=1, padx=10, pady=10)

        self.last_name_label = tk.Label(self.root, text="Last Name:")
        self.last_name_label.grid(row=2, column=0, padx=10, pady=10)
        self.last_name_entry = tk.Entry(self.root)
        self.last_name_entry.grid(row=2, column=1, padx=10, pady=10)

        self.full_name_label = tk.Label(self.root, text="Full Name:")
        self.full_name_label.grid(row=3, column=0, padx=10, pady=10)
        self.full_name_entry = tk.Entry(self.root)
        self.full_name_entry.grid(row=3, column=1, padx=10, pady=10)

        self.show_button = tk.Button(self.root, text="Show Full Name", command=self.show_full_name)
        self.show_button.grid(row=4, column=1, padx=10, pady=10)

    def show_full_name(self):
        first_name = self.first_name_entry.get()
        middle_name = self.middle_name_entry.get()
        last_name = self.last_name_entry.get()
        full_name = f"{first_name} {middle_name} {last_name}"
        self.full_name_entry.delete(0, tk.END)
        self.full_name_entry.insert(0, full_name)

    def run(self):
        self.root.mainloop()


if __name__ == '__main__':
    gui = MidtermProblem2()
    gui.run()
