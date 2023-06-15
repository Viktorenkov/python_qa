"""
# The English language has five vowels: A, E, I, O, and U
# Please count each vowel occurence in text bellow ( sum of lower and capital cases)
# and write output as table smth like this
# -----------------
# | vowel | count |
# -----------------
# |   a   |  11   |
# |   e   |  23   |
#   ...
# -----------------

# then modify text where each vowel replaced with
# A->À;  a->à ; E-> É ; e->é; I->Í , i->í ; O->Ó ; o->ó; U->Ú; u->ú
# ex. "Í wàndéréd lónély...."   and print it
"""

poem_text = """I wandered lonely as a cloud
That floats on high o'er vales and hills,
When all at once I saw a crowd,
A host, of golden daffodils;
Beside the lake, beneath the trees,
Fluttering and dancing in the breeze. 

Continuous as the stars that shine
And twinkle on the Milky Way,
They stretched in never-ending line
Along the margin of a bay:
Ten thousand saw I at a glance,
Tossing their heads in sprightly dance."""

from collections import Counter

vowels = ['A', 'E', 'I', 'O', 'U']

# Count vowel occurrences
counts = Counter(char.upper() for char in poem_text if char.upper() in vowels)

# Print the table
print("-----------------")
print("| vowel | count |")
print("-----------------")
for vowel in vowels:
    count = counts.get(vowel, 0)
    print(f"|   {vowel.lower()}   |  {count}{' ' * (3 - len(str(count)))}  |")
print("-----------------")


translation_table = str.maketrans('AEIOUaeiou', 'ÀÉÍÓÚàéíóú')

modified_text = poem_text.translate(translation_table)

print(modified_text)