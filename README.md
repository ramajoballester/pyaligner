# Pyaligner

![Read the Docs](https://img.shields.io/readthedocs/pyaligner?style=flat-square)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/pyaligner?style=flat-square)

**PyAligner** is a python library to automatically transcribe audio files and align them with the transcription. Is is based on OpenAI's [Whisper](https://github.com/openai/whisper) model and the [Montreal Forced Aligner (MFA)](https://montreal-forced-aligner.readthedocs.io/en/latest/) library. It also provides a friendly graphical user interface to facilitate the use of the library:

<p align="center">
  <img src="docs/images/gui_example.png" alt="Your Image" width="200">
</p>

Check the [documentation](https://ramajoballester.github.io/pyaligner/) for more information about the installation and the complete user guide.

# Installation

You can install the library via pip:

```bash
pip install pyaligner
```

Although it is recommended to install it following the [installation guide](file:///home/breaststroker/alvaro/pyaligner/docs/build/html/install.html).


# Command Line Interface

Apart from the graphical interface, PyAligner has a command line interface to provide a greater flexibility and customization options. You can check the available commands by running:

```bash
pyaligner --help
```

