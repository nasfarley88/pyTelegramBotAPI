# -*- coding: utf-8 -*-
import sys
import time

sys.path.append('../')
from telebot import types
from telebot import apihelper
import telebot


def test_message_listener():
    msg_list = []
    for x in range(100):
        msg_list.append(create_text_message('Message ' + str(x)))

    def listener(messages):
        assert len(messages) == 100

    tb = telebot.TeleBot('')
    tb.set_update_listener(listener)


def test_message_handler():
    tb = telebot.TeleBot('')
    msg = create_text_message('/help')

    @tb.message_handler(commands=['help', 'start'])
    def command_handler(message):
        message.text = 'got'

    tb.process_new_messages([msg])
    time.sleep(1)
    assert msg.text == 'got'


def create_text_message(text):
    params = {}
    params['text'] = text
    return types.Message(1, None, None, 1, 'text', params)


def test_is_string_unicode():
    s1 = u'string'
    assert apihelper.is_string(s1)


def test_is_string_string():
    s1 = 'string'
    assert apihelper.is_string(s1)


def test_not_string():
    i1 = 10
    assert not apihelper.is_string(i1)
