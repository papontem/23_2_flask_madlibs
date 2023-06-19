from stories import *

# Here's a story to get you started
# story = Story(
#     ["place", "noun", "verb", "adjective", "plural_noun"],
#     """Once upon a time in a long-ago {place}, there lived a
#        large {adjective} {noun}. It loved to {verb} {plural_noun}."""
# )
# ans = {
#     "place"         :"answer",
#     "noun"          :"answer",
#     "verb"          :"answer",
#     "adjective"     :"answer",
#     "plural_noun"   :"answer",
#        }

my_ans = {
    "place"         : "beach",
    "adjective"     : "pink",
    "noun"          : "Pearl",
    "verb"          : "ride",
    "plural_noun"   : "waves",
}

myStory = story.generate(my_ans)

print(myStory)

#PAM gonna grab this later
# <!--{% for prompt in prompts %}<label for="{{prompt}}">{{prompt}}</label><input type="text" placeholder="{{prompt}}" name="{{prompt}}" /><br><br>{% endfor %}-->