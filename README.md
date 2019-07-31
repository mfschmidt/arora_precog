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

From there, you can explore the methods used and reproduce them if desired.
