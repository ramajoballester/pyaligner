# Pyaligner
Automatic audio transcriptor and aligner

# Installation

## Install Anaconda / Miniconda

If you don't have conda installed, install [Anaconda](https://docs.anaconda.com/free/anaconda/install/index.html) or [Miniconda](https://docs.anaconda.com/free/miniconda/miniconda-install/).

If you already have conda installed, update it:

```bash
conda update conda
```

and uninstall the packages in base environment (be careful with this step if you use base environment for other projects):

```bash
conda install --rev 0
```


## Install dependencies

Once conda is installed, create a new environment, (e.g. pyaligner_env) and install the dependencies:

```bash
conda activate base
conda install -c conda-forge mamba
```

Then, create the environment and install the dependencies:

```bash
mamba create -n pyaligner_env -c conda-forge python montreal-forced-aligner pyqt git
```

After that, you might need to run `mamba init` and restart the terminal to activate mamba.


## Clone the repository

Activate the environment and clone the repository:

```bash
mamba activate pyaligner_env
git clone https://github.com/ramajoballester/pyaligner.git
cd pyaligner
pip install .
```


# Usage

Do not forget to activate the environment:

```bash
mamba activate pyaligner_env
```

before running the commands:

```bash
pyaligner gui
```



# Requirements

Install ffmpeg:
```bash
sudo apt update
sudo apt install ffmpeg
```

# Pipeline

1. Transcription. Load audio and transcribe it to text with whisper.
2. Alignment. Align the transcription with the original audio.
3. Replace audio filenames with folder name + 000n

- auto: all
- align:
```bash
mfa align . spanish_mfa spanish_mfa ../results/ --clean
```
- download:
```bash
mfa download spanish
```bash
mfa model download dictionary spanish_mfa
```
- transcribe:



# Configuration

- Model size: the bigger the model, the better the transcription but the slower the process.

mfa align . spanish_mfa arsdtarsd_mfa ../results/ --clean


# Dependencies

libxcb-cursor0

```bash
sudo apt upgrade libgtk-3-0
```

Mac:

xcode-select --install

