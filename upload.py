import os
import subprocess


def generate_html_file(source_folder, output_file, download_folder):

    files = os.listdir(source_folder)

    files = [
        f for f in files if os.path.isfile(os.path.join(source_folder, f))
    ]

    html_content = "<html><body><ul>"

    for file_name in files:
        file_path = os.path.join(download_folder, file_name)
        download_link = f"<a href='{file_path}' download><button>Download</button></a> {file_name}"
        html_content += f"<li>{download_link}</li>"

    if os.path.exists(output_file):
        os.remove(output_file)

    with open(output_file, 'w') as f:
        f.write(html_content)


def restart_nginx():
    subprocess.run(['sudo', 'service', 'nginx', 'restart'])


def start_ngrok():
    subprocess.run(['ngrok', 'http', '3000'])


source_folder = '/dados/upload/download'
output_file = '/dados/upload/arquivos.html'
download_folder = '/download'

generate_html_file(source_folder, output_file, download_folder)

restart_nginx()

start_ngrok()
