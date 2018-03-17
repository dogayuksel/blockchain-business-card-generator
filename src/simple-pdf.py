from fpdf import FPDF
from SolveHash import SolveHash

start_block_no = 0
start_block_hash = '{0}'.format(''.join(map(str, [0] * 32)))

name = 'Doga'
surname = 'Yuksel'
title = 'Frontend Developer'
phone_number = '0176 80783662'
e_mail = 'doga@konfid.io'

DEBUG = True

sh = SolveHash(
    start_block_no,
    start_block_hash,
    name,
    surname,
    title,
    phone_number,
    e_mail)

nonce, hash = sh.solve()


def do_header(pdf):
    global start_block_no
    pdf.set_fill_color(240)
    pdf.set_text_color(120)
    pdf.set_font('Courier', '', 12)
    pdf.cell(
        40,
        4,
        'Block #{0}'.format(start_block_no),
        fill=DEBUG
    )
    start_block_no = start_block_no + 1
    pdf.ln()
    pdf.cell(40, 4, 'Parent Hash', fill=DEBUG)
    pdf.ln()
    pdf.set_font('Courier', '', 7)
    pdf.cell(
        50,
        3,
        start_block_hash,
        fill=DEBUG
    )
    pdf.ln(10)
    pdf.line(5, 15, 54, 15)


def do_body(pdf):
    pdf.set_fill_color(240)
    pdf.set_text_color(0)
    pdf.set_font('Arial', 'B', 16)
    pdf.cell(50, 8, name, fill=DEBUG)
    pdf.ln()
    pdf.cell(50, 8, surname, fill=DEBUG)
    pdf.ln(12)
    pdf.set_font('Arial', 'B', 12)
    pdf.cell(50, 5, title, fill=DEBUG)
    pdf.ln()
    pdf.cell(50, 5, phone_number, fill=DEBUG)
    pdf.ln()
    pdf.cell(50, 5, e_mail, fill=DEBUG)
    pdf.ln()


def do_footer(pdf):
    pdf.set_fill_color(240)
    pdf.set_text_color(120)
    pdf.line(4, 64, 54, 64)
    pdf.set_xy(4, 65)
    pdf.set_font('Courier', '', 12)
    pdf.cell(
        15,
        4,
        'Nonce',
        fill=DEBUG
    )
    pdf.set_font('Courier', '', 7)
    pdf.cell(
        20,
        4,
        '{0}'.format(nonce),
        fill=DEBUG
    )
    pdf.ln()
    pdf.set_font('Courier', '', 12)
    pdf.cell(40, 4, 'Block Hash', fill=DEBUG)
    pdf.ln()
    pdf.set_font('Courier', '', 7)
    pdf.cell(
        50,
        3,
        hash,
        fill=DEBUG
    )


pdf = FPDF('P', 'mm', (55, 84))
pdf.set_margins(4, 4, 4)
pdf.set_auto_page_break(False)

for x in range(10):
    pdf.add_page()
    do_header(pdf)
    do_body(pdf)
    do_footer(pdf)

pdf.output('simple-test.pdf', 'F')
