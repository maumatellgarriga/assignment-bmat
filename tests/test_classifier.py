import pytest
from api.classifier import Classifier
from api.models import SoundRecording

@pytest.fixture
def sound_recording_1():
    return SoundRecording(
        id=1,
        artists = "Beyonce",
        title = "Love On Top",
        sr_id = "348900sdla2019",
        isrcs = "GEJTR98719826",
        contributors = "")

@pytest.fixture
def sound_recording_2():
    return SoundRecording(
        id=2,
        artists = "The Bellas",
        title = "Love On Top",
        sr_id = "8sehfb83g4823",
        isrcs = "HGRID854215",
        contributors = "Pitch Perfect")
   
def test_compute_features(sound_recording_1, sound_recording_2):
    clf = Classifier(sound_recording_1, sound_recording_2, model_file_path ="")
    clf.compute_features()
    assert clf.artists_similarity == 24
    assert clf.title_similarity == 100
    assert clf.isrcs_coincidence == 0
    assert clf.contributors_similarity == 0
