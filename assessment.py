"""
Part 1: Discussion

1. What are the three main design advantages that object orientation
   can provide? Explain each concept.
   - Abstraction: Allows you to obscure all but the relevant data about an object
        to reduce complexity and repetition, and increase efficiency.
   - Encapsulation: You don't need to know/understand details in the code to use it.
   - Polymorphism: You can use the same simple method for accessing differing
        (possibly more complex) underlying data. Often using class inheritance.

2. What is a class?
    - An object that lets you structure your software to add consistency
    to your programs so that they can be used in a cleaner way.

3. What is an instance attribute?
    - Instance attributes only apply to the specific instance of a class.

4. What is a method?
    - A method is a function which is a member of a class.

5. What is an instance in object orientation?
    - A specific realization of any class. You must instantiate a class to use its instance.

6. How is a class attribute different than an instance attribute?
    - Class attributes are same for all instances of class.
    - Instance attributes only apply to the individual instance of a class.

   Give an example of when you might use each.

class(Cat):
    sound = purr # class attribute
fluffy = Cat()
fluffy.name = "fluffy" # instance attribute


"""


# Parts 2 through 5:
# Create your classes and class methods

# Students

# Class students can have first and last names and addresses.
# Here is an example student. Write a class that can store data like this:

# {'first_name': 'Jasmine',
#  'last_name': 'Debugger',
#  'address': '0101 Computer Street'}

class Student(object):
    """Class to store student data."""

    def __init__(self, fname, lname, addr):
        self.fname = fname
        self.lname = lname
        self.addr = addr

    # student = {'first_name': fname,
    #            'last_name': lname,
    #            'address': address}

    # return student


# Questions:

# Class questions include a question and a correct answer.
# Here are two example questions. Write a class that can store data like this:

# {'question': 'What is the capital of Alberta?',
#  'correct_answer': 'Edmonton'}

# {'question': 'Who is the author of Python?',
#  'correct_answer': 'Guido Van Rossum'}

class Question(object):
    """Class to store exam questions."""

    def __init__(self, q, a):
        self.q = q
        self.a = a

    def ask_and_evaluate(self):
        answer = raw_input(self.q)
        if answer == self.a:
            return True
        else:
            return False


class Exam(object):
    """Class to hold exam info"""

    def __init__(self, exname):
        self.exaname = exname
        self.questions = []

    def add_question(self, q, ans):
        self.questions.append((q, ans))

    def administer(self):
        score = 0
        count = 0
        for ques, ans in self.questions:
            count += 1
            new_question = Question(ques, ans)
            if new_question.ask_and_evaluate() is True:
                score += 1
        total_score = (score * 100) / count
        return "Score %: " + str(total_score)


def take_test(exam, student):
    """Administers test and prints student score"""

    student.score = exam.administer()
    print student.score


def example():
    """Run a test exam."""

    test_exam = Exam("Test")
    test_exam.add_question("what is your favorite color? >>> ", "blue")
    test_student = Student("Joe", "Dirt", "1313 Mockingbird Lane")
    take_test(test_exam, test_student)
