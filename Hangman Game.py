import time
import random

word_choose = ["blue","words","change","mask","gold","lamp","sky","frog","paint","sword","prize","ghost","blank"]

print("🎮 Welcome to Hangman!")
print("Try to guess the hidden word, one letter at a time.")
print("You have 6 chances before... you're hanged! 😵")

i=1
while i!=0:
    choose = input("\n👉 Press [Enter] to start a new game or type 'exit' to quit: ").lower()
    choose_exit=choose.lower()
    if(choose_exit=='exit'):
        print("\nThanks for playing! See you next time. 👋")
        break

    word_selection = []
    guess_word = []
    right = 0
    computer_choice = random.choice(word_choose)
    for word in computer_choice:
        word_selection.append(word)
    
    print("\n🔍 Wait choosing a word...")
    time.sleep(3)
    display_remaining = ['_']*len(word_selection)
    print("\n🔍 A new word has been chosen!")
    print(f"The word has {len(computer_choice)} letters: ", ' '.join(display_remaining))

    z=6
    while(z!=0):
        user_input = input("\n✏️  Enter a letter: ").lower()
        j=0
        while(j<len(word_selection)):
            if(user_input==word_selection[j]):
                if(user_input not in guess_word):
                    display_remaining[j]=user_input
                    right+=1
                    print("✅ Right guess!\n")
            j+=1
        if(right==len(word_selection)):
            print(f"\n🎉 Congratulations! You guessed the word:- {computer_choice.upper()} 🏆")
            break
        elif(user_input==""):
            print("👻 Silence won't save you... type a letter!")
        elif(user_input in guess_word):
            print("⚠️  You've already guessed that letter. Try something new.")
        elif(len(user_input)>1):
            print("❗ Please enter **one valid letter** at a time.")
        elif(user_input not in word_selection):
            if z == 6:
                time.sleep(1)
                print("   _____ \n"
                      "  |      \n"
                      "  |      \n"
                      "  |      \n"
                      "  |      \n"
                      "  |      \n"
                      "  |      \n"
                      "__|__\n")
                print("❌ Wrong guess.",(z-1)," guesses remaining\n")

            elif z == 5:
                time.sleep(1)
                print("   _____ \n"
                      "  |     | \n"
                      "  |     |\n"
                      "  |      \n"
                      "  |      \n"
                      "  |      \n"
                      "  |      \n"
                      "__|__\n")
                print("❌ Wrong guess.",(z-1)," guesses remaining\n")

            elif z == 4:
                time.sleep(1)
                print("   _____ \n"
                      "  |     | \n"
                      "  |     |\n"
                      "  |     | \n"
                      "  |      \n"
                      "  |      \n"
                      "  |      \n"
                      "__|__\n")
                print("❌ Wrong guess.",(z-1)," guesses remaining\n")

            elif z == 3:
                time.sleep(1)
                print("   _____ \n"
                      "  |     | \n"
                      "  |     |\n"
                      "  |     | \n"
                      "  |     O \n"
                      "  |      \n"
                      "  |      \n"
                      "__|__\n")
                print("❌ Wrong guess.",(z-1)," guesses remaining\n")

            elif z == 2:
                time.sleep(1)
                print("   _____ \n"
                      "  |     | \n"
                      "  |     |\n"
                      "  |     | \n"
                      "  |     O \n"
                      "  |    /|\\\n"
                      "  |        \n"
                      "__|__\n")
                print("❌ Wrong guess. last guess remaining\n")

            elif z == 1:
                time.sleep(1)
                print("   _____ \n"
                      "  |     | \n"
                      "  |     |\n"
                      "  |     | \n"
                      "  |     O \n"
                      "  |    /|\\\n"
                      "  |    / \\\n"
                      "__|__\n")
                print("❌ Wrong guess. You are hanged!!!\n")
            z-=1
        
        print("🎲 Guess the letter: ", end="")
        for d_r in range(len(word_selection)):
            print(display_remaining[d_r],end=" ")

        guess_word.append(user_input)
                
    if(right!=len(word_selection)):
        print(f"\n😢 Game Over! You ran out of guesses. The word was: **{computer_choice.upper()}**")
        z+=1

i+=1