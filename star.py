# Define the size of the matrix
n = 5

# Create a 5x5 matrix filled with stars
matrix = [['*' for _ in range(n)] for _ in range(n)]

# Function to print the matrix
def print_matrix(mat):
    for row in mat:
        print(" ".join(row))

# Call the function to print the matrix
print_matrix(matrix)