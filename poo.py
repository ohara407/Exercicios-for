""""
class Cachorro:
    nome = ''
    raca = ''
    disponibilidade = True
caramelo = Cachorro()
caramelo.nome = 'Farofa'
caramelo.raca = 'Sem raça definida'
print(caramelo)
print(dir(caramelo))
print(vars(caramelo))  #mostra o caramelo sem raça definida
"""
class Musica:
    artista = ''
    duracao = ''
    nome = ''
musica1 = Musica()
musica1.nome = "in the end"
musica1.artista = "linkin park"
musica1.duracao = "3:39"

musica2 = Musica()
musica2.nome = "Billie jean"
musica2.artista = "Michael jackson"
musica2.duracao = "4:54"

musica3 = Musica()
musica3.nome = "Superman"
musica3.artista = "Eminem"
musica3.duracao = "4:47"

print("Música.1")
print(vars(musica1))

print("Musica.2")
print(vars(musica2))

print("Musica.3")
print(vars(musica3))
