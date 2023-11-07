import tkinter as tk
from tkinter import messagebox, simpledialog
from tkinter import ttk
import numpy as np

class Usuario:
    def __init__(self, id, contraseña):
        self.id = id
        self.contraseña = contraseña
        self.ingresos = 0
        self.egresos = 0
        self.saldo = 0
        self.movimientos = []  # Lista para almacenar movimientos
        self.plan_ahorro = 0  # Plan de ahorro del usuario
        self.numero_cuotas = None  # Número de cuotas para el plan de ahorro


class LoginFrame:
    def __init__(self, notebook, verificar_credenciales, cerrar_sesion):
        
        self.verificar_credenciales = verificar_credenciales # Asigna el método a un atributo
        self.cerrar_sesion = cerrar_sesion
        self.notebook = notebook
        self.frame_login = tk.Frame(notebook)
        notebook.add(self.frame_login, text="Login")
        self.notebook.pack(expand=1, fill="both")

        self.label_usuario = ttk.Label(self.frame_login, text="Usuario actual: ")
        self.label_id = ttk.Label(self.frame_login, text="ID de usuario:")
        self.label_contraseña = ttk.Label(self.frame_login, text="Contraseña:")
        self.entry_id = ttk.Entry(self.frame_login)
        self.entry_contraseña = ttk.Entry(self.frame_login, show="*")
        self.boton_login = ttk.Button(self.frame_login, text="Iniciar sesión", command=self.verificar_credenciales)
        self.boton_cerrar_sesion = ttk.Button(self.frame_login, text="Cerrar sesión", command=self.cerrar_sesion)
        self.boton_cerrar_sesion.config(state="disabled")

        self.label_usuario.grid(row=0, columnspan=2, padx=5, pady=5, sticky="w")
        self.label_id.grid(row=1, column=0, padx=5, pady=5)
        self.label_contraseña.grid(row=2, column=0, padx=5, pady=5)
        self.entry_id.grid(row=1, column=1, padx=5, pady=5)
        self.entry_contraseña.grid(row=2, column=1, padx=5, pady=5)
        self.boton_login.grid(row=3, columnspan=2, padx=5, pady=5)
        self.boton_cerrar_sesion.grid(row=4, columnspan=2, padx=5, pady=5)
        
class RegistroFrame:
    def __init__(self, notebook, registrar_nuevo_usuario):
        self.frame_registro = tk.Frame(notebook)
        notebook.add(self.frame_registro, text="Registrar usuario")
        self.registrar_nuevo_usuario = registrar_nuevo_usuario
        self.label_nuevo_id = ttk.Label(self.frame_registro, text="Nuevo ID de usuario:")
        self.label_nueva_contraseña = ttk.Label(self.frame_registro, text="Nueva Contraseña:")
        self.entry_nuevo_id = ttk.Entry(self.frame_registro)
        self.entry_nueva_contraseña = ttk.Entry(self.frame_registro, show="*")
        self.boton_registro = ttk.Button(self.frame_registro, text="Registrar nuevo usuario", command=self.registrar_nuevo_usuario)

        self.label_nuevo_id.grid(row=0, column=0, padx=5, pady=5)
        self.label_nueva_contraseña.grid(row=1, column=0, padx=5, pady=5)
        self.entry_nuevo_id.grid(row=0, column=1, padx=5, pady=5)
        self.entry_nueva_contraseña.grid(row=1, column=1, padx=5, pady=5)
        self.boton_registro.grid(row=2, columnspan=2, padx=5, pady=5)

