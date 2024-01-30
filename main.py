import gymnasium as gym

from Agent import Agent

env = gym.make("CartPole-v1", render_mode="human")
agent = Agent()
total_score = 0

episodes = 20
for episode in range(episodes):
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

    print(f"Episode: {episode}, Score: {score}")
    total_score += score

env.close()

print(f"Average Score: {total_score/episodes}")