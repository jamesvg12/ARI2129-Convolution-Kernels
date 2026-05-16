import streamlit as st
import cv2
import numpy as np
from PIL import Image

st.set_page_config(
    page_title="Convolution Kernel Simulator",
    page_icon="🔬",
    layout="wide"
)

st.title("Convolution Kernel Simulator")
st.markdown("Explore how different convolution kernels affect an image")

st.divider()

col_controls, col_output = st.columns([1, 1])

with col_controls:
    st.subheader("Controls")


    #image input
    st.markdown("#### Step 1: Choose an Image")

    image_source = st.radio(
        "Image source",
        ["Upload my own", "Use a sample image"],
        horizontal=True
    )

    image_bgr = None  #working image in BGR format for OpenCV

    if image_source == "Upload my own":
        uploaded_file = st.file_uploader(
            "Upload an image",
            type=["jpg", "jpeg", "png"]
        )
        if uploaded_file is not None:
            pil_image = Image.open(uploaded_file).convert("RGB")
            image_rgb = np.array(pil_image)
            #RGB to BGR for OpenCV
            image_bgr = cv2.cvtColor(image_rgb, cv2.COLOR_RGB2BGR)

    else:
        sample_choice = st.selectbox(
            "Choose a sample image",
            ["Checkerboard", "Gradient", "Noise"]
        )
        if sample_choice == "Checkerboard":
            tile = np.zeros((32, 32), dtype=np.uint8)
            tile[0:16, 0:16] = 255
            tile[16:32, 16:32] = 255
            gray = np.tile(tile, (8, 8))
            image_bgr = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)
        elif sample_choice == "Gradient":
            gray = np.tile(np.arange(256, dtype=np.uint8), (256, 1))
            image_bgr = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)
        elif sample_choice == "Noise":
            gray = np.random.randint(0, 256, (256, 256), dtype=np.uint8)
            image_bgr = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)

    #kernel selector and paramater slides
    st.markdown("#### Step 2: Choose a Kernel")

    kernel_type = st.selectbox(
        "Kernel type",
        ["Gaussian", "Sobel", "Laplacian"]
    )

    st.markdown("#### Step 3: Adjust Parameters")

    #gaussian parameters
    if kernel_type == "Gaussian":
        kernel_size = st.slider(
            "Kernel size (must be odd)", 
            min_value=3, max_value=31, value=5, step=2
        )
        sigma = st.slider(
            "Sigma (blur spread)",
            min_value=0.1, max_value=10.0, value=1.0, step=0.1
        )
        padding = st.slider(
            "Padding", 
            min_value=0, max_value=10, value=0, step=1
        )
        stride = st.slider(
            "Stride", 
            min_value=1, max_value=5, value=1, step=1
        )

        #showing kernel matrix values
        st.markdown("**Kernel Matrix:**")
        kernel_matrix = cv2.getGaussianKernel(kernel_size, sigma)
        kernel_2d = kernel_matrix @ kernel_matrix.T  # Outer product gives 2D kernel
        st.dataframe(
            np.round(kernel_2d, 4),
            use_container_width=True
        )

    #sobel parameters
    elif kernel_type == "Sobel":
        kernel_size = st.slider(
            "Kernel size (must be odd)",
            min_value=3, max_value=7, value=3, step=2
        )
        direction = st.radio(
            "Direction",
            ["X (vertical edges)", "Y (horizontal edges)", "Combined"],
            horizontal=True
        )
        
        #toggle for sobel output display mode
        sobel_display_mode = st.radio(
            "Output display mode",
            ["Absolute (bright edges on black)", "Normalised (shows edge direction)"],
            horizontal=False,
            help="Absolute: takes the absolute value so all edges appear bright white. "
                 "Normalised: preserves sign so dark=negative edge, grey=no edge, white=positive edge."
        )
        
        padding = st.slider(
            "Padding",
            min_value=0, max_value=10, value=0, step=1
        )
        stride = st.slider(
            "Stride",
            min_value=1, max_value=5, value=1, step=1
        )

        #showing sobel kernel matrix
        st.markdown("**Kernel Matrix:**")
        if "X" in direction:
            sobel_display = cv2.getDerivKernels(1, 0, kernel_size)
        elif "Y" in direction:
            sobel_display = cv2.getDerivKernels(0, 1, kernel_size)
        else:
            sobel_display = cv2.getDerivKernels(1, 0, kernel_size)
        kx = sobel_display[0]
        ky = sobel_display[1]
        sobel_2d = kx @ ky.T
        st.dataframe(
            np.round(sobel_2d, 4),
            use_container_width=True
        )

    #laplacian parameters
    elif kernel_type == "Laplacian":
        kernel_size = st.slider(
            "Kernel size (must be odd)",
            min_value=1, max_value=31, value=3, step=2
        )
        padding = st.slider(
            "Padding",
            min_value=0, max_value=10, value=0, step=1
        )
        stride = st.slider(
            "Stride",
            min_value=1, max_value=5, value=1, step=1
        )

        #showing basic laplacian kernel for reference
        st.markdown("**Kernel Matrix (reference):**")
        if kernel_size == 1:
            lap_display = np.array([[0, 1, 0], [1, -4, 1], [0, 1, 0]])
        else:
            lap_display = np.array([[0, 1, 0], [1, -4, 1], [0, 1, 0]])
        st.dataframe(lap_display, use_container_width=True)

    #output dimension calculation
    if image_bgr is not None:
        h, w = image_bgr.shape[:2]
        out_h = (h + 2 * padding - kernel_size) // stride + 1
        out_w = (w + 2 * padding - kernel_size) // stride + 1
        st.markdown("**Output Dimensions:**")
        st.markdown(
            f"Input: `{w}×{h}` → Output: `{out_w}×{out_h}` "
            f"(kernel: {kernel_size}, padding: {padding}, stride: {stride})"
        )


