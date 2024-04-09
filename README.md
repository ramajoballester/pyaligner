# Pyaligner

![Read the Docs](https://img.shields.io/readthedocs/pyaligner?style=flat-square)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/pyaligner?style=flat-square)

**PyAligner** is a python library to automatically transcribe audio files and align them with the transcription. Is is based on OpenAI's [Whisper](https://github.com/openai/whisper) model and the [Montreal Forced Aligner (MFA)](https://montreal-forced-aligner.readthedocs.io/en/latest/) library. It also provides a friendly graphical user interface to facilitate the use of the library:

<p align="center">
  <img src="https://github.com/ramajoballester/pyaligner/blob/fdb6b6d8605dee9bb4f1c9c62210249ffdcc8631/docs/images/gui_example.png?raw=true" alt="Your Image" width="200">
</p>

Check the [documentation](https://pyaligner.readthedocs.io/en/latest/) for more information about the installation and the complete user guide.

# Installation

You can install the library via pip:

```bash
pip install pyaligner
```

Although it is recommended to install it following the [installation guide](https://pyaligner.readthedocs.io/en/latest/install.html).


# Command Line Interface

Apart from the graphical interface, PyAligner has a command line interface to provide a greater flexibility and customization options. You can check the available commands by running:

```bash
pyaligner --help
```

