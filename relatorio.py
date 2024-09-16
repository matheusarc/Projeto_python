from fpdf import FPDF

class PDF(FPDF):

    def titulo(self, label):
        self.set_font('helvetica', 'B', size=24)
        self.cell(0, 60, label, 0, 1, 'C')

    def sub_titulo(self, label):
        self.set_font('helvetica', 'I', size=16)
        self.cell(0, 10, label, 0, 1, 'C')
    
    def linha_centralizada(self, label):
        self.set_font('helvetica', '', size=12)
        self.cell(0, 10, label, 0, 1, 'C')
    
    def titulo_base(self, label):
        self.set_font('helvetica', 'B', size=16)
        self.cell(0, 8, label, 0, 1, 'L')
        self.ln()
        
    def destaque(self, label):
        self.set_font('helvetica', 'B', size=14)
        self.cell(0, 4, label, 0, 1, 'L')
        self.ln()

    def paragrafo(self, text):
        self.set_font('helvetica', '', size=12)
        self.multi_cell(0, 6, text)
        self.ln()

    def imagem(self, img, x, y, w):
        self.image(img, x, y, w)

pdf = PDF()

#capa
pdf.add_page()

pdf.titulo("Análise educacional Brasileira")
pdf.image("img_capa.webp", 40, 90, 130)
pdf.ln(160)

#pag
pdf.add_page()

pdf.titulo_base("Introdução")

pdf.paragrafo("A educação é um dos fundamentos essenciais para a construção de uma sociedade mais equitativa e justa. Embora o Brasil tenha registrado importantes progressos nas últimas décadas, ainda existem desafios que afetam tanto a qualidade quanto a quantidade da educação oferecida, especialmente no ensino superior. ")

pdf.paragrafo("Esses desafios estão relacionados a fatores regionais, econômicos, sociais e administrativos, que geram uma diversidade de realidades complexas em um país de grande extensão territorial. Com isso, é evidente que esforços contínuos são necessários para superar essas desigualdades e proporcionar uma educação de qualidade para todos.")


#pag
pdf.add_page()

pdf.destaque("Distribuição de categorias administrativas por regiões brasileiras")

pdf.paragrafo("Os gráficos mostram que as regiões Sudeste e Nordeste concentram a maioria das vagas, influenciadas pela densidade populacional e grandes centros urbanos. O Sudeste, com a maior oferta, destaca-se em número de vagas, mas essa concentração pode agravar as desigualdades no acesso à educação de qualidade em outras partes do país.")

pdf.imagem("Gráfico_Categorias_Adm_Região_CENTRO_OESTE.png", 40, 50, 130)
pdf.imagem("Gráfico_Categorias_Adm_Região_IGNORADO_EXTERIOR.png", 40, 140, 130)
pdf.imagem("Gráfico_Categorias_Adm_Região_NORDESTE.png", 40, 230, 130)

pdf.add_page()
pdf.imagem("Gráfico_Categorias_Adm_Região_NORTE.png", 40, 50, 130)
pdf.imagem("Gráfico_Categorias_Adm_Região_SUDESTE.png", 40, 140, 130)
pdf.imagem("Gráfico_Categorias_Adm_Região_SUL.png", 40, 230, 130)


#pag
pdf.add_page()

pdf.destaque("Distribuição de modalidades de cursos no Brasil")

pdf.paragrafo("O gráfico a seguir mostra a evidente diferença entre as duas modalidades distintas no Brasil, com uma diferença de 85% a modalidade EAD vem ganhando cada vez mais força após o ano de 2020, onde a pandemia alavancou este tipo de ensino a distância, além de ter outros fatores por ele ser preferido pela grande maioria dos alunos de ensino superior, o preço mais em conta e também o fato de que a modalidade permite que os alunos consigam um controle melhor do tempo de estudos.")

pdf.imagem("Gráfico_Modalidade_Ensino.png", 40, 70, 100)


#pag
pdf.add_page()

pdf.paragrafo('É evidente que uma parcela significativa da população escolhe ingressar em instituições privadas, sejam elas com ou sem fins lucrativos. Esse comportamento é impulsionado, em grande parte, pela intensa concorrência por vagas em universidades públicas, que reduz significativamente as oportunidades de acesso. Além disso, muitos estudantes, especialmente aqueles que precisam equilibrar trabalho e sustento familiar, enfrentam dificuldades para dedicar o tempo necessário aos estudos, o que torna ainda mais desafiador competir por essas vagas tão disputadas.')
pdf.imagem('Categoria_Administrativas.png', 13, 50, 175)


#final
pdf.add_page()

pdf.titulo_base("Conclusão")

pdf.paragrafo("A análise mostra que ainda há uma grande desigualdade na distribuição de vagas de ensino superior no Brasil, principalmente entre regiões. O Sudeste e o Nordeste concentram a maioria das vagas devido a fatores econômicos e demográficos. A educação a distância tem crescido bastante, mas o acesso à tecnologia ainda é um desafio para muitos, especialmente em áreas remotas. Além disso, as instituições privadas com fins lucrativos, em especial no Sudeste, acabam criando barreiras para estudantes de baixa renda. Embora tenha havido avanços, é necessário que políticas públicas ajudem a tornar a educação superior mais acessível e justa para todos.")

pdf.output("relatório.pdf")