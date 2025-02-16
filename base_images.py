import os
import tarfile
from PIL import Image
from io import BytesIO
import json

import numpy as np
from skimage import data
from skimage.util import montage
import matplotlib.pyplot as plt

# Caminho para o arquivo .tar.gz
tar_path = 'H:\Documentos\\14_semestre\PDI\projeto\Digital-Image-Processing\database.tar.gz'

metadados = 'H:\Documentos\\14_semestre\PDI\projeto\Digital-Image-Processing\metadados.json'

grupo_imagens = []
imagens = []

# Abrir o arquivo JSON
with open(metadados, 'r') as file:
    # Carregar o conteúdo JSON do arquivo para uma variável
    data = json.load(file)

    for i in data['fruits']:
        grupo_imagens.append(i) #append nos metadados
        imagens.append([])  #matriz que terá as imagens de cada fruta

print(grupo_imagens)

# Abrir o arquivo .tar.gz
with tarfile.open(tar_path, 'r:gz') as tar:
    
    # Listar os arquivos dentro do tar
    for member in tar.getmembers():
        #print(member)
        # Verificar se o arquivo é uma imagem (por exemplo, PNG, JPEG)
        if member.name.endswith('.png') or member.name.endswith('.jpg'):
            # Extrair a imagem diretamente para a memória
            file = tar.extractfile(member).read()
            
            print(file)

            # Carregar a imagem com PIL
            imagens.append(Image.open(BytesIO(file)))
            
            

            # Exibir a imagem (ou faça outra manipulação)
            #img.show()

    montage_image = montage(imagens)

    plt.imshow(montage_image)
    plt.axis('off')  # Desliga os eixos
    plt.show()