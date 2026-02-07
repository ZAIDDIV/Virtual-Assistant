Virtual Assistant

A lightweight, boot-time voice-activated virtual assistant built with Python and integrated with a Rainmeter voice visualization skin. The assistant listens for a predefined wake phrase, launches authorized applications, and then terminates itself along with Rainmeter to maintain optimal system performance.

Overview

This project is designed to run automatically when the system starts. It continuously listens for a user-defined wake phrase through the microphone. Once the wake phrase is detected, the assistant launches specific applications using predefined file paths and then cleanly shuts down all related background processes.

A Rainmeter Voice Bar skin is used to visually indicate microphone activity while the assistant is listening.

Key Features

Automatic execution on system startup

Voice recognition using microphone input

Custom wake phrase detection

Application launching via predefined executable paths

Automatic self-termination after task execution

Automatic Rainmeter shutdown for performance optimization

Real-time microphone activity visualization using Rainmeter

Lightweight and resource-efficient design

Technologies Used
Programming Language

Python 3.x

Python Libraries
import speech_recognition as sr
import os
import pyttsx3
import sys
import time

Library Usage

speech_recognition – Captures and processes voice commands

pyttsx3 – Text-to-speech functionality

os – Application execution and process handling

sys – Script control and termination

time – Execution timing and delays

How It Works

The system boots up

The virtual assistant starts automatically

Rainmeter Voice Bar skin launches with microphone access

The assistant listens for the configured wake phrase

Upon detection:

Authorized applications are launched using their file paths

After execution:

The Python assistant terminates itself

Rainmeter is also closed to free system resources

Customization

The project allows customization of:

Wake phrase

Application executable paths

Startup behavior

Rainmeter skin design and behavior

Only applications explicitly defined by the user can be launched.

Requirements

Windows operating system

Python 3.x installed

Microphone access enabled

Rainmeter installed

Notes

Designed for efficiency and minimal background usage

No unnecessary persistent processes

Suitable for personal automation and voice-controlled system experiments
