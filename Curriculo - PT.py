from fpdf import FPDF
from PIL import Image
import os

class PDF(FPDF):
    def header(self):
        if self.page_no() == 1 and os.path.exists("/mnt/data/pfp.png"):
            self.image('/mnt/data/pfp.png', 10, 8, 33, 33)
            self.set_line_width(1)
            self.rect(10, 8, 33, 33)
            self.set_font('Arial', 'B', 15)
            self.set_text_color(0, 0, 128)
            self.cell(80)
            self.cell(30, 10, 'Pedro Henrique Alcântara Ramos', 0, 1, 'C')
            self.set_font('Arial', 'I', 12)
            self.cell(80)
            self.cell(30, 10, 'Fullstack | AR+VR | PHP | Javascript | SQL | C#', 0, 1, 'C')
            self.ln(20)
            self.set_text_color(0, 0, 0)
        else:
            self.set_font('Arial', 'I', 8)
            self.cell(0, 10, 'Pedro Henrique Alcântara Ramos - Currículo', 0, 0, 'C')
            self.ln(10)

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.set_text_color(169, 169, 169)
        self.cell(0, 10, 'Página %s' % self.page_no(), 0, 0, 'C')

    def chapter_title(self, title):
        self.set_font('Arial', 'B', 14)
        self.set_fill_color(211, 211, 211)
        self.cell(0, 10, title, 0, 1, 'L', fill=True)
        self.ln(4)

    def chapter_body(self, body):
        self.set_font('Arial', '', 12)
        self.multi_cell(0, 10, body)
        self.ln()

    def section_separator(self):
        self.set_fill_color(0, 0, 128)
        self.cell(0, 1, '', 0, 1, 'C', fill=True)
        self.ln(4)

pdf = PDF()

pdf.add_page()

pdf.chapter_title('Contato:')
pdf.chapter_body("Endereço: Rua Ruy Pinto Bandeira, 310, apt 701, Jardim Camburi, Vitória - ES\n"
                 "Telefone: +55 27 98112-0666\n"
                 "E-mail: ph00.ramos@gmail.com\n"
                 "LinkedIn: https://www.linkedin.com/in/pedro-henrique-alcântara-ramos/\n"
                 "GitHub: https://github.com/Pedro-Brando")
pdf.section_separator()

pdf.chapter_title('Objetivo Profissional:')
pdf.chapter_body("Desejo aplicar minhas habilidades como desenvolvedor Fullstack e em tecnologias AR/VR "
                 "para contribuir em projetos inovadores. Estou buscando oportunidades para crescimento profissional "
                 "e para trabalhar em ambientes colaborativos que desafiem minhas habilidades técnicas.")
pdf.section_separator()

pdf.chapter_title('Resumo:')
pdf.chapter_body("Desenvolvedor apaixonado por jogos e tecnologias de realidade virtual. Estudante de Ciência da Computação "
                 "com experiência em PHP, Laravel e Javascript, além de desenvolvimento de jogos em C# com Unity e suas tecnologias "
                 "VR/AR. Buscando continuamente aprender e crescer profissionalmente. Aberto a novas oportunidades e conexões na área "
                 "de desenvolvimento.")
pdf.section_separator()

pdf.chapter_title('Experiência Profissional:')
experiencias = [
    {
        "empresa": "Penumbra Digital LTDA",
        "cargo": "Desenvolvedor PHP Fullstack Júnior",
        "periodo": "Março de 2024 - Presente",
        "local": "Bahia, Brasil (Remota)",
        "descricao": [
            "Desenvolvimento de aplicações web usando Laravel, PHP e JavaScript.",
            "Front-end responsivo e interativo com HTML e CSS.",
            "Gerenciamento de bancos de dados MySQL."
        ]
    },
    {
        "empresa": "Microcamp",
        "cargo": "Professor de Games/Unity",
        "periodo": "Março de 2023 - Agosto de 2023",
        "local": "Vitória, Espírito Santo, Brasil",
        "descricao": [
            "Ensino de desenvolvimento de jogos em Unity e C# para turmas de alunos.",
            "Criação de materiais didáticos e planos de aula personalizados para cada turma.",
            "Acompanhamento e orientação individual dos alunos em seus projetos de jogos.",
            "Participação em reuniões pedagógicas e workshops para aprimoramento de metodologias e técnicas de ensino."
        ]
    },
    {
        "empresa": "Vale",
        "cargo": "Unity Developer (VR)",
        "periodo": "Janeiro de 2021 - Junho de 2022",
        "local": "Vila Velha, Espírito Santo, Brasil (Remota)",
        "descricao": [
            "Participação em um projeto de virtualização de sistemas em colaboração com a Vale no laboratório de realidade virtual da UVV.",
            "Desenvolvimento de aplicativo em C# com Unity para simulação de processos industriais.",
            "Criação de ambientes virtuais interativos para treinamento de trabalhadores e melhoria de segurança no trabalho.",
            "Colaboração com equipe multidisciplinar para aprimorar o desenvolvimento de tecnologias em realidade virtual."
        ]
    }
]

