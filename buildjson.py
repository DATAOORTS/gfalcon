import json

# Define individual code snippets
code1 = """
import numpy as np

def expensive_computation(matrix_size=1000):
    # Generate two large random matrices of the specified size
    A = np.random.rand(matrix_size, matrix_size)
    B = np.random.rand(matrix_size, matrix_size)
    
    # Perform matrix multiplication
    result = np.dot(A, B)
    
    return result

# Example usage
output = expensive_computation(4000)  # This will multiply two 2000x2000 matrices
print("Computation completed python for 4000.")
"""

code2 = """
#include <iostream>
#include <vector>
#include <cstdlib>
#include <ctime>

// Function to multiply two matrices
std::vector<std::vector<double>> matrixMultiply(const std::vector<std::vector<double>>& A, const std::vector<std::vector<double>>& B) {
    int n = A.size();
    std::vector<std::vector<double>> result(n, std::vector<double>(n, 0.0));
    
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            for (int k = 0; k < n; ++k) {
                result[i][j] += A[i][k] * B[k][j];
            }
        }
    }
    
    return result;
}

// Function to generate a random matrix
std::vector<std::vector<double>> generateRandomMatrix(int n) {
    std::vector<std::vector<double>> matrix(n, std::vector<double>(n));
    
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            matrix[i][j] = static_cast<double>(rand()) / RAND_MAX;
        }
    }
    
    return matrix;
}

int main() {
    int matrix_size = 900; // Adjust the matrix size as needed

    // Seed random number generator
    std::srand(std::time(0));
    
    // Generate two large random matrices
    std::vector<std::vector<double>> A = generateRandomMatrix(matrix_size);
    std::vector<std::vector<double>> B = generateRandomMatrix(matrix_size);
    
    // Perform matrix multiplication
    std::vector<std::vector<double>> result = matrixMultiply(A, B);
    
    std::cout << "Computation completed c++ for 900." << std::endl;

    return 0;
}
"""
code3 = """
#include <iostream>
#include <vector>
#include <cstdlib>
#include <ctime>

// Function to multiply two matrices
std::vector<std::vector<double>> matrixMultiply(const std::vector<std::vector<double>>& A, const std::vector<std::vector<double>>& B) {
    int n = A.size();
    std::vector<std::vector<double>> result(n, std::vector<double>(n, 0.0));
    
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            for (int k = 0; k < n; ++k) {
                result[i][j] += A[i][k] * B[k][j];
            }
        }
    }
    
    return result;
}

// Function to generate a random matrix
std::vector<std::vector<double>> generateRandomMatrix(int n) {
    std::vector<std::vector<double>> matrix(n, std::vector<double>(n));
    
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            matrix[i][j] = static_cast<double>(rand()) / RAND_MAX;
        }
    }
    
    return matrix;
}

int main() {
    int matrix_size = 700; // Adjust the matrix size as needed

    // Seed random number generator
    std::srand(std::time(0));
    
    // Generate two large random matrices
    std::vector<std::vector<double>> A = generateRandomMatrix(matrix_size);
    std::vector<std::vector<double>> B = generateRandomMatrix(matrix_size);
    
    // Perform matrix multiplication
    std::vector<std::vector<double>> result = matrixMultiply(A, B);
    
    std::cout << "Computation completed c++ for 700." << std::endl;

    return 0;
}
"""
code4 = """
import numpy as np

def expensive_computation(matrix_size=1000):
    # Generate two large random matrices of the specified size
    A = np.random.rand(matrix_size, matrix_size)
    B = np.random.rand(matrix_size, matrix_size)
    
    # Perform matrix multiplication
    result = np.dot(A, B)
    
    return result

# Example usage
output = expensive_computation(3000)  # This will multiply two 2000x2000 matrices
print("Computation completed python for 3000.")
"""
# Define the JSON structure
payload = {
    "auth_token": "your_auth_token_here",
    "machine": "cpu/gpu",
    "params": {
        "X_VALUE": "value1",
        "Y_VALUE": "value2",
        "Z_Value": "value3"
    },
    "gfalcon": [
        { 
            "follow": "serial",
            "language": "python",
            "code": code1
        },
        { 
            "follow": "parallel",
            "language": "c++",
            "code": code2
        },
        { 
            "follow": "serial",
            "language": "c++",
            "code": code3
        },
        { 
            "follow": "parallel",
            "language": "python",
            "code": code4
        }
    ]
}

# Serialize to JSON with indentation for readability
json_payload = json.dumps(payload, indent=2)
