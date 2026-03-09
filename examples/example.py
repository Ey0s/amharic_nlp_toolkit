from amnlp.pipeline.processor import AmharicProcessor

text = """
ኢትዮጵያ በአፍሪካ ውስጥ ታላቅ ሀገር ናት።
አዲስ አበባ የኢትዮጵያ ዋና ከተማ ናት።
ተማሪዎች በትምህርት ቤት ትምህርት ይማራሉ።
እኔ ኮምፒውተር ሳይንስ እማራለሁ።
ቴክኖሎጂ በዓለም ላይ በፍጥነት እየተሻሻለ ነው።
"""

processor = AmharicProcessor()

result = processor.process(text)

print(result)