from fuzzywuzzy import fuzz
import pickle

class Classifier(object):
    def __init__(self, sound_recording_a, sound_recording_b, model_file_path: str) -> None:
        self.model_file_path = model_file_path
        self.title_similarity = fuzz.ratio(sound_recording_a.title, sound_recording_b.title)
        self.artists_similarity = fuzz.ratio(sound_recording_a.artists, sound_recording_b.artists)
        self.contributors_similarity = fuzz.ratio(sound_recording_a.contributors, sound_recording_b.contributors)
        self.isrcs_coincidence = True if sound_recording_a.isrcs == sound_recording_b.isrcs else False
        

    def load_classifier_model(self):
        return pickle.load(open(self.model_file_path, "rb"))

    def get_features_array(self):
        return [[self.title_similarity, self.artists_similarity, self.isrcs_coincidence, self.contributors_similarity]]

    def get_prediction(self):
        return self.load_classifier_model().predict(self.get_features_array()).tolist()[0]