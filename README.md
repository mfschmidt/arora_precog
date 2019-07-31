This project contains data and code supporting Arora, et al. 2019. Instructions for setting up the environment in linux follow.

    git clone https://github.com/mfschmidt/arora_precog_2019.git
    cd arora_precog_2019
    pipenv install  # installs ipykernel and jupyter, both required for this, because they're listed in the pipfile
    pipenv shell
    python -m ipykernel install --user --name=arora_precog_2019
    jupyter notebook
    
From there, you can explore the methods used and reproduce them if desired.
