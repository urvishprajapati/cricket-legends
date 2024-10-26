from django import forms

class StoryForm(forms.Form):
    name = forms.CharField(max_length=100, label="Your Name")
    story = forms.CharField(widget=forms.Textarea, label="Your Story")

class VoteForm(forms.Form):
    players = forms.ChoiceField(
        choices=[('player1', 'Player 1'), ('player2', 'Player 2'),
                 ('player3', 'Player 3'), ('player4', 'Player 4')],
        label="Choose your favorite player"
    )
