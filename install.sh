#!/bin/bash

helpMessage() {
   echo "Usage: `basename $0` [-e env [env_name]] [-hv]"
   echo "Options:"
   echo -e "\te: enviroment type (conda or pip)"
   echo -e "\tenv_name: name of the environment for creation, mandatory for the conda environment"
   echo -e "\th: see this message"
   echo -e "\tv: get software version"
   exit
}

while getopts "hv" OPT
do
    case $OPT in
        e) ENV=$OPTARG
        h) helpMessage ;;
        v)
            echo "`basename $0` version 0.1"
            exit ;;
        ?) helpMessage ;;
    esac
done
shift $((OPTIND-1))

case $ENV in
    conda)
        if [ -z $1 ]
        then
            helpMessage
        fi

        echo ""
        echo "Create enviroment"
        {
            which conda \
            && conda create -n $1 -f geoschem_data_analysis.yml -y \
            && source activate $1 || conda activate $1
        } || {
            echo "[ERROR] Conda could not be found"
            exit
        }
        ;;
    pip)
        echo ""
        echo "Create enviroment"
        {
            which pip \
            && pip install -r requirements.txt
        } || {
            echo "[ERROR] Pip could not be found"
            exit
        }
        ;;
    ?) helpMessage ;;
esac

echo ""
echo "Install widget jupyter and execute"
jupyter labextension install @jupyter-widgets/jupyterlab-manager

echo ""
echo "done."
