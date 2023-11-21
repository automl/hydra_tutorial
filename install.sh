conda create -n hydratutorial python=3.11 -y
conda activate hydratutorial
pip install -e .

git clone git@github.com:automl/hydra-smac-sweeper.git
cd hydra-smac-sweeper
pip install -e . --config-settings editable_mode=compat
pip install bokeh  # for Dask dashboard
cd ..
