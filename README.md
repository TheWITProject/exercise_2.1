## Summary
You will be creating an object oriented design for a deck of cards. Once you are done with this exercise, please push your code and open a PR with the following name: `<YOUR_NAME>_exercise_2.1`.

## Instructions
Create an object oriented design for a deck of cards. You can do this from scratch or you can use the starting point in `starting_point.py`.

<details>
<summary>What kind of hierarchy might we use for our design?</summary>
  
  - We probably want to separate our `Deck` class and our `Card` class.
  - We can even create a `Suit` class that extends the `Card` class. Would this be overkill though? Explain why or why not in the codeblock below.
  ```
I don't think it's overkill. A suit is a type of card so it will have the same features as a card and more.
  ```
   
</details>

<details>
<summary>What kind of attributes might we include on each class?</summary>

  - Our `Deck` instance needs to know what cards it contains.
  - Our `Card` instance needs to know the suit and value of itself.
  - Our `Card` instance might also want to know whether it's face-up or face-down.
   
</details>

<details>
<summary>What kind of methods might we include on each class?</summary>
  
  - Our `Deck` instance needs a method to build its cards when _it is created_*.
  - Our `Deck` instance needs a method to reset the cards after use*.
  - Our `Deck` instance might need a method to shuffle its cards.
  - Our `Card` instance might need a method to flip.
  - Can you think of anything else? You can do whatever you want! Get a random card, discard a card, etc.
  
  *Note: Two important things to think about with these two functions:
  - How can we create all of the cards efficiently? Surely, we don't want to do this manually as demonstrated below. It seems very _repetetive_. Hm, repetetive...
  ```py
  Card('Queen', 'Hearts')
  Card('Queen', 'Spades')
  Card('Queen', 'Diamonds')
  ```
  - Do these two methods seem like they're doing something similar? How we resuse the functionality without writing the same code twice?
   
</details>

<details>
<summary>Are there any class attributes or methods we want to create?</summary>
  
  - I can't think of any that are too important. It depends on what you want to build.
  - What if we run a casino with a limited number of decks? Maybe we can have an attribute to count the number of decks in use.
   
</details>

<details>
<summary>What else can you do?</summary>
  
  - Let's create a game by creating another class!
   
</details>
