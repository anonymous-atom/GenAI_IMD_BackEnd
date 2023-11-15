import torch
from torchvision import transforms
from sentiment_posterv2.main import RecorderMeter, RecorderMeter1, ProgressMeter
from sentiment_posterv2.detect_sentiment import pyramid_trans_expr2
from PIL import Image

def load_pretrained_weights(model, checkpoint):
    import collections
    if 'state_dict' in checkpoint:
        state_dict = checkpoint['state_dict']
    else:
        state_dict = checkpoint
    model_dict = model.state_dict()
    new_state_dict = collections.OrderedDict()
    matched_layers, discarded_layers = [], []
    for k, v in state_dict.items():
        # If the pretrained state_dict was saved as nn.DataParallel,
        # keys would contain "module.", which should be ignored.
        if k.startswith('module.'):
            k = k[7:]
        if k in model_dict and model_dict[k].size() == v.size():
            new_state_dict[k] = v
            matched_layers.append(k)
        else:
            discarded_layers.append(k)
    # new_state_dict.requires_grad = False
    model_dict.update(new_state_dict)

    model.load_state_dict(model_dict)
    print('load_weight', len(matched_layers))
    return model


# Define a function to preprocess the image for the model
def preprocess_image(image):
    preprocess = transforms.Compose([
        transforms.Grayscale(num_output_channels=3),  # Convert to RGB
        transforms.Resize(224),
        transforms.ToTensor(),
    ])
    image = preprocess(image)
    return image.unsqueeze(0)  # Add an extra dimension for batch (1 image)


model = pyramid_trans_expr2()
checkpoint = torch.load("/home/karun/PycharmProjects/GenAI_IMD_BackEnd/raf-db-model_best.pth",
                        map_location=torch.device('cpu'))
checkpoint['state_dict'] = {k.replace('module.', ''): v for k, v in checkpoint['state_dict'].items()}
model.load_state_dict(checkpoint['state_dict'])


# Load the image using PIL
image = Image.open("/home/karun/PycharmProjects/GenAI_IMD_BackEnd/train_00006_aligned.jpg")

# Preprocess the image for the model
input_tensor = preprocess_image(image)
print(input_tensor.shape)
# Pass the preprocessed image through the model
output = model(input_tensor)
