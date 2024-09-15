from flask import Flask, jsonify
import subprocess

app = Flask(__name__)

def get_maze_from_c():
    # Running the C program to generate the maze
    result = subprocess.run(['./maze'], stdout=subprocess.PIPE)
    maze_output = result.stdout.decode('utf-8').splitlines()
    return maze_output

@app.route('/api/maze', methods=['GET'])
def get_maze():
    maze = get_maze_from_c()
    return jsonify(maze)

if __name__ == '__main__':
    app.run(debug=True)

