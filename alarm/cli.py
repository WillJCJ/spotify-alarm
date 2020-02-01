"""CLI for the controller module using python-fire."""
import fire

from controller import Controller

if __name__ == '__main__':
    fire.Fire(Controller)
