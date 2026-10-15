
import tkinter as tk
from tkinter import ttk, messagebox


class ShopGeneratorApp(tk.Tk):

    def __init__(self):
        super().__init__()

        # 1. Finestra principale
        self.title("D&D Shop Generator")
        self.geometry("1050x700")
        self.minsize(850, 550)

        # 2. Variabili collegate ai widget
        self.shop_name = tk.StringVar(value="La Forgia Antica")
        self.shop_type = tk.StringVar(value="Armeria")
        self.zone = tk.StringVar(value="Città ricca")
        self.product_count = tk.IntVar(value=5)
        self.include_magic = tk.BooleanVar(value=True)
        self.magic_level = tk.StringVar(value="Normale")
        self.discount = tk.DoubleVar(value=0)

        # Dati dimostrativi
        self.products = [
            ("Spada lunga", "Armi", "Comune", 15),
            ("Pozione curativa", "Oggetti magici", "Comune", 50),
            ("Anello incantato", "Gioielli", "Rara", 250),
        ]

        self.create_menu()
        self.create_layout()
        self.refresh_table()

    # --------------------------------------------------
    # MENU SUPERIORE
    # --------------------------------------------------

    def create_menu(self):
        menubar = tk.Menu(self)

        file_menu = tk.Menu(menubar, tearoff=False)
        file_menu.add_command(
            label="Nuovo negozio",
            command=self.reset_form
        )
        file_menu.add_command(
            label="Esporta catalogo",
            command=self.export_catalogue
        )
        file_menu.add_separator()
        file_menu.add_command(
            label="Esci",
            command=self.destroy
        )

        help_menu = tk.Menu(menubar, tearoff=False)
        help_menu.add_command(
            label="Informazioni",
            command=lambda: messagebox.showinfo(
                "Informazioni",
                "D&D Shop Generator - Demo Tkinter"
            )
        )

        menubar.add_cascade(label="File", menu=file_menu)
        menubar.add_cascade(label="Aiuto", menu=help_menu)

        self.config(menu=menubar)

    # --------------------------------------------------
    # LAYOUT PRINCIPALE
    # --------------------------------------------------

    def create_layout(self):
        # Frame principale: contiene configurazione e risultati
        main = ttk.Frame(self, padding=12)
        main.pack(fill="both", expand=True)

        main.columnconfigure(0, weight=1)
        main.columnconfigure(1, weight=2)
        main.rowconfigure(0, weight=1)

        self.create_configuration_panel(main)
        self.create_results_panel(main)

        # Area messaggi in fondo alla finestra
        self.status = tk.StringVar(value="Pronto.")
        status_bar = ttk.Label(
            self,
            textvariable=self.status,
            relief="sunken",
            anchor="w",
            padding=5
        )
        status_bar.pack(fill="x", side="bottom")

    # --------------------------------------------------
    # PANNELLO DI CONFIGURAZIONE
    # --------------------------------------------------

    def create_configuration_panel(self, parent):
        panel = ttk.LabelFrame(
            parent,
            text="Configurazione negozio",
            padding=12
        )
        panel.grid(
            row=0, column=0,
            sticky="nsew", padx=(0, 10)
        )

        panel.columnconfigure(1, weight=1)

        # Label + Entry
        ttk.Label(
            panel, text="Nome:"
        ).grid(row=0, column=0, sticky="w", pady=6)

        name_entry = ttk.Entry(
            panel,
            textvariable=self.shop_name
        )
        name_entry.grid(
            row=0, column=1,
            sticky="ew", pady=6
        )

        # Combobox: menu a tendina
        ttk.Label(
            panel, text="Tipo:"
        ).grid(row=1, column=0, sticky="w", pady=6)

        type_combo = ttk.Combobox(
            panel,
            textvariable=self.shop_type,
            values=[
                "Armeria",
                "Alchimia",
                "Gioielleria",
                "Abbigliamento",
                "Alimentari",
            ],
            state="readonly"
        )
        type_combo.grid(
            row=1, column=1,
            sticky="ew", pady=6
        )

        # Seconda Combobox
        ttk.Label(
            panel, text="Zona:"
        ).grid(row=2, column=0, sticky="w", pady=6)

        zone_combo = ttk.Combobox(
            panel,
            textvariable=self.zone,
            values=[
                "Città ricca",
                "Città povera",
                "Zona turistica",
                "Zona commerciale",
                "Zona montana",
            ],
            state="readonly"
        )
        zone_combo.grid(
            row=2, column=1,
            sticky="ew", pady=6
        )

        # Spinbox: quantità numerica
        ttk.Label(
            panel, text="Prodotti:"
        ).grid(row=3, column=0, sticky="w", pady=6)

        ttk.Spinbox(
            panel,
            from_=1,
            to=100,
            textvariable=self.product_count
        ).grid(
            row=3, column=1,
            sticky="ew", pady=6
        )

        ttk.Separator(panel).grid(
            row=4, column=0, columnspan=2,
            sticky="ew", pady=12
        )

        # Checkbutton: opzione sì/no
        ttk.Checkbutton(
            panel,
            text="Includi oggetti magici",
            variable=self.include_magic
        ).grid(
            row=5, column=0, columnspan=2,
            sticky="w", pady=5
        )

        # Radiobutton: scelta esclusiva
        ttk.Label(
            panel, text="Livello di magia:"
        ).grid(
            row=6, column=0, columnspan=2,
            sticky="w", pady=(12, 3)
        )

        for row, level in enumerate(
            ["Basso", "Normale", "Alto"], start=7
        ):
            ttk.Radiobutton(
                panel,
                text=level,
                variable=self.magic_level,
                value=level
            ).grid(
                row=row, column=0, columnspan=2,
                sticky="w", padx=8, pady=2
            )

        # Scale: selezione tramite cursore
        ttk.Label(
            panel, text="Sconto generale (%):"
        ).grid(
            row=10, column=0, columnspan=2,
            sticky="w", pady=(12, 0)
        )

        ttk.Scale(
            panel,
            from_=0,
            to=50,
            variable=self.discount,
            command=self.update_discount_label
        ).grid(
            row=11, column=0, columnspan=2,
            sticky="ew", pady=5
        )

        self.discount_label = ttk.Label(
            panel, text="Sconto: 0%"
        )
        self.discount_label.grid(
            row=12, column=0, columnspan=2,
            sticky="w"
        )

        # Pulsanti
        ttk.Button(
            panel,
            text="Genera negozio",
            command=self.generate_shop
        ).grid(
            row=13, column=0, columnspan=2,
            sticky="ew", pady=(20, 5)
        )

        ttk.Button(
            panel,
            text="Aggiungi prodotto di prova",
            command=self.add_product
        ).grid(
            row=14, column=0, columnspan=2,
            sticky="ew", pady=5
        )

    # --------------------------------------------------
    # PANNELLO RISULTATI
    # --------------------------------------------------

    def create_results_panel(self, parent):
        panel = ttk.Frame(parent)
        panel.grid(row=0, column=1, sticky="nsew")

        panel.columnconfigure(0, weight=1)
        panel.rowconfigure(1, weight=3)
        panel.rowconfigure(3, weight=1)

        ttk.Label(
            panel,
            text="Catalogo prodotti",
            font=("TkDefaultFont", 15, "bold")
        ).grid(row=0, column=0, sticky="w", pady=(0, 10))

        # Treeview: tabella
        columns = ("name", "category", "rarity", "price")

        self.table = ttk.Treeview(
            panel,
            columns=columns,
            show="headings",
            selectmode="browse"
        )

        self.table.heading("name", text="Nome")
        self.table.heading("category", text="Categoria")
        self.table.heading("rarity", text="Rarità")
        self.table.heading("price", text="Prezzo")

        self.table.column("name", width=170)
        self.table.column("category", width=140)
        self.table.column("rarity", width=90)
        self.table.column("price", width=90, anchor="e")

        self.table.grid(
            row=1, column=0, sticky="nsew"
        )

        # Scrollbar verticale collegata alla tabella
        scrollbar = ttk.Scrollbar(
            panel,
            orient="vertical",
            command=self.table.yview
        )
        scrollbar.grid(row=1, column=1, sticky="ns")
        self.table.configure(yscrollcommand=scrollbar.set)

        # Evento: doppio clic su una riga
        self.table.bind(
            "<Double-1>",
            self.show_product_details
        )

        # Notebook: schede separate
        notebook = ttk.Notebook(panel)
        notebook.grid(
            row=3, column=0, columnspan=2,
            sticky="nsew", pady=(12, 0)
        )

        details_tab = ttk.Frame(notebook, padding=8)
        log_tab = ttk.Frame(notebook, padding=8)

        notebook.add(details_tab, text="Dettagli")
        notebook.add(log_tab, text="Registro")

        # Text: descrizioni e dettagli
        self.details = tk.Text(
            details_tab,
            height=5,
            wrap="word",
            state="disabled"
        )
        self.details.pack(fill="both", expand=True)

        # Listbox: elenco degli eventi
        self.log = tk.Listbox(log_tab, height=5)
        self.log.pack(fill="both", expand=True)

    # --------------------------------------------------
    # CALLBACK E LOGICA DIMOSTRATIVA
    # --------------------------------------------------

    def refresh_table(self):
        for item in self.table.get_children():
            self.table.delete(item)

        for name, category, rarity, price in self.products:
            self.table.insert(
                "",
                "end",
                values=(name, category, rarity, f"{price} MO")
            )

    def generate_shop(self):
        name = self.shop_name.get().strip()
        shop_type = self.shop_type.get()

        if not name:
            messagebox.showwarning(
                "Dato mancante",
                "Inserisci il nome del negozio."
            )
            return

        try:
            count = self.product_count.get()
            if not 1 <= count <= 100:
                raise ValueError
        except (ValueError, tk.TclError):
            messagebox.showerror(
                "Valore non valido",
                "Il numero di prodotti deve essere tra 1 e 100."
            )
            return

        self.status.set(
            f"Configurazione pronta: {name} ({shop_type})"
        )
        self.log.insert(
            "end",
            f"Negozio configurato: {name}, "
            f"zona {self.zone.get()}, "
            f"{count} prodotti richiesti."
        )

        messagebox.showinfo(
            "Configurazione",
            f"Negozio: {name}\n"
            f"Tipo: {shop_type}\n"
            f"Zona: {self.zone.get()}\n"
            f"Prodotti richiesti: {count}\n"
            f"Magia: {self.magic_level.get()}\n"
            f"Oggetti magici: {self.include_magic.get()}\n"
            f"Sconto: {self.discount.get():.0f}%\n\n"
            "Demo: nessun negozio reale è stato generato."
        )

    def add_product(self):
        name = f"Oggetto {len(self.products) + 1}"

        self.products.append(
            (name, "Oggetti magici", "Comune", 50)
        )

        self.refresh_table()
        self.log.insert("end", f"Aggiunto: {name}")
        self.status.set(f"Prodotto aggiunto: {name}")

    def show_product_details(self, event):
        selected = self.table.selection()

        if not selected:
            return

        values = self.table.item(selected[0], "values")
        text = (
            f"Nome: {values[0]}\n"
            f"Categoria: {values[1]}\n"
            f"Rarità: {values[2]}\n"
            f"Prezzo: {values[3]}"
        )

        self.details.configure(state="normal")
        self.details.delete("1.0", tk.END)
        self.details.insert("1.0", text)
        self.details.configure(state="disabled")

    def update_discount_label(self, value):
        self.discount_label.configure(
            text=f"Sconto: {float(value):.0f}%"
        )

    def reset_form(self):
        self.shop_name.set("")
        self.shop_type.set("Armeria")
        self.zone.set("Città ricca")
        self.product_count.set(5)
        self.include_magic.set(True)
        self.magic_level.set("Normale")
        self.discount.set(0)
        self.update_discount_label(0)
        self.status.set("Configurazione azzerata.")

    def export_catalogue(self):
        # Per ora stampa i dati nel terminale.
        # In seguito potrai usare il modulo csv.
        for product in self.products:
            print(product)

        messagebox.showinfo(
            "Esportazione",
            "Catalogo stampato nel terminale."
        )


if __name__ == "__main__":
    app = ShopGeneratorApp()
    app.mainloop()
