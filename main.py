import os


def bulk_rename_img(directory, prefix, extension=".jpg"):
    for num, filename in enumerate(os.listdir(directory), start=1):
        if filename.endswith(extension):
            os.rename(os.path.join(directory, filename), os.path.join(directory, f"{prefix}-{num}{extension}"))


if __name__ == "__main__":
    # define your directory here, the prefix for new filenames, and the file extension.
    directory = "add path here"
    prefix = "data-analysis"
    extension = ".jpg"

    bulk_rename_img(directory, prefix, extension)
