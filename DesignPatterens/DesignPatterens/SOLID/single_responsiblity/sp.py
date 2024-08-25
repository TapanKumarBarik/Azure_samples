# SINGLE RESPONSIBILITY

class Journal:
    def __init__(self):
        self.entries=[]
        self.count=0

    def add_entry(self,text):
        self.count+=1
        self.entries.append(f"{self.count} : {text}")
    def remove_entry(self,pos):
        del self.entries[pos]
    def __str__(self):
        return '\n'.join(self.entries)

    ## BREAKING SRP
    ## BAD APPROACH
    def save(self,filename):
        file=open(filename,'w')
        file.write(str(self))
        file.close()

    def load(self,filename):
        pass
    def load_from_web(self,url):
        pass
    ## BAD APPROACH---------END


## CORRECT WAY TO D0
class PerstistanceManager:
    @staticmethod
    def save_to_file(journal,filename):
        file=open(filename,'w')
        file.write(str(journal))
        file.close()

j=Journal()
j.add_entry("I cried today")
j.add_entry("I ate chicken")
print(f"Journal entries :\n{j}")
file= "august_25.txt"
PerstistanceManager.save_to_file(j,file)

## TAKE WAY

"""
- The Single Responsibility Principle (SRP) states that a class or module should have only one reason to change.
- SRP ensures that a class or module has only one responsibility or job.
- Adhering to SRP leads to modular and maintainable code.
- SRP reduces the impact of changes and minimizes the risk of introducing bugs.
- Following SRP enhances the testability and understandability of your code.
"""

