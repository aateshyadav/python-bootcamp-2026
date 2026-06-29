import re
text="the quick brown fox jumps over the lazy dog. brown"

# search for a pattern
""" match=re.search("brown",text)
print(match)
if match:
    print("match found!")
    print("start index:",match.start())
    print("end index:",match.end())
 """
# find all occurrences of a pattern
""" matches=re.findall("the", text, re.IGNORECASE) # Case-insensitive search
print("matches:",matches) """

new_text=re.sub("fox","cat",text)
print("new text :",new_text)..