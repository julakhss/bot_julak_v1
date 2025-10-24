#!/usr/bin/python3
# -*- coding: utf-8 -*-

import logging
import sqlite3
import datetime as DT
import os
import paramiko
import asyncio
import httpx

from telegram import Update, ReplyKeyboardMarkup, KeyboardButton, InputFile
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters, ConversationHandler
from telegram.error import BadRequest
