from fpdf import FPDF

DEBUG = False


class CreatePDF:
    def __init__(
        self,
        start_block_no,
        number_of_cards,
        nonce_array,
        name,
        surname,
        title,
        phone_number,
        e_mail,
        hash_array
    ):
        self.start = start_block_no

        self.nonce_array = nonce_array
        self.name = name
        self.surname = surname
        self.title = title
        self.phone_number = phone_number
        self.e_mail = e_mail
        self.hash_array = hash_array

        self.pdf = FPDF('P', 'mm', (55, 84))
        self.pdf.set_margins(4, 4, 4)
        self.pdf.set_auto_page_break(False)

        start_index = start_block_no
        last_index = start_index + number_of_cards

        for i in range(start_index, last_index):
            self.pdf.add_page()
            self.do_header(i)
            self.do_body()
            self.do_footer(i)

        self.pdf.output('simple-test.pdf', 'F')

    def do_header(self, i):
        self.pdf.set_fill_color(240)
        self.pdf.set_text_color(120)
        self.pdf.set_font('Courier', '', 12)
        self.pdf.cell(
            40,
            4,
            'Block #{0}'.format(i),
            fill=DEBUG
        )
        self.pdf.ln()
        self.pdf.cell(40, 4, 'Parent Hash', fill=DEBUG)
        self.pdf.ln()
        self.pdf.set_font('Courier', '', 7)
        self.pdf.cell(
            50,
            3,
            self.hash_array[i - self.start],
            fill=DEBUG
        )
        self.pdf.ln(10)
        self.pdf.line(5, 15, 54, 15)

    def do_body(self):
        self.pdf.set_fill_color(240)
        self.pdf.set_text_color(0)
        self.pdf.set_font('Arial', 'B', 16)
        self.pdf.cell(50, 8, self.name, fill=DEBUG)
        self.pdf.ln()
        self.pdf.cell(50, 8, self.surname, fill=DEBUG)
        self.pdf.ln(12)
        self.pdf.set_font('Arial', 'B', 12)
        self.pdf.cell(50, 5, self.title, fill=DEBUG)
        self.pdf.ln()
        self.pdf.cell(50, 5, self.phone_number, fill=DEBUG)
        self.pdf.ln()
        self.pdf.cell(50, 5, self.e_mail, fill=DEBUG)
        self.pdf.ln()

    def do_footer(self, i):
        self.pdf.set_fill_color(240)
        self.pdf.set_text_color(120)
        self.pdf.line(4, 64, 54, 64)
        self.pdf.set_xy(4, 65)
        self.pdf.set_font('Courier', '', 12)
        self.pdf.cell(
            15,
            4,
            'Nonce',
            fill=DEBUG
        )
        self.pdf.set_font('Courier', '', 7)
        self.pdf.cell(
            20,
            4,
            '{0}'.format(self.nonce_array[i - self.start]),
            fill=DEBUG
        )
        self.pdf.ln()
        self.pdf.set_font('Courier', '', 12)
        self.pdf.cell(40, 4, 'Block Hash', fill=DEBUG)
        self.pdf.ln()
        self.pdf.set_font('Courier', '', 7)
        self.pdf.cell(
            50,
            3,
            str(self.hash_array[i + 1 - self.start]),
            fill=DEBUG
        )
