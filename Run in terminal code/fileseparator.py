import os,shutil

dict_extension={
    'Audio_extension':('.mp3','.m4a','.wav','.flac','.aac','.wav','.wma'),
    'Video_extension':('.mp4','.mov','.wmv','.avi','.avchd','.flv','.f4v','.swf','.mkv','.webm','mpeg-2'),
    'Document_extension':('.doc','.docx','.pdf','.txt','.pptx','.htm','.odt','.xls','.xlsx','.ods','.ppt','.webp'),
    'Coding_extension':('.py','.js','.css','.html','.cpp','.c','.java'),
    'Image_extension':('.jpg','.png','.jpeg','.RAW','.gif','.tiff','.psd','.eps','.ai','.ind'),
    'Compressed_extension':('.zip','.rar')
}

folderpath=input("Enter the folder path: ")

def file_finder(folder_path,file_extension):
    files=[]
    for file in os.listdir(folder_path):
        for extension in file_extension:
            if file.endswith(extension):
                files.append(file)
    return files


for extension_type,extension_tuple in dict_extension.items():
    folder_name=extension_type.split('_')[0]+'Files'
    folder_path=os.path.join(folderpath,folder_name)
    if os.path.exists(folder_path):
        print(f"\'{folder_name}\' FOLDER ALREADY EXISTS")
        while True:
            given_folder=input(f"Enter a new folder to write in \'{folder_name}\' folder:-  ")
            folder_path=os.path.join(folder_path,given_folder)
            if os.path.exists(folder_path):
                print(f"\'{given_folder}\' folder also already exists")
            else:
                os.mkdir(folder_path)
                break
    else:
        os.mkdir(folder_path)
    for items in file_finder(folderpath,extension_tuple):
        item_path=os.path.join(folderpath,items)
        item_new_path=os.path.join(folder_path,items)
        shutil.move(item_path,item_new_path)


