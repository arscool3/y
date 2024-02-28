import streamlit as st

import os
import sys
from pathlib import Path

import django

PROJECT_ROOT_DIR = Path(os.path.abspath(__file__))
DJANGO_ROOT_DIR = PROJECT_ROOT_DIR / "y"


def django_setup() -> None:
    """
    Allows to setup Django if it's not already running on a server. Should be called before any Django imports.
    """
    # Add the project base directory to the sys.path
    sys.path.append(DJANGO_ROOT_DIR.as_posix())

    # The DJANGO_SETTINGS_MODULE has to be set to allow us to access django imports
    os.environ.setdefault(
        "DJANGO_SETTINGS_MODULE", "y.settings"
    )

    # This is for setting up django
    django.setup()


django_setup()

from core.models import Task, Child

if "page" not in st.session_state:
    st.session_state.page = 0

main = st.empty()
sub = st.empty()


def nextpage():
    st.session_state.page += 1
    main.empty()

if st.session_state.page == 0:
    with main.container():

        st.title("привет, нурали и ислам")

        name = st.selectbox(
            'Выбери под кем зайти',
            ('нурали', 'ислам')
        )
        password = st.text_input('Введи пароль', type='password')
        st.session_state.user = Child.objects.get(name=name)
        if st.session_state.user.password == password:
            nextpage()

if st.session_state.page > 0:
    with sub.container():
        # print(user)
        # print(use)
        task = st.session_state.user.tasks.get(id=st.session_state.page)
        st.header(task.title)
        st.subheader(task.text)

        answer = st.text_input('Введи ответ')
        if task.answer == answer:
            task.is_done = True
        task.save()
        nextpage()

