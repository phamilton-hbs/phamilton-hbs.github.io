# Colab Notebooks

+ [Creating New Notebooks](#creating-new-notebooks)
+ [Working Process for Notebooks](#working-process-for-notebooks)
+ [Developing a Notebook](#developing-a-notebook)
+ [Reading Data into Notebooks](#reading-data-into-notebooks)
+ [Tips & Tricks](#tips-amp-tricks)

All coding in the course is done within Colab notebooks. These are browser-based code notebooks that run on Google machines. Just like Google Docs, they can be easily distributed to a large set of users through a single URL. 

---

## Creating New Notebooks

Because the course is taught in R, all of our notebooks need to use the R kernel. However, Google does not officially support the R kernel for Colab; instead by default all notebooks are created with the Python kernel. If you follow the official process for creating a notebook by clicking `New` in Drive and selecting `Google Colaboratory` (see GIF below), you will only be able to create notebooks with the Python kernel. 

<video style="padding:1px;border:1px solid black;" width="640" height="480" controls>
  <source src="https://i.imgur.com/SYIgbfy.mp4" type="video/mp4">
</video>

Therefore, we have developed a work around to create new R notebooks. To create a new R notebook, you must make a copy of the `Notebook Template.ipynb` file from `DSM/Templates` and then move the copy to your destination folder. This copy will inherit the R kernel from the template.

## Working Process for Notebooks

There should be two versions of every notebook created for the course - a "starter" version which is distributed to the students, and a "finisher" version which is only accessible by the teaching team. These two notebooks should be identical in content and structure. However, the finisher notebook should contain the complete code and written answers to all exercises, while the starter notebook should have much of the code and written answers removed for the students to fill in themselves.

Maintaining two versions of the same file is bad practice. For example, imagine we created a starter and finisher notebook in parallel, and then received feedback and needed to make significant changes. This would require propagating the same set of changes through both versions of the file. Not only is this inefficient, but if we make a mistake and miss a change in one of the two files, they will very quickly become out-of-sync. Therefore, when developing notebooks for the course it is best practice to *only* work on the finisher notebook. While the content of the notebook is still in progress, the starter version should be kept blank. Only once the finisher notebook is finalized and approved by the team should the content be copied over to the starter notebook. 

For example, imagine we were creating the prework notebook for the Yelp case. We begin by copying the notebook template from `DSM/Templates` and moving it to the `notebooks` folder within `Class 5 - Analysis of Experiments (Yelp)`. We will copy the template twice, once for the finisher notebook and once for the starter notebook. 

<video style="padding:1px;border:1px solid black;" width="640" height="480" controls>
  <source src="https://i.imgur.com/gAHUQoB.mp4" type="video/mp4">
</video>

Next we rename the files by right clicking and selecting `Rename`. The finisher notebook should have the same name as the starter, but with `(FINISHER)` appended at the end. 

<video style="padding:1px;border:1px solid black;" width="640" height="480" controls>
  <source src="https://i.imgur.com/YKyZrxC.mp4" type="video/mp4">
</video>

As we develop the notebook we should *only* work out of the finisher file, and the starter version should remain blank. This means that the finisher notebook is the one that should be shared with the rest of the teaching team for their feedback. Once the notebook is finalized and there are no more changes to implement, the content of the finisher can be copied over to the starter notebook. At this point, the next step is to copy all of the cells from the finisher into the starter, and then remove the code and written answers that we want the students to fill in themselves. To copy all the cells in the finisher, click the cell at the very top of the notebook, scroll to the bottom of the notebook, then hold the `Shift` key and click the last cell in the notebook. This will highlight all of the cells in the finisher. Then copy them by right-clicking and selecting `Copy cells`:

<video style="padding:1px;border:1px solid black;" width="640" height="480" controls>
  <source src="https://i.imgur.com/FjoIMuQ.mp4" type="video/mp4">
</video>

Next, to create the starter:
1. Paste those cells into the blank starter notebook by pressing `Ctrl` + `v`;
2. At the top of the starter notebook, click `Edit` -> `Clear all outputs`; and
3. Walk through the starter notebook and remove code or written answers that we want the students to fill in themselves. Empty code cells should contain `# ADD COMMAND(S) HERE`, and empty text cells should contain `[ADD ANSWER HERE]`.

<video style="padding:1px;border:1px solid black;" width="640" height="480" controls>
  <source src="https://i.imgur.com/8NPAtJJ.mp4" type="video/mp4">
</video>

Once this is finished, the starter notebook is ready to be shared with the students. 

## Developing a Notebook

The Colab notebooks that accompany each case serve two primary purposes:
1. They give students the opportunity to practice applying the analytical techniques they learned in the prework (*i.e.* in the videos, readings, etc.); and 
2. They allow students to analyze the data associated with a case to inform our case discussion. 

The notebooks need to strike a careful balance between challenging the students' coding ability and guiding them through the analyses for a case. If we do not provide enough guidance in the notebooks and the students are unable to properly analyze the data, the case discussion will fall flat. On the other hand, if we provide too much instruction the students will not get sufficient practice and by the end of the course they will not have built up their coding skills. 

The notebooks should follow the "see one, do one" model as much as possible. Typically the students begin preparation for an upcoming class by reading a section from the [dsm.business](https://dsm.business/) site (or one of the module notes) and completing the associated tutorial. The reading introduces a new tool or technique and shows how it can be applied to a real data set in R. The tutorial includes a set of questions about the reading, and then features a video of an instructor walking through an example problem. After working through these materials, the students should then be ready to apply the concept on their own. They do this by working through the Colab notebook for the case. In general, this means that the notebook should provide guidance on the steps students should take to carry out an analysis, but much of the actual coding and interpretation of results should be left to the students. **Note** As of Fall 2022, many of the later notebooks in the course come with an "Unguided" and "Guided" track. The unguided track features almost no guidance and is for students who want to challenge themselves. The guided track provides more infrastructure for students who need more direction. 

For an example of a fully-developed notebook with unguided and guided tracks, see the notebook for the Yelp case [here](https://colab.research.google.com/drive/1yMr3PAR7_8FRdxo8_akhb87vFLIfBjc8?usp=sharing).

The module sequence of the course (EDA, Inference, Prediction & Machine Learning) is strategic in that this is meant to follow the sequence of an actual data science project. Therefore, where possible we try to structure the notebooks according to this sequence. For example, in later classes when we cover machine learning topics, we start the notebooks with some questions on exploratory data analysis and hypothesis testing.  

## Reading Data into Notebooks

With the R kernel, reading data from a file into a Colab notebook is not as seamless as it is with the Python kernel. There are three primary ways we read in data in the course.

**Method 1**

The first method is to have the students download the file onto their machine, upload it to the working directory within their notebook, and then read it in. We typically start with this method and do it this way for the first few notebooks so the students see how they can upload their own data sets to Colab. Once the students are comfortable with this method, we switch to one of the other two options (which are much more seamless). An example of this method can be seen in the notebook for the DDS exercise [here](https://colab.research.google.com/drive/1j9vpm0Hyt0XeaBHQdrMaFZZG__5K85c8?usp=sharing) (see the *Read in Data* section). 

To set up the file so that it can be read in this way, we first need to host the data on Drive so that the students can download it through a link provided in the Colab notebook. To do this:
1. Upload the data file to the appropriate `data` folder; 
2. Right-click the file and select `Share`, then click `Change to anyone with the link`;
3. Change the settings so that anyone with the link can *view* the file;
4. Copy the link; and
5. Paste the link into the notebook.

<video style="padding:1px;border:1px solid black;" width="640" height="400" controls>
  <source src="https://i.imgur.com/T5rCih6.mp4" type="video/mp4">
</video>

Now a student working through the notebook can read in the data using the following steps:
1. Click the link to the file on Drive and download it to their machine;
2. Open the `Files` pane in the notebook and click `Upload to session storage`; and
3. Run the `read_csv()` command to read the data from the file into R.

<video style="padding:1px;border:1px solid black;" width="640" height="380" controls>
  <source src="https://i.imgur.com/gOvMa4E.mp4" type="video/mp4">
</video>

**Method 2**

The second method is to host the data file on a website, and read it in directly through a URL. Below is an example from the `Class 4: Videos.ipynb` notebook in the archived folder from `DSM I (Fall 2021, EC)`. A subsequent section of the documentation ([Hosting Files](../website/cpanel.md#hosting-files)) describes how to host a data file on the dsm.business site.

<video style="padding:1px;border:1px solid black;" width="640" height="380" controls>
  <source src="https://i.imgur.com/XQLwOB6.mp4" type="video/mp4">
</video>

**Method 3** 

The last method is to host the file on Drive and download the file into the notebook through a system command. To do this:
1. Upload the file to the appropriate `data` folder and share it to anyone with the link with *view* access;
2. Copy the link; 
3. From the link, note the file ID, which is the sequence of characters between `/d/` and `/view` - for example, in the file URL below the ID is `12FGnAzTM2QWjS4YospNmA0x1s3xUItTU`;
	+ https://drive.google.com/file/d/12FGnAzTM2QWjS4YospNmA0x1s3xUItTU/view?usp=sharing
4. In the notebook cell where the data is read in, include the command `system("gdown --id [FILE_ID]")` - this will automatically download the file from Drive into the current working session. 

For an example of this method, see the notebook for the Warriors case [here](https://colab.research.google.com/drive/1wpsvcJt40WBXuw7HWoyUQdKgiSXmeFOn?usp=sharing). 

## Tips & Tricks

This section contains miscellaneous tips and tricks for working with Colab notebooks. 

**Packages**

Most packages are *not* pre-installed on the virtual machines that run Colab notebooks. Therefore, in each working session one needs to install and load any packages used throughout the notebook, which can sometimes take several minutes. Notably, the `tidyverse` and `ggplot2` packages are pre-installed, so these packages can simply be loaded. We always install and load all required packages at the top of each notebook. Additionally, we typically begin each notebook with a reminder for the students to make a copy of the notebook in their personal Drive account, as well as a reminder to install and load all necessary packages. For example, here is the header of a typical notebook:

<kbd>
<img src="\..\_media\notebook_head.png" alt="drawing">
</kbd>

**Hiding Code Cells**

Occasionally we want to provide students with the option to reveal code if it is particularly challenging. For example:

<video style="padding:1px;border:1px solid black;" width="640" height="420" controls>
  <source src="https://i.imgur.com/Q4tWEFt.mp4" type="video/mp4">
</video>

To do this, create the code cell, click into it, and then select `View` -> `Show/hide code`:

<video style="padding:1px;border:1px solid black;" width="640" height="300" controls>
  <source src="https://i.imgur.com/T4WAXpE.mp4" type="video/mp4">
</video>
