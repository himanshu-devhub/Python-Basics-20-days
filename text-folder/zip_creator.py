import zipfile
import pathlib

def make_archive(filepaths,dest_dir):
    dest_path = pathlib.Path(dest_dir,"compressed.zip")
    with zipfile.ZipFile(dest_path,'w') as archive:
        for filepath in filepaths:
            archive.write(filepath,arcname= filepath.name)
        
if __name__ == "__name__":
    make_archive(filepaths= ["ex-01.py","ex-02.py"],dest_dir= "dest")
