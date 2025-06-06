# 🤟 Sign Language Detection App

A real-time sign language detection system using the **TensorFlow 2 Object Detection API** and **OpenCV**. This project recognizes 16 different hand signs through your webcam and can be extended further.

---

## 🧠 Model

The app uses **SSD MobileNet V2 FPNLite 320x320**, pretrained on COCO, and fine-tuned to detect the following 16 custom hand signs:

- Fine  
- Hello  
- Help  
- Home  
- I  
- I Hate You  
- I Love You  
- Mother  
- No  
- Pray  
- Call  
- Thank You  
- Time  
- Water  
- Where  
- Yes  

---

## 🛠 Project Structure

```
Tensorflow/
├── workspace/
│   ├── annotations/
│   ├── images/
│   │   ├── train/
│   │   └── test/
│   ├── models/
│   │   └── my_ssd_mobnet/
│   └── pre-trained-models/
├── scripts/
│   └── generate_tfrecord.py
└── models/  <-- cloned from TensorFlow GitHub repo
```

---

## 🧪 Setup Instructions

1. Clone the TensorFlow models repo (from within `Tensorflow/`):
   ```
   git clone https://github.com/tensorflow/models.git
   ```

2. Generate `label_map.pbtxt` for 16 classes.

3. Generate TFRecord files:
   ```bash
   python Tensorflow/scripts/generate_tfrecord.py -x Tensorflow/workspace/images/train -l Tensorflow/workspace/annotations/label_map.pbtxt -o Tensorflow/workspace/annotations/train.record
   python Tensorflow/scripts/generate_tfrecord.py -x Tensorflow/workspace/images/test -l Tensorflow/workspace/annotations/label_map.pbtxt -o Tensorflow/workspace/annotations/test.record
   ```

4. Copy the `pipeline.config` from the pre-trained model into `my_ssd_mobnet/`.

5. Edit `pipeline.config` to:
   - Set `num_classes = 16`
   - Set `fine_tune_checkpoint` to the pretrained model's checkpoint
   - Update paths for `train.record`, `test.record`, and `label_map.pbtxt`

6. Train the model:
   ```bash
   python Tensorflow/models/research/object_detection/model_main_tf2.py \
   --model_dir=Tensorflow/workspace/models/my_ssd_mobnet \
   --pipeline_config_path=Tensorflow/workspace/models/my_ssd_mobnet/pipeline.config \
   --num_train_steps=8000
   ```

---

## 🎥 Real-Time Detection

After training, load the model and run real-time detection using your webcam:

- Initializes webcam feed  
- Detects a hand sign in each frame  
- Overlays bounding box and label in real time  
- Uses a confidence threshold of 0.5

> The app uses OpenCV to access the webcam and TensorFlow to process the frame through the trained model.

---

## ⚙️ Dependencies

- Python 3.x  
- TensorFlow 2.x  
- OpenCV  
- protobuf  
- Pillow  
- Jupyter Notebook (optional for development)

Install them via pip:
```bash
pip install tensorflow opencv-python protobuf pillow
```

---

## 👨‍💻 Author

**Tarun Parthiban**  
B.Tech CSE (AI & Robotics)  
Vellore Institute of Technology, Chennai
