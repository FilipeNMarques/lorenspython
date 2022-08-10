
- [X] Fazer a primeira chamada na api utilizando a url de exemplo e printando o retorno, qualquer moeda disponível na api.
  - Utilizar uma função para bater na api, dentro dessa func, chamar o requests e printar o resultado.

- [x] Criar um arquivo .txt vazio no nivel root do diretório do projeto.
- [x] Pesquisar como que ler e escrever em arquivos estáticos, ex: .txt
- [x] Escrever no arquivo estático o retorno da api que você printou na primeira task.
- [x] Printar o as infos que foram armazenadas no arquivo.


### Trabalhando com dados

##### Agora que você já aprendeu a utilizar funções, ler e escrever em arquivos, vamos aprofundar na forma como lidamos com os dados.

Lidando com dicionários

- [X] Pesquisar sobre o que é um dicinário e como faz para acessar os elementos dentro dele.
- [ ] Apagar as informações do `arquivo.txt` e deixar ele limpo para receber a nova estrutura
- [x ] Entender como que faz para escrver no arquivo sem apagar o que já existe
- [x ] Olhar na doc da api como que faz para chamar outras moedas, não só o btc como está agora
- [x ] Refatorar a func que faz a chamada na api para receber um parametro: `code` que é será o código da moeda desejada
- [ x] Tratar o retorno da api para utilizar só os dados que será salvo no arquivo
  - [x] Pesquisar e entender como que faz iteração nos dicionaários
- [x] Pesquisar e entender o que são listas
- [x] Pesquisar e entender como iterar uma lista
- [x] Pesquisar e entender como acessar elementos dentro de uma lista
- [ x] Escrever no arquivo a nova estrutura de dados:
  - Criar um dicionário com uma propriedade `criptos` que será uma lista de dicionários 
- [x ]  Salvando os dados na lista de criptos:
    - Com os dados retornados da api, acesse o dicionário e salve apenas os elementos:
        ``"<codigo que foi utilizado na funcao de chamar a api>": {
         "high": "132646.99993000",
         "low": "123292.44629000",
         "vol": "110.72929985",
         "last": "124699.99357043",
         "date": 1658408448 }``
- [ x ] Fazer uma função que retorne todas as criptos dentro da lista da seguinte forma:
{"data": "dia/mes/ano", "ultimo_preco": "\<dado>", "alta": "\<dado>", "baixa": "\<dado>", "volume": "\<dado>"}

  - [ ] Se não tiver nenhuma cripto na lista retornar: {"message": "Sem criptos na sua carteira"} 



## Critérios de aceite

- Pelos menos 3 criptos dentro do arquivo com esse novo modelo de dados
- Estrutura de dados dentro do `arquivo.txt` igual ao solicitado
- Func que retorna as criptos da carteira igual a solicitada


# Divirta-se!!! 