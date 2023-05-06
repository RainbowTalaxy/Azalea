import spacy
from spacy import displacy

nlp = spacy.load("en_core_web_lg")

text = 'The Conservatives\' planning reform explicitly gives rural development priority over conservation, even authorizing "off-plan" building where local people might object.'

doc = nlp(text)

for chunk in doc.noun_chunks:
    print(
        "[" + chunk.text + "]", chunk.root.text, chunk.root.dep_, chunk.root.head.text
    )

for token in doc:
    print(
        "[" + str(token.idx) + "]",
        token.text,
        token.pos_,
        token.dep_,
        token.head.text,
        token.head.idx,
    )

displacy.serve(doc, style="dep", port=8080, host="localhost")
