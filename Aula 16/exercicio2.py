class Midia:
    def __init__(self, titulo, duracao_seg):
        self.titulo = titulo
        self.duracao_seg = duracao_seg

    def exibir(self):
        print(f"Titulo:{self.titulo} com duração de {self.duracao_seg}")

    def __str__(self):
        return f"{self.titulo}"

class Musica(Midia):
    def __init__(self, titulo, duracao_seg, artista):
        super().__init__(titulo,duracao_seg)
        self.artista = artista

    def exibir(self):
        print(f"Titulo:{self.titulo} com duração de {self.duracao_seg} do artista {self.artista}")

class Video(Midia):
    def __init__(self, titulo, duracao_seg, resolucao):
        super().__init__(titulo,duracao_seg)
        self.resolução = resolucao

    def exibir(self):
        print(f"Titulo:{self.titulo} com duração de {self.duracao_seg} na resolução {self.resolucao}")

Musica1 = Musica("Rock", 54, "Mike")
Video1 = Video("Rock in roll", 30, ".mp3" )

dicionario:dict[str,list[Midia]] = {"musica":[], "videos":[]}
dicionario["musica"].append(Musica1)
dicionario["videos"].append(Video1)
print(dicionario)

for item in dicionario.values():
    for midia in item:
        midia.exibir()

