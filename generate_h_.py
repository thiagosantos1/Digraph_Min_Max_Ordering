# generate all combinations, for pais, for all vertecies in graph
def generate_combinations(file_name, file_out):
	try:
		graph_file = open(file_name, 'r')
	except IOError as exc:
		print("Failure opening file " + str(file_name) )
		sys.exit(2)

	num_vertices = int(graph_file.readline())
	
	num_pairs = (num_vertices * num_vertices) - num_vertices
	try:
		pais_out = open(file_out, "w")
	except IOError as exc:
		print("Failure creating file " + str(file_out) )
		sys.exit(2)

	pais_out.write(str(num_pairs) + "\n")
	for x in range(num_vertices -1):
		for y in range(x+1,num_vertices):
			pais_out.write(str(x) + " " + str(y) + "\n" )
			pais_out.write(str(y) + " " + str(x))
			if x < num_vertices-2:
				pais_out.write("\n")

def main(file_name, file_out):
	generate_combinations(file_name,file_out)

if __name__ == '__main__':
	main("graph_h.txt", "pairs.txt")

