import spacy


nlp = spacy.load("en_core_web_lg")

text = "‘Wow, scary thought, the boy You-Know-Who,’ said Ron quietly, as they took their places around one of the gnarled Snargaluff stumps that formed that term’s project, and began pulling on their protective gloves."

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
