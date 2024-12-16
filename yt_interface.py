from tkinter import *
from func_download import *




# janela principal
def janela():

    #fucao para fazer o download do video/audio
    def enviar():
        valor_url = url.get()

        download_vid(url=valor_url)

        print(f"A url inserida e: {valor_url}")

        #testando lista
    
    #iniciando interface
    janela = Tk()
    janela.title("Youtube Downloader")
    janela.geometry("400x300")
    janela.resizable(False, False)


    #titulo
    titulo = Label(font=("arial", 20, "bold"), text="Coloque sua URL")
    titulo.pack()

    #valor para introduzir a URL
    url = Entry(janela, font=("arial", 12), width=10)
    url.pack()

    #escolhei a resolucao

    #botao de enviar
    download = Button(janela, text="download", command=enviar)
    download.pack()


    janela.mainloop()

janela()

