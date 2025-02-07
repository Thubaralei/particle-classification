from miso.training.parameters import MisoParameters
from miso.training.trainer import train_image_classification_model

tp = MisoParameters()
tp.source = "https://1drv.ws/u/s!AiQM7sVIv7fah4MNU5lCmgcx4Ud_dQ?e=nPpUmT"
# tp.source = r"/media/ross/DATA/Datasets/Weeds/DeepWeedsConverted"
tp.output_dir = "/media/ross/DATA/Datasets/Weeds/DeepWeedsTraining"
tp.cnn_type = "resnet50_cyclic_tl"
tp.img_shape = [224, 224, 3]
tp.img_type = 'rgb'
train_image_classification_model(tp)


tp = MisoParameters()
tp.source = "https://1drv.ws/u/s!AiQM7sVIv7fah4MNU5lCmgcx4Ud_dQ?e=nPpUmT"
tp.output_dir = "."
tp.cnn_type = "resnet50_cyclic_tl"
tp.img_shape = [224, 224, 3]
tp.img_type = 'rgb'
train_image_classification_model(tp)