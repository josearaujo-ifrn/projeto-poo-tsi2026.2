# projeto-poo-tsi2026.2

### Atualizações (21/11/2026):
Após um teste em um codespace diferente, notei que os comandos anteriores de instalação de bibliotecas, execução de
diversos comandos não eram mais necessários.

# O que deve ser feito agora?
Só esperar, as portas 5901 e 6080 vão abrir sozinhas, ao clicar no botão "Portas", ao lado do "Terminal", vai aparecer
"noVNC Desktop (6080)", ao passar o mouse em cima do nome da porta, vai aparecer um símbolo de globo, após isso clique nele
e a simulação irá funcionar no navegador.

Quando tiver a simulação aberta, entre no terminal e execute um arquivo python, como por exemplo:
python app.py
O arquivo vai ser executado no simulador/emulador.

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