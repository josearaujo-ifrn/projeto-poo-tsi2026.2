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

c. No navegador, acesse a URL gerada e clique em Connect ou abra o arquivo vnc.html e em seguida clique no botão Conectar. Isso deverá exibir o ambiente do fluxbox

d. Volte ao terminal do Codespaces e execute seu script:
python app.py

### Alterações feitas pelo Gemini:
# 1. O que mudou no arquivo `devcontainer.json` e o que cada item faz?
Foram realizadas algumas alterações no arquivo `devcontainer.json` para corrigir avisos de configuração e melhorar a compatibilidade do ambiente com o PySide6 e o noVNC.

# 1.1. Configuração `features` (`desktop-lite:1`)

**Como estava antes:**
```json
"desktopElement": "fluxbox"
```

**Como ficou agora:**
```json
"version": "latest",
"webPort": "6080",
"vncPort": "5901"
```

**O que mudou e para que serve?**

- O parâmetro `desktopElement` não existe oficialmente nessa extensão, o que gerava um aviso amarelo no VS Code.
- A propriedade `version` define a versão da extensão utilizada.
- `webPort` define a porta 6080, utilizada para acessar o ambiente gráfico pelo navegador.
- `vncPort` define a porta 5901, utilizada pela conexão VNC interna.

O Fluxbox já é o gerenciador de janelas padrão instalado pela extensão, portanto, não é necessário configurá-lo manualmente.

# 1.2. Configuração `postCreateCommand`

**Como estava antes:**

O comando de instalação terminava com as bibliotecas:

```bash
libgl1 libegl1
```

**Como ficou agora:**

Foram adicionadas duas bibliotecas:

```bash
libdbus-1-3 libfontconfig1
```

**O que mudou e para que serve?**

- `libfontconfig1`: permite que o sistema encontre e gerencie fontes utilizadas na interface gráfica.
- `libdbus-1-3`: fornece suporte à comunicação entre processos e serviços do sistema Linux.

Essas bibliotecas ajudam a garantir o funcionamento adequado do PySide6 no Debian 12 (`bookworm`), evitando problemas relacionados à inicialização e à exibição de janelas.

# 1.3. Configuração `portsAttributes` (`onAutoForward`)

**Como estava antes:**

```json
"onAutoForward": "notify"
```

**Como ficou agora:**

```json
"onAutoForward": "openBrowser"
```

**O que mudou e para que serve?**

Essa propriedade define o comportamento do Codespace quando uma porta é identificada e encaminhada automaticamente.

Existem duas possibilidades utilizadas nessa configuração:

- `notify`: exibe uma notificação no VS Code informando que a porta foi aberta.
- `openBrowser`: solicita que o Codespace abra automaticamente uma aba do navegador para acessar o serviço disponibilizado naquela porta.

Nesse caso, a alteração facilita o acesso ao noVNC pela porta 6080, sem precisar abrir o endereço manualmente.

---

### Resumo das alterações

As modificações tiveram três objetivos principais:

1. **Corrigir a configuração do ambiente gráfico:** remover uma propriedade inválida e definir explicitamente as portas utilizadas pelo desktop-lite.
2. **Melhorar a compatibilidade com o PySide6:** adicionar bibliotecas necessárias para o funcionamento adequado da interface gráfica.
3. **Facilitar o acesso ao noVNC:** configurar a abertura automática do navegador quando a porta 6080 for encaminhada.