# [pyp-c3-a1] Role-playing game

**Work in progress**

### Objective of the game

**Console based** game intended to use **advanced OOP features** like Mixins, multiple inheritance and metaclasses.

### What I have so far

The game will allow you to create characters that can have different _characteristics_ or _traits_. Some example characteristics could be: _super speed_, _super strength_, _flying ability_, _stop time_, etc.

When you start the game you'll be able to choose just 2 traits/characteristics for your character. Example:

```python
python game.py -c flying super-speed
```

That way each trait will be implemented with a different class and the character class can be constructed through the use of mixins:

```python
class FlyingTrait(GameCharacterTrait):
    pass


class SuperSpeedTrait(GameCharacterTrait):
    pass


class Character(SuperSpeedTrait, FlyingTrait):
    pass

```

### What I need

The most important thing! What/how to play it? What should the character do? Some ideas I'm thinking about:

**Idea 1**
The game can consist of different challenges that the character needs to perform. Some challenges to tackle. Every new challenge the character completes it improves it's skills. We could also grant new skills/traits after a few completed challenges.

**Idea 2**
Do it a 1vs1 game. Instead of just 1 character it's a game to play against someone else. So when the game starts you can select your traits and the other player can select other traits. Then the game begins and you compete against the other player. **What I don't know is HOW you compete! What do you do?**

Example: `python game.py --player1 flying super-speed --player2 flying super-strength`
