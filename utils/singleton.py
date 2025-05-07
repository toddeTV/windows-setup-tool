# class _Singleton(type):
#     """
#     A metaclass that creates a Singleton base class when called.
#     This ensures that only one instance of the class is created and used throughout the application.
#     Source: https://stackoverflow.com/a/6798042
#     """

#     _instances = {}

#     def __call__(cls, *args, **kwargs):
#         if cls not in cls._instances:
#             cls._instances[cls] = super(_Singleton, cls).__call__(*args, **kwargs)
#         return cls._instances[cls]


# class Singleton(_Singleton("SingletonMeta", (object,), {})):
#     """
#     A metaclass that creates a Singleton base class when called.
#     This ensures that only one instance of the class is created and used throughout the application.
#     Source: https://stackoverflow.com/a/6798042
#     """

#     pass


class Singleton(type):
    """
    A metaclass that creates a Singleton base class when called.
    This ensures that only one instance of the class is created and used throughout the application.
    Source: https://stackoverflow.com/a/6798042
    """

    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]
