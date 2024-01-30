import gymnasium as gym
from gymnasium.wrappers import RecordVideo

from Agent import Agent

env = gym.make("CartPole-v1", render_mode="rgb_array")
env = RecordVideo(env, "videos", name_prefix="expert")

agent = Agent()

observation, info = env.reset()
done = False
score = 0

while not done:
    action = agent(observation)

    observation, reward, terminated, truncated, info = env.step(action)
    score += reward
    env.render()

    if terminated or truncated:
        done = True

print(f"Score: {score}")

