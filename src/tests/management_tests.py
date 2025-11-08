import os

from octobot.configuration_manager import init_config
from octobot_commons.constants import CONFIG_FILE
from octobot_commons.tests.test_config import TEST_CONFIG_FOLDER


def get_fake_config_path():
    return os.path.join(TEST_CONFIG_FOLDER, f"test_{CONFIG_FILE}")


def test_init_config():
    config_path = get_fake_config_path()
    if os.path.isfile(config_path):
        os.remove(config_path)

    init_config(config_file=config_path, from_config_file=os.path.join(TEST_CONFIG_FOLDER, CONFIG_FILE))
    assert os.path.isfile(config_path)
    os.remove(config_path)
