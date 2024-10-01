# PDF Analyser

## Table of Contents

- [Introduction](#introduction)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Running Docker](#running-docker)
  - [Running Locally](#start-rabbitmq-service)
  - [Testing](#testing)
  
- [Contributing](#contributing)
- [License](#license)


## Introduction
 The PDF Analyser is an application built with <a href="https://www.django-rest-framework.org/">Django Rest Framework</a>. The system is composed of an API service hat analyzes a PDF file, extracts the nouns and verbs contained in the file, and displays them to the frontend.


### Features
 - PDF Upload: Users can upload PDF files through a user-friendly interface.
 - Text Extraction: The application reads the content of the uploaded PDF file and extracts nouns and verbs using Natural Language Processing (NLP) techniques with NLTK.
 - Data Storage: Extracted nouns and verbs, along with the email of the user, are stored in a MongoDB database using MongoEngine.
 - Display Results: Users can view the extracted nouns and verbs on a dedicated results page after upload.


### Technologies Used
 - Django: The web framework used to build the application.
 - MongoDB: A NoSQL database for storing extracted data.
 - MongoEngine: An Object-Document Mapper (ODM) for working with MongoDB in Django.
 - NLTK: A Natural Language Processing library for Python to perform text analysis.
 - PyPDF2: A library for reading PDF files.
 - Testing: Django's built-in test framework (APITestCase, APIClient)
 - Containerization - Docker


## Getting Started

To run this web application on your local machine, follow the steps below:

### Prerequisites

Before getting started, ensure that you have the following software installed on your machine:

- Python: Download and install Python from the official website: https://www.python.org/downloads/
- GIT: Download and install GIT from the official website: https://git-scm.com/downloads
- Docker: 
  - For Windows or macOS, download and install Docker Desktop from the official website: https://www.docker.com/products/docker-desktop/
  - On Linux, you can install Docker Engine directly using your package manager without needing Docker Desktop. [Follow the official Docker Engine installation instructions.](https://docs.docker.com/engine/install/)


### Installation

Step-by-step guide on how to install the project and its dependencies.

1. Clone the repository to your local machine using Git: <br>
HTTPS

```bash
git clone https://github.com/bosukeme/pdf-analyser.git
```

SSH
```bash
git clone git@github.com:bosukeme/pdf-analyser.git
```

<br>

2. Navigate to the project directory

```bash
cd pdf-analyser
```

Before you start the application, you need to set up an environment variables. Here's how you can do it:

- Create a file called `.env` file at the root folder with the environment variables in the `.env.sample` file


### Running Docker

navigate to the root directory

```bash
docker-compose up --build
```

### visit 
```bash
http://localhost:8000/
```

To stop the containers

```bash
docker-compose stop
```

### Running locally

navigate to the root directory

```bash
python manage.py runserver
```

### visit 
```bash
http://localhost:8000/
```



### Testing


```bash
python manage.py backend.tests

```



## Contributing
If you would like to contribute, please follow these steps:

- Fork the repository.
- Create a new branch for your feature or bugfix.
- Submit a pull request.


## Authors

Ukeme Wilson
- <a href="https://www.linkedin.com/in/ukeme-wilson-4825a383/">Linkedin</a>.
- <a href="https://medium.com/@ukemeboswilson">Medium</a>.
- <a href="https://www.ukemewilson.sbs/">Website</a>.

