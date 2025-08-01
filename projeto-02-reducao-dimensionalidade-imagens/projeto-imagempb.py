# -*- coding: utf-8 -*-
"""
Projeto: Redução de Dimensionalidade em Imagens para Redes Neurais
Desenvolvido por: Edson Gomes Chaves
Data: 07/2025
"""

import tkinter as tk
from tkinter import filedialog
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

def carregar_imagem():
    print("=" * 70)
    print("Projeto: Redução de Dimensionalidade em Imagens para Redes Neurais")
    print("Desenvolvido por Edson Gomes Chaves - 07/2025 - Dio.me")
    print("=" * 70)
    print("[INFO] Selecione uma imagem para iniciar o processamento...")
    root = tk.Tk()
    root.withdraw()
    caminho_imagem = filedialog.askopenfilename(
        title="Selecione uma imagem",
        filetypes=[("Imagens", "*.png *.jpg *.jpeg *.bmp")]
    )
    return caminho_imagem

def ler_imagem(path):
    img = mpimg.imread(path)
    if img.shape[2] == 4:
        img = img[:, :, :3]
    return img

def converter_para_cinza(img_rgb):
    altura, largura, _ = img_rgb.shape
    img_cinza = np.zeros((altura, largura), dtype=np.uint8)
    w_r, w_g, w_b = 0.299, 0.587, 0.114
    for i in range(altura):
        for j in range(largura):
            r, g, b = img_rgb[i][j]

            if r <= 1.0 and g <= 1.0 and b <= 1.0:
                cinza = int((w_r * r + w_g * g + w_b * b) * 255)
            else:
                cinza = int(w_r * r + w_g * g + w_b * b)

            img_cinza[i][j] = np.clip(cinza, 0, 255)
    return img_cinza

def binarizar(img_cinza):
    media = int(np.mean(img_cinza))
    print(f"[INFO] Threshold para binarização: {media}")
    img_bin = np.where(img_cinza >= media, 255, 0).astype(np.uint8)
    return img_bin

def exibir_e_salvar(original, cinza, binaria):
    fig, axs = plt.subplots(2, 3, figsize=(18, 9))  # ~600x450 px cada imagem

    axs[0][0].imshow(original)
    axs[0][0].set_title("Figura 1: Original")
    axs[0][0].axis('off')

    axs[0][1].imshow(cinza, cmap='gray')
    axs[0][1].set_title("Figura 2: Níveis de Cinza")
    axs[0][1].axis('off')

    axs[0][2].imshow(binaria, cmap='gray')
    axs[0][2].set_title("Figura 3: Preto e Branco")
    axs[0][2].axis('off')

    # Única descrição centralizada
    descricao = (
        "Descrição:\n"
        "A imagem original foi carregada com canais RGB. A segunda imagem representa a transformação para tons de cinza, "
        "realizada com base em pesos lineares perceptuais (regressão linear). "
        "A terceira imagem foi binarizada utilizando o valor médio dos pixels como limiar, resultando em preto (0) ou branco (255)."
    )

    axs[1][0].text(0.5, 0.5, descricao, ha='center', va='center', fontsize=10, wrap=True)
    axs[1][0].axis('off')
    axs[1][1].axis('off')
    axs[1][2].axis('off')

    # Rodapé institucional
    fig.suptitle("Projeto: Redução de Dimensionalidade em Imagens para Redes Neurais", fontsize=15)
    fig.text(0.5, 0.04, "Dio.me – projeto desenvolvido por Edson Gomes Chaves – 07-2025", 
             ha='center', fontsize=9)

    plt.tight_layout(rect=[0, 0.08, 1, 0.94])
    plt.show()

    salvar = input("\nDeseja salvar a imagem combinada com os resultados? (s/n): ").strip().lower()
    if salvar == 's':
        caminho_saida = filedialog.asksaveasfilename(
            defaultextension=".png",
            filetypes=[("PNG", "*.png")],
            title="Salvar imagem de saída"
        )
        if caminho_saida:
            fig.savefig(caminho_saida, dpi=100)
            print(f"[SUCESSO] Imagem salva em: {caminho_saida}")
        else:
            print("[INFO] Salvamento cancelado.")

if __name__ == "__main__":
    caminho = carregar_imagem()
    if not caminho:
        print("[ERRO] Nenhuma imagem selecionada.")
        input("Pressione ENTER para sair...")
    else:
        imagem_rgb = ler_imagem(caminho)
        imagem_cinza = converter_para_cinza(imagem_rgb)
        imagem_binaria = binarizar(imagem_cinza)
        exibir_e_salvar(imagem_rgb, imagem_cinza, imagem_binaria)
        input("\nProcesso concluído. Pressione ENTER para sair...")
