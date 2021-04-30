fetch('/posts')
    .then(posts => posts.json())
    .then(posts => {
        const main = document.getElementById("posts")
        for (let i in posts) {
            const li = document.createElement("li");
            li.textContent = posts[i];
            main.appendChild(li);
            const del = document.createElement("button");
            del.textContent = '❌';
            main.appendChild(del);
            del.addEventListener('click', () => {
                fetch('/posts', {
                    method: 'DELETE',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({id: i})
                }).then(() => location.reload())
            })
        }
    })
