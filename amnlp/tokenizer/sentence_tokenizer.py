import re

class SentenceTokenizer:

    def split(self, text):

        sentences = re.split(r'[።!?]', text)

        return [s.strip() for s in sentences if s.strip()]