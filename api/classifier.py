from fuzzywuzzy import fuzz
import pickle
from models import SoundRecording 
from sklearn.ensemble import RandomForestClassifier

class Classifier(object):
    def __init__(self, sound_recording_a: SoundRecording, sound_recording_b: SoundRecording , model_file_path: str) -> None:
        self.sound_recording_a = sound_recording_a
        self.sound_recording_b = sound_recording_b
        self.model_file_path = model_file_path
        self.compute_features()

    def compute_features(self):
        self.title_similarity = fuzz.ratio(self.sound_recording_a.title, self.sound_recording_b.title)
        self.artists_similarity = fuzz.ratio(self.sound_recording_a.artists, self.sound_recording_b.artists)
        self.contributors_similarity = fuzz.ratio(self.sound_recording_a.contributors, self.sound_recording_b.contributors)
        self.isrcs_coincidence = True if self.sound_recording_a.isrcs == self.sound_recording_b.isrcs else False

    def load_classifier_model(self) -> RandomForestClassifier:
        return pickle.load(open(self.model_file_path, "rb"))

    def get_features_array(self) -> list:
        return [[self.title_similarity, self.artists_similarity, self.isrcs_coincidence, self.contributors_similarity]]

    def get_prediction(self) -> int:
        return self.load_classifier_model().predict(self.get_features_array()).tolist()[0]