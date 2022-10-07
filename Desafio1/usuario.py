class Usuario:

    def __init__(self, id, nombre_usuario):
        self.id = id
        self.nombre_usuario = nombre_usuario
        self.correos_enviados = 0
        self.correos_recibidos = 0

    def enviar_correo(self, usuario_destino):
        self.correos_enviados += 1
        usuario_destino.correos_recibidos += 1


usuario_1 = Usuario(1, 'knajarro94')
usuario_2 = Usuario(2, 'maritzag.lopez')

usuario_1.enviar_correo(usuario_2)

print(f'Correos enviados, usuario_1: {usuario_1.nombre_usuario} {usuario_1.correos_enviados}')
print(f'Correos recibidos, usuario_1: {usuario_1.nombre_usuario} {usuario_1.correos_recibidos}')
print(f'Correos enviados, usuario_2: {usuario_2.nombre_usuario} {usuario_2.correos_enviados}')
print(f'Correos recibidos, usuario_2: {usuario_2.nombre_usuario} {usuario_2.correos_recibidos}')
