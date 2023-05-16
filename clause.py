import spacy
from nltk import Tree

nlp = spacy.load("en_core_web_lg")


def to_nltk_tree(node):
    if node.n_lefts + node.n_rights > 0:
        return Tree(node.orth_, [to_nltk_tree(child) for child in node.children])
    else:
        return node.orth_


text = 'The Conservatives\' planning reform explicitly gives rural development priority over conservation, even authorizing "off-plan" building where local people might object.'

seen = set()  # keep track of covered words

doc = nlp(text)

[to_nltk_tree(sent.root).pretty_print() for sent in doc.sents]
