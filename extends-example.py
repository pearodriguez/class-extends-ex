
def main():
    
    value = []
    person1 = Person(' ', value)
    
    print('\nPerson class example')
    person1.speak('I am here to eat')
    person1.eat('pizza')
    person1.eat('ice cream')

    print('------------------')
    print('\nBob class example')
    bob_person = Bob(' ', value)
    bob_person.eat('tacos')
    bob_person.eat('cake')
    bob_person.speak('I want to eat food')

class Person: 

    def __init__(self, language, stomach = []):
        self.__language = language
        self.__stomach = stomach

    def set_language(self, language):
        self.__language = language 

    def set_stomach(self, stomach):
        self.__stomach = stomach

    def get_language (self):
        return self.__language 
    
    def get_stomach(self):
        return self.__stomach 

    # methods

    def eat(self, food):
        self.__stomach.append(food)
        return print(self.__stomach)

    def speak(self, sentence):
        self.__language = sentence 
        return print(self.get_language()) 

class Bob (Person): 
    
    def __init__ (self, language, stomach = []):
        Person.__init__ (self, language, stomach= []) 

    def speak(self, sentence):
        new_sentence = sentence.split()
        blah_sentence = ''
        for word in new_sentence:
            word = 'blah'
            blah_sentence += word + " "
        print(str(blah_sentence))

main()
