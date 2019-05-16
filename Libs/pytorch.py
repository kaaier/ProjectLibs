import torch 
from torch.autograd import Variable


x=torch.unsqueeze(torch.linspace(-1,1,100),dim=1)
y=x.pow(2)+0.2*torch,randn(x.size())

x,y=Variable(x),Variable(y)


class Net(torch.nn.Module):
	def __init__(self):
		super(Net).__init__()
		self.conv=torch.nn.Sequential(
			torch.nn.Linear(),
			torch.nn.Relu()
			torch.nn.Linear()
			) 

	def forward(x):
		y=self.conv(x)
		return y
net=Net()
optimizer=torch.optim.SGD(net.parameters(),lr=0.5)

loss=torch.nn.MSELoss()
train_step=100
for i in rannge(train_step):
	prediction=net(x)
	loss=loss(prediction,y)
	optimizer.zero_grad()#迭代清空上次的梯度
	loss.backward()#反向传播
	optimizer.step() #更新梯度


#可视化
plt.scatter(x,y)
plt.plot(x,prediction,'r--',lw=5)
plt.show()

#保存模型
torch.save(net,'net.pkl')
net=torch.load('pkl')
#保存参数
torch.save(net.state_dict(),'net.pkl')
net.load_state_dict(torch.load('pkl'))