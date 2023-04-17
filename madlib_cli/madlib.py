import re

def read_template(path):
           """ reading file  and check if the file don't exist"""
           try : 
            with open(path, 'r') as reader:
              return reader.read() 
           except FileNotFoundError:
             print("Sorry, your file not found")
             raise

def parse_template(s):
    """Parse a template string and return a tuple of stripped template string and parts."""
    parts = []
    user = []
    # Replace each template part with a {} placeholder in the stripped string
    stripped = re.sub(r"{[^}]+}", "{}", s)
    # Extract the template parts and return them as a tuple
    parts = tuple(re.findall(r"{([^}]+)}", s))
    return stripped, parts
    
    # stripped1 = s.replace(a1,"{}").replace(a2,"{}").replace(n,"{}") 
    # user = (re.findall(a1,s),re.findall(a2,s),re.findall(n,s))
    # return stripped1, user

def merge(stripped,parts):
     """merge between the stripped string which is contain empty brackets and the parts which is the elements that was inside the brackets """

     return stripped.format(*parts)

if __name__ == "__main__":
 print("Welcome ^_^")
 print("We will ask you to provide us with some adjectives, Nouns, and others, then we will fill them in with Funny text, and you will be surprised!")
 value = parse_template(read_template("assets/make_me_a_video_game_template.txt")) 
 # print(value[0])
 # print(value[1])
 p = []
 for i in range(len(value[1])):
     t = input(f"{value[1][i]}")
     p.append(t)

 g = tuple(p)
 with open("assets/copy.txt",'w') as writer: 
             writer.write(merge(value[0],g))
 with open("assets/copy.txt", 'r') as reader:
              print(reader.read())
 