# Classes are the blueprints for creating objects that will be used in the code life cycle

# Private classes - These are classes/methods that can only be accessed within the same file or scope
# Syntax: class <underscore><class-name>:
class _Private(object):
    # This is a private class and everything in it is private

    def __init__(self, private):
        self.private = private


# Public classes - These are classes/methods that are accessible to the whole program/world
# Syntax: class <class-name>:
class NotPrivate(object):
    # This is a public class

    def __init__(self, not_private):
        self.not_private = not_private

    # Methods can also either be private or public
    def _private_method(self):
        print(f'This is a private method with an underscore')

    def public_method(self):
        print(f'This is a public method with no underscore')
