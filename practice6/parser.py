import nltk

groucho_grammar = nltk.CFG.fromstring("""
S -> NP VP
NP -> Det N PP | Det N
VP -> V NP PP | V NP | V
PP -> P NP
NP -> 'I'
Det -> 'the' | 'a'
N -> 'man' | 'park' | 'dog' | 'telescope'
V -> 'ate' | 'saw'
P -> 'in' | 'under' | 'with'
""")

#sent = ['the','man','saw','a','dog','in','the','park']
sent = ['the','man','with','a','man','with','a','man','with','a','man','saw','a','dog','with','a','dog','with','a','dog','in','the','park']
parser = nltk.ChartParser(groucho_grammar)

for tree in parser.parse(sent):
	print(tree)