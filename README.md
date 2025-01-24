# prog_JingjiePeng_2025


Code used in a manuscript by Jing-Jie Peng†, Beate Throm†, Maryam Najafian Jazi, Ting-Yun Yen, Hannah Monyer*‡, Kevin Allen*‡


## Python Environment

1. I installed the default [Anaconda](https://www.anaconda.com/).

Get an updated link to the installation script from https://www.anaconda.com/products/distribution

You might have to adjust the name of the exact file.
```
cd ~/Downloads
curl -O https://repo.anaconda.com/archive/Anaconda3-2022.10-Linux-x86_64.sh
chmod u+xrw Anaconda3-2022.10-Linux-x86_64.sh
./Anaconda3-2022.10-Linux-x86_64.sh
```

2. Get Deeplabcut source code:

```
git clone https://github.com/DeepLabCut/DeepLabCut.git
```

3. Modify the DEEPLABCUT.yaml file
I remove the `[gui]` from the DEEPLABCUT.yaml file and added seaborn.
```
emacs ~/repo/DeepLabCut/conda-environments/DEEPLABCUT.yaml
```

4. Install the DEEPLABCUT conda environment: 


```
cd DeepLabCut/conda-environments
conda env create -f DEEPLABCUT.yaml
```



5. `conda activate DEEPLABCUT`
6. `echo "conda activate DEEPLABCUT" >> ~/.bashrc`
7. `conda install -c anaconda ipykernel`
8. `python -m ipykernel install --user --name=DEEPLABCUT`
9. `conda install Cython`
10. `conda install -c conda-forge jupyterlab`
11. Install [spikeA](https://github.com/kevin-allen/spikeA/blob/main/docs/main.md) (Don't install dependency, use conda to install them if needed)

```
cd ~/repo
git clone https://github.com/kevin-allen/spikeA.git
cd ~/repo/spikeA
pip install -e ~/repo/spikeA
cd ~/repo/spikeA/spikeA/
python setup.py build_ext --inplace
```


12. Install [autopipy](https://github.com/kevin-allen/autopipy/blob/master/docs/easy_installation.md)

```
cd ~/repo
git clone https://github.com/kevin-allen/autopipy.git
pip install -e ~/repo/autopipy
```

13. Install positrack2

The starting point for the analysis is in the README.md located in the behavior_only and electrophys_behavior directories.
