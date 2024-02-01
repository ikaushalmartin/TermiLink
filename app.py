from flask import Flask
import paramiko

app = Flask(__name__)

@app.route('/')
def shell_access():
    hostname = "192.168.1.44"
    prt = 22
    user = "martin"
    passwrd = "1234"

    try:
        client = paramiko.SSHClient()
        client.load_system_host_keys()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(hostname, port=prt, username=user, password=passwrd)

        while True:
            try:
                cmd = input("$> ")
                if cmd == "exit":
                    break
                stdin, stdout, stderr = client.exec_command(cmd)
                output = stdout.read().decode()
                print(output)

            except KeyboardInterrupt:
                break

        client.close()
        return output

    except Exception as err:
        print(str(err))
        return str(err)

if __name__ == "__main__":
    app.run(debug=True)
