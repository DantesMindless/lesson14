# task3
from functools import wraps


def arg_rules(type_: type, max_length: int, contains: list):
    def stopwords_inner(func):
        @wraps(func)
        def wrap(*args, **kwargs):
            res = func(*args, **kwargs)
            user_name = ''.join(args)

            if len(user_name) > max_length:
                return "User name cannot hold more than 15 chars"
            if not isinstance(user_name, type_):
                return "User name must be a string"
            for word in contains:
                if word not in user_name:
                    return 'Should contain needed characters'
            return res

        return wrap

    return stopwords_inner

    pass


@arg_rules(type_=str, max_length=15, contains=['05', '@'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"


slogan = create_slogan('Clown205@')
print(slogan)