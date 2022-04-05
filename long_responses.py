import random

R_EATING = "I don't like eating anything because I'm a bot obviously!"
R_ADVICE = "If I were you, I would go to the internet and type exactly what you wrote there!"
L_LIKE = "Sorry, i can't tell you that...its personal!"
H_HELP = "I would Help, but I need Internet for that.."

def unknown():
    response = ["Could you please re-phrase that? ",
                "...",
                "Sounds about right.",
                "What does that mean?",
                "I think you should Google it..."][
        random.randrange(5)]
    return response