with col_output:
    st.subheader("Output")

    if image_bgr is not None:
        #convert BGR to RGB for display
        image_rgb_display = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2RGB)
        st.markdown("**Original Image**")
        st.image(image_rgb_display, use_container_width=True)

        #applying selected kernel
        st.markdown("**Processed Image**")

        #convert to grayscale for processing
        gray = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2GRAY)

        #apply padding first using zero-padding (border reflects 0s)
        if padding > 0:
            gray_padded = cv2.copyMakeBorder(
                gray,
                padding, padding, padding, padding,
                cv2.BORDER_CONSTANT, value=0
            )
        else:
            gray_padded = gray

        #applying gaussian
        if kernel_type == "Gaussian":
            processed = cv2.GaussianBlur(
                gray_padded,
                (kernel_size, kernel_size),
                sigma
            )

        #applying sobel
        elif kernel_type == "Sobel":
            if "X" in direction:
                processed = cv2.Sobel(
                    gray_padded, cv2.CV_64F, 1, 0, ksize=kernel_size
                )
            elif "Y" in direction:
                processed = cv2.Sobel(
                    gray_padded, cv2.CV_64F, 0, 1, ksize=kernel_size
                )
            else:
                #compute x and y then merge for combined
                sobel_x = cv2.Sobel(
                    gray_padded, cv2.CV_64F, 1, 0, ksize=kernel_size
                )
                sobel_y = cv2.Sobel(
                    gray_padded, cv2.CV_64F, 0, 1, ksize=kernel_size
                )
                processed = cv2.magnitude(sobel_x, sobel_y)

            #toggle between absolute value and normalised display
            if sobel_display_mode == "Absolute (bright edges on black)":
                #takes absolute value, both positive and negative
                #edges show as bright white on black background
                processed = cv2.convertScaleAbs(processed)
            else:
                #normalise
                #zero/no-edge appears as grey (128)
                #shows direction of intensity change
                processed = cv2.normalize(
                    processed, None, 0, 255, cv2.NORM_MINMAX
                )

        #applying laplacian
        elif kernel_type == "Laplacian":
            processed = cv2.Laplacian(
                gray_padded, cv2.CV_64F, ksize=kernel_size
            )
            #normalise for display
            processed = cv2.normalize(
                processed, None, 0, 255, cv2.NORM_MINMAX
            )

        #applying stride by sampling every Nth pixel
        #(stride=1 keeps all pixels, stride=2 keeps every other, etc.)
        processed_strided = processed[::stride, ::stride]

        #convert to uint8 for display
        processed_display = np.uint8(processed_strided)

        st.image(processed_display, use_container_width=True)

    else:
        st.info("Upload an image or select a sample to get started.")