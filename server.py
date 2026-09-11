from flask import Flask, render_template, request 
from EmotionDetection.emotion_detection import test_emotion_detector

app = Flask("Sentiment Analyzer")