import cv2
import numpy as np

# Define model file paths
model_prototxt = "pose_deploy_linevec.prototxt"
model_caffemodel = "pose_iter_440000.caffemodel"

def load_model():
    """Load the human pose estimation model."""
    return cv2.dnn.readNetFromCaffe(model_prototxt, model_caffemodel)

def preprocess_image(image):
    """Preprocess the image for model input."""
    # Ensure the image has 3 channels (RGB)
    if image.shape[2] == 1:
        image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
    elif image.shape[2] == 4:
        image = cv2.cvtColor(image, cv2.COLOR_BGRA2BGR)
    image = cv2.resize(image, (368, 368))
    image = image.transpose((2, 0, 1))
    image = image / 255.0
    return image

def measure_body(image, model):
    """Detect the body using a human pose estimation model and calculate the
    chest, waist, hip circumferences, and height."""
    # Detect the body.
    keypoints = detect_body(image, model)

    # Calculate the circumferences and height.
    chest_circumference = calculate_circumference(keypoints[5], keypoints[6], keypoints[7])
    waist_circumference = calculate_circumference(keypoints[11], keypoints[12])
    hip_circumference = calculate_circumference(keypoints[23], keypoints[24])
    height = calculate_height(keypoints[1], keypoints[15])

    return chest_circumference, waist_circumference, hip_circumference, height

def detect_body(image, model):
    """Detect the body using a human pose estimation model and return the
    keypoints."""
    model.setInput(image)
    out = model.forward()
    keypoints = [out[i, :] for i in range(out.shape[0])]
    return keypoints

def calculate_circumference(point1, point2, point3):
    """Calculate the circumference of a triangle given three points."""
    distances = [np.linalg.norm(point1 - point2), np.linalg.norm(point2 - point3), np.linalg.norm(point3 - point1)]
    circumference = sum(distances) / 2.0 * np.pi
    return circumference

def calculate_height(point1, point2):
    """Calculate the height of a person given two points."""
    distance = np.linalg.norm(point1 - point2)
    height = distance * 170.0 / 100.0
    return height

# Read an image from a file
image = cv2.imread('4.jpg', cv2.IMREAD_COLOR)
RGB = cv2.imread('4.jpg')[...,::-1]
# Convert the image to RGB and preprocess it
#image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
preprocessed_image = preprocess_image(RGB)

# Load the model
model = load_model()

# Measure the body
chest_circumference, waist_circumference, hip_circumference, height = measure_body(preprocessed_image, model)

# Display the measurements
print('Chest circumference:', chest_circumference)
print('Waist circumference:', waist_circumference)
print('Hip circumference:', hip_circumference)
print('Height:', height)
