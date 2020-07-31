# Como eu fiz o desafio
## tsv_parser.py  
Primeiramente eu desenvolvi um script que extrai as informações dos arquivos .tsv 
fornecidos e salva-as em uma database (data.db).   
O programa é altamente versátil porquê permite que o programador especifique qual arquivo ele deseja extrair e quais colunas também, filtrando apenas as informações necessárias.  
Caso você deseje utilizar esse arquivo para outros fins, é possivel mudar as especificações default, na lista **'info_to_be_parsed', linha 81**  
O programa descarta linhas com erros de encoding ou com caracteres ilegíveis, também contabiliza-os e salva as informações na database, na table de nome **'errors'**  
  
### Dúvida sobre a contabilização dos erros
Entretanto, fiquei na dúvida como deveria contabilizar e descartar os erros, eu espereva um UnidecodeError que seria facilmente localizado e contabilizado, porém nenhum erro desse tipo aconteceu.  
Um tempo depois descobri que havia umas caracteres estranhas como 'υφ' em alguns nomes, então os erros contablizados e colunas descartadas são as que continham essas caracteres.  
   
    
   
##data_processors.py
Esse arquivo é responsavel pela filtragem e processamento da data fornecida. O método **JOIN** fornecido pela linguagem SQL e o **defaultdict** pelo próprio Python foram muito eficientes nisso.

##graph_builder.py
Esse arquivo é o responsavel pela construção dos gráficos e conversão para json, para serem futuramente inseridos no html da página, usei a biblioteca **Plotly**.
## app.py  
Agora ficou fácil, foi só criar uma aplicação web com o Flask e definir seus endpoints apontando para as funções em **functions/data_processors.py** e **functions/graph_buildes.py**

