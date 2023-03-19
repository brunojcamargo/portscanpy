import socket
from tqdm import tqdm
import click

@click.command()
@click.option('--type', prompt='F for all ports or C for common ports', type=click.Choice(['f', 'c']))
def menu(type):
    host = input("Enter the host to scan: ")
    click.echo(f'Run on host {host}')
    if(type == 'f'):
        scannFull(host)
    else:
        scannCommon(host)

def scanner(port, host):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.0000033)
    result = s.connect_ex((host, port))
    if result == 0:
        print(f"\n Port {port} is open ")

    s.close()

def scannFull(host):
    for port in tqdm(range(1, 65535)):
        scanner(port, host)

def scannCommon(host):
    with open('ports.txt', 'r') as file:
        for line in tqdm(file):
            scanner(int(line.strip()),host)

if __name__ == '__main__':
    menu()