# pyaligner
Automatic audio transcriptor and aligner


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