import random

class Agent():
    def __init__(self, agent_type: str = "expert"):
        self.agent_type = agent_type

    def random(self, observation):
        return random.randint(0, 1)

    def right(self, observation):
        return 1

    def left(self, observation):
        return 0

    def moderate(self, observation):
        return int(observation[2] > 0)

    def expert(self, observation):
        if observation[2] > 0:
            if observation[2] > .12 or observation[3] > -0.3:
                return 1
            else:
                return 0
        else:
            if observation[2] < -0.12 or observation[3] < 0.3:
                return 0
            else:
                return 1

    def __call__(self, observation):
        match self.agent_type:
            case "random":
                return self.random(observation)
            case "right":
                return self.right(observation)
            case "left":
                return self.left(observation)
            case "moderate":
                return self.moderate(observation)
            case "expert":
                return self.expert(observation)