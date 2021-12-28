# python-fluent-results

![App workflow](https://github.com/kaypee90/python-fluent-results/actions/workflows/python-publish.yml/badge.svg)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)


Propagate errors and data nicely with a uniform interface in your python project


* Install using the command: `pip install pyfluent-results`
### - How to use fluent results

==============================

* Returning a success and failure response
```
from fluent_results.results import Result

def add_two_integers(x, y):
    if not isinstance(x, int) or isinstance(y, int):
        return Result.fail("Both arguments must be integers")
    
    total = x + y
    return Result.ok(total)
```

* Adding additional information to results as reasons
```
from fluent_results.results import Result

def add_two_integers(x, y):
    if not isinstance(x, int) or isinstance(y, int):
        r = Result.fail("Both arguments must be integers")
        r.with_reason("Addition failed because an argument provided was not an integer.")
        return r
    
    total = x + y
    r = Result.ok(total, "Numbers added successfully!")
    r.with_reason("Both arguments were integers")
    return r
```

* Handling multiple error and success messages
```
from fluent_results.results import Result

def validate_person(person):
    error_messages = []
    if person.age < 18:
        error_messages.append("Person must be 18years or above")

    if not person.name:
        error_messages.append("Person must have a name")

    if error_messages:
        r = Result.fail("Person failed validation")
        r.with_errors(error_messages)
        return r
    
    success_messages = [
        "Person has a name", 
        "Person is above 17 years"
    ]
    r = Result.ok(person, "Validation passed!")
    r.with_successes(success_messages)
    return r
```

* Convert Result to a dictionary
```
from fluent_results.results import Result

r = Result.ok({"data":"Sample data"})
print(r.convert_to_dict())
```

* Access response return in Result object
```
from fluent_results.results import Result

r = Result.ok({"data":"Sample data"}, "Successful operation")

r.is_success  # check if process succeeded.
r.is_failed   # check if process failed.
r.value       # get data added when result is successful.
r.errors      # get the list of error messages.
r.sucesses    # get the list of success messages.
r.reasons     # get the list of added reasons.
```

