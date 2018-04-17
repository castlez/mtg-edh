# mtg-edh
Gonna be a pretty open ended Commander playing client.

#### Install and Play (it doesn't do much right now though)
Pull the repo and run:
```
\mtg-edh:> pip install -r requirements
\mtg-edh:> cd src
\mtg-edh\src:> python game.py
```

The above will currently download a deck and set up a game of two of the same 
player with that deck (told ya).

#### TODO (cause I already do to much JIRA stuff)
So this is still in a very unfinished stage, but I plan on keeping this simple, 
and as practical as possible. 
- Cache downloaded decks
  - Need a way to uniquely identify decks
- UI
  - Decide on framework, start with just a screen with movable cards
  - Consider scalability
  - Consider platform
- Multiplayer
  - Platform dependent 
  - Scalability again (though max player count would be low)