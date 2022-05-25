# Managing the Site with cPanel

[Reading the Documentation](#reading-the-documentation)

The dsm.business website is managed through a web hosting service called cPanel. This section describes how to access and use this tool. 

---

To access the cPanel for the dsm site, navigate to https://dsm.business/cpanel. To log in you will need the username and password for the administrator account, which are owned by the course RA. 

## Hosting Files

Often we want to host different files on the site. For example, as we saw in the section [Reading Data into Notebooks](drive/colab.md#reading-data-into-notebooks), we often host data files on the dsm site and read them into Colab notebooks through a URL. To upload a file, start by clicking the `File Manager` tool under `FILES` on the site cPanel page:

<kbd>
<img src="\..\pages\DSM\DSM.github.io\_media\file_manager.png" alt="drawing" width="900"/>
</kbd>

Next, click into the `public_html` directory:

<kbd>
<img src="\..\pages\DSM\DSM.github.io\_media\public_html.png" alt="drawing" width="900"/>
</kbd>

Now choose the subdirectory where you want to host the file. If we were uploading a data set, we would choose the `data` directory. If we were uploading an image, we would choose `_images`, etc. For now we'll upload a data file, so we will choose the `data` folder:

<kbd>
<img src="\..\pages\DSM\DSM.github.io\_media\data_folder.png" alt="drawing" width="900"/>
</kbd>

To upload the file to this directory, click the `Upload` button at the top of the page and then either click `Select File` or drag the file onto the upload box. Once the file is finished uploading, click `Go Back to ...`.

<video style="padding:1px;border:1px solid black;" width="640" height="480" controls>
  <source src="https://i.imgur.com/fDbuYZu.mp4" type="video/mp4">
</video>

Now the data is available at https://dsm.business/data/dds_data.csv. 

## Redirect Links

Another common use for the website is redirect links. Often we want to distribute a Colab notebook or document on the fly during class, but the links auto-generated by Google Drive are unruly. Therefore, we set up a redirect link through the website so the students just need to type in a short, intuitive URL in their browser and they are automatically directed to the file. For example, in the first class we want students to access the notebook at https://colab.research.google.com/drive/1wpsvcJt40WBXuw7HWoyUQdKgiSXmeFOn?usp=sharing, but we set up a redirect to this document at dsm.business/colab/class1 so that it is easier for the students to navigate to it. 

To do this, start by clicking the `Redirects` tool under `DOMAINS` on the site cPanel page:

<kbd>
<img src="\..\pages\DSM\DSM.github.io\_media\redirect_panel.png" alt="drawing" width="900"/>
</kbd>

Next enter the desired path in the `/` bar (`colab/class1`) and the full URL of the file in the `Redirects to` bar. Then click `Add` at the bottom.

<kbd>
<img src="\..\pages\DSM\DSM.github.io\_media\add_redirect.png" alt="drawing" width="900"/>
</kbd>

Although we have now set up the redirect, it will *not* work until we create directories for the path specified in the `/` bar. In this case our path is `colab/class1`, which means that our site needs to have a `colab` folder containing an empty `class1` folder to the redirect to work. Using the file manager, go into `public_html`, and then into the `colab` directory. Note that the `colab` directory already exists, but if it did not we would need to create it. Then, within `colab` we create a blank folder called `class1` by clicking `+ Folder` at the top left of the screen. Once the `colab/class1` directory is created, the redirect link will now work. 

<video style="padding:1px;border:1px solid black;" width="640" height="480" controls>
  <source src="https://i.imgur.com/OnLdOy6.mp4" type="video/mp4">
</video>