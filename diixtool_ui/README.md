# DiixTool UI

Interface gráfica oficial do framework DiixTool.

## Tecnologias

- Python 3.12+
- CustomTkinter
- CTkTable
- Pillow
- Dark Theme (Black)

## Instalação

```bash
pip install -r requirements.txt
```

## Execução

```bash
python main.py
```

## Estrutura

```
diixtool_ui/
├── main.py              # Ponto de entrada principal
├── requirements.txt     # Dependências
├── ui/
│   ├── config/         # Configurações (tema, etc.)
│   ├── pages/          # Páginas da interface
│   ├── components/     # Componentes reutilizáveis
│   └── controllers/    # Controladores
└── assets/             # Recursos (ícones, imagens)
```

## Tema

Tema padrão: **Dark Black**

- Background Principal: `#0D0D0D`
- Painéis: `#141414`
- Sidebar: `#111111`
- Cards: `#1A1A1A`

## Funcionalidades

- Dashboard com informações rápidas
- Gerenciamento de dispositivos
- Visualizador de aplicativos
- Package Info detalhado
- XML Inspector
- Logcat
- Scrcpy integration
- Screenshot
- Plugins
- Configurações

## Atalhos

- `Ctrl+R` / `F5` - Atualizar
- `Ctrl+F` - Buscar
- `Ctrl+S` - Salvar
- `F11` - Fullscreen

## Arquitetura

MVC/MVP com Programação Orientada a Objetos.

A interface **não implementa regras de negócio**, apenas:
- Solicita informações ao Framework
- Exibe dados
- Recebe ações do usuário
