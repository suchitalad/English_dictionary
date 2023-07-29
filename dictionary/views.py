from django.shortcuts import render
from PyDictionary import PyDictionary

# Create your views here.
def index(request):
    return render(request, 'index.html')

def word(request):
    search = request.GET.get('search')
    dictionary = PyDictionary()

    # Get the meanings of the word for all parts of speech
    meanings = dictionary.meaning(search)
    meaning_noun = meanings.get('Noun', ['Not found'])[0] if meanings else 'Not found'

    # Get synonyms and antonyms
    # synonyms = dictionary.synonym(search)
    # antonyms = dictionary.antonym(search)

    # # Handle cases where synonyms and antonyms are not found
    # synonyms = synonyms if synonyms else ['Not found']
    # antonyms = antonyms if antonyms else ['Not found']

    context = {
        'word': search,
        'meaning': meaning_noun,
        # 'synonyms': synonyms,
        # 'antonyms': antonyms,
    }
    return render(request, 'word.html', context)
