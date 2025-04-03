import requests

security_headers = {
    "Strict-Transport-Security": "Protege contra ataques downgrade para HTTP.",
    "Content-Security-Policy": "Restringe carregamento de scripts e previne XSS.",
    "X-Frame-Options": "Previne ataques de clickjacking.",
    "X-Content-Type-Options": "Impede execução de arquivos com MIME suspeitos.",
    "Referrer-Policy": "Controla vazamento de informações ao acessar outros sites.",
    "Permissions-Policy": "Restringe acesso a APIs do navegador.",
    "X-XSS-Protection": "Ativa proteção contra XSS em navegadores antigos.",
}

url = input("Digite o site para verificar os cabeçalhos (exemplo: https://exemplo.com): ").strip()


try: 
    response = requests.get(url)
    headers = response.headers

    with open("resultado.txt", "w", encoding="utf-8") as f:
        f.write("=== CABEÇALHOS HTTP do site ===\n")
        for chave, valor in headers.items():
         f.write(f"{chave}: {valor}\n")

        f.write("\n=== VERIFICAÇÃO DE SEGURANÇA ===\n")
        for header, description in security_headers.items():
         if header in headers:
            f.write(f"[✔] {header} está presente. {description}\n")
         else:
            f.write(f"[✘] {header} está AUSENTE! {description}\n")
    
    print("Resultados salvos em 'resultados.txt'.")

except requests.exceptions.RequestException as e:
    print(f"Erro ao acessar o site: {e}")
