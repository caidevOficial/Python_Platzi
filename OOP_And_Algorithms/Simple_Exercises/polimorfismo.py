
class Person:
    def __init__(self, name):
        self.name = name

    def run(self):
        print('Running!')

class Runner(Person):
    def __init__(self, name):
        super().__init__(name)
    
    def run(self):
        print('I am running now!')

def main():
    thisPerson = Person('Julius')
    thisPerson.run()

    thisRunner = Runner('Chronos')
    thisRunner.run()

if __name__ == '__main__':
    main()