for exp in experiencias:
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(0, 10, exp["empresa"], 0, 1)
    pdf.set_font("Arial", 'I', 12)
    pdf.cell(0, 10, f"{exp['cargo']} - {exp['periodo']}", 0, 1)
    pdf.cell(0, 10, f"Local: {exp['local']}", 0, 1)
    pdf.set_font("Arial", '', 12)
    for desc in exp["descricao"]:
        pdf.multi_cell(0, 10, f"- {desc}")
    pdf.ln(5)
pdf.section_separator()

pdf.chapter_title('Formação Acadêmica:')
pdf.chapter_body("Universidade Vila Velha - UVV\n"
                 "Superior Cursando em Ciência da Computação (2020 - 2025)\n"
                 "UPVIX União de Professores - UP\n"
                 "Ensino Médio Completo (2016-2018)")
pdf.section_separator()

pdf.chapter_title('Certificações e Cursos Complementares:')
certificacoes = [
    "CCNA: Switching, Routing, and Wireless Essentials - Cisco (Emitido em Junho de 2024)",
    "CCNA: Introduction to Networks - Cisco (Emitido em Dezembro de 2023)"
]
for cert in certificacoes:
    pdf.chapter_body(f"- {cert}")
pdf.section_separator()

pdf.chapter_title('Idiomas:')
idiomas = [
    "Inglês: Fluente ou nativo",
    "Português: Fluente ou nativo"
]
for idioma in idiomas:
    pdf.chapter_body(f"- {idioma}")
pdf.section_separator()

pdf.chapter_title('Projetos:')
projetos = [
    {
        "nome": "VR Ping Pong",
        "periodo": "Maio de 2021 - Maio de 2021",
        "associado": "Associado(s) a Vale",
        "descricao": "Simulador de Ping Pong em VR feito em Unity para treinamento.",
        "competencias": "Competências: Desenvolvimento de jogos eletrônicos"
    },
    {
        "nome": "Hangman",
        "periodo": "Março de 2021 - Março de 2021",
        "associado": "Associado(s) a Vale",
        "descricao": "Jogo da forca feito em Unity para treinamento.",
        "competencias": "Competências: Desenvolvimento de jogos eletrônicos"
    },
    {
        "nome": "Run, Merlin!",
        "periodo": "Dezembro de 2020 - Dezembro de 2020",
        "descricao": "Projeto de jogo no estilo 'Infinity Runner' para o processo seletivo do projeto LawVR da UVV em colaboração com a Vale.",
        "competencias": "Competências: Desenvolvimento de jogos eletrônicos",
        "git": "Scripts no GitHub: https://github.com/Pedro-Brando/Selecao-VR-2020-2"
    },
    {
        "nome": "Sheep Saviour",
        "periodo": "Dezembro de 2020 - Dezembro de 2020",
        "descricao": "Jogo criado para a CEET Game Jam, feito em 5 dias.",
        "competencias": "Competências: Desenvolvimento de jogos eletrônicos",
        "git": "Scripts no GitHub: https://github.com/Pedro-Brando/CEET_game_jam"
    }
]

for proj in projetos:
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(0, 10, proj["nome"], 0, 1)
    pdf.set_font("Arial", 'I', 12)
    pdf.cell(0, 10, f"Período: {proj['periodo']}", 0, 1)
    if "associado" in proj:
        pdf.cell(0, 10, f"Associado: {proj['associado']}", 0, 1)
    pdf.set_font("Arial", '', 12)
    pdf.multi_cell(0, 10, f"Descrição: {proj['descricao']}")
    pdf.multi_cell(0, 10, f"Competências: {proj['competencias']}")
    if "git" in proj:
        pdf.multi_cell(0, 10, f"Git: {proj['git']}")
    pdf.ln(5)
pdf.section_separator()

output_path = "/mnt/data/Curriculo_Pedro_Henrique_Alcantara_Ramos.pdf"
pdf.output(output_path)

output_path
