from pytubefix import YouTube

def download_vid(url):

    #pegando o valor da url
    value_url = url

    #formatando para texto
    form_url = str(value_url)

    #baixando o video/audio
    donwload = YouTube(form_url)

    #escolhendo resolucao

    donwload_format = donwload.streams.filter(progressive=True, file_extension="mp4",).first()

    donwload_video = donwload_format.download()

