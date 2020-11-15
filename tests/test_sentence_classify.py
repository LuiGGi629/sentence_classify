import pytest
from sentence_classify.sentence_classify import sentence_classify


class TestSentenceClassify(object):
    def test_tak_category(self):
        test_sentence = "no trudno powiedzieć ale myślę, że w zasadzie to tak"
        expected = "tak"
        actual = sentence_classify(test_sentence)
        assert actual == expected, f"Expected: 'tak', Actual: {actual}"

    def test_nie_category(self):
        test_sentence = "w żadnym wypadku"
        expected = "nie"
        actual = sentence_classify(test_sentence)
        assert actual == expected, f"Expected: 'nie', Actual: {actual}"

    def test_nie_wiem_category(self):
        test_sentence = "skąd mam wiedzieć"
        expected = "nie wiem"
        actual = sentence_classify(test_sentence)
        assert actual == expected, f"Expected: 'nie wiem', Actual: {actual}"

    def test_missing_category(self):
        test_sentece = "ciężko stwierdzić"
        expected = None
        actual = sentence_classify(test_sentece)
        assert (
            actual is expected
        ), f"sentence_classify('ciężko stwierdzić') should return None, but it actually returned {actual}"
