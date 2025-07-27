import os
import cv2


def _get_directory() -> list or int:
    """
    Gets the path, corrects bar for windows path and verify dir exists.:
    :return List if found or -1 if not.:
    """

    while True:
        try:
            path = input(r"Enter the directory path: ").replace('\\', '/')
            if path == -1:
                return -1
            assert os.path.isdir(path)

        except AssertionError:
            print("Directory is not a valid path, digit -1 to exit")

        else:
            return path


def _get_list_of_texture_paths(dir_name) -> list:
    """
    Creates a list of the path names from all valid textures in the directory
    :param dir_name:
    :return list:
    """

    list_of_texture_paths = []
    list_of_texture_names = []
    for file_name in os.listdir(dir_name):

        file_path = f'{dir_name}/{file_name}'
        if cv2.haveImageReader(file_path) and cv2.haveImageWriter(file_path):
            print(f'New file: {file_name} \nFound in: {file_path}\n')
            list_of_texture_paths.append(file_path)
            list_of_texture_names.append(file_name)

    return list_of_texture_paths, list_of_texture_names


def _load_textures(path_list) -> list or int:
    """
    Loads textures in a list from a list of paths.
    :param path_list:
    :return list of textures recognized by cv2.imread() method if any, -1 if not:
    """

    texture_list = []
    for path in path_list:
        texture = cv2.imread(path)
        if texture is not None:
            texture_list.append(texture)

    return texture_list if len(texture_list) > 0 else -1


def _make_new_dir(dir_name, intensity) -> bool or str:
    new_dir_name = f'{dir_name}_downsampled_by_{intensity}X'
    try:
        os.makedirs(new_dir_name)
    except OSError:
        return False
    else:
        return new_dir_name


def _get_downsample_factor() -> int:
    """
    Get from user the factor for the downsampling
    :return int specifying the downsampling intensity, or -1 if not:
    """

    while True:
        try:
            factor = int(input('Type the value of the downsample factor (x>0, int): '))
            if factor == -1:
                return -1
            assert factor > 0
        except ValueError:
            print("'factor' is not int, try again.")
        except AssertionError:
            print("'factor' should be greater than zero, try again.")
        else:
            return factor


def _downsample_textures(texture_list, intensity_value) -> list:
    """
    Downsamples textures according to the given intensity value.
    :param texture_list:
    :param intensity_value:
    :return list of downsampled textures:
    """
    textures_to_pyrdown_list = []

    for texture in texture_list:
        for _ in range(intensity_value):
            texture = cv2.pyrDown(src=texture)
        textures_to_pyrdown_list.append(texture)

    return textures_to_pyrdown_list


def _save_new_down_sampled_textures(textures, factor, path_to_save, names_list) -> None:
    """
    Saves new down sampled textures.
    :param textures:
    :param factor:
    :param path_to_save:
    :param names_list:
    :return None:
    """

    for i, texture in enumerate(textures):

        name, extension = names_list[i].split('.')
        cv2.imwrite(
            f'{path_to_save}/{name}_down_sampled_by_{factor}X.{extension}',
            texture
        )


# main
def main():

    print('Python script to downsample textures from a directory or folder.')
    print('Type -1 to exit anytime.')

    dir_name = _get_directory()
    if dir_name == -1:
        exit()

    factor = _get_downsample_factor()
    if factor == -1:
        exit()

    new_dir_path = _make_new_dir(dir_name, factor)
    if new_dir_path is False:
        print('This textures has already been downsampled to this factor')
        exit()

    path_list, names_list = _get_list_of_texture_paths(dir_name)

    textures = _load_textures(path_list)

    if textures == -1:
        print('No textures found in path')
        os.rmdir(new_dir_path)
        exit()

    textures = _downsample_textures(textures, factor)
    _save_new_down_sampled_textures(textures, factor, new_dir_path, names_list)


main()
