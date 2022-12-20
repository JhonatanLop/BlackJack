# BlackJack Game ♣️

> Status: Em desenvolvimento ⏱️

  O objetivo desse projeto é aprender mais sobre python. Por ser algo que tem capacidade de explorar muito das funções, acho interessenta começar com um jogo simples de blackjack, e ir aprimorando essa idéia.

  A primeira versão do jogo já está pronta. O jogo é executádo via terminal e para seu funcionamento os arquivos ***game.py*** e ***utilidades.py*** devem estar num  mesmo diretório dentro do seu pc. 

## Como funciona? ⚙️
Ao invéz do modo tradicional, nessa versão o jogador compra as cartas dele primeiro e quando decidir que já deu, o bot irá comprar e continuar comprando cartas até que a mão dele tenha no mínimo 16.

Seus status como cartas e soma, são exibidas durante o jogo. No final, sua mão é comparada com a do adversário e um resultado é anunciado junto com a distribuição de fichas.

## Como jogar? ♟️
Ao iniciar, é exibido uma mensagem de boas vindas, basta apertar qualquer tecla<br>

* ### Aposta  💰

> * O algoritmo pede para você fornecer um valor a ser apostado, que seja menor ou igual ao número de fichas que você possui. <br>
> Automaticamente, a quantidade de fichas que você apostou é retirada do seu "cofre". <br>
> * Também é possível fazer apostas durante o game.

* ### Compra de Cartas  ♠️

> * Caso você ainda não esteja confiante com a sua mão, é possível comprar mais cartas. Dentro do game existe uma ***trigger*** que é ativada quando sua mão "estoura" ou é igual a 21, Não sendo possível comprar mais cartas.
> * Ao finalizar sua compra de cartas, é a vez do oponente (*que também possui a mesma **trigger***)<br>
> * É possível ver a primeira carta do oponente durante o jogo.

* ### Ganhar ou perder?  👊

> * O jogo possui alguns tipos de validações de resultado para determinar quem venceu a partida.
> * Caso você ganhe, recebe o dobro do valor que apostou, exemplo:<br>
> * Supondo que você tenha apostado 500, esse valor será retirado da sua quantidade total de fichas. Se ganhar, essas fichas voltam para você com mais 500. O dobro que apostou.

* ### Como rodar o jogo? 🕹️

> 1. Você pode clonar esse repositório na sua máquina ou copiar os dois arquivos mencionados acima (*utilidades.py* e *game.py*).
> 2. Abra o terminal no diretório que os arquivos foram baixados ou copiados *(ambos precisam estar no mesmo diretório)*
> 3. Caso você tenha o python instalado na sua máquina, Digite no terminal python:

~~~ 
python game.py 
~~~

## Melhorias Feitas 🚀

* Foi diminuido o tamanho do código em mais da metada em comparação da versão anterior
* É possível ver a 1º carta do adversário
* Agora é possível fazer apostas com o jogo em andamento


## Agradecimentos ✌️

> *Obrigado por acessar meu github e conhecer meu projeto. Caso queira enviar sugestões meu email e instagram estarão logo abaixo*
> <br>
>
>
> <a href = "mailto:jhooliveira.lopes@gmail.com"><img src="https://img.shields.io/badge/-Gmail-%23333?style=for-the-badge&logo=gmail&logoColor=white" target="_blank"></a> <a href="https://www.instagram.com/jhonatan_lopes_lmao/?next=%2F" target="_blank"><img src="https://img.shields.io/badge/-Instagram-%23E4405F?style=for-the-badge&logo=instagram&logoColor=white" target="_blank"></a> 
