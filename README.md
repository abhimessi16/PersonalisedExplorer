# PersonalisedExplorer
Using shortcuts to open folders we mostly use.

This project is about using keyboard presses. A keyboard listener will be actively looking for key events. When we want to activate our app, we press certain keys and similarly to deactivate. Once activated, we type the folder name we want to access and the folder we want will already be stored with its full address and the explorer will be opened with the folder.
That's a vague idea of what I want to accomplish. It might seem unneccesary but we do open quite a few folders from different locations on our computer in a given day. I wouldn't count them but they'd be many, it's like one of those innovations that isn't needed but makes life easier. If we do think about it this will be quite useful and...

I have always liked the idea of a computer doing my work for me. Not that i'm lazy (not true either!), but I like this idea. I am a big fan of AI and I will in the future use AI/ML to make this simple project of mine more complex, kidding, to make it even more useful and productive.

For now, I'll just hardcode all the operations that I would like my Personalised Explorer to perform!

I am using pynput library.
A keyboard listener, etc

1) The first task is to work on the activation process of the application, I'm using a keyboard hotkey, which when pressed for a period of time would activate the application and vice-versa. This turned out to be little bit difficult, but it is done for now.
You can see the implementation I used for the activation part in test.py
I believe there are still bugs that I need to work on, because this was way too easy.

2) The second task is to now listen for keys which can then be searched for in the dictionary to perform the task it corresponds to. I am unable to understand how i'm supposed to accomplish this, I might have to use two different listerners, which means mutithreading, or maybe I could work with the listerner I have already created for the activation process.

I'll leave at this because there is still a lot to do and learn.
