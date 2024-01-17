# Job Analyser: Exploring the Data and AI Job Market in Egypt 
![38413-Job-Analyzer](https://github.com/Aml-Hassan-Abd-El-hamid/-wuzzuf_job_analyser/assets/66205928/ecbf59ae-a813-425d-a6f1-967d69a8d952)

### Problem Statment:

Navigating the Data and Artificial Intelligence (AI) job market in Egypt can be confusing, particularly for newcomers, every job description feels like it with a new surprise and it seems like every company has their definition of roles like (ML engineer, data scientist, data analyst, ...). This project aims to systematically collect and analyze data related to the Data and AI job market in Egypt. The primary objective is to gain insights into key aspects of the market, including the common skills in demand.

### Running the project locally:

1. Clone the project repo

2. Set up the project env, you can do that by following those steps

    * Install **poetry** at the system level following the instructions from here: https://python-poetry.org/docs/

    * In the project directory where you can see pyproject.toml, write the following commands in your terminal:
    ```
    poetry install
    ```
    * You can now run `poetry shell` in your terminal to activate the environment. 

**To run the Wuzzuf scrapper and save the scrapped data into a file do the following after setting up your enviornment:**<br>
   * In the main folder of the project run the command `poetry shell` in your terminal to activate the environment.
   * Run the command `cd scrapper/scrapper/spiders` in your terminal to get the folder of the spiders.
   * Run the command `scrapy crawl wuzzufspider -a group="your_wuzzuf_search_link" -o your_file_name.csv` in your terminal.

**To run the scrappy shell:**
   * In the main folder of the project run the command `poetry shell` in your terminal to activate the environment.
   * Run the command `cd scrapper/scrapper/spiders` in your terminal to get the folder of the spiders.
   * Run the command `scrapy shell` in your terminal to start the scrappy shell.
   * you can run the command `fetch('the website name')` in your terminal.
### ToDo List of the project:

- [ ] Wuzzuf scrapper<br>

   Should extract the following features:

   - [x]  Job Name
   - [x]  Company Name
   - [x]  Job Location
   - [x]  Job Type
   - [x]  Job and Company URLs
   - [x]  Job description body
   - [ ]  Job Skills
   - [ ]  Experience Needed for the job
   - [ ]  Job Requirements body if there<br>
   
   Cleaning:

   - [ ]  Job description body and Job Requirements body -if there's one- should be merged and used to extract as much info as possible from them.
   - [ ]  Job Skills
- [ ] The job analyzer<br>
- [ ] LinkedIn Scrapper<br>
- [ ] Deployment <br>

### Useful tutorials:
- [Scrapy Course from freeCodeCamp](https://www.youtube.com/watch?v=mBoX_JCKZTE&t=4599s)
- [tutorialspoint scrappy tutorial](https://www.tutorialspoint.com/scrapy/index.htm)
