import requests
import argparse
import sys

def parse_arguments():
    parser = argparse.ArgumentParser(prog='Reecon-CTI', description='Coleta de informações sobre ameaças')

    parser.add_argument('-t', '--type', type=str, required=True)
    parser.add_argument('-a', '--apikey', type=str, required=True)
    parser.add_argument('-hs', '--hash', type=str, default=" ", required=False)
    parser.add_argument('-i', '--ip', type=str, default=" ", required=False)

    return parser.parse_args()

def requestVT(apikey, hash):
    header = {
        "Accept": "application/json",
        "x-apikey": f"{apikey}"
    }

    try:
        response = requests.get(f"https://www.virustotal.com/api/v3/files/{hash}", headers=header)
    
        if response.status_code == 200:
            with open('VT-CTI.csv', 'wb') as file:
                file.write(response.content)
        else:
            print("Erro ao baixar o arquivo csv!")

    except requests.ConnectionError as error:
        print(error)

def requestCensys(apikey, ip):
    header = {
        "Accept": "application/json",
        "Authorization": f"Basic {apikey}"
    }

    try:
        response = requests.get(f"https://search.censys.io/api/v2/hosts/{ip}", headers=header)

        if response.status_code == 200:
            with open('CENSYS-CTI.csv', 'wb') as file:
                file.write(response.content)
        else:
            print("Erro ao baixar o arquivo csv!")

    except requests.ConnectionError as error:
        print(error)

if __name__ == '__main__':
    if 'unittest' in sys.modules.keys():
        pass
    else:
        args = parse_arguments()

        if args.type.lower() == "vt":
            requestVT(args.apikey, args.hash)

        elif args.type.lower() == "censys":
            requestCensys(args.apikey, args.ip)
        else:
            print("Tipo de requisição inválido! Use 'VT' para VirusTotal ou 'censys' para Censys.")
