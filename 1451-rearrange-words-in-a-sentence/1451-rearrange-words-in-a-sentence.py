class Solution:
    def arrangeWords(self, text: str) -> str:
        text = text.lower().split()
        text.sort(key = lambda x : len(x))
        return " ".join(text).capitalize()