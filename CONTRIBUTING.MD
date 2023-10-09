# CONTRIBUTING.MD
Bear with me here, this being the first open source project I intend on being serious with for a long time (and the first CONTRIBUTING MD i've written)

## Adding Dependencies / Libraries

It has to have at least an acceptable license that this project can abide by. I will be reluctant to using them, being a fan of homebrewing solutions, but I look forward to not doing that as much.

This is a vague concept for the reason above. I barely use libraries. 

## Coding Style and Syntax

This might seem like a very strict set of rules to abide by. You can *lightly* bend them if you must, but it's for the sake of readability; **you should be able to mildly grasp the idea of what something does just by looking at it.**

**YOU MUST**...

- Provide type hinting wherever possible.  
  - I understand Python is **NOT** a static typed language  
  I definitely do not treat it as one here
  - I understand that it can be tedious  
Nevertheless, type hinting greatly helps in avoiding errors and providing autocomplete
  - I understand that it can be utterly confusing to type hint  
Google it, and keep throwing stuff at it until the IDE gets it. It *has* worked for me so far, and while it might have cost me several hours looking for answers, it keeps the `Any` types away

- Have separate Python files be able to run on their own[**\***](#footnotes)  
This is a personal philosphy I'm trying out, and have stuck to so far. As you can see in each .py file, many of them include ways to run them via the terminal.

- Use Uppercase for Function and Class definitions, lowercase for all others
    - camelCase and snake_case are somewhat acceptably interchangeable. Looking back on my own code, it seems I myself can't subconciously decide.

- Take breaks! ☕  
This is just as good advice for me as it is for you. This is only an open source project, and it can be quite easy to get frustrated and not be your 100%. Taking a minute to get a breath of fresh air and sunlight every once in a while does wonders, for me at least

Please do...

- Use names that are definitive of the value they define  
[example i have to write]
- Leave comments that generally describe general portions of code
    - Especially on oneliners [like this monstrosity](/OnlineTimeline/OTPlugin/VariableKeyDict.py#L32)...  
    ```python
    # Get a list of all keys that match, None where it does not
     k = [key if key.regex.match(value) else None for key in self.keys()]
     ```  

And **DON'T**

- Use super condensed  names  
Names like the following are unacceptable  
  - `v,k` for 'Value' and 'Key'  
  One letter names are only ever acceptable for something alike `x,y,z,w` for coordinates.  
  `val, key` are acceptable
    - Unless it's in a scope that shares similar names, in which case, please be more defining, such as `eventVal, eventKey`
  - `FwdToHist` for 'ForwardToHistory'  
  Abbreviations are only good for very commonly used abbreviations, such as `cmd` for command, and `pos` for position  
  Using only the initial few letters of a word is also pretty bad 

The current state of the code is an issue by itself, and I will work on fixing that at some point

## Pull Requests

I have never dealt with pull requests, so bear with me here

[text i have to finish]

## Issues

I have never dealt with issues either, so bear with me here too

[more text i have to finish]


Footnotes
=========
\* I will always try to be open-minded about anything. If you bring a compelling argument to the table to convince me otherwise about something, it might just work.