# views.py

from django.core.mail import send_mail
from django.shortcuts import render, redirect
from .forms import StoryForm, VoteForm

def fan_zone(request):
    if request.method == 'POST':
        story_form = StoryForm(request.POST)
        vote_form = VoteForm(request.POST)
        
        if 'submit_story' in request.POST and story_form.is_valid():
            name = story_form.cleaned_data['name']
            story = story_form.cleaned_data['story']
            
            # Send email with the story details
            send_mail(
                subject=f"New Story Submission from {name}",
                message=f"Story:\n{story}",
                from_email='your_email@gmail.com',
                recipient_list=['udiman03@gmail.com'],  # Replace with your email
                fail_silently=False,
            )
            return redirect('fan-zone')  # Redirect to prevent resubmission
        
        if 'submit_vote' in request.POST and vote_form.is_valid():
            player = vote_form.cleaned_data['players']
            
            # Send email with the vote details
            send_mail(
                subject="New Vote Submitted",
                message=f"Vote for: {player}",
                from_email='your_email@gmail.com',
                recipient_list=['udiman03@gmail.com'],  # Replace with your email
                fail_silently=False,
            )
            return redirect('fan-zone')  # Redirect to prevent resubmission

    else:
        story_form = StoryForm()
        vote_form = VoteForm()

    return render(request, 'fan-zone.html', {'story_form': story_form, 'vote_form': vote_form})
