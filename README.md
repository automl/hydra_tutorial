# HydraTutorial at AutoML Fall School 2023
Looking to improve your experimental workflow? Tired of dealing with all the different experimental setups?

If so, I would like to introduce you to Hydra (https://github.com/facebookresearch/hydra).

Hydra elegantly configures complex applications and has loads of advantages like

* easy and clear experimental configuration
* no boilerplate regarding IO
* dynamic composition of configurations
* easy parallel running on local machine and on compute clusters
* easy optimization of your function

Hydra basically is a supercharged argument parser and we will show you how to use it!

Together, we will configure a basic (Auto)ML experiment.

This tutorial can serve you as an entry point and reference for your own experimental configurations with Hydra.

Check out `tutorial.ipynb` and try yourself. 🤗

We will also give you a sneak peek to our Hydra-SMAC-sweeper in the tutorial, the combined power of hydra and HPO via SMAC!



## Installation
Run `bash install.sh` to create and activate a conda environment and to install this repo.


```bash
git clone git@github.com:automl/hydra_tutorial.git
cd hydra_tutorial
conda create -n hydratutorial python=3.11
conda activate hydratutorial

# Install for usage
pip install .

# Install for development
make install-dev
```