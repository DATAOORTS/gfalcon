import os
import json
import subprocess
import tempfile
import threading

def run_code_snippet(snippet):
    with tempfile.NamedTemporaryFile(delete=False, suffix=get_extension(snippet['language'])) as temp_file:
        temp_file.write(snippet['code'].encode())
        temp_file_name = temp_file.name

    try:
        command = None
        if snippet['language'] == 'python':
            command = f"python {temp_file_name}"
        elif snippet['language'] == 'c++':
            compile_command = f"g++ {temp_file_name} -o {temp_file_name}.out"
            subprocess.run(compile_command, shell=True, check=True)
            command = f"{temp_file_name}.out"
        elif snippet['language'] == 'javascript':
            command = f"node {temp_file_name}"
        elif snippet['language'] == 'go':
            command = f"go run {temp_file_name}"
        elif snippet['language'] == 'c':
            compile_command = f"gcc {temp_file_name} -o {temp_file_name}.out"
            subprocess.run(compile_command, shell=True, check=True)
            command = f"{temp_file_name}.out"
        elif snippet['language'] == 'r':
            command = f"Rscript {temp_file_name}"
        elif snippet['language'] == 'c#':
            command = f"dotnet run --project {temp_file_name}"
        elif snippet['language'] == 'php':
            command = f"php {temp_file_name}"
        elif snippet['language'] == 'java':
            compile_command = f"javac {temp_file_name}"
            subprocess.run(compile_command, shell=True, check=True)
            command = f"java {temp_file_name}"
        elif snippet['language'] == 'ruby':
            command = f"ruby {temp_file_name}"
        elif snippet['language'] == 'mojo':
            command = f"mojo {temp_file_name}"
        elif snippet['language'] == 'bash':
            command = f"bash {temp_file_name}"
        elif snippet['language'] == 'scala':
            command = f"scala {temp_file_name}"
        elif snippet['language'] == 'codon':
            command = f"codon run -release {temp_file_name}"
        elif snippet['language'] == 'elixir':
            command = f"elixir {temp_file_name}"
        elif snippet['language'] == 'cobol':
            compile_command = f"cobc -x -o {temp_file_name}.out {temp_file_name}"
            subprocess.run(compile_command, shell=True, check=True)
            command = f"{temp_file_name}.out"
        elif snippet['language'] == 'node.js':
            command = f"node {temp_file_name}"
        elif snippet['language'] == 'fortran':
            compile_command = f"gfortran {temp_file_name} -o {temp_file_name}.out"
            subprocess.run(compile_command, shell=True, check=True)
            command = f"{temp_file_name}.out"
        elif snippet['language'] == 'typescript':
            command = f"ts-node {temp_file_name}"
        else:
            print(f"Unsupported language: {snippet['language']}")
            return

        if command:
            result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
            print(result.stdout)

    except subprocess.CalledProcessError as e:
        print(f"Error executing {snippet['language']} code: {e}")

def get_extension(language):
    extensions = {
        'python': '.py',
        'c++': '.cpp',
        'c': '.c',
        'r': '.r',
        'c#': '.cs',
        'go': '.go',
        'php': '.php',
        'java': '.java',
        'ruby': '.rb',
        'mojo': '.mojo',
        'bash': '.sh',
        'scala': '.scala',
        'codon': '.py',
        'elixir': '.ex',
        'cobol': '.cob',
        'node.js': '.js',
        'fortran': '.f90',
        'javascript': '.js',
        'typescript': '.ts',
    }
    return extensions.get(language, '')

def execute_code(json_payload):
    data = json.loads(json_payload)  # Load the JSON payload
    
    # Set environment variables from params using subprocess
    for key, value in data['params'].items():
        subprocess.run(f"jifer {key}={value}", shell=True, check=True)

    threads = []

    for snippet in data['gfalcon']:
        if snippet['follow'] == 'serial':
            run_code_snippet(snippet)
        elif snippet['follow'] == 'parallel':
            thread = threading.Thread(target=run_code_snippet, args=(snippet,))
            threads.append(thread)
            thread.start()

    for thread in threads:
        thread.join()

    # Print the RESULT environment variable
    #result = subprocess.run("printenv RESULT", shell=True, capture_output=True, text=True).stdout.strip()
    result = os.getenv('RESULT')
    print(f"RESULT: {result}")
