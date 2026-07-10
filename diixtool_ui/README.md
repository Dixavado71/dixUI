# DiixTool UI

Interface gráfica oficial do framework DiixTool.

## Tecnologias

- Python 3.12+
- CustomTkinter 6.x
- CTkTable 1.1+
- Pillow 11.x
- Dark Theme (Black)
- Arquitetura MVC/MVP
- Programação Orientada a Objetos

## Requisitos

- Python 3.12 ou superior
- Ambiente gráfico (X11, Wayland, Windows, macOS)

## Instalação

```bash
pip install -r requirements.txt
```

### Dependências Principais

- `customtkinter>=6.0.0` - Framework GUI moderno
- `CTkTable>=1.1` - Tabelas para CustomTkinter
- `Pillow>=11.0.0` - Processamento de imagens
- `packaging>=24.0` - Utilitários de versionamento

## Execução

```bash
python main.py
```

Ou execute diretamente do diretório raiz:

```bash
cd diixtool_ui
python main.py
```

## Estrutura do Projeto

```
diixtool_ui/
├── main.py              # Ponto de entrada principal (App Window)
├── requirements.txt     # Dependências do projeto
├── README.md           # Documentação
├── ui/
│   ├── __init__.py
│   ├── config/         # Configurações (tema, cores, fontes)
│   │   ├── __init__.py
│   │   └── theme.py    # Tema Dark Black e paleta de cores
│   ├── pages/          # Páginas da interface
│   │   ├── __init__.py
│   │   └── dashboard.py # Página Dashboard
│   ├── components/     # Componentes reutilizáveis
│   │   └── __init__.py
│   └── controllers/    # Controladores (integração com Framework)
│       └── __init__.py
└── assets/             # Recursos (ícones, imagens, logos)
```

## Tema: Dark Black

O tema padrão foi cuidadosamente projetado para oferecer uma experiência visual profissional com alto contraste e foco em produtividade.

### Paleta de Cores

| Elemento | Cor Hex | Uso |
|----------|---------|-----|
| Background Principal | `#0D0D0D` | Área principal da aplicação |
| Painéis | `#141414` | Menus e barras |
| Sidebar | `#111111` | Navegação lateral |
| Cards | `#1A1A1A` | Containers de informação |
| Hover | `#222222` | Estado de hover |
| Seleção | `#2E2E2E` | Itens selecionados |
| Texto Principal | `#FFFFFF` | Títulos e textos importantes |
| Texto Secundário | `#BFBFBF` | Labels e descrições |
| Sucesso | `#00C853` | Operações concluídas |
| Erro | `#F44336` | Mensagens de erro |
| Warning | `#FFC107` | Alertas |
| Info | `#29B6F6` | Informações |

### Indicadores de Status

- 🟢 **Verde** (`#00C853`) - Operação concluída / Conectado
- 🟡 **Amarelo** (`#FFC107`) - Em processamento
- 🔵 **Azul** (`#29B6F6`) - Informação
- 🔴 **Vermelho** (`#F44336`) - Erro
- ⚪ **Cinza** (`#BFBFBF`) - Desconectado

## Funcionalidades

### Navegação Lateral (Sidebar)

- 🏠 **Dashboard** - Visão geral com cards informativos
- 📱 **Dispositivos** - Gerenciamento de dispositivos Android
- 📦 **Aplicativos** - Lista e gerenciamento de apps instalados
- 📑 **Package Info** - Informações detalhadas de pacotes
- 🧩 **Activities** - Visualização de Activities
- ⚙ **Services** - Serviços do sistema
- 📡 **Receivers** - Broadcast Receivers
- 🗂 **Providers** - Content Providers
- 🔐 **Permissions** - Permissões do sistema
- 📁 **APK Explorer** - Explorador de APKs
- 📂 **File Explorer** - Explorador de arquivos
- 🖼 **XML Inspector** - Inspetor de layout XML
- 📋 **Logcat** - Visualizador de logs em tempo real
- 🖥 **Scrcpy** - Espelhamento de tela
- 🤖 **Automação** - Scripts e automações
- 📸 **Screenshot** - Captura de tela
- 🔌 **Plugins** - Gerenciamento de extensões
- ⚙ **Configurações** - Preferências da aplicação

