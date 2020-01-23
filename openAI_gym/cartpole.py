import gym
env = gym.make('CartPole-v0')

# 10回テスト
for i in range(10):
    observation = env.reset()
    for t in range(1000):
        env.render() # 描画
        # 盤面の情報, 報酬, 
        observation, reward, done, info = env.step(env.action_space.sample())
        if done:
            print("Episode{} finished after {} timesteps".format(i, t+1))
            break
env.close()