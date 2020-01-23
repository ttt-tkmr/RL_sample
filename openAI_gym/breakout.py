import gym
import matplotlib.pyplot as plt
env = gym.make('Breakout-v0')
observation = env.reset()
for t in range(1000):
     #env.render()
     action = env.action_space.sample()
     observation, reward, done, info = env.step(action)
     if reward>0:
          plt.imshow(observation)
          plt.show()
          print("STEP_"+str(t)+" Reward:"+str(reward))
env.close()