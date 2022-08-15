import pkg_resources


DATA_PATH = pkg_resources.resource_filename("ansible_events_qa", "data/")


def get_data_path(path: str) -> str:
    """
    Returns the absolute path from the default test data path given a relative path
    """
    return DATA_PATH + path
