import zipfile
import pathlib

def make_archive(filepaths, dest_dir):
    dest_path = pathlib.Path(dest_dir, "compressed.zip")
    with zipfile.ZipFile(dest_path, 'w') as archive:

        for filepath in filepaths:
            #following is added so that we get the path of the destination location only
            filepath = pathlib.Path(filepath)
            #print(filepath)
            archive.write(filepath, arcname=filepath.name)