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
            self.cell(0, 10, 'Pedro Henrique Alcântara Ramos - Resume', 0, 0, 'C')
            self.ln(10)

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.set_text_color(169, 169, 169)
        self.cell(0, 10, 'Page %s' % self.page_no(), 0, 0, 'C')

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

pdf.chapter_title('Contact:')
pdf.chapter_body("Address: Rua Ruy Pinto Bandeira, 310, apt 701, Jardim Camburi, Vitória - ES\n"
                 "Phone: +55 27 98112-0666\n"
                 "E-mail: ph00.ramos@gmail.com\n"
                 "LinkedIn: https://www.linkedin.com/in/pedro-henrique-alcântara-ramos/\n"
                 "GitHub: https://github.com/Pedro-Brando")
pdf.section_separator()

pdf.chapter_title('Career Objective:')
pdf.chapter_body("I aim to apply my skills as a Fullstack developer and in AR/VR technologies "
                 "to contribute to innovative projects. I am seeking opportunities for professional growth "
                 "and to work in collaborative environments that challenge my technical abilities.")
pdf.section_separator()

pdf.chapter_title('Summary:')
pdf.chapter_body("Developer passionate about games and virtual reality technologies. Computer Science student "
                 "with experience in PHP, Laravel, and Javascript, as well as game development in C# with Unity and its VR/AR technologies. "
                 "Continuously seeking to learn and grow professionally. Open to new opportunities and connections in the development field.")
pdf.section_separator()

pdf.chapter_title('Professional Experience:')
experiencias = [
    {
        "empresa": "Penumbra Digital LTDA",
        "cargo": "Junior PHP Fullstack Developer",
        "periodo": "March 2024 - Present",
        "local": "Bahia, Brazil (Remote)",
        "descricao": [
            "Development of web applications using Laravel, PHP, and JavaScript.",
            "Responsive and interactive front-end with HTML and CSS.",
            "Database management with MySQL."
        ]
    },
    {
        "empresa": "Microcamp",
        "cargo": "Games/Unity Teacher",
        "periodo": "March 2023 - August 2023",
        "local": "Vitória, Espírito Santo, Brazil",
        "descricao": [
            "Teaching game development in Unity and C# to student groups.",
            "Creating educational materials and lesson plans tailored to each class.",
            "Individual student guidance on their game projects.",
            "Participation in pedagogical meetings and workshops to improve teaching methodologies and techniques."
        ]
    },
    {
        "empresa": "Vale",
        "cargo": "Unity Developer (VR)",
        "periodo": "January 2021 - June 2022",
        "local": "Vila Velha, Espírito Santo, Brazil (Remote)",
        "descricao": [
            "Participation in a system virtualization project in collaboration with Vale at UVV's virtual reality lab.",
            "Development of an application in C# with Unity for industrial process simulation.",
            "Creation of interactive virtual environments for worker training and safety improvement.",
            "Collaboration with a multidisciplinary team to enhance the development of virtual reality technologies."
        ]
    }
]

for exp in experiencias:
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(0, 10, exp["empresa"], 0, 1)
    pdf.set_font("Arial", 'I', 12)
    pdf.cell(0, 10, f"{exp['cargo']} - {exp['periodo']}", 0, 1)
    pdf.cell(0, 10, f"Location: {exp['local']}", 0, 1)
    pdf.set_font("Arial", '', 12)
    for desc in exp["descricao"]:
        pdf.multi_cell(0, 10, f"- {desc}")
    pdf.ln(5)
pdf.section_separator()

pdf.chapter_title('Academic Background:')
pdf.chapter_body("Vila Velha University - UVV\n"
                 "Bachelor's in Computer Science (2020 - 2025)\n"
                 "UPVIX União de Professores - UP\n"
                 "High School Diploma (2016-2018)")
pdf.section_separator()

pdf.chapter_title('Certifications and Additional Courses:')
certificacoes = [
    "CCNA: Switching, Routing, and Wireless Essentials - Cisco (Issued in June 2024)",
    "CCNA: Introduction to Networks - Cisco (Issued in December 2023)"
]
for cert in certificacoes:
    pdf.chapter_body(f"- {cert}")
pdf.section_separator()

pdf.chapter_title('Languages:')
idiomas = [
    "English: Fluent or native",
    "Portuguese: Fluent or native"
]
for idioma in idiomas:
    pdf.chapter_body(f"- {idioma}")
pdf.section_separator()

pdf.chapter_title('Projects:')
projetos = [
    {
        "nome": "VR Ping Pong",
        "periodo": "May 2021 - May 2021",
        "associado": "Associated with Vale",
        "descricao": "VR Ping Pong simulator made in Unity for training.",
        "competencias": "Skills: Game development"
    },
    {
        "nome": "Hangman",
        "periodo": "March 2021 - March 2021",
        "associado": "Associated with Vale",
        "descricao": "Hangman game made in Unity for training.",
        "competencias": "Skills: Game development"
    },
    {
        "nome": "Run, Merlin!",
        "periodo": "December 2020 - December 2020",
        "descricao": "Infinity Runner style game project for the LawVR project selection process at UVV in collaboration with Vale.",
        "competencias": "Skills: Game development",
        "git": "Scripts on GitHub: https://github.com/Pedro-Brando/Selecao-VR-2020-2"
    },
    {
        "nome": "Sheep Saviour",
        "periodo": "December 2020 - December 2020",
        "descricao": "Game created for the CEET Game Jam, made in 5 days.",
        "competencias": "Skills: Game development",
        "git": "Scripts on GitHub: https://github.com/Pedro-Brando/CEET_game_jam"
    }
]

for proj in projetos:
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(0, 10, proj["nome"], 0, 1)
    pdf.set_font("Arial", 'I', 12)
    pdf.cell(0, 10, f"Period: {proj['periodo']}", 0, 1)
    if "associado" in proj:
        pdf.cell(0, 10, f"Associated with: {proj['associado']}", 0, 1)
    pdf.set_font("Arial", '', 12)
    pdf.multi_cell(0, 10, f"Description: {proj['descricao']}")
    pdf.multi_cell(0, 10, f"Skills: {proj['competencias']}")
    if "git" in proj:
        pdf.multi_cell(0, 10, f"Git: {proj['git']}")
    pdf.ln(5)
pdf.section_separator()

output_path = "/mnt/data/Curriculum_Pedro_Henrique_Alcantara_Ramos.pdf"
pdf.output(output_path)

output_path
