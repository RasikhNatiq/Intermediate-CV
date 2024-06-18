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


def search(state,level):
	global init
	global path
	global lines
	if state == init:
		return path
	for idx in range(int(12**(level+1)),int((12**(level+2)))+13):
		x = lines[idx]
		str_state = deepcopy(state)
		
		node = x.split("#")
		if node[0] == str(str_state):
			a = correct_path(node[2])[0]
			path.append(a)
			graph = Node(a,state)
			search(graph._state,level-1)
			return path

	
		
def correct_path(path):
	a = []
	if path[1]=='+':
		a.append(path[0]+'-')
	elif path[1]=='-':
		a.append(path[0]+'+')	
	return a

def extract_state(state):
	ext_state = {'U': [],
		   'D': [],
		   'F': [],
		   'B': [],
		   'L': [],
		   'R': []}	
	temp_list = []
	temp_list1 = []
	count = 0
	for key,val in capture_state.items():
		for key1,val1 in val.items():
			temp_list.append(val1)
			count += 1
			if count == 3:
				temp_list1.append(temp_list)
				temp_list = []
				count = 0
		
		ext_state[key] = temp_list1
		temp_list1 = []
	return ext_state

if __name__ == '__main__':

	x = int(input("Enter number of changes made : "))
	capture_cube = CaptureCube()
	capture_cube.capture_cube()
	capture_state = capture_cube._cube
	state = extract_state(capture_state)
	#state1 = {'U': [['o', 'w', 'r'], ['o', 'w', 'r'], ['b', 'b', 'w']], 'D': [['g', 'g', 'o'], ['r', 'y', 'o'], ['r', 'y', 'o']], 'F': [['r', 'r', 'g'], ['r', 'r', 'y'], ['w', 'w', 'y']], 'B': [['b', 'o', 'y'], ['w', 'o', 'y'], ['w', 'o', 'y']], 'L': [['g', 'g', 'w'], ['g', 'g', 'w'], ['g', 'g', 'o']], 'R': [['r', 'y', 'y'], ['b', 'b', 'b'], ['b', 'b', 'b']]}
	init = {'U': [['w', 'w', 'w'],				 ['w', 'w', 'w'],				 ['w', 'w', 'w']],		   'D': [['y', 'y', 'y'],				 ['y', 'y', 'y'],				 ['y', 'y', 'y']],		   'F': [['r', 'r', 'r'],				 ['r', 'r', 'r'],				 ['r', 'r', 'r']],		   'B': [['o', 'o', 'o'],				 ['o', 'o', 'o'],				 ['o', 'o', 'o']],		   'L': [['g', 'g', 'g'],				 ['g', 'g', 'g'],				 ['g', 'g', 'g']],		   'R': [['b', 'b', 'b'],				 ['b', 'b', 'b'],				 ['b', 'b', 'b']]}		
	path = []
	lines = []
	with open('test.txt',"r") as f:
		lines = f.readlines()
	patha = search(state,x,init)
	print(path)



	


