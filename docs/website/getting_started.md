# Getting Started 

This guide assumes that you have already forked the `dsm_website` repository at https://code.harvard.edu/DSM/dsm_website. Here you will learn how to run and edit the book out of your local copy of the repo.

---

The course book managed in the repo above is built using [Jupyter Book](https://jupyterbook.org/intro.html), an "open source project for building beautiful, publication-quality books and documents from computational material." To edit and build the book, you will need to install Jupyter Book locally. Before this, you must have Python 3 installed on your machine. 

1. **Install Python** If you do not already have Python installed, install the Anaconda distribution [following the steps here](https://docs.anaconda.com/anaconda/install/).

2. **Install Jupyter Book** Now [follow the steps here](https://jupyterbook.org/start/your-first-book.html) to install Jupyter Book, and build your first book.
    + You only need to work through the subsection *Create your own content file*.
    + **Note** if you are working on a Windows machine - on Windows, Jupyter Book is incompatible with python versions greater than 3.7. Therefore, it is recommended that you create a custom environment for the book that has python 3.7 installed (and not a later version). See the [page here](https://jupyterbook.org/advanced/windows.html?highlight=python%20version) for more details. 

After completing the Jupyter Book tutorial in Step 2 above, you should know how to build a book on your local machine. To build the course text locally, simply build the book stored in the `dsm_website` repository.
