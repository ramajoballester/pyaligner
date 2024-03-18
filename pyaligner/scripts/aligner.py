#!/usr/bin/env python
import argparse
import os
import sys
import torch
import whisper
from tqdm import tqdm
from pyaligner.utils import utils
from PyQt5.QtWidgets import QApplication


def align_action(args, progress_signal=None, error_signal=None):
    try:
        if progress_signal:
            progress_signal.emit(0)
            QApplication.processEvents()
        # Get a list of all filenames in the input folder and its subdirectories
        folder_path = utils.get_correct_path(args.input_folder)
        filenames = []
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                if file.endswith('.txt'):
                    filenames.append(os.path.join(root, file))
        filenames.sort()

        print(f'Checking MFA models for {args.language}')
        if error_signal:
            error_signal.emit(f'Checking MFA models for {args.language} language')
            QApplication.processEvents()
        os.system(f'mfa models download acoustic {args.language}')
        os.system(f'mfa models download dictionary {args.language}')
        command = f'mfa align {folder_path} {args.language} {args.language} {folder_path} --clean'
        if args.overwrite:
            command += ' --overwrite'
        if not args.verbose:
            command += ' --quiet'
            command += ' > /dev/null 2>&1'

        print(f'Aligning {len(filenames)} audio-transcription files')
        if error_signal:
            error_signal.emit(f'Aligning {len(filenames)} audio-transcription files')
            QApplication.processEvents()

        os.system(command)
        print('Alignment complete')
        if progress_signal:
            progress_signal.emit(100)
            QApplication.processEvents()
        if error_signal:
            error_signal.emit('Alignment complete')
            QApplication.processEvents()
    except Exception as e:
        if error_signal:
            error_signal.emit(str(e))
        else:
            raise e


def auto_action(args, progress_signal=None, error_signal=None):
    try:
        language = transcribe_action(args)
        language = whisper.tokenizer.LANGUAGES[language]
        if language + '_mfa' in utils.mfa_languages:
            args.language = language + '_mfa'
        elif language + '_cv' in utils.mfa_languages:
            args.language = language + '_cv'
        else:
            raise ValueError(f'Detected language {language} is not supported by MFA')
        args.overwrite = False
        args.verbose = False
        align_action(args)
        if error_signal:
            error_signal.emit('Transcription and alignment complete')
            QApplication.processEvents()
    except Exception as e:
        if error_signal:
            error_signal.emit(str(e))
            QApplication.processEvents()
        else:
            raise e


def transcribe_action(args, progress_signal=None, error_signal=None):
    try:
        if progress_signal:
            progress_signal.emit(0)
            QApplication.processEvents()
        folder_path = utils.get_correct_path(args.input_folder)
        filenames = []
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                if (not file.endswith('.txt') and not file.endswith('.TextGrid')
                    and not file.startswith('.')):
                    filenames.append(os.path.join(root, file))        
        filenames.sort()

        device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        print(f'Using device: {device}')
        print('Loading Whisper model')
        if error_signal:
            error_signal.emit('Loading Whisper model')
            QApplication.processEvents()
        model = whisper.load_model('medium')

        print(f'Transcribing {len(filenames)} files')
        if error_signal:
            error_signal.emit(f'Transcribing {len(filenames)} audio files')
            QApplication.processEvents()
    
        for i, filename in enumerate(tqdm(filenames)):
            if progress_signal:
                progress_signal.emit(int(i / len(filenames) * 100))
                QApplication.processEvents()
            # print(f'Transcribing {filename}')
            audio = whisper.load_audio(filename)
            transcription = whisper.transcribe(model, audio)
            transcription_file = os.path.splitext(filename)[0] + '.txt'
            with open(str(transcription_file), 'w') as f:
                f.write(transcription['text'])

        print('Transcription complete')
        if progress_signal:
            progress_signal.emit(100)
            QApplication.processEvents()
        if error_signal:
            error_signal.emit('Transcription complete')
            QApplication.processEvents()

        return transcription['language']

    except Exception as e:
        if error_signal:
            error_signal.emit(str(e))
            QApplication.processEvents()
        else:
            raise e


