Átom — Assistente de Voz com IA


Átom é um assistente de voz pessoal com interface gráfica, desenvolvido em Python. Ele ouve comandos por microfone, processa com inteligência artificial (Google Gemini) e responde com voz sintetizada (ElevenLabs), tudo dentro de uma interface visual construída com Pygame.
Funcionalidades:
- Reconhecimento de voz via microfone
- Respostas inteligentes com Google Gemini
- Síntese de voz com ElevenLabs (voz natural em PT-BR)
- Interface gráfica animada com Pygame
- Loop contínuo de escuta (diga "desligar" ou "sair" para encerrar)
- Estrutura do Projeto


PRÉ-REQUISITOS: 
Python 3.13+
Microfone funcionando
Conta com chave de API do Google AI Studio (Gemini)
Conta com chave de API do ElevenLabs

INSTALAÇÃO
Clone o repositório:

bash
   git clone https://github.com/seu-usuario/atom.git   cd atom
Crie e ative um ambiente virtual:
bash
   python -m venv venv   no Windows:  venv\Scripts\activate   no Linux/macOS:  source venv/bin/activate
Instale as dependências:

bash
   pip install -r requirements.txt
Configure as variáveis de ambiente:

bash
   cp .env.example .env
Abra o arquivo .env e preencha com suas chaves:


   GOOGLE_API_KEY='sua_chave_aqui'  ELEVENLABS_API_KEY='sua_chave_aqui'

▶ Como usar

bash
python modules/atom.py

O Átom iniciará a interface gráfica e ficará ouvindo automaticamente.
Fale seu comando após o aviso "Ouvindo..."
Para encerrar, diga: "desligar" ou "sair"

DICA DE SEGURANÇA: 
Nunca compartilhe seu arquivo .env. Ele está listado no .gitignore e não deve ser enviado ao repositório.
Use o .env.example como referência para outros colaboradores.

Dependências principais
PacoteUsopygameInterface gráficagoogle-generativeaiIA com GeminielevenlabsSíntese de vozspeechrecognition / pyaudioCaptura de áudiopython-dotenvLeitura do .env
Lista completa em requirements.txt.
