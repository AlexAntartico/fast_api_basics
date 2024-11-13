from typing import List

# If types become too lengthy, it will be difficult to read
# You can build your own custom type
Image = List[List[int]]

def flatten_image(pic: Image)->List:
    flat_list = []
    for sublist in image:
        for item in sublist:
            flat_list.append(item)
    return flat_list


image = [[1,2,3],[4,5,6]]


from typing import List, Optional


class Job:
    def __init__(self, title:str,description:Optional[str])-> None:
        self.title = title
        self.description = description


    def __repr__(self):
        return self.title


job1 = Job(title="SDE2",description="Sdfdk")
job2 = Job(title="Senior Manager", description="jfjdj")      

print(job1)
print(job2)

jobs: List[Job] = [job1,job2]     #notice the List[Job] , Job is our custom class
print(jobs)


def smart_divide(func):
    def inner(a, b):
        if b == 0:
            print("Whoops! Division by 0")
            return None

        return func(a, b)
    return inner


@smart_divide
def divide(a, b):
    print(a/b)

divide(9, 0)

# to annotate this function:

from typing import Callable

def smart_divide(func:Callable[[int,int],float]):
    def inner(a, b):
        if b == 0:
            print('Whoops! Division by 0')
            return None

        return func(a, b)
    return inner