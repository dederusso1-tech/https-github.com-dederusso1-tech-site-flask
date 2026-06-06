import os
from flask import Flask, render_template_string

app = Flask(__name__)

# SE VOCÊ JÁ TIVER O LINK REAL DA KIWIFY, ALTERE O TEXTO ENTRE AS ASPAS ABAIXO.
# SE NÃO TIVER, PODE DEIXAR COMO ESTÁ APENAS PARA FAZER O SITE VOLTAR AO AR!
LINK_DE_PAGAMENTO = "https://pay.kiwify.com.br/dTqsezY"

# Modelo HTML estruturado com CSS integrado para a página de vendas
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ativação da Atração de Alma Gêmea</title>
    <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght=300;400;600;700&family=Playfair+Display:ital,wght=0,400;0,700;1,400&display=swap" rel="stylesheet">
    <style>
        :root {
            --bg-color: #FFF5F5;
            --primary-color: #D4AF37; /* Dourado */
            --text-color: #3A2E2B;
            --accent-color: #B85A6C; /* Rosa Velho */
            --white: #FFFFFF;
        }

        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: 'Montserrat', sans-serif; background-color: var(--bg-color); color: var(--text-color); line-height: 1.6; }
        h1, h2, h3 { font-family: 'Playfair Display', serif; font-weight: 700; }
        .container { max-width: 1100px; margin: 0 auto; padding: 0 20px; }
        
        /* Hero Section */
        .hero { background: linear-gradient(135deg, #FFE4E6 0%, #FFF5F5 100%); padding: 80px 0; text-align: center; }
        .hero h1 { font-size: 3rem; color: var(--accent-color); margin-bottom: 20px; }
        .hero p { font-size: 1.2rem; max-width: 800px; margin: 0 auto 30px; font-weight: 300; }
        
        /* Botões */
        .btn { display: inline-block; background-color: var(--primary-color); color: var(--white); padding: 18px 36px; font-weight: 700; text-decoration: none; border-radius: 50px; font-size: 1.1rem; box-shadow: 0 4px 15px rgba(212,175,55,0.4); transition: transform 0.2s; }
        .btn:hover { transform: translateY(-2px); }
        .sub-btn { font-size: 0.85rem; margin-top: 10px; opacity: 0.7; }

        /* Seções Gerais */
        .section { padding: 60px 0; }
        .text-center { text-align: center; }
        .section h2 { font-size: 2.2rem; margin-bottom: 40px; color: var(--accent-color); }

        /* Grid de Fases */
        .grid-fases { display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 20px; margin-top: 30px; }
        .fase-card { background: var(--white); padding: 30px; border-radius: 15px; box-shadow: 0 5px 15px rgba(0,0,0,0.03); border-top: 4px solid var(--accent-color); }
        .fase-card h3 { margin-bottom: 15px; color: var(--accent-color); }

        /* Preço e Oferta */
        .oferta { background-color: var(--white); border-radius: 20px; padding: 50px; box-shadow: 0 10px 30px rgba(0,0,0,0.05); max-width: 600px; margin: 40px auto; }
        .preco { font-size: 2.5rem; color: var(--accent-color); font-weight: 700; margin: 20px 0; }

        /* Garantia */
        .garantia { max-width: 700px; margin: 40px auto 0; background: #FFF; padding: 25px; border-radius: 10px; border-left: 5px solid #4CAF50; font-size: 0.95rem; }
    </style>
</head>
<body>

    <section class="hero">
        <div class="container">
            <p><strong>Chega de encontros frustrantes. Está na hora de sintonizar com o amor da sua vida.</strong></p>
            <h1>Ativação da Atração de Alma Gêmea</h1>
            <p>Um método prático e espiritual para destravar seus bloqueios energéticos e atrair o parceiro ideal que já está alinhado com o seu propósito.</p>
            <a href="{link_pagamento}" class="btn">QUERO ATIVAR MINHA ALMA GÊMEA AGORA</a>
            <p class="sub-btn">🔒 Compra 100% segura | Acesso imediato</p>
        </div>
    </section>

    <section class="section text-center" style="background-color: #FFF;">
        <div class="container">
            <h2>Você sente que o amor de verdade não é para você?</h2>
            <p style="max-width: 750px; margin: 0 auto; font-size: 1.1rem;">
                Muitas pessoas passam anos repetindo os mesmos padrões de relacionamentos dolorosos. O problema não é você, é a sua <strong>frequência vibracional</strong>. Se você cansou de atrair pessoas emocionalmente indisponíveis, existe um caminho magnético para mudar isso.
            </p>
        </div>
    </section>

    <section class="section">
        <div class="container text-center">
            <h2>O Método de Ativação</h2>
            <div class="grid-fases">
                <div class="fase-card">
                    <h3>Fase 1: A Limpeza</h3>
                    <p>Desatar nós de relacionamentos passados para abrir espaço para o novo.</p>
                </div>
                <div class="fase-card">
                    <h3>Fase 2: Alinhamento</h3>
                    <p>Resgatar seu amor-próprio e se tornar magneticamente irresistível.</p>
                </div>
                <div class="fase-card">
                    <h3>Fase 3: A Ativação</h3>
                    <p>Meditações guiadas e reprogramação mental para emitir o sinal ao universo.</p>
                </div>
                <div class="fase-card">
                    <h3>Fase 4: O Encontro</h3>
                    <p>Como identificar os sinais claros quando sua alma gêmea aparecer.</p>
                </div>
            </div>
        </div>
    </section>

    <section class="section text-center" id="comprar" style="background-color: #FFE4E6;">
        <div class="container">
            <h2>Chegou a sua hora de amar e ser amado(a)</h2>
            <div class="oferta">
                <p>Todo o treinamento + Bônus Exclusivos por apenas:</p>
                <div class="preco">12x de R$ 29,70</div>
                <p>ou R$ 297,00 à vista</p>
                <br>
                <a href="{link_pagamento}" class="btn">QUERO ME INSCREVER AGORA</a>
                
                <div class="garantia">
                    <strong>🛡️ Risco Zero: Garantia de 7 Dias</strong><br>
                    Assista às aulas. Se não gostar, devolvemos 100% do seu dinheiro sem perguntas.
                </div>
            </div>
        </div>
    </section>

</body>
</html>
"""

@app.route('/')
def home():
    html_renderizado = HTML_TEMPLATE.replace("{link_pagamento}", LINK_DE_PAGAMENTO)
    return render_template_string(html_renderizado)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
