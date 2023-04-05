class User:
    def __init__(self, name):
        self.name = name
        self.is_logged_in = False


def is_aunthenticated(function):
    def wrapper(*args, **kwargs):
        if args[0].is_logged_in:
            function(args[0])
    return wrapper


@is_aunthenticated
def create_blogpost(user):
    print(f"This is {user.name}'s new blog post.")


new_user = User("Arpit")
new_user.is_logged_in = True
create_blogpost(new_user)
