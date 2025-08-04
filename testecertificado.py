from PIL import Image, ImageDraw, ImageFont  
import os

names = [
    "Leticia R de Lima",
    "Karol Brito",
    "Renan Soares",
    "Emili Lima"
]

os.makedirs('Python Automate', exist_ok=True)  

for index, name in enumerate(names, start=1):
    certificado_modelo = Image.open('certificadoteste.png')

    desanhador = ImageDraw.Draw(certificado_modelo)

    font = ImageFont.truetype("C:/Users/leticia.lima/Desktop/Python automate/Roboto_Condensed-Regular.ttf",50)

    text_posicao = (607, 645)

    desanhador.text(text_posicao, name, fill="green", font=font)

    nome_arq = f"{name}.png"

    arq_saida = os.path.join("Python Automate", nome_arq)

    certificado_modelo.save(arq_saida)

    print (f'{index}, Certificado Teste {name}')