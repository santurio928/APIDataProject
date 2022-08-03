# Instructions

This are the instructions I followed for creating the API. The API was made in a MacBook, so the commands for the terminal are different form Windows.

## IDE

The API was made in Visual Studio Code, so you need to have it installed. VSCode was used for comfort, because of being more visual when having folders opened and making changes with them.

## Steps

### 1. Create Folder

Create a folder where the API is going to be (in local). The folder can have any name, but is better not to have blank spaces.

### 2. Libraries needed

Open the folder in VSCode, and then open  the terminal also in VSCode for writing the following commands:

```
pip list
```
This shows all the libraries installed at that moment there. Search for flask and virtualenv. If they are not there or an update is needed you can write the following commands:
```
pip install flask
pip install virtualenv
```

### 3. Creating env

For creating the environment, in the same terminal:
```
python -m virtualenv env
```
This will create a folder called _env_ that is going to be the environment data.


### 4. Creating the funtional API

In the same folder where _env_ is, you need to create another folder called _src_ where the code for the API is going to be. You can create it either by right click and create or in the terminal typing:

```
mkdir src
```

### 5. Coding the API

You have to create a _.py_ file inside _src_ folder. It can have any name, in this repository there is an example of an API code named _dataTeamAPI.py_ made for practicing how to make an API and explained in the code how it works. Once the code is finished or if any trials are needed the API can be executed writing this command in the terminal (first save the file):
```

```

This will run the API locally. In the terminal you can see the endpoint URL, you can click on it and the requests will be made in a browser or you can copy and paste that URL for making requests from python or insomnia.

If you want to terminate the execution of the API you can click: _control + C_
