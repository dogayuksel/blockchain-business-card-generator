#!/usr/bin/python
# -*- coding: utf-8 -*-
from CreatePDF import CreatePDF
from SolveHash import SolveHash

number_of_cards = 10

start_block_no = 0
start_block_hash = '{0}'.format(''.join(map(str, [0] * 32)))

name = 'Doga'
surname = 'Yuksel'
title = 'Frontend Developer'
phone_number = '0176 80783662'
e_mail = 'doga@konfid.io'

prev_block_hash_array = []
nonce_array = []
block_hash_array = []

block_hash_array.append(start_block_hash)

start_index = start_block_no
last_index = start_index + number_of_cards

for i in range(start_index, last_index):
    sh = SolveHash(
        i,
        block_hash_array[-1],
        name,
        surname,
        title,
        phone_number,
        e_mail
    )
    nonce, hash = sh.solve()
    print i, nonce, hash
    nonce_array.append(nonce)
    block_hash_array.append(hash)

CreatePDF(
    start_block_no,
    number_of_cards,
    nonce_array,
    name,
    surname,
    title,
    phone_number,
    e_mail,
    block_hash_array
)
