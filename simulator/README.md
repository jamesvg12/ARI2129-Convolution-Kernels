# Convolution Kernel Simulator

An interactive simulator for exploring convolution kernels in computer vision.
Built with Streamlit and OpenCV.

## Setup

1. Clone the repository
2. Navigate to the simulator folder:
        cd kernel-simulator
3. Install dependencies:
        pip install -r requirements.txt
4. Launch the simulator:
        python -m streamlit run app.py

## Features

- Upload your own image or choose a built-in sample
- Choose between Gaussian, Sobel, and Laplacian kernels
- Adjust parameters live: kernel size, sigma, stride, padding
- View the kernel matrix updating in real time
- Toggle Sobel output between absolute and normalised display
- See output dimensions update as parameters change

## Parameters

| Parameter | Description |
|---|---|
| Kernel size | Width/height of the kernel grid (must be odd) |
| Sigma | Gaussian blur spread — higher = stronger blur |
| Stride | Step size of kernel movement — higher = smaller output |
| Padding | Zero-padding added to image border before convolution |

## Kernel Types

- **Gaussian** — smoothing and noise reduction
- **Sobel** — edge detection in X, Y, or combined directions
- **Laplacian** — omnidirectional edge detection using second derivative