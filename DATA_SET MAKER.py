from capture import CaptureCube
from copy import deepcopy

class Node:
	def __init__(self, action = None,state = {},prev = None):
		self.prev = prev
		self.action = action
		if action == None:
			self._state = {'U': [['w', 'w', 'w'],
				 ['w', 'w', 'w'],
				 ['w', 'w', 'w']],
		   'D': [['y', 'y', 'y'],
				 ['y', 'y', 'y'],
				 ['y', 'y', 'y']],
		   'F': [['r', 'r', 'r'],
				 ['r', 'r', 'r'],
				 ['r', 'r', 'r']],
		   'B': [['o', 'o', 'o'],
				 ['o', 'o', 'o'],
				 ['o', 'o', 'o']],
		   'L': [['g', 'g', 'g'],
				 ['g', 'g', 'g'],
				 ['g', 'g', 'g']],
		   'R': [['b', 'b', 'b'],
				 ['b', 'b', 'b'],
				 ['b', 'b', 'b']]}		
		else:
			self._state = deepcopy(state)

		CLOCKWISE = {'+': {
									(0, 0): (0, 2),
									(0, 1): (1, 2),
									(0, 2): (2, 2),
									(1, 0): (0, 1),
									(1, 1): (1, 1),
									(1, 2): (2, 1),
									(2, 0): (0, 0),
									(2, 1): (1, 0),
									(2, 2): (2, 0)
								},
								'-': {
									(0, 0): (2, 0),
									(0, 1): (1, 0),
									(0, 2): (0, 0),
									(1, 0): (2, 1),
									(1, 1): (1, 1),
									(1, 2): (0, 1),
									(2, 0): (2, 2),
									(2, 1): (1, 2),
									(2, 2): (0, 2)
								}}		
		
		copy = self.clone_state()

		if action == 'U+':
			self._state['F'][0] = [copy['R'][0][j] for j in range(3)]
			self._state['L'][0] = [copy['F'][0][j] for j in range(3)]
			self._state['B'][0] = [copy['L'][0][j] for j in range(3)]
			self._state['R'][0] = [copy['B'][0][j] for j in range(3)]
			for pos in CLOCKWISE['+']:
				self._state['U'][CLOCKWISE['+'][pos][0]][CLOCKWISE['+'][pos][1]] = copy['U'][pos[0]][pos[1]] 
		elif action == 'U-':
			self._state['F'][0] = [copy['L'][0][j] for j in range(3)]
			self._state['L'][0] = [copy['B'][0][j] for j in range(3)]
			self._state['B'][0] = [copy['R'][0][j] for j in range(3)]
			self._state['R'][0] = [copy['F'][0][j] for j in range(3)]
			for pos in CLOCKWISE['-']:
				self._state['U'][CLOCKWISE['-'][pos][0]][CLOCKWISE['-'][pos][1]] = copy['U'][pos[0]][pos[1]]
		elif action == 'D+':
			self._state['F'][2] = [copy['L'][2][j] for j in range(3)]
			self._state['L'][2] = [copy['B'][2][j] for j in range(3)]
			self._state['B'][2] = [copy['R'][2][j] for j in range(3)]
			self._state['R'][2] = [copy['F'][2][j] for j in range(3)]

			for pos in CLOCKWISE['+']:
				self._state['D'][CLOCKWISE['+'][pos][0]][CLOCKWISE['+'][pos][1]] = copy['D'][pos[0]][pos[1]]
		elif action == 'D-':
			self._state['F'][2] = [copy['R'][2][j] for j in range(3)]
			self._state['L'][2] = [copy['F'][2][j] for j in range(3)]
			self._state['B'][2] = [copy['L'][2][j] for j in range(3)]
			self._state['R'][2] = [copy['B'][2][j] for j in range(3)]

			for pos in CLOCKWISE['-']:
				self._state['D'][CLOCKWISE['-'][pos][0]][CLOCKWISE['-'][pos][1]] = copy['D'][pos[0]][pos[1]]
		elif action == 'F+':
			self._state['U'][2] = [copy['L'][2 - i][2] for i in range(3)]

			self._state['L'][0][2] = copy['D'][0][0]
			self._state['L'][1][2] = copy['D'][0][1]
			self._state['L'][2][2] = copy['D'][0][2]

			self._state['D'][0] = [copy['R'][2 - i][0] for i in range(3)]

			self._state['R'][0][0] = copy['U'][2][0]
			self._state['R'][1][0] = copy['U'][2][1]
			self._state['R'][2][0] = copy['U'][2][2]

			for pos in CLOCKWISE['+']:
				self._state['F'][CLOCKWISE['+'][pos][0]][CLOCKWISE['+'][pos][1]] = copy['F'][pos[0]][pos[1]]
		elif action == 'F-':
			self._state['U'][2] = [copy['R'][i][0] for i in range(3)]

			self._state['R'][0][0] = copy['D'][0][2]
			self._state['R'][1][0] = copy['D'][0][1]
			self._state['R'][2][0] = copy['D'][0][0]

			self._state['D'][0] = [copy['L'][i][2] for i in range(3)]

			self._state['L'][0][2] = copy['U'][2][2]
			self._state['L'][1][2] = copy['U'][2][1]
			self._state['L'][2][2] = copy['U'][2][0]

			for pos in CLOCKWISE['-']:
				self._state['F'][CLOCKWISE['-'][pos][0]][CLOCKWISE['-'][pos][1]] = copy['F'][pos[0]][pos[1]]
		elif action == 'B+':
			self._state['U'][0] = [copy['R'][i][2] for i in range(3)]

			self._state['R'][0][2] = copy['D'][2][2]
			self._state['R'][1][2] = copy['D'][2][1]
			self._state['R'][2][2] = copy['D'][2][0]

			self._state['D'][2] = [copy['L'][i][0] for i in range(3)]

			self._state['L'][0][0] = copy['U'][0][2]
			self._state['L'][1][0] = copy['U'][0][1]
			self._state['L'][2][0] = copy['U'][0][0]

			for pos in CLOCKWISE['+']:
				self._state['B'][CLOCKWISE['+'][pos][0]][CLOCKWISE['+'][pos][1]] = copy['B'][pos[0]][pos[1]]
		elif action == 'B-':
			self._state['U'][0] = [copy['L'][2 - i][0] for i in range(3)]

			self._state['L'][0][0] = copy['D'][2][0]
			self._state['L'][1][0] = copy['D'][2][1]
			self._state['L'][2][0] = copy['D'][2][2]

			self._state['D'][2] = [copy['R'][2 - i][2] for i in range(3)]

			self._state['R'][0][2] = copy['U'][0][0]
			self._state['R'][1][2] = copy['U'][0][1]
			self._state['R'][2][2] = copy['U'][0][2]

			for pos in CLOCKWISE['-']:
				self._state['B'][CLOCKWISE['-'][pos][0]][CLOCKWISE['-'][pos][1]] = copy['B'][pos[0]][pos[1]]
		elif action == 'L+':
			for i in range(3):
				self._state['F'][i][0] = copy['U'][i][0]
				self._state['U'][i][0] = copy['B'][2 - i][2]
				self._state['B'][i][2] = copy['D'][2 - i][0]
				self._state['D'][i][0] = copy['F'][i][0]

			for pos in CLOCKWISE['+']:
				self._state['L'][CLOCKWISE['+'][pos][0]][CLOCKWISE['+'][pos][1]] = copy['L'][pos[0]][pos[1]]
		elif action == 'L-':
			for i in range(3):
				self._state['F'][i][0] = copy['D'][i][0]
				self._state['D'][i][0] = copy['B'][2 - i][2]
				self._state['B'][i][2] = copy['U'][2 - i][0]
				self._state['U'][i][0] = copy['F'][i][0]

			for pos in CLOCKWISE['-']:
				self._state['L'][CLOCKWISE['-'][pos][0]][CLOCKWISE['-'][pos][1]] = copy['L'][pos[0]][pos[1]]
		elif action == 'R+':
			for i in range(3):
				self._state['F'][i][2] = copy['D'][i][2]
				self._state['D'][i][2] = copy['B'][2 - i][0]
				self._state['B'][i][0] = copy['U'][2 - i][2]
				self._state['U'][i][2] = copy['F'][i][2]

			for pos in CLOCKWISE['+']:
				self._state['R'][CLOCKWISE['+'][pos][0]][CLOCKWISE['+'][pos][1]] = copy['R'][pos[0]][pos[1]]
		elif action == 'R-':
			for i in range(3):
				self._state['F'][i][2] = copy['U'][i][2]
				self._state['U'][i][2] = copy['B'][2 - i][0]
				self._state['B'][i][0] = copy['D'][2 - i][2]
				self._state['D'][i][2] = copy['F'][i][2]

			for pos in CLOCKWISE['-']:
				self._state['R'][CLOCKWISE['-'][pos][0]][CLOCKWISE['-'][pos][1]] = copy['R'][pos[0]][pos[1]]

	def clone_state(self):
		copy = {}
		for face in ['U', 'D', 'F', 'B', 'L', 'R']:
			copy[face] = [[self._state[face][i][j] for j in range(3)] for i in range(3)]

		return copy

class Tree:
	global tree
	def __init__(self, actions):
		queue = []
		self.level = 0
		self.root = Node()
		tree.append(self.root)
		queue.append(self.root)
		count = 0
		while len(queue) != 0:
			for e in actions:
				node = Node(e,queue[0]._state,tree.index(queue[0]))
				count+=1
				tree.append(node)
				if self.level < 1:
					queue.append(node)
			queue.pop(0)
			for pow in range(12):
				if 12**pow == count:			
					self.level += 1
		

	def print_cube(self):
		global tree
		for i,j in enumerate(tree):
			print("at ",i )
			print()
			print(j._state)
			print()

if __name__ == '__main__':

	tree = []
	actions = ['U+', 'U-','L+','L-','R+','R-','F+','F-','B+','B-','D+','D-']
	graph = Tree(actions)
	with open('test.txt', 'w') as f:
		for node in tree:
			f.write(f"{node._state}#{node.prev}#{node.action}")
			f.write('\n')



	

