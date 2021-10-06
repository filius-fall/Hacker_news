import pytest
import os

from Hackerjobs.main import move_file_to_config
from testfixtures import tempdir, compare,TempDirectory


def test_move_file_to_config():
    dir = TempDirectory()
    path = "tok.json"
    des = "/home/filius-fall/.config/hackerjobs/tok.json"
    dir.write(path,b'testing')

    move_file_to_config(path)
    compare(dir.read(path),dir.read(des))
    os.remove(dir)
    dir.cleanup()