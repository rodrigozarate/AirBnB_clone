# 0x00. AirBnB clone - The console

## Description of the project
It's a Shell with a single purpose, create, modify or delete storage objects of the AirBnB clone 
## Description of the command interpreter:
Create objects and translate it to JSON strings that can be stored, readed, and updated from a file.

### Flow of serialization-deserialization
<class 'BaseModel'> -> to_dict() -> <class 'dict'> -> JSON dump -> <class 'str'> -> FILE -> <class 'str'> -> JSON load -> <class 'dict'> -> <class 'BaseModel'>
 
### How to start it
Download repo and extract or clone

Entry point
 Type `./console.py`

### How to use it
Send objects to the package either by interactive or non interactive mode

The order of parameters is important
Command - Class - ID - Name - Value

First create BaseModel
 (hbnb) `create BaseModel`

You'll get an ID number
This number identify your object inside the file

#### 1. Interactive mode
(hbnb) help

(hbnb) show BaseModel 1234-1234-1234

(hbnb) update BaseModel 1234-1234-1234 email "example@mail.com"

(hbnb) destroy BaseModel 1234-1234-1234

(hbnb) quit:
#### 2. Non interactive mode
echo "help" | ./console.py

