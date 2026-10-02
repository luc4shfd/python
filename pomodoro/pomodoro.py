import tkinter as tk
from tkinter import ttk

try:
    import winsound  # só existe no Windows
except ImportError:
    winsound = None

FOCO, CURTA, LONGA = "Foco", "Pausa curta", "Pausa longa"
CORES = {FOCO: "#e74c3c", CURTA: "#2ecc71", LONGA: "#3498db"}
CICLOS_ATE_PAUSA_LONGA = 4


class Pomodoro(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Pomodoro")
        self.resizable(False, False)

        self.modo = FOCO
        self.ciclos = 0
        self.rodando = False
        self.after_id = None

        self.var_foco = tk.StringVar(value="25")
        self.var_curta = tk.StringVar(value="5")
        self.var_longa = tk.StringVar(value="15")
        self.restante = self.duracao(FOCO)

        self._montar_interface()
        self._atualizar_tela()

        for var in (self.var_foco, self.var_curta, self.var_longa):
            var.trace_add("write", lambda *_: self._config_alterada())

    # ---------- interface ----------
    def _montar_interface(self):
        self.lbl_modo = tk.Label(self, font=("Segoe UI", 16, "bold"), width=20)
        self.lbl_modo.pack(pady=(15, 0))

        self.lbl_tempo = tk.Label(self, font=("Segoe UI", 56, "bold"))
        self.lbl_tempo.pack(padx=30)

        self.lbl_ciclos = tk.Label(self, font=("Segoe UI", 10))
        self.lbl_ciclos.pack()

        botoes = tk.Frame(self)
        botoes.pack(pady=12)
        self.btn_iniciar = ttk.Button(botoes, text="Iniciar", command=self.alternar)
        self.btn_iniciar.grid(row=0, column=0, padx=4)
        ttk.Button(botoes, text="Resetar", command=self.resetar).grid(row=0, column=1, padx=4)
        ttk.Button(botoes, text="Pular", command=self.pular).grid(row=0, column=2, padx=4)

        cfg = ttk.LabelFrame(self, text="Duração (minutos)")
        cfg.pack(padx=15, pady=(0, 15), fill="x")
        for i, (nome, var) in enumerate(
            [("Foco", self.var_foco), ("Pausa curta", self.var_curta), ("Pausa longa", self.var_longa)]
        ):
            ttk.Label(cfg, text=nome).grid(row=0, column=i, padx=8, pady=(6, 0))
            ttk.Spinbox(cfg, from_=1, to=180, width=5, textvariable=var, justify="center").grid(
                row=1, column=i, padx=8, pady=(0, 8)
            )

    # ---------- lógica ----------
    def duracao(self, modo):
        var = {FOCO: self.var_foco, CURTA: self.var_curta, LONGA: self.var_longa}[modo]
        padrao = {FOCO: 25, CURTA: 5, LONGA: 15}[modo]
        try:
            minutos = int(var.get())
            return max(1, minutos) * 60
        except ValueError:
            return padrao * 60

    def _config_alterada(self):
        # só aplica na hora se o timer estiver parado
        if not self.rodando:
            self.restante = self.duracao(self.modo)
            self._atualizar_tela()

    def alternar(self):
        if self.rodando:
            self.rodando = False
            if self.after_id:
                self.after_cancel(self.after_id)
            self.btn_iniciar.config(text="Continuar")
        else:
            self.rodando = True
            self.btn_iniciar.config(text="Pausar")
            self._tick()

    def _tick(self):
        if not self.rodando:
            return
        if self.restante <= 0:
            self._terminou()
            return
        self.restante -= 1
        self._atualizar_tela()
        if self.restante <= 0:
            self._terminou()
            return
        self.after_id = self.after(1000, self._tick)

    def _terminou(self):
        self.rodando = False
        self.btn_iniciar.config(text="Iniciar")
        self._avisar()
        self._proximo_modo()

    def _proximo_modo(self):
        if self.modo == FOCO:
            self.ciclos += 1
            self.modo = LONGA if self.ciclos % CICLOS_ATE_PAUSA_LONGA == 0 else CURTA
        else:
            self.modo = FOCO
        self.restante = self.duracao(self.modo)
        self._atualizar_tela()

    def pular(self):
        if self.after_id:
            self.after_cancel(self.after_id)
        self.rodando = False
        self.btn_iniciar.config(text="Iniciar")
        self._proximo_modo()

    def resetar(self):
        if self.after_id:
            self.after_cancel(self.after_id)
        self.rodando = False
        self.btn_iniciar.config(text="Iniciar")
        self.restante = self.duracao(self.modo)
        self._atualizar_tela()

    def _avisar(self):
        if winsound:
            winsound.Beep(1000, 600)
        else:
            self.bell()
        self.deiconify()
        self.lift()
        self.attributes("-topmost", True)
        self.after(1500, lambda: self.attributes("-topmost", False))

    def _atualizar_tela(self):
        mm, ss = divmod(self.restante, 60)
        texto = f"{mm:02d}:{ss:02d}"
        cor = CORES[self.modo]
        self.lbl_tempo.config(text=texto, fg=cor)
        self.lbl_modo.config(text=self.modo, fg=cor)
        self.lbl_ciclos.config(text=f"Pomodoros concluídos: {self.ciclos}")
        self.title(f"{texto} - {self.modo}")


if __name__ == "__main__":
    Pomodoro().mainloop()