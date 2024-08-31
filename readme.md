# BlackJack Game ♣️

Replicando jogo de cartas "21" usando python OOP


  O objetivo desse projeto é aprender mais sobre python. Por ser algo que tem capacidade de explorar muito das funções, acho interessenta começar com um jogo simples de blackjack, e ir aprimorando essa idéia.

  A primeira versão do jogo já está pronta. O jogo é executádo via terminal e para seu funcionamento os arquivos ***game.py*** e ***utilidades.py*** devem estar num  mesmo diretório dentro do seu pc. 

## Como funciona? ⚙️
Ao invéz do modo tradicional, nessa versão o jogador compra as cartas dele primeiro e quando decidir que já deu, o bot irá comprar e continuar comprando cartas até que a mão dele tenha no mínimo 16.

Seus status como cartas e soma, são exibidas durante o jogo. No final, sua mão é comparada com a do adversário e um resultado é anunciado junto com a distribuição de fichas.

## Como jogar? ♟️
Ao iniciar, é perguntado se você deseja jogar<br>
Caso a resposta seja *sim*, o jogo começa.<br>
Caso a resposta seja *não*, é exibida uma mensagem e o jogo se fecha.<br>
> As respostas em sí são dados como "*s*" ou "*n*"

* ### Aposta  💰

> O algoritmo pede para você fornecer um valor a ser apostado, que seja menor ou igual ao número de fichas que você possui. <br>Automaticamente, a quantidade de fichas que você apostou é retirada do seu "cofre". <br>
> * ⚠️  Vale lembrar que só é permitido fazer **UMA** aposta dentro do game, que é a inicial. ⚠️</p>

* ### Compra de Cartas  ♠️

> Caso você ainda não esteja confiante com a sua mão, é possível comprar mais cartas. <br>Dentro do game existe uma ***trigger*** que é ativada quando sua mão "estoura". Não sendo possível comprar mais cartas ou fazer apostas
> Quando a soma de suas cartas é == 21, a compra de cartas não estará mais disponível<br>
> Ao finalizar sua compra de cartas, é a vez do oponente (*que também possui a mesma **trigger***)<br>

* ### Ganhar ou perder?  👊

> O jogo possui 4 tipos de validações:
> * sua mão é maior que a do adversário **E** sua mão não "estourou"
> * sua mão e menor que a do adversário **E** a mão dele não "estourou"
> * sua mão é igual que a do adversário
> * as duas mãos estouraram<br>
> 
> Caso você ganhe, recebe o dobro do valor que apostou, exemplo:<br>
> Supondo que você tenha apostado 500, esse valor será retirado da sua quantidade total de fichas. Se ganhar, essas fichas voltam para você com mais 500. O dobro que apostou.

* ### Como rodar o jogo? 🕹️

> 1. Você pode clonar esse repositório na sua máquina ou copiar os dois arquivos mencionados acima (*utilidades.py* e *game.py*).
> 2. Abra o terminal no diretório que os arquivos foram baixados ou copiados *(ambos precisam estar no mesmo diretório)*
> 3. Caso você tenha o python instalado na sua máquina, Digite no terminal python:

~~~ 
python game.py 
~~~

## Futuras melhorias 🚀

* Atualmente o código do arquivo principal do jogo "***game.py***", possui um número muito grande de linhas, coisa que pretendo mudar numa segunda versão reduzindo o tamanho do código e implementando extrtuturas mais complexas que a atual.<br>
> O arquivo *utilidades.py* tinha sido criado inicialmente para abrigar funções a serem utilizadas dentro do arquivo principal *game.py*.
* Planejo adicionar a possibilidade de poder ver a primeira carta de todos os jogadores (*assim como no jogo tradicional*)
* Também pretendo adicionar a possibilidades de fazer apostas durante o jogo, caso esteja confiante e ache que sua aposta inicial foi baixa.



## Agradecimentos ✌️

> *Obrigado por acessar meu github e conhecer meu projeto. Caso queira enviar sugestões meu email e instagram estarão logo abaixo*
> <br>
>
>
> <a href = "mailto:jhooliveira.lopes@gmail.com"><img src="https://img.shields.io/badge/-Gmail-%23333?style=for-the-badge&logo=gmail&logoColor=white" target="_blank"></a> <a href="https://www.instagram.com/jhonatan_lopes_lmao/?next=%2F" target="_blank"><img src="https://img.shields.io/badge/-Instagram-%23E4405F?style=for-the-badge&logo=instagram&logoColor=white" target="_blank"></a> 
