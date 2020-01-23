import gym
env = gym.make('CarRacing-v0')
observation = env.reset()
for t in range(1000):
    env.render()
    observation, reward, done, info = env.step(env.action_space.sample())
env.close()