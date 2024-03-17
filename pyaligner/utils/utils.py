import os

# Get a list of filenames and directories in the folder

def get_folder_contents(folder_path):
    folder_contents = os.listdir(folder_path)
    folder_filenames = [filename for filename in folder_contents 
                        if os.path.isfile(os.path.join(folder_path, filename))]
    folder_directories = [directory for directory in folder_contents 
                            if os.path.isdir(os.path.join(folder_path, directory))]
    return folder_filenames, folder_directories

def get_correct_path(path):
    # Get full path of the folder
    path = os.path.abspath(path)
    # If folder_path ends with a slash, remove it
    path = path[:-1] if path.endswith('/') else path
    return path



mfa_languages = [
    'abkhaz_cv', 'armenian_cv', 'bashkir_cv', 'basque_cv', 'belarusian_cv', 
    'bulgarian_cv', 'bulgarian_mfa', 'chuvash_cv', 'croatian_mfa', 'czech_cv', 
    'czech_mfa', 'dutch_cv', 'english_india_mfa', 'english_mfa', 
    'english_nigeria_mfa', 'english_uk_mfa', 'english_us_arpa', 
    'english_us_mfa', 'french_mfa', 'french_prosodylab', 'georgian_cv', 
    'german_mfa', 'german_prosodylab', 'greek_cv', 'guarani_cv', 'hausa_mfa', 
    'hindi_cv', 'hungarian_cv', 'indonesian_cv', 'italian_cv', 'japanese_mfa', 
    'kazakh_cv', 'korean_jamo_mfa', 'korean_mfa', 'kurmanji_cv', 'kyrgyz_cv', 
    'maltese_cv', 'mandarin_china_mfa', 'mandarin_erhua_mfa', 'mandarin_mfa', 
    'mandarin_pinyin', 'mandarin_taiwan_mfa', 'polish_cv', 'polish_mfa', 
    'portuguese_brazil_mfa', 'portuguese_cv', 'portuguese_mfa', 
    'portuguese_portugal_mfa', 'punjabi_cv', 'romanian_cv', 'russian_cv', 
    'russian_mfa', 'sorbian_upper_cv', 'spanish_latin_america_mfa', 
    'spanish_mfa', 'spanish_spain_mfa', 'swahili_mfa', 'swedish_cv', 
    'swedish_mfa', 'tamil_cv', 'tatar_cv', 'thai_cv', 'thai_mfa', 
    'turkish_cv', 'turkish_mfa', 'ukrainian_cv', 'ukrainian_mfa', 'urdu_cv', 
    'uyghur_cv', 'uzbek_cv', 'vietnamese_cv', 'vietnamese_hanoi_mfa', 
    'vietnamese_ho_chi_minh_city_mfa', 'vietnamese_hue_mfa', 'vietnamese_mfa'
]