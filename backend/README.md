<h1 align="center">
    <img alt="E-Diaristas" title="Adote Um Pet" src="../.github/media/logo.svg" width="220px" />
</h1>

<p align="center">
  <a href="#rocket-tecnologias">Tecnologias</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#-projeto">Projeto</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#rodando">Rodando</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#-como-contribuir">Como contribuir</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
</p>

<a id="-projeto">
<p align="center">
 <img src="https://img.shields.io/static/v1?label=PRs&message=welcome&color=7159c1&labelColor=000000" alt="PRs welcome!" />

  <img alt="License" src="https://img.shields.io/static/v1?label=license&message=MIT&color=7159c1&labelColor=000000">
</p>

<br>

<p align="center">
  <img alt="E-Diaristas-Frontend" src="../.github/media/app.png" width="100%">
</p>

<a id="rocket-tecnologias"></a>

## 🚀 Tecnologias

O Backend da aplicação foi desenvolvido com as seguintes tecnologias:

![](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white) ![](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

<a id="rodando"></a>

## 💻 Rodando

### 🐬 Usando Docker

Para usar com docker basta apenas executar o comando:

```bash
docker-compose up
```

### 📁 Rodando através da fonte:

Tenha certeza de ter o Docker e o Python instalado com PIP.

Abra o terminal no projeto e então execute os códigos abaixo.

Para instalar as dependências:

```bash
pip install -r requirements.txt
```

Antes de iniciar a aplicação tenha certeza que você rodou o docker.

```bash
docker-compose up db
```

Para rodar a aplicação:

```bash
python manage.py runserver
```

## 🤔 Como contribuir

<a id="-como-contribuir"></a>

- Faça um fork desse repositório;
- Cria uma branch com a sua feature: `git checkout -b minha-feature`;
- Faça commit das suas alterações: `git commit -m 'feat: Minha nova feature'`;
- Faça push para a sua branch: `git push origin minha-feature`.

Depois que o merge da sua pull request for feito, você pode deletar a sua branch.
