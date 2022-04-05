from model import *
from PIL import Image
from fastapi import FastAPI, File, UploadFile
import uvicorn
from io import BytesIO
import numpy as np
from torchvision.transforms import Compose, Resize, ToTensor, Normalize


BATCH_SIZE = 32
device = "cuda" if torch.cuda.is_available() else "cpu"

model = BugNet()
model = torch.load('torch_model/best-model.pt')

model.eval()


def label_onehot(l):
    t = torch.zeros(NUM_CLASSES, dtype=torch.float)
    t[l] = 1
    return t

image_transforms = Compose([
    Resize((256,256)),
    ToTensor(),
    Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
])

target_labels = ['adalia bipunctata', 'calliteara pudibunda', 'cerambyx cerdo', 'gryllotalpa gryllotalpa', 'lucanus cervus', 'mantis religiosa', 'melolontha melolontha', 'phyrrochorus apterus', 'rhaphigaster nebulosa', 'sesia apiformis', 'tettigonia viridissima', 'xylocopa violacea']


def classify(model, image_transform, image_path, classes):
    model = model.eval()
    image = Image.open(image_path)
    image = image_transform(image).float().to(device)
    image = image.unsqueeze(0)

    output = model(image)
    _, predicted = torch.max(output.data, 1)
    print(classes[predicted.item()])


classify(model, image_transforms, "test_photo.jpg", classes=target_labels)

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:3000",
]

@app.get("/ping")
async def ping():
    return "Bok Deane, ovo zasad radi :D"

def read_file_as_image(data) -> np.ndarray:
    image = Image.open(BytesIO(data))
    return image

@app.post("/predict")
async def predict(
    file: UploadFile = File(...)
):
    model.eval()
    image = read_file_as_image(await file.read())
    image = image_transforms(image)
    img_batch = torch.unsqueeze(image, 0)
    img_batch = img_batch.to(device)

    outputs = model(img_batch)
    outputs = nn.Softmax(dim=1)(outputs).cpu().detach().numpy()
    print(outputs)

    predicted_class = target_labels[np.argmax(outputs[0])]
    confidence = np.max(outputs[0])

    return {
        'class': predicted_class,
        'confidence': float(confidence)
    }



if __name__ == "__main__":
    uvicorn.run(app, host='localhost', port=8000)
