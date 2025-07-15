function fetchEvents() {
    fetch('/events')
        .then(res => res.json())
        .then(data => {
            const ul = document.getElementById("event-list");
            ul.innerHTML = '';
            data.forEach(event => {
                let li = document.createElement('li');
                let ts = new Date(event.timestamp).toUTCString();
                if (event.event === 'push') {
                    li.innerText = `${event.author} pushed to ${event.to_branch} on ${ts}`;
                } else if (event.event === 'pull_request') {
                    li.innerText = `${event.author} submitted a pull request from ${event.from_branch} to ${event.to_branch} on ${ts}`;
                }
                ul.appendChild(li);
            });
        });
}
setInterval(fetchEvents, 15000);
fetchEvents();
