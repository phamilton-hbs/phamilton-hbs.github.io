# Bootcamp Tutorials

The `R BOOTCAMP` section of the dsm.business site (starting [here](https://dsm.business/00_bootcamp/01_rbasics/rbasics.html)) contains embedded R tutorials built using a tool called `learnr`. These tutorials are managed in the `bootcamp_exercises` repository in the course GitHub organization (direct link: https://code.harvard.edu/DSM/bootcamp_exercises). Like the Shiny apps, these are also published through shinyapps.io. 

To learn how to create `learnr` tutorials, work through the [guide here](https://rstudio.github.io/learnr/). These tutorials are published through shinyapps.io in the same way that Shiny apps are published. 

Once the tutorials are published through shinyapps.io, the next step is to embed them in the `R BOOTCAMP` section of the course website. For example, the [R as a Calculator](https://dsm.business/00_bootcamp/01_rbasics/r_as_a_calculator.html) section of the bootcamp has an interactive console where the students enter basic R commands. This application is published through shinyapps.io as `r_as_a_calculator` [here](https://www.shinyapps.io/admin/#/application/5353332). The URL for the application is `https://hbs-data-science.shinyapps.io/r_as_a_calculator/`. If you open the file `dsm_website/00_bootcamp/01_rbasics/r_as_a_calculator.md`, you will see the following line at the bottom of the file:

`<iframe src="https://hbs-data-science.shinyapps.io/r_as_a_calculator/" width="800" height="350" frameborder="0" marginheight="0" marginwidth="0"  scrolling="no">Loading…</iframe>`

This embeds the web application within the website page using an iframe. Any of the published web applications can be embedded in this way by changing the URL after `src=`. The `width` and `height` parameters control the size of the application within the web page.  