from flask import Flask, redirect , render_template , request 
import subprocess , re
app = Flask(__name__)


@app.route("/", methods=['GET' , 'POST'])
def main():
    if request.method == 'POST':
        pass
    return render_template('index.html')

@app.route("/result")

def get_address():
    output = subprocess.check_output('ipconfig', shell=True, text=True)
    pattern = r'IPv4 Address[ .]*: (\d+\.\d+\.\d+\.\d+)'
    address = re.findall(pattern, output)
    return address[-1]

if __name__ == "__main__":
    app.run(debug=True, host=get_address())
