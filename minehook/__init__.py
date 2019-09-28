"""
Minehook is a Python library utilizing Flask and PyCraft that simplifies making webhook actions in your minecraft world.
"""
from threading import Thread
from flask import Flask, abort, request
from minecraft.networking.connection import Connection
from minecraft.networking.packets import Packet, clientbound, serverbound

webserver = Flask("")

version = "3"

class Parameter:
    def __init__(self, command_parameter: str):
        self.content = command_parameter

class JSONKey:
    def __init__(self, json_key: str):
        self.content = json_key

class Command:
    def __init__(self, command: str):
        self.content = command

class ChatMessage:
    def __init__(self, message: str):
        self.content = message

address = None
port = 25565
username = "minehook"

commands = {}

def add_hook(url: str,action,*args):
    command = {}
    command["action"] = action
    command_params = []
    for arg in args:
        command_params.append(arg)
    command["params"] = command_params
    commands[url] = command


def __minecraft_chat():
    print('Minehook : Connecting...')
    global connection
    connection = Connection(address, port, username=username)

    def on_join(join_game_packet):
        print('Minehook : Connected to server.')

    connection.register_packet_listener(
        on_join, clientbound.play.JoinGamePacket)

    connection.connect()

def __packet_send(command,jsonData):
    packet = serverbound.play.ChatPacket()
    commandArgs = []
    if "params" in commands[command]:
        for arg in commands[command]["params"]:
            if isinstance(arg,Parameter):
                commandArgs.append(arg.content)
            elif isinstance(arg,JSONKey):
                commandArgs.append(jsonData[arg.content])

    if isinstance(commands[command]["action"],Command):
        packet.message = "/" + commands[command]["action"].content

    elif isinstance(commands[command]["action"],ChatMessage):
        packet.message = commands[command]["action"].content

    packet.message = packet.message + " " + " ".join(commandArgs)
    connection.write_packet(packet)

def run():
    @webserver.route('/<command>')
    def execute(command):
        if not command in commands: abort(404)
        jsonData = request.get_json()
        print(jsonData)
        send = Thread(target=__packet_send,args=((command),jsonData,))
        send.start()
        return "Done!"
    
    def flask_run():
        webserver.run(host='0.0.0.0',port=8080)
    
    flaskThread = Thread(target=flask_run)
    flaskThread.start()
    minecraftThread = Thread(target=__minecraft_chat)
    minecraftThread.start()