# 0x00. AirBnB clone - The console

<h1>HBNB - The Console <img src="https://i.imgur.com/elr4ah9.png" width=55 align=center> </h1>

![AirBnB Logo](https://i.imgur.com/9WkM9nn.png)

**Welcome to AirBnB clone - The console, a simple command-line interface (CLI) that mimics the basic functionalities of the AirBnB website.**
*created by* [Hiba A. Mohamed](https://github.com/hiba-emording). (⌐■_■)


## 💡 Overview 💡
The AirBnB clone project aims to replicate the core features of the popular lodging rental platform AirBnB. It provides a command-line interface that allows users to interact with various components of the system, such as creating, updating, and deleting instances of different entities like users, places, cities, and more. The project is structured into modules for ease of development, testing, and maintenance.

### Description
The AirBnB Console Module is designed to provide a command-line interface (CLI) for managing AirBnB-like objects.
It utilizes the `cmd` module in Python, offering a simple yet effective way to interact with the AirBnB system through a series of commands.

### Features
- Allows users to create, read, update, and delete instances of various classes (e.g., User, State, City, Amenity, Place, Review).
- Provides commands for querying and manipulating data within the AirBnB system.
- Supports basic functionalities such as showing all instances, displaying specific instances, updating instance attributes, and more.
- Offers tab-completion and history functionalities for improved user experience.

### Repository Structure:
AirBnB_clone/<br>
├── console.py<br>
├── models/<br>
│$$$├── __init__.py<br>
│$$$├── base_model.py<br>
│$$$├── user.py<br>
│$$$├── state.py<br>
│$$$├── city.py<br>
│$$$├── amenity.py<br>
│$$$├── place.py<br>
│$$$├── review.py<br>
│$$$└── engine/<br>
│$$$$$$$├── __init__.py<br>
│$$$$$$$└── file_storage.py<br>
└── tests/<br>
$$$$├── test_console.py<br>
$$$$└── test_models/<br>
$$$$$$$$├── __init__.py<br>
$$$$$$$$├── test_base_model.py<br>
$$$$$$$$├── test_user.py<br>
$$$$$$$$├── test_state.py<br>
$$$$$$$$├── test_city.py<br>
$$$$$$$$├── test_amenity.py<br>
$$$$$$$$├── test_place.py<br>
$$$$$$$$├── test_review.py<br>
$$$$$$$$└── test_engine/<br>
$$$$$$$$$$$$├── __init__.py<br>
$$$$$$$$$$$$└── test_file_storage.py<br>

### Components
1. **Console (`console.py`):**
   The console module serves as the main entry point for interacting with the AirBnB clone. It provides a command-line interface (CLI) for executing various commands to manage and manipulate data within the system.

2. **Models (`models`):**
   The models directory contains the core components of the AirBnB clone, including classes that represent different entities within the system. Each model file corresponds to a specific entity and defines its attributes and behaviors. This includes classes such as `BaseModel`, `User`, `State`, `City`, `Amenity`, `Place`, and `Review`.

3. **Engine (`engine`):**
   The engine directory houses the backend storage mechanism for the AirBnB clone. It includes the implementation of the storage engine responsible for storing and retrieving data from various data sources. The File Storage Engine is utilized for serializing and deserializing instances to and from JSON files, ensuring persistence and efficient data management.

4. **Tests (`tests`):**
   The tests directory contains unit tests to ensure the correctness and functionality of the AirBnB clone components. It includes test cases for both the models and the engine modules, verifying the behavior of classes and storage mechanisms.


## 👨‍💻 Basic Usage 👨‍💻

### How to Start the Command Interpreter
To start the AirBnB console, follow these steps:
**1-Clone the repository:**
```bash
git clone https://github.com/hiba-emording/AirBnB_clone.git
```
**2-Navigate to the project directory:**
```bash
cd AirBnB_clone
```
**3-Start the console:**
```bash
./console.py
```

### How to Use the Command Interpreter
Once the console is running, you can interact with it by typing commands and pressing Enter. Here are some basic commands you can use:
- `create <class name>`: Create a new instance of the specified class.
- `show <class name> <id>`: Display details of a specific instance.
- `destroy <class name> <id>`: Delete an instance based on its class name and ID.
- `all [<class name>]`: Show all instances or instances of a specific class.
- `update <class name> <id> <attribute name> "<attribute value>"`: Update attributes of a specific instance.

🌟 Pro Tip: Type `help` for a list of available commands and their usage. You can also use the `help <command>` command to get specific information about a particular command.

### Exiting the Console
To exit the AirBnB Console, you can use one of the following methods:
- Typing `quit` and pressing Enter.
- Pressing `Ctrl+D` (EOF) on your keyboard.

### Examples
```bash
(hbnb) create User
(d8a5a36f-9876-4f25-b6fc-b3e872f8d59e)
(hbnb) show User d8a5a36f-9876-4f25-b6fc-b3e872f8d59e
[User] (d8a5a36f-9876-4f25-b6fc-b3e872f8d59e) {'id': 'd8a5a36f-9876-4f25-b6fc-b3e872f8d59e'}
(hbnb) update User d8a5a36f-9876-4f25-b6fc-b3e872f8d59e email "user@example.com"
(hbnb) all
[[User] (d8a5a36f-9876-4f25-b6fc-b3e872f8d59e) {'id': 'd8a5a36f-9876-4f25-b6fc-b3e872f8d59e', 'email': 'user@example.com'}]
```


🚀 **Happy AirBnBing!** 🚀
