# Motion Detector with Graph

A Python project that uses OpenCV to detect motion through your webcam and logs the start and end times of motion events. It then visualizes these events using Bokeh as an interactive timeline graph.

## 📸 Features
- Real-time motion detection via webcam
- Saves motion timestamps to `Times.csv`
- Interactive graph of motion intervals

## 🧪 How to Use

1. Run `MovementDetection.py` -Make sure to step away for a second when recording starts -Make some movements -press `q` to stop recording.
  
2. Run `plotting.py` — it opens a motion graph in your browser.

## 💾 Requirements

Install required packages:
```bash
pip install -r requirements.txt
