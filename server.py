from flask import Flask, request, send_file
import torch
from PIL import Image
import numpy as np
import io
import os
from albumentations import Compose, Resize, HorizontalFlip, Normalize
from albumentations.pytorch import ToTensorV2
from Training.model import Generator
from flask_cors import CORS

# Initialize Flask app
app = Flask(__name__)
CORS(app)

# Load your PyTorch models
VanGoghModel = Generator(3)
MonetModel = Generator(3)
MunchModel = Generator(3)

VanGoghModel.load_state_dict(torch.load("Models/vanGoghModel.pt", map_location=torch.device('cpu'), weights_only = True))
MonetModel.load_state_dict(torch.load("Models/monetModel.pt", map_location=torch.device('cpu'), weights_only = True))
MunchModel.load_state_dict(torch.load("Models/munchModel.pt", map_location=torch.device('cpu'), weights_only = True))

VanGoghModel.eval()
MonetModel.eval()
MunchModel.eval()

# Define image preprocessing
transforms = Compose(
    [
        Resize(width=256, height=256),
        Normalize(mean=[0.5, 0.5, 0.5], std=[0.5, 0.5, 0.5], max_pixel_value=255),
        ToTensorV2(),
    ]
)

def preprocess_image(image_bytes):
    """
    Preprocesses the image for model inference.
    Args:
        image_bytes: Byte data from the uploaded file.
    Returns:
        Preprocessed PyTorch tensor.
    """
    # Open the image
    image = Image.open(io.BytesIO(image_bytes)).convert("RGB")
    # Convert to NumPy array and apply Albumentations
    original_width, original_height = image.size 
    image_np = np.array(image)
    transformed = transforms(image=image_np)
    # Add batch dimension and return tensor
    return transformed["image"].unsqueeze(0), (original_width, original_height)  # Shape: [1, C, H, W]

def tensor_to_image(tensor):
    """
    Converts a PyTorch tensor to a PIL image.
    Args:
        tensor: PyTorch tensor output from the model.
    Returns:
        PIL Image encoded in PNG format.
    """
    tensor = tensor.squeeze(0)  # Remove batch dimension
    tensor = tensor.permute(1, 2, 0)  # Change to (H, W, C)
    tensor = tensor.clamp(0, 255)  # Ensure the values are in [0, 255]
    tensor = tensor.byte().cpu().numpy()  # Convert to NumPy
    image = Image.fromarray(tensor)
    # Save to a byte buffer as PNG
    buffer = io.BytesIO()
    image.save(buffer, format="PNG")
    buffer.seek(0)
    return buffer

def denormalize_image(tensor):
    """
    Denormalizes the image by reversing the normalization step.
    Args:
        tensor: The output tensor from the model.
    Returns:
        Denormalized image tensor.
    """
    mean = torch.tensor([0.5, 0.5, 0.5])
    std = torch.tensor([0.5, 0.5, 0.5])
    tensor = tensor * std[:, None, None] + mean[:, None, None]  # Reverse normalization
    tensor = tensor * 255.0  # Scale to [0, 255]
    return tensor.clamp(0, 255) 

@app.route("/predictVanGogh", methods=["POST"])
def predict_vanGogh():
    """
    Endpoint for image prediction.
    Receives an image file, preprocesses it, runs inference, and returns an image.
    """
    # Check if the request has a file
    if "file" not in request.files:
        return {"error": "No file uploaded"}, 400
    
    # Read the file
    file = request.files["file"]
    image_bytes = file.read()
    
    # Preprocess the image
    input_tensor, original_dims = preprocess_image(image_bytes)
    
    # Perform inference
    with torch.no_grad():
        output_tensor = VanGoghModel(input_tensor)
    
    # Denormalize the output tensor
    output_tensor = denormalize_image(output_tensor)
    
    # Convert the output tensor to an image
    output_image = tensor_to_image(output_tensor)

    original_width, original_height = original_dims
    resized_image = Image.open(output_image).resize((original_width, original_height))

    buffer = io.BytesIO()
    resized_image.save(buffer, format="PNG")
    buffer.seek(0)
    
    # Send the image back as a response
    return send_file(buffer, mimetype="image/png")

@app.route("/predictMonet", methods=["POST"])
def predict_Monet():
    """
    Endpoint for image prediction.
    Receives an image file, preprocesses it, runs inference, and returns an image.
    """
    # Check if the request has a file
    if "file" not in request.files:
        return {"error": "No file uploaded"}, 400
    
    # Read the file
    file = request.files["file"]
    image_bytes = file.read()
    
    # Preprocess the image
    input_tensor, original_dims = preprocess_image(image_bytes)
    
    # Perform inference
    with torch.no_grad():
        output_tensor = MonetModel(input_tensor)
    
    # Denormalize the output tensor
    output_tensor = denormalize_image(output_tensor)
    
    # Convert the output tensor to an image
    output_image = tensor_to_image(output_tensor)

    original_width, original_height = original_dims
    resized_image = Image.open(output_image).resize((original_width, original_height))

    buffer = io.BytesIO()
    resized_image.save(buffer, format="PNG")
    buffer.seek(0)
    
    # Send the image back as a response
    return send_file(buffer, mimetype="image/png")

@app.route("/predictMunch", methods=["POST"])
def predict_Munch():
    """
    Endpoint for image prediction.
    Receives an image file, preprocesses it, runs inference, and returns an image.
    """
    # Check if the request has a file
    if "file" not in request.files:
        return {"error": "No file uploaded"}, 400
    
    # Read the file
    file = request.files["file"]
    image_bytes = file.read()
    
    # Preprocess the image
    input_tensor, original_dims = preprocess_image(image_bytes)
    
    # Perform inference
    with torch.no_grad():
        output_tensor = MunchModel(input_tensor)
    
    # Denormalize the output tensor
    output_tensor = denormalize_image(output_tensor)
    
    # Convert the output tensor to an image
    output_image = tensor_to_image(output_tensor)

    original_width, original_height = original_dims
    resized_image = Image.open(output_image).resize((original_width, original_height))

    buffer = io.BytesIO()
    resized_image.save(buffer, format="PNG")
    buffer.seek(0)
    
    # Send the image back as a response
    return send_file(buffer, mimetype="image/png")

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=False)