### Menu Superior

- **Arquivo** - Novo, Abrir Projeto, Salvar, Configurações, Sair
- **ADB** - Atualizar dispositivos, Reconectar, Reiniciar/Encerrar servidor
- **Ferramentas** - Scrcpy, Terminal, Dump XML, Logcat, Captura de Tela
- **Visualizar** - Painéis, Tema, Zoom
- **Ajuda** - Documentação, GitHub, Sobre

### Barra de Status

Informações em tempo real:
- Dispositivo conectado
- Estado do ADB
- Status do Scrcpy
- Uso de CPU e RAM
- Tema ativo

## Atalhos de Teclado

| Atalho | Ação |
|--------|------|
| `Ctrl+R` / `F5` | Atualizar |
| `Ctrl+F` | Buscar |
| `Ctrl+L` | Limpar |
| `Ctrl+S` | Salvar |
| `Ctrl+P` | Configurações |
| `Ctrl+D` | Dispositivos |
| `Ctrl+A` | Aplicativos |
| `Ctrl+X` | XML Inspector |
| `Ctrl+G` | Logcat |
| `Ctrl+T` | Terminal |
| `F11` | Fullscreen |

## Arquitetura

O DiixTool UI segue o padrão **MVC/MVP** com Programação Orientada a Objetos:

```
UI Layer
│
├── Window (main.py)
│   └── DiixToolUI - Janela principal
│
├── Views (ui/pages/)
│   ├── Dashboard
│   ├── Devices
│   ├── Packages
│   └── ...
│
├── Components (ui/components/)
│   ├── Cards
│   ├── Tables
│   ├── Forms
│   ├── Dialogs
│   └── Widgets
│
├── Controllers (ui/controllers/)
│   └── Integração com Framework DiixTool
│
└── Config (ui/config/)
    └── Theme - Configurações de tema e cores
```

### Princípios de Design

1. **Separação de Responsabilidades**
   - A UI não implementa regras de negócio
   - Toda lógica pertence ao Framework DiixTool
   - Interface apenas exibe dados e recebe ações

2. **Responsividade**
   - Layout adaptável a diferentes resoluções
   - Suporte a múltiplos monitores
   - Redimensionamento em tempo real
   - Painéis ajustáveis

3. **Performance**
   - Não bloqueia durante operações longas
   - Utiliza Workers para tarefas assíncronas
   - Atualização via eventos

4. **Consistência Visual**
   - Tema único em toda aplicação
   - Ícones consistentes
   - Espaçamento uniforme
   - Tipografia clara

## Boas Práticas

✅ **A interface DEVE:**
- Permanecer totalmente responsiva
- Nunca bloquear durante operações
- Utilizar Workers para tarefas longas
- Utilizar eventos para atualização visual
- Separar componentes reutilizáveis
- Utilizar ícones consistentes
- Manter espaçamento uniforme
- Seguir padrão visual único

❌ **A interface NÃO DEVE:**
- Executar comandos ADB diretamente
- Interpretar dados do dumpsys
- Realizar parser de XML
- Implementar lógica de automação
- Manipular dados internos do Android

## Integração com Framework

A comunicação com o Framework DiixTool ocorre exclusivamente através da API pública:

```python
# Exemplo de integração (controller)
class DeviceController:
    def __init__(self, api_client):
        self.api = api_client
    
    def get_devices(self):
        """Solicita lista de dispositivos ao Framework"""
        return self.api.devices.list()
    
    def get_app_info(self, package_name):
        """Solicita informações de um app ao Framework"""
        return self.api.packages.info(package_name)
```

## Contribuição

1. Fork o projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## Licença

Este projeto faz parte do ecossistema DiixTool.

## Suporte

- Documentação: [Link da documentação]
- GitHub: [Link do repositório]
- Issues: [Link para reportar problemas]

---

**DiixTool UI** - Interface moderna e profissional para o framework DiixTool.
