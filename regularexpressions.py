import re

pattern = r"[A-Z]+thical"

text = '''Ethics is the philosophical study of moral phenomena, or what people ought to do. 
It includes three main branches: normative ethics, which seeks general principles for how people should act; 
applied ethics, which addresses specific real-life ethical issues like abortion; and metaethics, 
which explores underlying concepts and assumptions.
Influential Ethical normative theories are consequentialism, deontology, and virtue ethics.'''

matchces = re.finditer(pattern, text)
for match in matchces:
    print(match)


#https://regexr.com/ - will learn more about regular expression
