# CycleGAN Style Transfer API

This repository contains the backend for a CycleGAN-based style transfer web application that transforms user-uploaded images into artworks in the styles of famous painters — **Vincent van Gogh**, **Edvard Munch**, and **Claude Monet**.

All models were personally trained using artist-specific datasets and implemented with reference to research literature. This repo includes the Flask API that powers the web app, the trained models, and the Jupyter notebooks used for model development.

---

## Features

- RESTful API built with **Flask**
- Supports style transfer using **pretrained CycleGAN models**
- Models trained using **custom curated datasets** per artist
- Supports styles: **Van Gogh**, **Munch**, and **Monet**
- Integration-ready: communicates seamlessly with a Flutter frontend

---

## Models

Each model is a CycleGAN trained for unpaired image-to-image translation using TensorFlow/Keras. Architectures were adapted from research papers and tuned specifically for stylistic consistency.

The following styles are available:
- `vanGoghModel.pth`
- `munchModel.pth`
- `monetModel.pth`

Models are located in the `/models/` directory.
