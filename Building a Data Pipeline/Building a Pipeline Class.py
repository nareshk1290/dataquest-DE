################ Building a Pipeline Class ################

## Mission 3

def add(a, b):
    return a + b

def partial(func, *args):
    parent_args = args
    def inner(*inner_args):
        return func(*(parent_args + inner_args))
    return inner

add_two = partial(add, 2)
print(add_two(7))


## Mission 4

@catch_error
def throws_error():
    raise Exception('Throws Error')
    
def catch_error(func):
    def inner(*args):
        try:
            return func(*args)
        except Exception as e:
            return e
    return inner

print(throws_error())

## Mission 5

class Pipeline:
    def __init__(self):
        self.tasks = []
        
    def task(self):
        def inner(f):
            self.tasks.append(f)
            return f
        return inner
    
pipeline = Pipeline()

@pipeline.task()
def first_task(x):
    return x + 1

print(pipeline.tasks)

## Mission 6

class Pipeline:
    def __init__(self):
        self.tasks = []
        
    def task(self, depends_on=None):
        idx = 0
        if depends_on:
            idx = self.tasks.index(depends_on) + 1
        def inner(f):
            self.tasks.insert(idx, f)
            return f
        return inner

pipeline = Pipeline()
    
@pipeline.task()
def first_task(x):
    return x + 1

@pipeline.task(depends_on=first_task)
def second_task(x):
    return x * 2

@pipeline.task(depends_on=second_task)
def last_task(x):
    return x - 4

print(pipeline.tasks)

## Mission 7

class Pipeline:
    def __init__(self):
        self.tasks = []
        
    def task(self, depends_on=None):
        idx = 0
        if depends_on:
            idx = self.tasks.index(depends_on) + 1
        def inner(f):
            self.tasks.insert(idx, f)
            return f
        return inner
    
    def run(self, input_):
        output = input_
        for task in self.tasks:
            output = task(output)
        return output

pipeline = Pipeline()
    
@pipeline.task()
def first_task(x):
    return x + 1

@pipeline.task(depends_on=first_task)
def second_task(x):
    return x * 2

@pipeline.task(depends_on=second_task)
def last_task(x):
    return x - 4

print(pipeline.run(20))

## Mission 8

import io

class Pipeline:
    def __init__(self):
        self.tasks = []
        
    def task(self, depends_on=None):
        idx = 0
        if depends_on:
            idx = self.tasks.index(depends_on) + 1
        def inner(f):
            self.tasks.insert(idx, f)
            return f
        return inner

    
pipeline = Pipeline()
log = open('example_log.txt')
class Pipeline:
    def __init__(self):
        self.tasks = []
        
    def task(self, depends_on=None):
        idx = 0
        if depends_on:
            idx = self.tasks.index(depends_on) + 1
        def inner(f):
            self.tasks.insert(idx, f)
            return f
        return inner
    
    def run(self, input_):
        output = input_
        for task in self.tasks:
            output = task(output)
        return output
    
pipeline = Pipeline()

@pipeline.task()
def parse_logs(logs):
    return parse_log(logs)

@pipeline.task(depends_on=parse_logs)
def build_raw_csv(lines):
    return build_csv(lines, header=[
        'ip', 'time_local', 'request_type',
        'request_path', 'status', 'bytes_sent',
        'http_referrer', 'http_user_agent'
    ],
    file=io.StringIO())

@pipeline.task(depends_on=build_raw_csv)
def count_uniques(csv_file):
    return count_unique_request(csv_file)

@pipeline.task(depends_on=count_uniques)
def summarize_csv(lines):
    return build_csv(lines, header=['request_type', 'count'], file=io.StringIO())

log = open('example_log.txt')
summarized_file = pipeline.run(log)
print(summarized_file.readlines())

# Check val
"['request_type,count\r\n', 'GET,3334\r\n', 'POST,3299\r\n', 'PUT,3367\r\n']"

