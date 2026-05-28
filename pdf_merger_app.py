# first run pip install pypdf in a venv

import tkinter as tk
from tkinter import filedialog, messagebox
from pypdf import PdfWriter


class PDFMergerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("PDF Merger")
        self.root.geometry("500x350")
        self.root.resizable(False, False)

        self.pdf_files = []
        self.output_path = ""

        title = tk.Label(root, text="PDF Merger", font=("Arial", 18, "bold"))
        title.pack(pady=15)

        self.file_list = tk.Listbox(root, width=60, height=8)
        self.file_list.pack(pady=10)

        btn_frame = tk.Frame(root)
        btn_frame.pack()

        tk.Button(btn_frame, text="Add PDFs", command=self.add_pdfs, width=15).grid(row=0, column=0, padx=5)
        tk.Button(btn_frame, text="Clear", command=self.clear_files, width=15).grid(row=0, column=1, padx=5)

        tk.Button(root, text="Choose Output File", command=self.choose_output, width=25).pack(pady=10)

        self.output_label = tk.Label(root, text="No output file selected", wraplength=450)
        self.output_label.pack()

        tk.Button(
            root,
            text="Merge PDFs",
            command=self.merge_pdfs,
            width=25,
            bg="#4CAF50",
            fg="white"
        ).pack(pady=20)

    def add_pdfs(self):
        files = filedialog.askopenfilenames(
            title="Select PDF files",
            filetypes=[("PDF Files", "*.pdf")]
        )

        for file in files:
            if file not in self.pdf_files:
                self.pdf_files.append(file)
                self.file_list.insert(tk.END, file)

    def clear_files(self):
        self.pdf_files.clear()
        self.file_list.delete(0, tk.END)

    def choose_output(self):
        self.output_path = filedialog.asksaveasfilename(
            title="Save merged PDF as",
            defaultextension=".pdf",
            filetypes=[("PDF Files", "*.pdf")]
        )

        if self.output_path:
            self.output_label.config(text=f"Output: {self.output_path}")

    def merge_pdfs(self):
        if not self.pdf_files:
            messagebox.showerror("Error", "Please add at least one PDF file.")
            return

        if not self.output_path:
            messagebox.showerror("Error", "Please choose an output file.")
            return

        try:
            writer = PdfWriter()

            for pdf in self.pdf_files:
                writer.append(pdf)

            with open(self.output_path, "wb") as output_file:
                writer.write(output_file)

            messagebox.showinfo("Success", "PDFs merged successfully!")

        except Exception as e:
            messagebox.showerror("Error", f"Something went wrong:\n{e}")


if __name__ == "__main__":
    root = tk.Tk()
    app = PDFMergerApp(root)
    root.mainloop()
    