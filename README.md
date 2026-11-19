# projeto-poo-tsi2026.2
### No terminal integrado do Codespaces, atualize os pacotes do Linux e instale o Xvfb (servidor X virtual), as bibliotecas Qt necessárias e o PySide6. Execute o seguinte comando no terminal:

sudo apt-get update && sudo apt-get install -y xvfb x11vnc fluxbox websockify novnc libgl1 libegl1 libxkbcommon-x11-0 libxcb-cursor0 libxcb-xinerama0 libxcb-icccm4 libxcb-image0 libxcb-keysyms1 libxcb-render-util0 libdbus-1-3 libfontconfig1 && pip install PySide6

### Iniciar a exibição virtual (Xvfb). Inicie o display virtual :99 em segundo plano para capturar a janela da aplicação. Execute o seguinte comando no terminal:

Xvfb :99 -screen 0 1024x768x16 & export DISPLAY=:99

### Subir o servidor de visualização no navegador (noVNC). Para visualizar a janela no navegador, execute o gerenciador de janelas (fluxbox) e o servidor web VNC. Execute o seguinte comando no terminal:

fluxbox & x11vnc -display :99 -forever -shared -rfbport 5900 & websockify --web=/usr/share/novnc/ 6080 localhost:5900 &

### Acessar a interface e rodar o aplicativo:
a. Vá para a aba Portas (ao lado do Terminal no VS Code).
b. Localize a porta 6080 e clique no ícone do globo (Open in Browser).
c. No navegador, acesse a URL gerada e clique em Connect ou abra o
arquivo vnc.html e em seguida clique no botão Conectar. Isso deverá
exibir o ambiente do fluxbox
d. Volte ao terminal do Codespaces e execute seu script:
python app.py