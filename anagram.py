class Anagrams():
    def __init__(self, words):
        self.lut = dict()

        for w in words:
            self.lut[''.join(sorted(w.lower().replace(" ", "")))] = w

    def getAnagram(self, text):
        text = ''.join(sorted(text.lower().replace(" ", "")))

        return self.lut.get(text, None)
    
