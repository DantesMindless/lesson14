# task2
from functools import wraps

def stop_words(words: list):
    def stopwords_inner(func):
        @wraps(func)
        def wrap(*args, **kwargs):
            res = func(*args, **kwargs)
            lol = ''
            for word in str(res).split():
                if word in words:
                    lol += '* '
                else:
                    lol += word + ' '
            return lol
        return wrap
    return stopwords_inner
@stop_words(['pepsi', 'BMW'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW !"

slogan = create_slogan("Clown")
print(slogan)
