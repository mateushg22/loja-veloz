# Plataforma Pedidos Veloz - Cloud DevOps

**Disciplina:** Cloud DevOps  
**Aluno:** Mateus Henrique Gomes | **RA:** 125071  
**Vídeo Pitch (YouTube):** https://youtu.be/JuQ6rVIM6xo

## Arquitetura da Solução
Projeto de modernização da plataforma de e-commerce **Loja Veloz**, contemplando ambiente local reproduzível com Docker Compose, imagem conteinerizada multi-stage sem privilégios de root, manifestos de produção em Kubernetes (Deployment, Service, ConfigMap, Secret, Probes e HPA), pipeline automatizada no GitHub Actions e esqueleto de IaC com Terraform.

## Como Executar Localmente

1. Suba toda a stack (API Gateway Nginx, Serviço de Pedidos e PostgreSQL) com um único comando:
```bash
docker compose up --build
```

2. Em outro terminal, valide o funcionamento:

* **Healthcheck via Gateway:**
```bash
curl http://localhost:8080/health
```

* **Criar um novo pedido:**
```bash
curl -X POST http://localhost:8080/orders \
  -H "content-type: application/json" \
  -d '{"customer":"Ana", "sku":"SKU-1", "quantity":2, "amount":149.90}'
```

* **Listar pedidos cadastrados:**
```bash
curl http://localhost:8080/orders
```