def rename_action(args):
    # Get all filenames in the input folder
    folder_path = utils.get_correct_path(args.input_folder)
    folder_filenames, folder_directories = utils.get_folder_contents(folder_path)
    
    for directory in folder_directories:
        args.input_folder = os.path.join(folder_path, directory)
        rename_action(args)

    # Check all filename have the same extension
    file_extensions = set([os.path.splitext(filename)[1] for filename in folder_filenames])
    if len(file_extensions) > 1:
        raise ValueError(f'Folder {folder_path} contains files with '
            f'different extensions: {file_extensions}. Please make sure '
            f'all files have the same extension.')

    folder_filenames.sort()
    n = len(folder_filenames) if len(folder_filenames) >= 10**5 else 5
    print(f'Renaming {len(folder_filenames)} files in {folder_path}')
    for i, filename in enumerate(tqdm(folder_filenames)):
        # Get the file extension
        file_extension = os.path.splitext(filename)[1]
        # Get name of the folder, not the full path
        folder_name = folder_path.split('/')[-1]
        # Create the new filename
        new_filename = f'{folder_name}-{i+1:0{n}}{file_extension}'
        # Rename the file
        os.rename(os.path.join(folder_path, filename), os.path.join(folder_path, new_filename))    

    print('Renaming complete')


def gui_action(args):
    from pyaligner.scripts.gui import PyalignerGUI
    app = QApplication(sys.argv)
    gui = PyalignerGUI()
    gui.show()
    sys.exit(app.exec_())


def main():
    parser = argparse.ArgumentParser(prog='pyaligner', description='Pyaligner command line interface')
    subparsers = parser.add_subparsers(title='subcommands', dest='subcommand')

    # Help menu for 'align' subcommand
    align_parser = subparsers.add_parser('align', 
        help='Align audio with corresponding transcription files')
    align_parser.add_argument('input_folder', 
        help='Input folder containing audio and transcription files')
    align_parser.add_argument('language', 
        help='Language to use for alignment. Check '
        'https://mfa-models.readthedocs.io/en/latest/dictionary/index.html#dictionary '
        'for a list of available dictionaries and \n'
        'https://mfa-models.readthedocs.io/en/latest/acoustic/index.html#acoustic '
        'for a list of available acoustic models')
    align_parser.add_argument('--verbose', action='store_true', 
        help='Print MFA verbose output')
    align_parser.add_argument('--overwrite', action='store_true',
        help='Overwrite existing files')
    
    align_parser.set_defaults(func=align_action)

    # Help menu for 'auto' subcommand
    auto_parser = subparsers.add_parser('auto', 
        help='Transcribe audio files and align them with the created transcriptions')
    auto_parser.add_argument('input_folder', 
        help='Input folder containing files')
    auto_parser.add_argument('--language',
        help='Language to use for alignment. Check '
        'https://mfa-models.readthedocs.io/en/latest/dictionary/index.html#dictionary '
        'for a list of available dictionaries and \n'
        'https://mfa-models.readthedocs.io/en/latest/acoustic/index.html#acoustic '
        'for a list of available acoustic models')
    auto_parser.set_defaults(func=auto_action)

    gui_parser = subparsers.add_parser('gui', 
        help='Start the graphical user interface')
    gui_parser.set_defaults(func=gui_action)


    # Help menu for 'rename' subcommand
    rename_parser = subparsers.add_parser('rename', 
        help='Rename files in a directory to folder names + file number pattern (e.g. folder1_001.wav)')
    rename_parser.add_argument('input_folder', 
        help='Input directory containing files to rename')
    rename_parser.set_defaults(func=rename_action)

    # Help menu for 'transcribe' subcommand
    transcribe_parser = subparsers.add_parser('transcribe', 
        help='Transcribe audio files')
    transcribe_parser.add_argument('input_folder', 
        help='Input folder containing audio files')
    transcribe_parser.set_defaults(func=transcribe_action)

    args = parser.parse_args()
    if not vars(args) or not hasattr(args, 'func'):
        parser.print_help()
    else:
        args.func(args)

if __name__ == '__main__':
    main()
