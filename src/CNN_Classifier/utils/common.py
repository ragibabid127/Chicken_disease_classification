import os
from box.exceptions import BoxValueError
import yaml
from CNN_Classifier.utils.logger import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
import base64

@ensure_annotations
def read_yaml(path: Path) -> ConfigBox:
    """"
    Reads a yaml file and returns a ConfigBox object.

    Args:
        path (Path): Path to the yaml file.
    
    Raises: 
        BoxValueError: If the yaml file is empty.
        Exception: otherwise.

    Returns:
        ConfigBox: ConfigBox object.
    """
    try:
        with open(path, 'r') as f:
            content = yaml.safe_load(f)
            logger.info(f"Read {path}")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e
    
@ensure_annotations
def create_directory(path_list: list, verbose=True) -> None:
    """
    Creates directories according to path_list.

    Args:
        path_list (list): List of directories to create
        verbose (bool, optional): If true writes in logs. Defaults to True.
    """
    for path in path_list:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Directory {path} created")
            
@ensure_annotations
def save_json(path: Path, data: dict) -> None:
    """
    Saves a json file at specified path.

    Args:
        path (Path): Path to save file at.
        data (dict): Data to save in json file. Must be a dictionary.
    """        
    with open(path, 'w') as f:
        json.dump(data, f, indent=4)
    logger.info(f"Saved data at {path}")
    

@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """
    Loads from a json file at specified path.

    Args:
        path (Path): path to json file.

    Returns:
        ConfigBox: _description_
    """    
    with open(path, 'r') as f:
        content = json.load(f)
    logger.info(f"Loaded data from {path}")
    return ConfigBox(content)

@ensure_annotations
def save_yaml(path: Path, data: dict) -> None:
    """
    Saves a yaml file at specified path.

    Args:
        path (Path): Path for saving file at.
        data (dict): Data to save in yaml file. Must be a dictionary.
    """    
    with open(path, 'w') as f:
        yaml.safe_dump(data, f)
    logger.info(f"Saved data at {path}")
    
@ensure_annotations
def save_bin(path: Path, data: Any) -> None:
    """
    Saves a binary file at specified path.

    Args:
        path (Path): Path for saving file at.
        data (Any): Data to be saved.
    """    
    joblib.dump(value=data, filename=path)
    logger.info(f"Saved data as binary at {path}")
    

@ensure_annotations
def load_bin(path: Path) -> Any:
    """
    Loads a binary file from specified path.

    Args:
        path (Path): Path to bin file

    Returns:
        Any: _description_
    """    
    data=joblib.load(path)
    logger.info(f"Loaded data from {path}")
    return data


@ensure_annotations
def get_size(path: Path) -> float:
    """
    Gets the size of a file in kilobytes.

    Args:
        path (Path): Path to file.

    Returns:
        float: File size in kilobytes.
    """    
    size = round(os.path.getsize(path)/1024)
    print(f"Size of {path} is {size} KB")
    return size


@ensure_annotations
def encode_base64(path: Path) -> Any:
    """
    Encodes a file to base64.

    Args:
        path (Path): Path to read file from

    Returns:
        Any: file data as a Binary string
    """    
    with open(path, 'rb') as f:
        return base64.b64encode(f.read())
    

@ensure_annotations
def decode_base64(binstring, path: Path):
    data=base64.b64decode(binstring)
    with open(path, 'wb') as f:
        f.write(data)
    logger.info(f"Saved at {path}")