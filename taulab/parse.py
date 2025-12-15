import os
import re
import pandas as pd
from pathlib import Path
from taulab.datatypes import ParseResult
from collections.abc import Callable


def parse_excel_folder(
    folder: str | os.PathLike | Path,
    filename_pattern: str | None = None,
    index_col: int | None = None,
) -> list[ParseResult]:
    """Parse a folder of excel files. It is assumed all files within the folder are excel
    files. Non-files are skipped. This function is useful when there are many automated
    measurements and their filenames fit a specific pattern, it allows the user to match
    a regex pattern to the filenames and return a group dictionary with each result.

    :param folder: Folder to look for files in
    :type folder: str | os.PathLike | Path
    :param filename_pattern: Optional filenames regex pattern, defaults to None
    :type filename_pattern: str | None, optional
    :param index_col: Optionally specify a column that is to be used as indices, similar
        to the pandas argument by the same name, defaults to None
    :type index_col: int | None, optional
    :return: Returns a list of ParseResult, each containing the dataframe corresponding
        to the excel table and metadata corresponding to the regex group dict if a pattern
        was supplied and matched
    :return type: list[ParseResult]
    """
    return _parse_folder_internal(pd.read_excel, folder, filename_pattern, index_col)


def parse_csv_folder(
    folder: str | os.PathLike | Path,
    filename_pattern: str | None = None,
    index_col: int | None = None,
) -> list[ParseResult]:
    """Parse a folder of csv files. It is assumed all files within the folder are csv
    files. Non-files are skipped. This function is useful when there are many automated
    measurements and their filenames fit a specific pattern, it allows the user to match
    a regex pattern to the filenames and return a group dictionary with each result.

    :param folder: Folder to look for files in
    :type folder: str | os.PathLike | Path
    :param filename_pattern: Optional filenames regex pattern, defaults to None
    :type filename_pattern: str | None, optional
    :param index_col: Optionally specify a column that is to be used as indices, similar
        to the pandas argument by the same name, defaults to None
    :type index_col: int | None, optional
    :return: Returns a list of ParseResult, each containing the dataframe corresponding
        to the csv table and metadata corresponding to the regex group dict if a pattern
        was supplied and matched
    :return type: list[ParseResult]
    """
    return _parse_folder_internal(pd.read_csv, folder, filename_pattern, index_col)


def _parse_folder_internal(
    parse_function: Callable[..., pd.DataFrame],
    folder: str | os.PathLike | Path,
    filename_pattern: str | None = None,
    index_col: int | None = None,
) -> list[ParseResult]:
    folder = Path(folder)
    results = []
    compiled_pattern = re.compile(filename_pattern) if filename_pattern else None
    for file in folder.iterdir():
        # Skip if not file
        if not file.is_file():
            continue

        metadata = {}
        # Handle regex pattern if supplied
        if compiled_pattern:
            result = compiled_pattern.match(file.name)
            if result:
                metadata = result.groupdict()
            else:
                # if file pattern is given, skip non-matching files
                continue

        # Read data and convert to DataFrame
        parse_result = ParseResult(parse_function(file, index_col=index_col), metadata)

        # If this raises, we let it propagate
        results.append(parse_result)

    # Return empty list if no files found
    return results
