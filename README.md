# marmitaria-tempero-caseiro-mvp

# Cardápio Digital e Gestão de Pedidos — Marmitaria Tempero Caseiro (MVP)

Aplicação web responsiva (*mobile-first*) desenvolvida para otimizar o atendimento no horário de pico (11h às 13h), organizar a fila de produção da cozinha e apoiar o fechamento financeiro diário da **Marmitaria Tempero Caseiro** (Piracicaba - SP), alinhada ao **ODS 8 (Trabalho Decente e Crescimento Econômico)**.

## Arquitetura e Tecnologias
- **Padrão Arquitetural:** Monolítico em Camadas (MVC/MVT)
- **Linguagem e Framework:** Python 3.12 + Django 5.1
- **Banco de Dados:** PostgreSQL 16 (hospedado/gerenciado via Supabase)
- **Interface e Acessibilidade:** HTML5/CSS3 responsivo com alto contraste (>= 4,5:1), áreas de toque >= 44x44px e alertas redundantes (texto, ícone e cor)

## Escopo do MVP
- **RF01:** Cadastro e ativação do cardápio diário com preços por tamanho (P, M e G).
- **RF02:** Cardápio digital público para envio de pedidos sem necessidade de login ou app.
- **RF03:** Painel autenticado da cozinha com fila cronológica e atualização de status (*Recebido, Em Preparo, Saiu para Entrega, Concluído*).
- **RF04:** Consolidação do fechamento diário por forma de pagamento e controle de clientes mensalistas.

## Segurança (OWASP Top 10)
- Autenticação administrativa com hash **PBKDF2-SHA256** (`django.contrib.auth`).
- Proteção nativa contra **SQL Injection** (Django ORM parametrizado), **XSS** (auto-escape em templates) e **CSRF**.
- Credenciais isoladas em variáveis de ambiente (`.env`).
