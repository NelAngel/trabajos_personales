import pytube
import time

def progress_bar(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percent = (bytes_downloaded / total_size) * 100
    bar_length = 30
    filled_length = int(bar_length * percent / 100)
    bar = '█' * filled_length + '-' * (bar_length - filled_length)
    print(f'\rEn progreso: [{bar}] {percent:.1f}%', end='', flush=True)

while True:
    url = input("Ingresa la URL del video que deseas descargar (o 'salir' para terminar): ")

    if url.lower() == 'salir':
        print("Hasta luego, cuídate...")
        break

    video = pytube.YouTube(url)

    formato = input("Selecciona el formato de descarga (mp4 o mp3): ")

    if formato.lower() == 'mp4':
        print("Descargando video en formato mp4:")
        video.register_on_progress_callback(progress_bar)
        video_stream = video.streams.get_highest_resolution()
        file_extension = video_stream.mime_type.split("/")[-1]
        file_name = f"{video.title}.{file_extension}"
        video_stream.download(output_path='./downloads/', filename=file_name)
        print("\n¡Descarga de video en formato mp4 completa!")
    elif formato.lower() == 'mp3':
        print("Descargando audio en formato mp3:")
        audio = video.streams.get_audio_only()
        audio.register_on_progress_callback(progress_bar)
        file_name = f"{video.title}.mp3"
        audio.download(output_path='./downloads/', filename=file_name)
        print("\n¡Descarga de audio en formato mp3 completa!")
    else:
        print("El formato es inválido, por favor selecciona 'mp4' o 'mp3'.")

    continuar = input("¿Deseas descargar otro video? (s/n): ")

    if continuar.lower() != 's':
        print("Hasta luego")
        break

