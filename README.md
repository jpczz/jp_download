# JP Download API Interface

Este script fornece uma interface de linha de comando para controlar câmeras conectadas ao Capture Grid 4 através de requisições via ZMQ. Ele permite baixar automaticamente vídeos e fotos capturados pelas câmeras conectadas.

Requisitos:

- Python 3.x
- Bibliotecas Python: zmq
- Capture Grid 4 configurado com as seguintes endpoints:
    - Event publisher: tcp://127.0.0.1:54543
    - Request/reply server: tcp://127.0.0.1:54544

Nota: Este script foi desenvolvido especificamente para o Capture Grid 4 e pode não ser compatível com outras versões ou softwares como o Smart Shooter. 

Como usar:

Exibindo informações sobre as câmeras conectadas:

O script obtém automaticamente informações sobre as câmeras conectadas. Essa informação é necessária para identificar as câmeras e realizar o download dos arquivos.

Baixar vídeos e fotos:

Para baixar os vídeos e fotos das câmeras conectadas, execute o script sem parâmetros adicionais. O script irá detectar automaticamente todas as câmeras conectadas e iniciar o processo de download.

python jp_download.py

Este comando irá:

- Detectar todas as câmeras conectadas.
- Iniciar o processo de download dos vídeos e fotos para cada câmera.
- Exibir mensagens de status (down_start e down_done) durante o processo.
- Baixar de uma câmera específica:
Se você quiser baixar os arquivos de uma câmera específica, utilize o parâmetro --camera-key seguido da chave da câmera desejada.

python jp_download.py --download --camera-key "Canon Inc.|Canon EOS REBEL T2i|1923127453"

Tratamento de erros:

O script exibe mensagens de erro claras caso ocorram problemas ao tentar se conectar com o Capture Grid 4 ou baixar os arquivos. Certifique-se de que o Capture Grid 4 está rodando corretamente e as configurações de endpoints estão corretas.

Mensagens de erro comuns:

- Erro ao obter informações das câmeras : Verifique se o Capture Grid 4 está conectado às câmeras e se as câmeras estão ligadas.
- Nenhuma câmera conectada : Certifique-se de que as câmeras estão conectadas fisicamente e reconhecidas pelo Capture Grid 4.
- Falha no download : Verifique se há espaço suficiente no disco e se o diretório de destino está acessível.

Notas:

- O script cria automaticamente o diretório padrão de download configurado no Capture Grid 4, caso ele não exista.
- O processo de download pode ser interrompido a qualquer momento pressionando Ctrl+C.
- As mensagens down_start e down_done indicam o início e o fim do processo de download, respectivamente.