class FinanzasFrame:
    def __init__(self, notebook, registrar_ingreso, registrar_egreso, mostrar_plan_ahorro):
        self.frame_finanzas = tk.Frame(notebook)
        self.registrar_ingreso = registrar_ingreso
        self.registrar_egreso = registrar_egreso
        self.mostrar_plan_ahorro = mostrar_plan_ahorro
        notebook.add(self.frame_finanzas, text="Gestión Financiera")
        self.label_saldo = ttk.Label(self.frame_finanzas, text="Saldo actual: 0")
        self.boton_registrar_ingreso = ttk.Button(self.frame_finanzas, text="Registrar Ingreso", command=self.registrar_ingreso)
        self.boton_registrar_egreso = ttk.Button(self.frame_finanzas, text="Registrar Egreso", command=self.registrar_egreso)
        self.boton_plan_ahorro = ttk.Button(self.frame_finanzas, text="Establecer Plan de Ahorro", command=self.mostrar_plan_ahorro)
        self.tabla_movimientos = ttk.Treeview(self.frame_finanzas)

        self.label_saldo.grid(row=0, column=0, padx=10, pady=10)
        self.boton_registrar_ingreso.grid(row=1, column=0, padx=10, pady=5)
        self.boton_registrar_egreso.grid(row=2, column=0, padx=10, pady=5)
        self.boton_plan_ahorro.grid(row=3, column=0, padx=10, pady=5)
        self.tabla_movimientos.grid(row=4, column=0, padx=10, pady=5)
        # Configurar la tabla de movimientos
        self.tabla_movimientos['columns'] = ('concepto', 'monto', 'tipo')
        self.tabla_movimientos.column('#0', width=0, stretch=tk.NO)
        self.tabla_movimientos.column('concepto', anchor=tk.W, width=200)
        self.tabla_movimientos.column('monto', anchor=tk.CENTER, width=100)
        self.tabla_movimientos.column('tipo', anchor=tk.W, width=100)
        self.tabla_movimientos.heading('#0', text='', anchor=tk.W)
        self.tabla_movimientos.heading('concepto', text='Concepto', anchor=tk.W)
        self.tabla_movimientos.heading('monto', text='Monto', anchor=tk.CENTER)
        self.tabla_movimientos.heading('tipo', text='Tipo', anchor=tk.W)

class PlanAhorroFrame:
    def __init__(self, notebook, usuario):
        self.frame = tk.Frame(notebook)
        notebook.add(self.frame, text="Plan de Ahorro")
        self.usuario = usuario
        self.meta = np.inf  # Valor de la meta de ahorro
        self.label_ahorro = ttk.Label(self.frame, text="Total ahorrado: 0")
        self.label_meta = ttk.Label(self.frame, text=f"Meta de ahorro: {self.meta}")
        self.label_felicitacion = ttk.Label(self.frame, text="")
        self.entry_meta = ttk.Entry(self.frame)
        self.entry_abono = ttk.Entry(self.frame)
        self.boton_fijar_meta = ttk.Button(self.frame, text="Fijar Meta", command=self.fijar_meta)
        
        self.actualizar_labels()

        # Posicionar elementos
        self.label_ahorro.pack()
        self.label_meta.pack()
        self.label_felicitacion.pack()
        self.entry_meta.pack()
        self.boton_fijar_meta.pack()
        
        

    def fijar_meta(self):
        self.meta = float(self.entry_meta.get())
        self.label_meta.config(text=f"Meta de ahorro: {self.meta}")
        self.mostrar_mensaje_felicitacion()
        
    def mostrar_plan_ahorro(self):
        monto_abono = simpledialog.askfloat("Plan de Ahorro", "Ingrese el monto para abonar al plan de ahorro:")
        if monto_abono is not None:
            if monto_abono > self.usuario.plan_ahorro:
                messagebox.showerror("Error", "Fondos insuficientes para el abono al ahorro.")
            else:
                self.usuario.saldo -= monto_abono
                self.usuario.plan_ahorro += monto_abono
                self.usuario.movimientos.append(("Abono a Plan de Ahorro", monto_abono, 'Ahorro'))
                self.actualizar_labels()  # Llamar a la actualización del valor del ahorro

    def actualizar_labels(self):
        self.label_ahorro.config(text=f"Total ahorrado: {self.usuario.plan_ahorro}")
        self.mostrar_mensaje_felicitacion()
        
    def mostrar_mensaje_felicitacion(self):
        if self.usuario.plan_ahorro >= self.meta:
            self.label_felicitacion.config(text="¡Felicidades! ¡Has alcanzado tu meta de ahorro!")    

