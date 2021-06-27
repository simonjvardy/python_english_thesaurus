![My Logo](https://github.com/simonjvardy/simonjvardy/blob/main/assets/img/GitHub-name.png)

# Command Line Engish Dictionary / Thesaurus App

## About ##

The aim of this little Python app is to create a working English language dictionary using a json data file containing the words and meanings.

The app also includes some basic fuzzy matching of words to return the most likely alternative word and meaning if the user mis-spells the word or enters a typo.

---

## Technologies ##

### **Languages** ###

- [Python3](https://www.python.org/)
  - Used to create the main application functionality

#### **Dependencies** ####

- [mysql-connector-python](https://github.com/mysql/mysql-connector-python)
---

## Deployment ##

The website was developed Visual Studio Code and using Git pushed to GitHub, which hosts the repository. I made the following steps to deploy and run the app:

### **Cloning Python English Thesaurus from GitHub** ###

#### **Prerequisites** ###

Ensure the following are installed locally on your computer:

- [Python 3.6 or higher](https://www.python.org/downloads/)
- [PIP3](https://pypi.org/project/pip/) Python package installer
- [Git](https://git-scm.com/) Version Control


#### **Cloning the GitHub repository** ####

- navigate to [simonjvardy/python_english_thesaurus](https://github.com/simonjvardy/python_english_thesaurus) GitHub repository.
- Click the **Code** button
- **Copy** the clone url in the dropdown menu
- Using your favourite IDE open up your preferred terminal.
- **Navigate** to your desired file location.

Copy the following code and input it into your terminal to clone python_english_thesaurus:

```Python
git clone https://github.com/simonjvardy/python_english_thesaurus.git
```

#### **Creation of a Python Virtual Environment** ####

*Note: The process may be different depending upon your own OS - please follow this [Python help guide](https://python.readthedocs.io/en/latest/library/venv.html) to understand how to create a virtual environment.*

#### **Install the App dependencies and external libraries** ####

- In your IDE terminal window, install the dependencies from the requirements.txt file with the following command:

```Python
pip3 install -r requirements.txt
```

#### **Running the app in the CLI** ####

- In your IDE terminal window, enter:

```python
python3 app1.py
```

---

## Acknowledgements ##

- [Udemy: The Python Mega Course - Build 10 Real World Applications](https://www.udemy.com/course/the-python-mega-course/) Credit: Ardit Sulce