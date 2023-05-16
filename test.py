import spacy
from spacy import displacy

nlp = spacy.load("en_core_web_lg")

text = 'The Conservatives\' planning reform explicitly gives rural development priority over conservation, even authorizing "off-plan" building where local people might object.'

doc = nlp(text)

for token in doc:
    print(
        "[" + str(token.idx) + "]",
        token.text,
        token.pos_,
        token.dep_,
        token.head.text,
        token.head.idx,
    )

print(doc.to_json())

# 新建一个文件 output.json
with open("output.json", "w") as f:
    f.write(str(doc.to_json()))

displacy.serve(doc, style="dep", port=8080, host="localhost")
