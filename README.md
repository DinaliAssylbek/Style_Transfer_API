# Art Style Transfer Project
This project explores the Cycle GAN technique for image style transfer. It was trained on three distinct artistic styles—Vincent van Gogh, Claude Monet, and Edvard Munch—using over 500 paintings per artist. The model allows for seamless transformation of any input image into the selected artistic style, without needing retraining for each new input.

### Key Components
1. Cycle GAN Model: The model was trained on unpaired datasets, allowing it to transfer artistic styles without requiring paired data. It leverages a dual-generator setup with cycle consistency loss for optimal performance.
2. Training: The model was trained on Google Colab using an A100 GPU. The training process took approximately 2 hours and 30 minutes per style with a learning rate of 1e-5 and 10 epochs.
3. Web Interface: A user-friendly Flutter web app allows users to upload an image, select an artist's style, and view the transformed output. The backend, powered by Flask and deployed on Railway, processes the image and returns the stylized version.

### API Documentation
This API allows you to apply artistic style transfer to images using Flask.

#### Endpoints
1. POST /predictVanGogh
- Apply the style of Vincent van Gogh to the uploaded image.
- Request: file (image)
- Response: PNG image in the style of Van Gogh

2. POST /predictMonet
- Apply the style of Claude Monet to the uploaded image.
- Request: file (image)
- Response: PNG image in the style of Monet

3. POST /predictMunch
- Apply the style of Edvard Munch to the uploaded image.
- Request: file (image)
- Response: PNG image in the style of Munch

### Results
![image](https://github.com/user-attachments/assets/7df5eef2-4e13-4027-9d4f-0e5c6857adb7)
