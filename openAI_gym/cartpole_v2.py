import gym

env = gym.make('CartPole-v0')

for i in range(10):
    observation = env.reset()
    for t in range(1000):
        env.render()

        action = 0
        if observation[2]>0:
            action = 1
        #observation, reward, done, info = env.step(env.action_space.sample())
        observation, reward, done, info = env.step(action)
        if done:
            print("Episode{} finished after {} timesteps".format(i, t+1))
            break
env.close()