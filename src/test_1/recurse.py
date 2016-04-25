# -*- coding: UTF-8 -*-
legal_actions = (
				(-1, 1, 15, -1),
				(-1, 2, -1, 0),
				(-1, -1, 3, 1),
				(2, 4, 7, 15),
				(-1, -1, 5, 3),
				(4, -1, 6, -1),
				(5, -1, -1, 7),
				(3, 6, 8, 11),
				(7, -1, -1, 9),
				(-1, 8, -1, 10),
				(11, 9, -1, -1),
				(15, 7, 10, 12),
				(13, 11, -1, -1),
				(14, -1, 12, -1),
				(-1, 15, 13, -1),
				(0, 3, 11, 14),
				)

def route_cal(start_pos, steps, neighbours, last_poses = {}, route_all = []):
	last_poses[steps] = start_pos
	dest_all = list(neighbours[start_pos])
	
	steps -= 1
	
	if len(last_poses) >= 2:
		for pos in dest_all:
			if pos == last_poses[steps+2]:
				dest_all.remove(pos)
				
	if steps > 0:
		for pos in dest_all:
			if pos != -1:
				route_cal(pos, steps, neighbours)
		return route_all
	elif steps == 0:
		for dest in dest_all:
			if dest != -1:
				last_poses[steps] = dest
				route_all.append(last_poses.copy())
		return route_all


routelines = route_cal(0, 4, legal_actions)
for routeline in routelines:
	print routeline