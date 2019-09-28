# minehook

Minehook is a Python library utilizing Flask and PyCraft that simplifies making webhook actions in your minecraft world, using a very simple Python API.

Creating webhooks using minehook is as easy as:
~~~
import minehook
minehook.address = "example.minecraftserver.net"
minehook.port = 25665
minehook.add_hook("test",minehook.Command("say Hello World!"))
minehook.run()
~~~
The result:
![Demonstration of the included code.](https://i.imgur.com/v0MtvBm.png)

JSON Keys can be passed to `add_hook` as well:
~~~
minehook.add_hook("test_json",minehook.Command("say I was told to say"),minehook.JSONKey("say_content"))
~~~
Now we can pass the following JSON to our webhook:
~~~
{
    "say_content":"that minehook is easy!"
}
~~~
And the result will be:
![Demonstration of the included code.](https://i.imgur.com/UORyxHR.png)