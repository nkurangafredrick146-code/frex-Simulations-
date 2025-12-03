import logging
from scene_env import Scene

logging.basicConfig(level=logging.INFO)

if __name__ == "__main__":
    scene = Scene(name="LoggedScene")
    logging.info(scene.render())
