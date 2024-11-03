# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.16.1
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# # Criando QR Code

# Para instalar:
#
# ```
# pip install qrcode
# pip install Pillow
# ```

# Documentação: https://github.com/lincolnloop/python-qrcode

# Links da Aleatórios:
#
# - https://www.facebook.com/
# - https://www.instagram.com/
# - https://www.youtube.com/
# - https://www.tiktok.com/

# ## QR Code simples

# !pip install qrcode
# !pip install Pillow

# +
import qrcode

imagem = qrcode.make("https://www.google.com")
imagem.save("google.jpg")
# -

# ## QR Code com imagem

# +
import qrcode 
from qrcode.image.styledpil import StyledPilImage

qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H)  # para poder adicionar uma imagem
qr.add_data("https://www.youtube.com")

imagem = qr.make_image(
    image_factory=StyledPilImage,
    embeded_image_path="logo.png",
)

imagem.save("qrcode_logo.png")
# -

# ## Criando diversos QR Code ao mesmo tempo

# +
redes_sociais = {
    "Facebook": "https://www.facebook.com",
    "Instagram": "https://www.instagram.com",
    "YouTube": "https://www.youtube.com/",
    "TikTok": "https://www.tiktok.com/",
}

for rede_social, url in redes_sociais.items():
    qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H)
    qr.add_data(url)

    imagem = qr.make_image(
        image_factory=StyledPilImage,
        embeded_image_path="logo.png",
    )

    imagem.save(f"sociais_{rede_social}.png")
# -


