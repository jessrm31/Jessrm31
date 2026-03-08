import requests # Biblioteca para fazer requisições web

def verificar_compliance(url):
    print(f"--- Iniciando Auditoria em: {url} ---")
    
    try:
        # Tenta acessar o site
        resposta = requests.get(url, timeout=5)
        
        # 1. Verificando se o site está online (Status 200)
        if resposta.status_code == 200:
            print("[✅] STATUS: Servidor Ativo.")
        else:
            print(f"[❌] STATUS: Erro no servidor (Código: {resposta.status_code}).")

        # 2. Verificando se usa HTTPS (Criptografia/Compliance)
        if url.startswith("https"):
            print("[✅] SEGURANÇA: Protocolo HTTPS detectado (Criptografia ativa).")
        else:
            print("[⚠️] ALERTA: Protocolo inseguro (HTTP). Risco de Compliance!")

    except Exception as e:
        print(f"[❌] ERRO: Não foi possível conectar ao alvo. Detalhes: {e}")

# Testando o script
alvo = "https://www.google.com" 
verificar_compliance(alvo)
