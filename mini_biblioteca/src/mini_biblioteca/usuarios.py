
class Usuario:
    def __init__(self, nome:str, id_usuario: str):
        self.nome = nome
        self.id_usuario = id_usuario

    def __str__(self):
        return f"Usuário({self.id_usuario}) {self.nome}"

