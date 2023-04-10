import re
print("Welcome ^_^")
print("We will ask you to provide us with some adjectives, Nouns, and others, then we will fill them in with Funny text, and you will be surprised!")
a1 = input("please enter Adjective")
a2 = input("please enter Adjective")
n = input("please enter Noun")

def read_template(path):
           """ insert into existing file the elements that user entered in certain template and check if the file don't exist"""
           try : 
            with open(path,'a') as writer: 
             writer.write(a1 + " and" + a2 +  " " +n +".")
           except FileNotFoundError as error :
               print("Sorry, your file not found")
           else:
            with open(path, 'r') as reader:
              return reader.read() 



def parse_template(s):
    """Parse a template string and return a tuple of stripped template string and parts."""
    parts = []
    user = []
    # Replace each template part with a {} placeholder in the stripped string
    # stripped = re.sub(r"{[^}]+}", "{}", s)
    # # Extract the template parts and return them as a tuple
    # parts = tuple(re.findall(r"{([^}]+)}", s))
    # return stripped, parts
    
    stripped1 = s.replace(a1,"{}").replace(a2,"{}").replace(n,"{}") 
    user = (re.findall(a1,s),re.findall(a2,s),re.findall(n,s))
    return stripped1, user

def merge(stripped,parts):
     """merge between the stripped string which is contain empty brackets and the parts which is the elements that was inside the brackets """
     return stripped.format(*parts)

print(read_template("assets/test.txt"))
print(parse_template("It was a  hot and cold  weather."))
print(merge('It was a  {} and {}  {}.',('hot', 'cold', 'weather')))