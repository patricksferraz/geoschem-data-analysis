#!/bin/bash


echo "#########################################"
echo "Initializing enviroment"
echo "#########################################"
if which conda;
then
    conda env create \
        --name geoschem_data_analysis \
        --file geoschem_data_analysis.yml
    conda activate geoschem_data_analysis

elif which conda;
then
    pip install -rrequirements.txt

else
    echo "#########################################"
    echo "[ERRO] Conda or pip could not be found"
    echo "#########################################"
    exit 1
fi

echo "#########################################"
echo "Install widget jupyter and execute"
echo "#########################################"
jupyter labextension install @jupyter-widgets/jupyterlab-manager
jupyter-lab