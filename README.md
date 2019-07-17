#Gestão de comissões Televendas


##Squad 4:
- [Fábio Matheus Mantelli](https://github.com/fabiomantelli)
- [Fillipe Calza](https://github.com/fcalza)
- [Julio Cezar Riffel](https://github.com/julioriffel)
- [Luan Fernando de Souza Ferreira](https://github.com/luanfsf)
- [Paulo Rogerio Kraemer](https://github.com/paulork)


##Objetivo
O objetivo desse produto é de calcular a comissão que cada vendedor do sistema ao longo dos meses seguindo a regra de comissão selecionada na hora que o vendedor for cadastrado. Seu objetivo é implementar os requisitos listados abaixo e criar uma API para que diferentes front-ends possam interagir com o seu sistema.

##Contextualização
Uma empresa de televendas gostaria de armazenar e calcular a comissão dos seus vendedores ao longo do tempo de acordo com o plano de comissão que eles escolheram. Para isso eles precisam de um sistema que fará tal cálculo da comissão ao adicionar o valor mensal das vendas no sistema. A empresa também precisa saber se as vendas dos seus vendedores estão satisfatórias através do cálculo da média ponderada dos valores de vendas nos últimos meses, e caso não esteja eles deverão ser notificados através do email.

##Requisitos técnicos obrigatórios
- Cadastrar Vendedores

Cadastro dos vendedores de telemarketing que irão receber comissões. Para o cadastro é necessário o nome, endereço, telefone, idade, email, CPF e o plano de comissões.

Exemplo de requisição para cadastrar um vendedor:

**POST /sellers**

`{“name”: “José Vendedor”, “address”: “Rua abcd, 123”, “telefone”: “48012345678”, “idade”: 30, “email”: “email@email.com”, “cpf”: “12345678910”, “commission_plan”: 1}`

Retorno:


`201 Created {“id”: 100}`

___
- Cadastrar plano de comissões

Cadastro dos planos de comissões para que os vendedores possam escolher qual o melhor plano para eles. Para cadastrar um novo plano é necessário definir qual a porcentagem menor, o valor mínimo que será necessário para considerar a porcentagem de comissão maior e a porcentagem maior. Exemplo: se o vendedor vender até 5000 R$ ele vai receber 2% de comissão, caso o valor seja acima de 5000 R$ ele irá receber 5% de comissão.

Exemplo de planos:

|**Porcentagem Menor**|	**Valor mínimo¹** |	**Porcentagem maior**|
|---|---|---|
|2,5% |R$ 15.000	|15%|
|5%	|R$ 50.000 |12,5%|
|2%	|R$100.000 |25%|

¹para pagar a porcentagem maior

Exemplo de requisição para cadastrar um plano de comissão:

**POST /comissions**

`{“lower_percentage”: 2.5, “min_value”: 5000.00, “upper_percentage”: 10.50}`

Retorno:

`201 Created
{“id”: 10}`

___
- Registrar vendas mensais

Registrar o valor das vendas mensais de cada vendedor para que o sistema possa calcular a comissão de acordo com o plano de comissões escolhido. Para o cálculo será necessário informar qual o vendedor, o mês (em números) que ele fez as vendas e o valor da vendas.

Exemplo de requisição para calcular o valor da comissão do vendedor:

**POST /month_comission**

`{“seller”: 10, “amount”: 10000.00, “month”: 2}`

**Retorno:**

`200 OK
{“id”: 100, “comission”: 300.89}`

___
- Calcular comissão dos vendedores


Ao registrar a venda de um vendedor será necessário também calcular o valor da comissão dele sobre as vendas. O cálculo da comissão deve verificar o valor da venda e calcular a porcentagem porcentagem de acordo com o plano de comissão que estiver cadastrado naquele vendedor. O resultado do cálculo da comissão deve ser armazenado para que seja possível consultar o histórico das comissões do vendedor. Esse cálculo deve ser feito quando a comissão for cadastrada considerando o plano escolhido pelo vendedor.

___

- Recuperar lista de vendedores ordenados pelo valor da comissão

Recuperar a lista dos vendedores ordenados pelo valor de suas comissões. Para consultar a lista será necessário informar qual o mês atual para que possa ser feito o filtro e a ordenação dos valores. Quando o vendedor não tiver comissão no mês selecionado deve-se considerar 0,00 R$. OBS: Esse endpoint pode ser feito juntamente com o endpoint de vendedores mas não é obrigatório.

Exemplo de requisição para recuperar a lista de vendedores ordenados:

**GET /vendedores/2**

Resposta:

`200 OK

[{“name”: “Vendedor1”, “id”: 10, “comission”: 1000.00}, {“name”: “Vendedor2”, “id”: 15, “comission”: 900.00}]
`

___
- Enviar notificação aos vendedores que estão com a média de comissão baixa nos últimos meses

Enviar uma notificação via email para o vendedor que não obtiver um valor acima do cálculo da média de comissões. Para calcular a média do vendedor, deve calcular a média ponderada dos últimos 5 meses desse vendedor considerando os maiores valores com os maiores pesos e se ele estiver abaixo em pelo menos 10% do valor da média deve-se enviar uma notificação para ele. Exemplo:



|**Mês**   |**Valor**   |**Peso**    |
|---|---|---|
|01|1000|R$ 2|
|02|	500 |R$ 1|
|03	|1100 |R$ 3|
|Média| |R$ 966,67|

Esse vendedor não deve ser notificado caso o valor do mês atual seja maior do que 966,67 R$ - 10% (870,00 R$).

Para efetuar a verificação, pode-se criar um endpoint que irá receber o valor atual de vendas e o ID do vendedor para calcular. Caso ele esteja abaixo do valor calculado uma notificação por email deve ser enviada para ele. Se não tiver o histórico de 5 meses basta considerar a quantidade de meses existentes para o cálculo. O cálculo sempre considera o mês corrente.

Exemplo de requisição para verificar se o vendedor deve ser notificado:

**POST /check_commision**

`{“seller”: 10, “amount”: 1000.65}`

Resposta:

`200 OK 
{“should_notify”: true}`


________
##Sobre a apresentação do projeto

Para que todos do grupo tenham a chance de apresentar seu trabalho, a apresentação deve ser feita de forma individual. Vocês podem ensaiar juntos, fazer um roteiro parecido, mas é importante que cada participante faça sua própria gravação.

Objetividade é muito importante - falem naturalmente e sem ler, por favor! :) Recomendamos que você faça um video-call e gravem este call. Assim, poderão ficar à vontade para compartilhar a tela e mostrar o código ou qualquer outra coisa importante. O vídeo deve ter no máximo 10 minutos.

Segue uma sugestão de roteiro:

Apresentação pessoal
“Oi, pessoal…, eu me chamo _____ e vou apresentar para vocês o projeto final que fiz com a squad ______(número e nome) da Aceleração _______ da Codenation.”

#### Apresentação do projeto

- Os membros da squad;
- Descrição do projeto e desenvolvimento do processo que a squad utilizou para resolver o problema;
- Divisão de tarefas entre os membros da squad e quais foram suas principais responsabilidades;
- Tecnologias utilizadas e eficácia;
- Aprendizados destacados durante o processo e ao final do projeto;
- Duas principais dificuldades, e como foram contornadas;
- Dois principais acertos ou escolhas acertadas que fizeram diferença no projeto e por quê.


Para ficar mais fácil, dê uma olhada nesta apresentação de projeto de um programa que realizamos em Joinville.
 https://drive.google.com/file/d/1Owc4VYM492svCn7RlMnNs_Bk4ZGjZkvj/view
 Neste caso, os participantes desenvolveram em squads uma aplicação (backend e frontend) que buscava anunciar animais perdidos ou animais para adoção. Assim, pessoas interessadas poderiam colaborar para adotar e/ou encontrar um pet. Fiz alguns comentários na apresentação para ajudar vocês! :)

####Como enviar os vídeos?

Após terem determinado o roteiro e feito suas gravações individuais, encaminhe por e-mail o link do vídeo no YouTube (lembre de colocá-lo como não listado, por favor). No título, use a seguinte descrição: “Apresentação projeto final [Seu Nome] [nome de sua squad]” . O link do vídeo deve ser enviado para mario.machado@codenation.dev e ingrid.adam@codenation.dev, juntamente com o link do Code Review do projeto na plataforma Codenation, com o assunto “AceleraDev Python - Squad [nº da sua squad]” até o dia 31/07/2019.