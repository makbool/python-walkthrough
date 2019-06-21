class User:
    name = ""

    def __init__(self, name="Python"):
        self.name = name

    def salutationWithName(self):
        print("Hello!", self.name)


def main():
    obj1 = User("Makbool")
    obj1.salutationWithName()

    obj2 = User()
    obj2.salutationWithName()


if __name__ == "__main__":
    main()
