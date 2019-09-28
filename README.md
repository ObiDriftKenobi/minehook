# minehook

Minehook is a Python library utilizing Flask and PyCraft that simplifies making webhook actions in your minecraft world, using a very simple Python API.

Creating webhooks using minehook is as easy as:
~~~
import minehook
minehook.address = "example.minecraftserver.net"
minehook.port = 25665
minehook.add_hook("saystuff",minehook.Command("say Someone told me to say:"),minehook.JSONKey("say"))
minehook.run()
~~~