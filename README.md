# AirBnB Clone - The Console

  
![AirBnB clone](https://miro.medium.com/v2/resize:fit:828/format:webp/1*87ce_sVbWHSHpDhCMBwKtA.png)



## Getting Started


**What’s a command interpreter?**

Do you remember the Shell? It’s exactly the same but limited to a specific use-case. In our case, we want to

be able to manage the objects of our project:



- Create a new object (ex: a new User or a new Place)

- Retrieve an object from a file, a database etc…

- Do operations on objects (count, compute stats, etc…)

- Update attributes of an object

- Destroy an object

### Learning Objectives



## General

 - How to create a Python package

  - How to create a command interpreter in Python using the cmd module

   - What is Unit testing and how to implement it in a large project

   - How to serialize and deserialize a Class

   - How to write and read a JSON file

   - How to manage datetime

   - What is an UUID

   - What is *args and how to use it

   - What is **kwargs and how to use it

   - How to handle named arguments in a function



 ## Execution

  
Your shell should work like this in interactive mode:

  
```
$ ./console.py
(Airbnb) help

Documented commands (type help <topic>):
========================================
EOF help quit

(Airbnb)
(Airbnb)
(Airbnb) quit
$
```

But also in non-interactive mode: (like the Shell project in C)

```
$ echo "help" | ./console.py

(Airbnb)

Documented commands (type help <topic>):
========================================

EOF help quit
(Airbnb)
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(Airbnb)


Documented commands (type help <topic>):
========================================
EOF help quit
(Airbnb)
$

```

## Usage Examples

**Launching the console**
```
$ ./console.py
(Airbnb) 
```
**Creating a new object**
```
(Airbnb) create
** class name missing **
(Airbnb) create User
670265eb-5982-489e-8b92-2dff054f0776
```
**Show an object**
```
(Airbnb) show User
** instance id missing **
(Airbnb) show User 670265eb-5982-489e-8b92-2dff054f0776
[User] (670265eb-5982-489e-8b92-2dff054f0776) {'created_at': datetime.datetime(2020, 2, 19, 18, 8, 58, 458246), 'id': '670265eb-5982-489e-8b92-2dff054f0776', 'updated_at': datetime.datetime(2020, 2, 19, 18, 8, 58, 458261)}
```
**Update an object**
```
(Airbnb) show User
** instance id missing **
(Airbnb) show User 670265eb-5982-489e-8b92-2dff054f0776
[User] (670265eb-5982-489e-8b92-2dff054f0776) {'created_at': datetime.datetime(2020, 2, 19, 18, 8, 58, 458246), 'id': '670265eb-5982-489e-8b92-2dff054f0776', 'updated_at': datetime.datetime(2020, 2, 19, 18, 8, 58, 458261)}
```
**Update an object**
```
(Airbnb) all
["[User] (70f71c16-962b-48ad-9df8-9203fe23d612) {'created_at': datetime.datetime(2020, 2, 19, 18, 11, 32, 341144), 'id': '70f71c16-962b-48ad-9df8-9203fe23d612', 'updated_at': datetime.datetime(2020, 2, 19, 18, 11, 32, 341161)}"]
(Airbnb) update
** class name missing **
(Airbnb) update User
** instance id missing **
(Airbnb) update User 70f71c16-962b-48ad-9df8-9203fe23d612
** attribute name missing **
(Airbnb) update User 70f71c16-962b-48ad-9df8-9203fe23d612  Age "20"
(Airbnb) all
["[User] (70f71c16-962b-48ad-9df8-9203fe23d612) {'Age': 20, 'created_at': datetime.datetime(2020, 2, 19, 18, 11, 32, 341144), 'id': '70f71c16-962b-48ad-9df8-9203fe23d612', 'updated_at': datetime.datetime(2020, 2, 19, 18, 13, 9, 937933)}"]
(Airbnb)
```
**Destroy an object**
```
(Airbnb) destroy
** class name missing **
(Airbnb) destroy User
** instance id missing **
(Airbnb) destroy User 670265eb-5982-489e-8b92-2dff054f0776
(Airbnb)
```