class AplicacionFinanzas:
    def __init__(self, root):
        
        
        self.usuarios_registrados = {
            "usuario1": Usuario("usuario1", "contraseña1"),
            "usuario2": Usuario("usuario2", "contraseña2")
        }
        self.root = root
        self.root.title("Gestión Financiera")
        self.usuario_actual = None

        self.notebook = ttk.Notebook(root)
        
        self.notebook.pack(expand=1, fill="both")

        self.login = LoginFrame(self.notebook, self.verificar_credenciales, self.cerrar_sesion)
        self.registro = RegistroFrame(self.notebook, self.registrar_nuevo_usuario)
        self.finanzas = FinanzasFrame(self.notebook, self.registrar_ingreso, self.registrar_egreso, self.mostrar_plan_ahorro)
        # self.plan_ahorro = PlanAhorroFrame(self.notebook, self.usuario_actual)

    def verificar_credenciales(self):
        id_ingresado = self.login.entry_id.get()
        contraseña_ingresada = self.login.entry_contraseña.get()

        if id_ingresado in self.usuarios_registrados:
            usuario = self.usuarios_registrados[id_ingresado]
            if contraseña_ingresada == usuario.contraseña:
                self.usuario_actual = usuario
                self.mostrar_interfaz_finanzas(usuario)
                self.root.title(f"Gestión Financiera - Usuario: {id_ingresado}")
                self.login.boton_cerrar_sesion.config(state="normal")
                messagebox.showinfo("¡Ingreso exitoso!", f"Bienvenido, {id_ingresado}!")
            else:
                messagebox.showerror("Error", "Credenciales incorrectas")
        else:
            messagebox.showerror("Error", "Usuario no encontrado")

    def cerrar_sesion(self):
        self.usuario_actual = None
        self.root.title("Gestión Financiera")
        self.login.label_usuario.config(text="Usuario actual: ")
        self.login.boton_cerrar_sesion.config(state="disabled")
        messagebox.showinfo("Sesión cerrada", "Sesión cerrada exitosamente.")

    def mostrar_interfaz_finanzas(self, usuario):
        self.login.frame_login.pack_forget()

        self.finanzas.label_saldo.config(text=f"Saldo actual: {usuario.saldo}")
        self.mostrar_movimientos(usuario.movimientos)
        
        self.plan_ahorro = PlanAhorroFrame(self.notebook, usuario)  # Guardar el PlanAhorroFrame en una variable

        self.finanzas.boton_plan_ahorro.config(command=lambda: self.mostrar_plan_ahorro(self.plan_ahorro))  # Llamar a mostrar_plan_ahorro
        
        

        # Código para mostrar la interfaz de finanzas...

    def registrar_nuevo_usuario(self):
        nuevo_id = self.registro.entry_nuevo_id.get()
        nueva_contraseña = self.registro.entry_nueva_contraseña.get()

        if nuevo_id and nueva_contraseña:
            if nuevo_id in self.usuarios_registrados:
                messagebox.showerror("Error", "El usuario ya existe")
            else:
                nuevo_usuario = Usuario(nuevo_id, nueva_contraseña)
                self.usuarios_registrados[nuevo_id] = nuevo_usuario
                messagebox.showinfo("Éxito", "Usuario registrado correctamente")
        else:
            messagebox.showerror("Error", "Ingrese un ID y contraseña válidos")
    
    def registrar_ingreso(self):
        try:
            monto = simpledialog.askfloat("Registrar Ingreso", "Ingrese el monto del ingreso:")
            concepto = simpledialog.askstring("Concepto", "Ingrese el concepto del ingreso:")

            if monto is not None:
                if monto <= 0:
                    raise ValueError("El monto debe ser mayor que cero")
                self.usuario_actual.ingresos += monto
                self.usuario_actual.saldo += monto
                self.usuario_actual.movimientos.append((concepto, monto, 'Ingreso'))
                messagebox.showinfo("Éxito", f"Ingreso de {monto} registrado.")
                self.actualizar_saldo()
                self.mostrar_movimientos(self.usuario_actual.movimientos)
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def registrar_egreso(self):
        try:
            monto = simpledialog.askfloat("Registrar Egreso", "Ingrese el monto del egreso:")
            concepto = simpledialog.askstring("Concepto", "Ingrese el concepto del egreso:")

            if monto is not None:
                if monto <= 0:
                    raise ValueError("El monto debe ser mayor que cero")
                if monto > self.usuario_actual.saldo:
                    raise ValueError("Fondos insuficientes")
                self.usuario_actual.egresos += monto
                self.usuario_actual.saldo -= monto
                self.usuario_actual.movimientos.append((concepto, monto, 'Egreso'))
                messagebox.showinfo("Éxito", f"Egreso de {monto} registrado.")
                self.actualizar_saldo()
                self.mostrar_movimientos(self.usuario_actual.movimientos)
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def actualizar_saldo(self):
        self.finanzas.label_saldo.config(text=f"Saldo actual: {self.usuario_actual.saldo}")

    def mostrar_movimientos(self, movimientos):
        self.finanzas.tabla_movimientos.delete(*self.finanzas.tabla_movimientos.get_children())
        for idx, (concepto, monto, tipo) in enumerate(movimientos, start=1):
            self.finanzas.tabla_movimientos.insert("", "end", text=str(idx), values=(concepto, monto, tipo))

    
    def mostrar_plan_ahorro(self, plan_ahorro_frame):
        monto_abono = simpledialog.askfloat("Plan de Ahorro", "Ingrese el monto para abonar al plan de ahorro:")
        if monto_abono is not None:
            if monto_abono > self.usuario_actual.saldo:
                messagebox.showerror("Error", "Fondos insuficientes para el abono al ahorro.")
            else:
                self.usuario_actual.saldo -= monto_abono
                self.usuario_actual.plan_ahorro += monto_abono
                self.usuario_actual.movimientos.append(("Abono a Plan de Ahorro", monto_abono, 'Ahorro'))
                self.actualizar_saldo()
                self.mostrar_movimientos(self.usuario_actual.movimientos)
                plan_ahorro_frame.actualizar_labels()  # Actualizar el PlanAhorroFrame pasado como argumento
                messagebox.showinfo("Éxito", f"Abono de {monto_abono} al Plan de Ahorro registrado.")

        plan_ahorro_frame.actualizar_labels()

    
        
    def agregar_usuario(self, id, contraseña):
        if id not in self.usuarios_registrados:
            nuevo_usuario = Usuario(id, contraseña)
            self.usuarios_registrados[id] = nuevo_usuario
            messagebox.showinfo("Éxito", "Usuario registrado correctamente.")
        else:
            messagebox.showerror("Error", "El usuario ya existe.")

    def eliminar_usuario(self, id):
        if id in self.usuarios_registrados:
            del self.usuarios_registrados[id]
            messagebox.showinfo("Éxito", f"Usuario {id} eliminado correctamente.")
        else:
            messagebox.showerror("Error", "El usuario no existe.")

    def modificar_contraseña(self, id, nueva_contraseña):
        if id in self.usuarios_registrados:
            self.usuarios_registrados[id].contraseña = nueva_contraseña
            messagebox.showinfo("Éxito", f"Contraseña modificada correctamente.")
        else:
            messagebox.showerror("Error", "El usuario no existe.")

def main():
    root = tk.Tk()
    app = AplicacionFinanzas(root)
    root.mainloop()

if __name__ == "__main__":
    main()



      

