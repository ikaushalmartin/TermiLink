import paramiko

def ssh_into_server(hostname, port, username, password, command):
    try:
         
        ssh_client = paramiko.SSHClient()
        # Automatically add the server's host key
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        
        # Connect to the server
        ssh_client.connect(hostname, port=port, username=username, password=password)

        # Run the command on the remote server
        stdin, stdout, stderr = ssh_client.exec_command(command)

        # Print the command output
        print("Command output:\n", stdout.read().decode("utf-8"))

    except Exception as e:
        print(f"Error: {e}")
    finally:
        # Close the SSH connection
        ssh_client.close()

# Replace these values with your server details
hostname = "192.168.1.44"
port = 22  # Default SSH port is 22
username = "martin"
password = "1234"

# Example command to run on the remote server
command_to_run = "ls"

# SSH into the server and run the command
ssh_into_server(hostname, port, username, password, command_to_run)
