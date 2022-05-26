# Editing the Site

+ [Book Structure](#book-structure)
+ [Writing Book Content](#writing-book-content)

Now that you know how to build the book locally, this section will provide an overview of how the book is structured. It will describe how the materials are organized, and explain how you can make local edits to the book. The next section will describe how to publish your local changes to the dsm.business website.

The [official Jupyter site](https://jupyterbook.org/en/stable/intro.html) has excellent documentation that is a very helpful reference when working on editing course content. 

---

## Book Structure

The primary structure of the book is defined in the `_toc.yml` file, which is stored in the outer `dsm_website` directory. From a high level the book is organized into modules (`R BOOTCAMP`, `EXPLORATORY DATA ANALYSIS`, etc.), which are themselves divided into multiple chapters. The chapters within the `R BOOTCAMP` module are unnumbered, while the remaining chapters are numbered. 

If you open the `_toc.yml` file, you will see that it starts with the following two lines:

```
format: jb-book
root: intro
```

The first line indicates that the materials should be formatted as a Jupyter Book, and the second line indicates the "home page" for the book. If you look into the outer `dsm_website` directory you should see a markdown file titled `intro.md`; this serves as the landing page for the website. 

The remainder of the book is organized under the `parts:` heading of the toc file. The book modules are defined with `-caption:`, and the chapters within each module are listed under `chapters:`. For example, take the `R BOOTCAMP` module:

```
format: jb-book
root: intro
parts:
  - caption: R Bootcamp
    chapters:
    - file: 00_bootcamp/01_rbasics/rbasics
      sections:
      - file: 00_bootcamp/01_rbasics/r_as_a_calculator
      - file: 00_bootcamp/01_rbasics/assignment
      - file: 00_bootcamp/01_rbasics/data_types
      - file: 00_bootcamp/01_rbasics/rbasics_quiz1
      - file: 00_bootcamp/01_rbasics/atomic_vectors
      - file: 00_bootcamp/01_rbasics/functions
      - file: 00_bootcamp/01_rbasics/rbasics_quiz2
    - file: 00_bootcamp/02_dataframes/dataframes
      sections:
      - file: 00_bootcamp/02_dataframes/r_packages
      - file: 00_bootcamp/02_dataframes/reading_in_data
      - file: 00_bootcamp/02_dataframes/data_frame_basics
      - file: 00_bootcamp/02_dataframes/df_basics_exercise
      - file: 00_bootcamp/02_dataframes/fixing_variable_types
      - file: 00_bootcamp/02_dataframes/sorting_data
      - file: 00_bootcamp/02_dataframes/filtering_rows
      - file: 00_bootcamp/02_dataframes/selecting_columns
      - file: 00_bootcamp/02_dataframes/df_manipulation_exercise
      - file: 00_bootcamp/02_dataframes/df_manipulation_quiz
    - file: 00_bootcamp/bootcamp_finish_message
```

This module contains three chapters: `R Basics`, `Data Frames`, and `Welcome to the Course!`. Each of these chapters are introduced by a single markdown file (`00_bootcamp/01_rbasics/rbasics.md`, `00_bootcamp/02_dataframes/dataframes.md`, and `00_bootcamp/bootcamp_finish_message.md`, respectively). The first two chapters have sub-sections that are defined by individual markdown files; these are listed under `sections:` below each chapter introduction file.  

Now consider the `EXPLORATORY DATA ANALYSIS` module, which is defined in the toc file as follows:

```
- caption: Exploratory Data Analysis
    numbered: True
    chapters:
      - file: 01_eda/eda
        sections:
        - file: 01_eda/what_is_data
        - file: 01_eda/summary_stats
        - file: 01_eda/visualization
        - file: 01_eda/eda_quiz
        - file: 01_eda/outliers
        - file: 01_eda/ggplot
      - file: 02_tidy/eda_tidyverse
        sections:
          - file: 02_tidy/pipe_operator
          - file: 02_tidy/summarise
```

Note that because the chapters within this module are numbered, we set `numbered: True` just under the `-caption` definition of the module name.

When the book is built, Jupyter Book uses the structure defined in the `_toc.yml` file to compile all of the individual markdown (`.md`) files into the proper configuration.

## Writing Book Content

Every page in the book is a markdown (`.md`) file. For a general reference on how to create notebooks entirely in markdown, see [here](https://jupyterbook.org/file-types/myst-notebooks.html). 

### Code in Markdown 

To see how we can create markdown files that contain formatted text, lines of R code, and code output, let's use the file `05_linear_regression/multiple_linear_regression.md` as an example. To see how this page looks when rendered, visit the page [here](https://dsm.business/05_linear_regression/multiple_linear_regression.html). 

If you open the `multiple_linear_regression.md` file, you will see the following at the top:

```
---
jupytext:
  cell_metadata_filter: -all
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.11.5
kernelspec:
  display_name: R
  language: R
  name: ir
---
```

This block indicates that any code cells within the markdown file should be run with the `R` kernel. This block needs to be included in any markdown files that contain R code. Next, we see the following:

``````
```{code-cell}
:tags: [remove-cell]
library(tidyverse)
employees <- read_csv("../_build/data/employee_data.csv")
employees$Salary <- parse_number(employees$Salary)
employees$Start_Date <- parse_date(employees$Start_Date, format = "%m/%d/%Y")
degreeLevels <- c("High School", "Associate's", "Bachelor's", "Master's", "Ph.D")
employees$Degree <- parse_factor(employees$Degree, levels = degreeLevels, ordered = TRUE)
```
``````

The purpose of this section is to load and process the `employees` data that will be used later in the page. We want to do this behind the scenes, so we do not want this code or any of its outputs to be present in the final rendered markdown. The directive `````` ```{code-cell} `````` indicates that the chunk contains code that needs to be executed (and not text to be formatted as markdown). The first line of the chunk, `:tags: [remove-cell]`, indicates that both the code and the output of the code should *not* be displayed in the rendered markdown file. There are several options for this setting (see [here](https://jupyterbook.org/interactive/hiding.html?highlight=tags#hide-code-cell-content) for additional info):

+ `:tags: [remove-cell]` - do not display the code or its outputs in the rendered markdown file;
+ `:tags: [hide-input]` - do not display the code in the rendered markdown file, but *do* display any output that the code produces; and
+ `:tags: [hide-output]` - do not display any output that the code produces in the rendered markdown file, but *do* display the code itself.

If you would like the rendered markdown to display both the code and its outputs, simply do not include this tag setting in your code chunk. For example, in the `Basic Diagnostic Plots` section of our markdown file, we have the following:

``````
```{code-cell}
plot(modelAgeRating, which = 1)
```
``````

When we look at the rendered markdown [here](https://dsm.business/05_linear_regression/multiple_linear_regression.html#basic-diagnostic-plots), we can see that the R code (`plot(modelAgeRating, which = 1)`) and the code's output (the residuals v. fitted plot) are both displayed. 

### Demonstrating Syntax

When displaying the syntax of a new function, create a content block with `{admonition} Syntax`. For example, in our markdown file we have:
``````
```{admonition} Syntax
`lm(y ~ x1 + x2 + ... + xp, data = df)`
+ *Required arguments*
  - `y`: The name of the dependent ($Y$) variable.
  - `x1`, `x2`, ... `xp`: The name of the first, second, and $pth$ independent variables.
  - `data`: The name of the data frame with the `y`, `x1`, `x2`, and `xp` variables.
```
``````

This is rendered as the `Syntax` block [here](https://dsm.business/05_linear_regression/multiple_linear_regression.html#multiple-linear-regression). For consistency, always use the following pattern to define the syntax of new functions:
``````
```{admonition} Syntax
`function(arg1 = default_param, arg2 = default_param, ...)`
+ *Required arguments*
  - `arg1`: Description of the first argument.
  - `arg2`: Description of the second argument.
+ *Optional arguments*
  - `optional_arg`: Description of an optional argument.
```
``````

### Sections Not in Module Note

Certain sections of the Jupyter book are not covered in the course, nor are they present in the officially published module notes. Within the book, these sections are marked with the symbol (§). In markdown, this symbol is represented by `(&sect;)`. Additionally, the top of these sections contains the following content block:

``````
:::{note}
This section is optional, and will not be covered in the DSM course.
:::
``````

For an example, see the file `02_tidy/ggplot.md`, which you can see rendered [here](https://dsm.business/02_tidy/ggplot.html#visualization-with-ggplot2).

