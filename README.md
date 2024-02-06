# AirBnB Clone

The larger AirBnB clone project has the goal of creating and deploying a simple copy of the [AirBnb website](https://www.airbnb.com/). It consists of 4 parts:

1. **Command interpreter:** to manipulate data without a visual interface, like in a Shell (perfect for development and debugging)
2. **Website:** shows the final product to everybody: static and dynamic (the front-end).
3. **Storage:** a database or files (data = objects)
4. **API:** provides a communication interface between the front-end and data (retrieve, create, delete, update them)

## The Console

The console project is a command interpreter for use in manipulating data. It enables managing the objects of the AirBnB clone project without a visual interface. Here we will be creating a storage engine that abstracts objects from their storage and persistence; offering basic CRUD functionality and a few other functions.

The specific objectives in this part of the project are:

* Creation of the data model
* CRUD functionality via a console
* JSON file persistence

![The Console objective - storage engine](assets/airbnb_clone-the_console.png)

### Starting

Clone this repo and navigate into it:

```bash
git clone https://github.com/nooby6/AirBnB_clone
cd AirBnB_clone
```

The python scripts in this project start with the shebang `#!/usr/bin/python3` and so can be executed directly on a Linux system.  
To start the console:

* Interactive mode

    ```bash
    $ ./console.py
    (hbnb)
    ```

* Non-interactive/Command mode

    ```bash
    ./console.py cmd args
    ```

For other platforms, pass in the path to the Python executable or if already added to path, use the appropriate python command(`python`, `python3`)

* Interactive mode

    ```bash
    $ python console.py
    (hbnb)
    ```

* Non-interactive/Command mode

    ```bash
    python console.py cmd args
    ```

### Usage

### Examples
