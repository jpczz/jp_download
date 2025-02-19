import json
import zmq

def get_camera_info(socket):
    """
    Envia um request para obter informações sobre todas as câmeras conectadas ao Capture Grid 4.
    Retorna a resposta JSON decodificada.
    """
    req = {
        "msg_type": "Request",
        "msg_id": "GetCamera",
        "msg_seq_num": 1,  # Número único para identificar o request
        "CameraSelection": "All"
    }
    socket.send_string(json.dumps(req))
    rep = socket.recv()
    json_msg = json.loads(rep.decode("utf-8"))
    return json_msg


def send_download_request(socket, camera_key):
    """
    Envia um request para baixar os vídeos da câmera especificada no Capture Grid 4.
    
    Parâmetros:
    - socket: O socket ZMQ configurado para se comunicar com o Capture Grid 4.
    - camera_key: O identificador único da câmera que contém o vídeo.
    
    Retorna:
    - True se o comando foi enviado com sucesso, False caso contrário.
    """
    req = {
        "msg_type": "Request",
        "msg_id": "Download",
        "msg_seq_num": 5,  # Número único para identificar o request
        "CameraSelection": "Single",
        "CameraKey": camera_key,
        "PhotoSelection": "All"  # Seleciona todas as fotos/vídeos
    }
    socket.send_string(json.dumps(req))
    rep = socket.recv()
    json_msg = json.loads(rep.decode("utf-8"))
    return json_msg.get("msg_result", False)


def download_videos(socket):
    """
    Envia um request para baixar os vídeos de todas as câmeras conectadas ao Capture Grid 4.
    Assume que o Capture Grid 4 gerencia o download.
    """
    print("down_start")  # Indica o início do download

    # Obtém informações das câmeras
    camera_info = get_camera_info(socket)
    if not camera_info.get("msg_result", False):
        print("Erro ao obter informações das câmeras.")
        return False

    cameras = camera_info.get("CameraInfo", [])
    if not cameras:
        print("Nenhuma câmera conectada.")
        return False

    # Itera sobre as câmeras e envia o comando de download
    for camera in cameras:
        camera_key = camera.get("CameraKey")
        if not camera_key:
            continue

        # Envia o comando de download para a câmera (sem mensagens intermediárias)
        send_download_request(socket, camera_key)

    print("down_done")  # Indica o fim do download
    print("Todos os arquivos foram baixados.")
    return True


def main():
    """
    Função principal do script jp_download.
    Inicializa a conexão com o Capture Grid 4 e inicia o processo de download.
    """
    context = zmq.Context()
    req_socket = context.socket(zmq.REQ)
    req_socket.connect("tcp://127.0.0.1:54544")

    # Inicia o processo de download
    if not download_videos(req_socket):
        print("O processo de download falhou.")


if __name__ == "__main__":
    main()