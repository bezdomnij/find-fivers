import argparse
from typing import Any


class ArgsNamespace(argparse.Namespace):

    def __init__(self, **kwargs: Any):
        super().__init__(**kwargs)
        self.filename = "lorem2.txt"
