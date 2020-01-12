'''
Programa para sincronizar pastas local e remotamente usando
rclone e dropbox.
@author: Joao F. Santanna Filho
Data:11/01/2020
versao : 1.2 para windows

1 - Primeiramente é necessario configurar o rclone para ele ter acesso ao dropbox, segue o tutorial da pagina do 
rclone : https://rclone.org/dropbox/

primeiro rode configure o rclone:

> rclone config

esse comando faz o rclone entrar no modo configuracao onde ele vai gerar uma chave que vai permir acessar os
aquivos guardados na nuvem do dropbox.

# primeiro ele vai pedir um nome de alias do sistema remoto

2020/01/11 18:07:59 NOTICE: Config file "C:\\Users\\jsantanna\\.config\\rclone\\rclone.conf" not found - using defaults
No remotes found - make a new one
n) New remote
s) Set configuration password
q) Quit config
n/s/q> n
name> remote

aqui eu dei o nome de remote, podia ser outro , isso vai impactar na hora de criar os comandos do rclone para
fazer o acesso

# em segundo lugar ele vai perguntar o serviço de armazenagem que vc quer se conectar e vai mostra uma serie de 
opcoes com os nomes e numeros , vc pode tanto usar um como outro ...

 1 / 1Fichier
   \ "fichier"
 2 / Alias for an existing remote
   \ "alias"
 3 / Amazon Drive
   \ "amazon cloud drive"
 4 / Amazon S3 Compliant Storage Provider (AWS, Alibaba, Ceph, Digital Ocean, Dreamhost, IBM COS, Minio, etc)
   \ "s3"
 5 / Backblaze B2
   \ "b2"
 6 / Box
   \ "box"
 7 / Cache a remote
   \ "cache"
 8 / Citrix Sharefile
   \ "sharefile"
 9 / Dropbox
   \ "dropbox"
10 / Encrypt/Decrypt a remote
   \ "crypt"

.... mais opcoes 
Storage> 9
** See help for dropbox backend at: https://rclone.org/dropbox/ **

# em terceiro lugar , o rclone vai fazer algumas configuracoes especiais (tunagem fina), eu deixei tudo como 
a configuracao default, ao final o programa vai abrir seu navegador web default para conseguir uma chave a acesso
para o programa poder acessar o serviço remotamente

Dropbox App Client Id
Leave blank normally.
Enter a string value. Press Enter for the default ("").
client_id>
Dropbox App Client Secret
Leave blank normally.
Enter a string value. Press Enter for the default ("").
client_secret>
Edit advanced config? (y/n)
y) Yes
n) No
y/n> n
Remote config
Use auto config?
 * Say Y if not sure
 * Say N if you are working on a remote or headless machine
y) Yes
n) No
y/n> y
If your browser doesn't open automatically go to the following link: http://127.0.0.1:53682/auth?state=LftirlFEBkQEzit7VkGp8Q
Log in and authorize rclone for access
Waiting for code...
Got code

# finalmente depois de conseguir o token de acesso, vc volta para o prontp de comando e ele vai perguntar se esta
tudo ok com a configuracao remote, vc responde yes , e ao final pede para sair da configuracao.

y) Yes this is OK
e) Edit this remote
d) Delete this remote
y/e/d> y
Current remotes:

Name                 Type
====                 ====
remote               dropbox

e) Edit existing remote
n) New remote
d) Delete remote
r) Rename remote
c) Copy remote
s) Set configuration password
q) Quit config
e/n/d/r/c/s/q> q

# pronto o rclone esta configurado para acessar a nuvem do dropbox

para testar se esta tudo ok , vc pode digitar o seguinte comando para listar suas pastas na nuvem

rclone lsd remote:

se aparecer uma lista de pastas é pq esta tudo configurado com sucesso :-) 
'''
import os
import time

print('''
        Programa para sincronizar pastas de trabalho 
        remotas usando Dropbox e Rclone - v 1.2
        Pastas: raizes 
        Syncronizacao nos dois sentidos
        Local ----> remoto
        remoto ----> local
''')

# variaveis que vão guardar os caminhos locais e remotos
local = 'local:/Users/jsantanna/Dropbox2'
remoto = 'remote:/'


while True:
    print('''
        Escolha uma opcao
        0- sair
        1- Ver configuracao
        -------sync--------
        2- Sincronizar Local -->  Remoto
        3- Sincronizar Remoto --> Local
        4- Sobre
    ''')
    try:
        op = int(input('Opcao >:'))

        if op == 0:
            print('\n\n')
            break

        elif op == 1:
            print(f'Endereco Remoto - {remoto}')
            print(f'Endereco Local - {local}')
        
        elif op == 2:
            comando = 'rclone sync ' + local + ' ' + remoto
            print('Iniciando sincronização Local --> Dropbox')
            print(f'local:{local} --> remoto:{remoto}')
            print('...Aguarde termino')
            r = os.system(comando)
            if r == 0:
                print('Sincronização completa com sucesso')
        
        elif op == 3:
            comando = 'rclone sync ' + remoto + ' ' + local
            print('Iniciando sincronização Dropbox --> Local')
            print(f'remoto:{remoto} --> local:{local}')
            print('...Aguarde termino')
            r = os.system(comando)
            if r == 0:
                print('Sincronização completa com sucesso')

        elif op == 4:
            print('''
                Rclone utility 
                configurada para Dropbox
                @author: Joao F. Santanna Filho
                @email: joaosantanna@yahoo.com.br
                @version: 1.2
                Open source software use with precaution
            ''')

        else:
            print('Comando não cadastrado')
    
    except ValueError as e:
        print('Erro na leitura do comando')
        print('voce deveria ter digitado um numero')
        print(f'Detalhe:{e}')
        time.sleep(4)
    except Exception as e:
        print('Erro inesperado')
        print('Tente novamente')
        print(f'Detalhe:{e}')
        time.sleep(4)