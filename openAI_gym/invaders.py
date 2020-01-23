import gym
import matplotlib.pyplot as plt

env = gym.make('SpaceInvaders-v0')
observation = env.reset()
for t in range(1000):
    #env.render()
    observation, reward, done, info = env.step(env.action_space.sample())
    if reward>0:
        print("STEP_"+str(t)+" Reward:"+str(reward))
        plt.imshow(observation)
        plt.show()
env.close()