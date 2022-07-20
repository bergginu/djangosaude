# Sobre

Teste de desenvolvimento Django.

# Deps

Django: 3.2 (LTS)
(vide requerements.txt)
Docker

# Build da imagem Docker
```bash
docker build . -t dsweb
```


# Observações

- Para esta tarefa, o desenvolvimento foi incorporado a branch _main_, embora o adequando seria _development_.
- _python:3.10-slim-bullseye_ foi usado como imagem docker padrão, baseado-se em estudos avaliando desempenho, tamanho, estabilidade, segurança e documentação, preterindo imagens baseadas no Linux Alpine.
- Um projeto mais completo incluiria containers docker para nginx (balanceamento de carga), redis, PostgreSQL, django/gunicorn, celery/django (workers) e, possivelmente, Celery Flower (monitoramento), dentre outros.