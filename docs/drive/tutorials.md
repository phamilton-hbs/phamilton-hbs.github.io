# Tutorials

+ [Structure of the Tutorials](#structure-of-the-tutorials)
+ [Creating the Notebook for the Tutorials](#creating-the-notebook-for-the-tutorials)
+ [Adding Questions to the Poll](#adding-questions-to-the-poll)
+ [Adding Videos to the Poll](#adding-videos-to-the-poll)

The tutorials for the course are administered through Google Polls. They allow the students to work through applied problems using the tools they learned in the reading. They typically consist of a few conceptual questions, a video where an instructor walks through an applied problem in R, and a set of practice problems in R for the students to try on their own. 

---

## Structure of the Tutorials

A template for the tutorials can be found on Drive at `DSM/Templates/Class XX Tutorial: Template` (direct link [here](https://docs.google.com/forms/d/1IEXmqNqmTO8mYHeSIhSOiIMV9rvFfoYOgsFrut83UWU/edit?usp=sharing)). If you open this template, you will see that it consists of several different sections. 

+ The first section provides an overview of the tutorial and includes the link to the code notebook that accompanies the tutorial (more on that later). This section also asks students to identify which section they are in. 
+ The second section consists of three to four conceptual questions on the reading from the dsm.business site (or module notes). These are not meant to be applied questions where students need to analyze any data. 
+ The third section contains a video where an instructor works through an applied problem in an accompanying Colab notebook. The students also have access to the notebook, and work through the problem along with the instructor. 
+ The fourth section contains additional applied problems for the students to work through on their own. For these questions, the students do need to use R to analyze real data. 
+ The last section is optional and contains challenge problems for students who want to push themselves. 

Not all of the tutorials include all of these sections. For certain cases, we want the students to analyze the case data on their own before coming to class. In these instances we remove the last two sections of the tutorial, as the code notebook accompanying the case fills that role. 

To create a new tutorial, copy this template into the appropriate folder and rename it. 

## Creating the Notebook for the Tutorials

If you navigate to the `Tutorials` folder on the Drive, you will see it contains three sub-folders:
+ `data`, which contains all of the data sets used in the tutorials;
+ `notebooks`, which contains all of the code notebooks used in the tutorials;
+ `quizzes`, which contains the tutorials themselves (*i.e.* the Google Polls); and
+ `videos`, which contains the video files for the tutorials. 

The first step to creating a new tutorial is to create the notebook that will accompany the tutorial. Like all the other notebooks in the course, these notebooks should have a starter and finisher version, and should follow all of the best practices described in [Colab Notebooks](drive/colab.md#colab-notebooks). The notebooks should have three sections: a `Video` section with a set of problems that the instructor will walk through in the video in section three of the tutorial; a `Try It Out` section that the students will work through on their own in section four of the tutorial; and a `Push Yourself (*Optional*)` section that students may choose to work through in section five of the tutorial. For an example of this, see the notebook for the tutorial on hypothesis testing [here](https://colab.research.google.com/drive/1rkKzh5s-e-xYhF5nk5VyYhbJ-TD8PuXj?usp=sharing). 

Once this notebook is finalized, an instructor will film a video of them working through the `Video` section. Additionally, a set of questions should be added to sections four and five of the tutorial based on the analyses in the `Try It Out` and `Push Yourself (*Optional*)` sections of the notebook (respectively). As students work through these sections of the notebook, they are expected to answer the corresponding questions in the Google Poll. 

## Adding Questions to the Poll

To add a new question to a poll, click on the desired section and then click the `Add question` button on the right-hand pane. For example, to add a question to `General Questions` (section 2):

<video style="padding:1px;border:1px solid black;" width="640" height="480" controls>
  <source src="https://i.imgur.com/iyEHnke.mp4" type="video/mp4">
</video>

Once a new question is created, the drop-down bar in the top right allows you to select the type of question you would like to create (multiple choice, short answer, checkboxes, etc.) For certain question types, such as multiple choice, checkboxes, and short answer, you can add a correct answer by clicking the `Answer key` button in the bottom right of the question window. When students complete the poll, this answer key will be used to evaluate the accuracy of their responses. For other question types, such as `Paragraph`, clicking `Answer key` allows you to provide question feedback that students will be able to read after they have submitted the poll. 

## Adding Videos to the Poll

To embed the video in section three of the tutorial, the first step is to upload the video to the course YouTube channel. To do this, go to youtube.com and log in with the dsmfaculty@gmail.com account. Once you are logged in to this account, select the `Your videos` tab on the left:

<kbd>
<img src="\..\_media\your_videos.png" alt="drawing" width="900"/>
</kbd>

This will take you to the studio page for the DSM channel. Next, click the `CREATE` button in the top right of the window, select `Upload videos`, and upload the video file:

<video style="padding:1px;border:1px solid black;" width="640" height="480" controls>
  <source src="https://i.imgur.com/FBvDa2E.mp4" type="video/mp4">
</video>

In the `Details` tab, give the video an appropriate title and then select `No, it's not made for kids` under `Audience`. Hit `NEXT` in the bottom right to get through the `Video elements` and `Checks` tabs. When you get to the final `Visibility` tab, select `Unlisted` under `Save or publish` so that the video is only viewable by users who have the link. Finally, click `SAVE` in the bottom right. This will begin the upload process, which may take several hours or days. 

Once the video is finished processing, find it in the `Content` tab of the YouTube Studio page and click the `Options` button to the right of the video. Then click `Get sharable link`:

<video style="padding:1px;border:1px solid black;" width="640" height="480" controls>
  <source src="https://i.imgur.com/uyygrKl.mp4" type="video/mp4">
</video>

This will automatically copy the public link to the video. Now go back to the new tutorial (the Google Poll), click into the `Video` tab (section 3), and click the `Add video` button on the right-hand pane. In the window that opens, select the `URL` tab and paste in the video URL copied in the previous step. Click `Select` in the bottom left. After this, the video will be embedded in the poll. 

<video style="padding:1px;border:1px solid black;" width="640" height="480" controls>
  <source src="https://i.imgur.com/dRp7zuh.mp4" type="video/mp4">
</video>