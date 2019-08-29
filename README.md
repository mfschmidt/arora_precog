This project contains data and code supporting Arora, et al. 2019.
Instructions for setting up the environment in linux follow.

    git clone https://github.com/mfschmidt/arora_precog.git
    cd arora_precog
    pipenv install  # (based on the Pipfile) installs ipykernel and jupyter
    pipenv shell
    python -m ipykernel install --user --name=arora_precog
    jupyter notebook
    
For MacOS or Windows, try installing Jupyter via Anaconda, and running from wherever you download
this git repository.

From there, you can explore the methods used and reproduce them if desired. The analyses are broken into three notebooks and one support file. If running analyses, each is dependent upon output from its predecessor, so 01 must be run first, then 02, then 03.

* common.py is a support file. It defines filenames and color palettes so other notebooks can be consistent without redefining them.
* 01_collect_data.ipynb pulls data from the Excel spreadsheet and stores it into dataframes appropriate for scipy and matplotlib analyses and plots.
* 02_summarize_data.ipynb summarizes hit rates and sex distribution. It also compares its own calculated hit rates to those calculated in the Excel spreadsheet.
* 03_analyze_data.ipynb does most of the work for publication. It builds plots to visualize relationships in the data. It then runs t-tests and correlations to quantify relationships.

Outputs (dataframes and images) are not controlled by git, so the notebooks must be executed locally to generate them.
