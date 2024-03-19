# brew update
# brew install -y wget ffmpeg

wget "https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-$(uname)-$(uname -m).sh"
bash Miniforge3-$(uname)-$(uname -m).sh

mamba create -n pyaligner_env -c conda-forge python montreal-forced-aligner pyqt
mamba init