Script em Python e Shell para automatizar o processo de criação de repositórios no Github. Para utilização, faz-se necessário um [token de acesso](https://docs.github.com/pt/free-pro-team@latest/github/authenticating-to-github/creating-a-personal-access-token) do GitHub.

## Instalação:

```
cd
git clone https://github.com/paulosell/auto-project-python
mv -r auto-project-python .auto-project-python
cd .auto-project-python
pip install -r requirements.txt
echo "seu_token_do_git" >> token-git.txt
chmod 777 create-project (pode precisar de sudo)
cp create-project /usr/local/bin (pode precisar de sudo)
```

## Uso:

```
Para usar o script basta digitar de qualquer lugar no terminal 'create-project -n <nome_do_projeto> -i [-i <lang1,lang2...langN>]'
```

