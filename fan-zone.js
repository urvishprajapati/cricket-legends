document.getElementById('fanStoryForm').addEventListener('submit', function(e) {
    e.preventDefault();
    alert("Story submitted! Thank you for sharing.");
});

function vote(player) {
    document.getElementById('voteResult').innerText = `You voted for ${player}!`;
}
