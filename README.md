# Trabalho de multicast da disciplina de Sistemas Distribuídos

* Esse trabalho tem como objetivo implementar uma rede multicast entre um sender (cliente) e receivers (servidores).

## Modo de uso

* Primeiro coloque os dois arquivos do projeto em todas as VMs.
* Entre em todas as VMs e insira a seguinte rota ``` route add -net 224.0.0.0 netmask 224.0.0.0 eth0 ```.
* Depois escolha uma das VMs para ser o sender e execute o arquivo sender.py nela. As demais serão os receivers, por isso você deve executar o arquivo receiver.py nas outras.
* Na execução do sender.py você deve inserir o comando ``` python sender.py --e "expressão_matemática" ```, onde dentro das aspas você deve inserir sua expressão matemática. Não se anime! Teste expressões simples! O objetivo do trabalho não é fazer uma calculadora. Caso tenha dúvidas sobre os parâmetros obrigatórios, digite ``` python sender.py --help ```.

** Importante: durante a execução dos receivers, espere eles processarem a requisição antes de pausar a VM. Também espere o sender receber por completo a resposta do multicast, pois caso contrário haverá conflito de requisições, o que pode ocorrer na resposta atrasada ao cliente de uma requisição passada. **

** Objetivos do trabalho:
- [x] Criar 4 máquinas virtuais e conectá-las por uma rede interna
- [x] Criar um sender e um receiver, ende o sender irá enviar mensagens para o grupo dos receivers
- [x] Fazer com que os receivers comuniquem-se através de um grupo próprio de multicast. Isso é necessário para fazer com que os mesmos saibam quais receivers estão online e aptos a responderem ao sender
- [x] Fazer com que apenas um dos receivers responda o sender, de uma forma que somente o de menor IP responda

