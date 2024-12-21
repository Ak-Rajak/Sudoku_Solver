from flask import Flask , render_template,request,jsonify , url_for
from logic import sudokuSolver

app = Flask(__name__ , static_folder='static', template_folder='templates')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/solve',methods = ['POST'])
def solve():
    try:
        data = request.get_json()
        board = data['board']

        # Validate the imput
        if not isinstance(board, list) or len(board) != 9:
            return jsonify({"error":"Invalid board format"}), 400
        
        for row in board:
            if not isinstance(row, list) or len(row) != 9:
                return jsonify({"error":"Invalid board format"}), 400
            
        solution = sudokuSolver(board)
        if solution == "No":
            return jsonify({"error":"No solution exists for this sudoku"}), 400
        
        return jsonify({"solution":solution}), 200
    except Exception as e:
        return jsonify({"error":str(e)}), 500
    
if __name__ == '__main__':
    app.run(debug=True)

